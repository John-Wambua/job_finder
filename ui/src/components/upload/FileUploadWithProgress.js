import {useEffect, useState} from "react";
import {Grid, LinearProgress} from "@material-ui/core";
import {postResume} from "../../services/resumeService";

export default ({file})=>{

    const [progress, setProgress] = useState(0)
    useEffect(()=>{
        const upload = async ()=>{

            try{
                const resp = await postResume(file, setProgress)
                // localStorage.setItem("cv_file", JSON.stringify(file))
                console.log('RESPONSE', resp)
            }catch (err){
                console.log('ERROR UPLOADING ....', err.response.data.message)
            }

        }
        upload()
    },[file])
    return (
        <Grid item>
            <LinearProgress variant="determinate" value={progress}/>
        </Grid>
    )
}

// const uploadFile = (file, onProgress)=>{
//     const url = 'https://api.cloudinary.com/v1_1/demo/auto/upload';
//     const upload_preset = 'docs_upload_example_us_preset'
//     const cloud_name = 'demo'
//
//     return new Promise((res, rej)=>{
//         const xhr = new XMLHttpRequest();
//         xhr.open('POST', url, true);
//
//         xhr.onload = ()=>{
//             const resp = JSON.parse(xhr.responseText);
//             console.log('response', resp)
//             // url where file is saved
//             res(resp.secure_url)
//         }
//         xhr.onerror = e => {
//             console.log('onerror ',e)
//             rej(e)
//         }
//         xhr.upload.onprogress = e =>{
//             if (e.lengthComputable){
//                 const percentage = (e.loaded / e.total) * 100
//                 onProgress(Math.round(percentage))
//             }
//         }
//
//         const formData = new FormData()
//         formData.append('file', file);
//         formData.append('cloud_name', cloud_name);
//         formData.append('upload_preset', upload_preset)
//
//         xhr.send(formData)
//     });
//
// }