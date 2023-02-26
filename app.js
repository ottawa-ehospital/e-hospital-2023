const {PythonShell} = require('python-shell');
const express = require('express');
var fileupload = require("express-fileupload");

var bodyParser = require('body-parser')
const app = express();

app.use(express.static('public'));
app.use(express.json());
app.use(fileupload());
app.use(bodyParser.urlencoded({ extended: false }));
//app.use(multipart());

// routes
app.post('/checkPnemonia', (req, res) => {
    try{
        req.files.imagefile.mv(`./public/pnemonia_images/${req.files.imagefile.name}`);
        
        let options = {
            scriptPath : __dirname,
            args : [`${__dirname}\\public\\pnemonia_images\\${req.files.imagefile.name}`]
        };
        
        PythonShell.run("test.py", options).then((err,resp)=>{
            if(err){
                console.log(err);
                res.status(500).json(err);
            }
            if(resp){
                res.status(200).json({result:resp});
            }
        });
        
    }
    catch(error){
        console.log(error);
        res.status(500).json({msg:'Something Went Wrong'});
    }
});

app.listen(7171,()=>{
    console.log('Listening on port 7171');
})