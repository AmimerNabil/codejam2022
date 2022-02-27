const aws = require('aws-sdk');
const express = require('express');
const multer = require('multer');
const multerS3 = require('multer-s3');
const uuid = require('uuid').v4;
const path = require('path');
const {PythonShell} = require('python-shell');
const { deflateSync } = require('zlib');



const app = express();
const s3 = new aws.S3({apiVersion : '2006-03-01'});

const upload = multer({
   storage : multerS3({
       s3:s3,
       bucket: 'codejam2022',
       metadata : (req,file,cb)=>{
           cb(null, {fieldName: file.fieldname});
       },
       key: (req, file, cb) => {
           const ext = path.extname(file.originalname);
           cb(null, file.originalname);
       }
   }) 
});


app.use(express.static('public/'));
app.post('/upload', upload.array('avatar'), (req,res) =>{
    console.log(res.json({status : 'OK', uploaded: req.files.length}));
    getAllObjectsFromS3Bucket("codejam2022");
});


async function getAllObjectsFromS3Bucket(bucket) {
    
    let isTruncated = true;
    let marker;
    while(isTruncated) {
        let params = {Bucket: bucket};
        if (marker) params.Marker = marker;
        const response = await s3.listObjects(params).promise();
        response.Contents.forEach(item => {
            var parameters = {
                Bucket: bucket,
                Key : item.Key
            };
            
            let options = {
                scriptPath : '',
                args : [parameters.Bucket, parameters.Key]
            };

            PythonShell.run(
                'getPdf.py',
                options,
                (err,res) =>{
                    if (err) throw err;
                    output = res;
                }
            )
            let optionsExtract = {
                scriptPath : '',
                args : ['uploads/'+parameters.Key,
                        parameters.Key]
            };
        
            PythonShell.run(
                'extraction.py',
                optionsExtract,
                (err,res) =>{
                    if (err) throw err;
                    console.log(res);
                }
            )         
        });



        isTruncated = response.IsTruncated
        if (isTruncated) {
            marker = response.Contents.slice(-1)[0].Key;
        }
    }
}

getAllObjectsFromS3Bucket("codejam2022");


app.listen(3001, () => console.log("app is listening..."));
