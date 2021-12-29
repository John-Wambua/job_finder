#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:03:34 2021

@author: john
"""

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import werkzeug
import os
import job_finder as jf
from werkzeug.utils import secure_filename

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()

UPLOAD_DIR="/home/john/Documents/IS_Project_II/job_finder/api/assets/images/cvs"

ALLOWED_EXTENSIONS = set(['txt', 'pdf',])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class CVProcessor(Resource):
    def post(self):
        parser.add_argument('cv_file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()
        
        cv_file = args['cv_file']
        
        # check if the post request has the file part
        if cv_file == None:
            resp = jsonify({
                'status' : 'fail',
                'message' : 'No file part in the request'
                })
            resp.status_code = 400
            return resp
        if (cv_file.filename == ''):
            resp = jsonify({
                'status' : 'fail',
                'message' : 'No file selected for uploading'
                })
            resp.status_code = 400
            return resp
        if cv_file and allowed_file(cv_file.filename):
            cv_file.save(os.path.join(UPLOAD_DIR, cv_file.filename))
            resp = jsonify({
                'status' : 'success',
                'message' : 'File successfully uploaded'
                })
            resp.status_code = 201
            return resp
        else:
            resp = jsonify({
                'status' : 'fail',
                'message' : 'Only txt and pdf files allowed'
                })
            resp.status_code = 400
            return resp
    
        # check if the post request has the file part
        # if 'file' not in request.files:
        #     resp = jsonify({'message' : 'No file part in the request'})
        #     resp.status_code = 400
        #     return resp
        # file = request.files['file']
        # if file.filename == '':
        #     resp = jsonify({'message' : 'No file selected for uploading'})
        #     resp.status_code = 400
        #     return resp
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     resp = jsonify({'message' : 'File successfully uploaded'})
        #     resp.status_code = 201
        #     return resp
        # else:
        #     resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        #     resp.status_code = 400
        #     return resp
        

api.add_resource(CVProcessor,'/cv_processor')

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    