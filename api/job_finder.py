#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 14:08:13 2021

@author: john
"""

import PyPDF2
import pandas as pd
import numpy as np
import process_cv as pcv
import process_job_postings as pjp
import indeed_scraper as isc
import pickle
from nltk.tokenize import word_tokenize,sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


tfidf_vec = TfidfVectorizer()

def main(filename):
    # Extract text from CV
    path = f'assets/cvs/{filename}'
    user_input = ''
    with open(path,'rb') as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        for page_number in range(number_of_pages):
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
            user_input += page_content
            
        pdf_file.close()
    
    
    corpus = pcv.main(user_input)
    
    results = isc.main('software engineer', 'remote')
    
    # Vectorize job postings
    job_postings = pjp.process_postings(results)
    
    # Append CV text to job postings dataframe
    job_postings = job_postings.append({
        'job_id': 'CV_CORPUS',
        'text': corpus
    }, ignore_index = True)
    
    
    job_vectorized = tfidf_vec.fit_transform((job_postings['text']))
    
    tfidf_df_jobs = pd.DataFrame(job_vectorized.toarray(), 
                            columns = tfidf_vec.get_feature_names())
    
    tfidf_df_jobs.index = job_postings['job_id']
    
    # Calculate the cosine similarity between all rows
    job_similarities = cosine_similarity(tfidf_df_jobs)
    
    # Wrap in a DataFrame for ease of use
    job_similarities_df = pd.DataFrame(job_similarities, 
                                             index=tfidf_df_jobs.index,
                                             columns=tfidf_df_jobs.index)
    # Find the similarities for the CV
    job_similarity_series = job_similarities_df.loc['CV_CORPUS']
    
    # Sort these values highest to lowest
    ordered_similarities = job_similarity_series.sort_values(ascending=False).drop_duplicates()
    
    top_jobs = ordered_similarities[1:11]
    
    final_df = pd.DataFrame(columns=results.columns)
    # print(final_df.columns)
    
    job_probs_df = pd.DataFrame({'JobID': top_jobs.index, 'Likelihood': top_jobs.values})
    
    for top_job_id, job_value in top_jobs.items():
        print(top_job_id, job_value)
        
        for index, job in results.iterrows():
            if (top_job_id == job['JobID']):
                print(job)
                final_df.loc[index] = job
                    
    final_df = pd.merge(final_df.drop_duplicates(subset=['JobID']), job_probs_df, on = 'JobID')
    return final_df
