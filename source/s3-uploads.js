const aws = require('aws-sdk');
const express = require('express');
const { appendFile } = require('fs');
const multer = require('multer');
const multerS3 = require('multer-s3');
const uuid = require('uuid').v4;
const path = require('path');


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
           cb(null, file.originalname+'.pdf');
       }
   }) 
});


app.use(express.static('public'));
app.post('/upload', upload.array('avatar'), (req,res) =>{
    return res.json({status : 'OK', uploaded: req.files.length});
});
app.listen(3001, () => console.log("app is listening..."));