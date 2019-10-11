const express = require('express');
const path = require('path');
const app = express();


app.use(express.static(path.join(__dirname, 'legorasp-control/build')));

app.get('/', function(req, res) {
  //res.sendFile(path.join(__dirname, 'legorasp-control/', 'index.html'));
  res.sendFile(path.join(__dirname, 'legorasp-control/', 'index.html'));
});

app.get('/cam2', function(req, res) {
console.log('ggg');
  //res.sendFile(path.join(__dirname, 'legorasp-control/', 'index.html'));
  //res.sendFile(path.join(__dirname, 'legorasp-control/', 'index.html'));
res.write('data');
        res.end('end');
});

app.get('/cam/left', function(req, res) {
  		
    const { spawn } = require('child_process');	
    const pyProg = spawn('python', ['../pycontroler/stepmotor.py']);
    res.end('end');
    pyProg.stdout.on('data', function(pydata) {
	const output = pydata;	
        console.log(pydata.toString());
        res.write('data' + output); 
   });		




});


app.listen(9001);
