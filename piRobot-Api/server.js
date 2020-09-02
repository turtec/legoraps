const express = require('./node_modules/express');
const path = require('path');
const app = express();

app.use(function (req, res, next) {

  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
  res.setHeader('Access-Control-Allow-Credentials', true);
  next();
});

app.get('/cam/right', function(req, res) {
 const { spawn } = require('child_process');	
 const pyProg = spawn('python', ['../piRobot-Core/stepmotor_right.py']);
 //console.log(pyProg.stdout)
 pyProg.stdout.on('data', (data) => {
   console.log('onData')
  output += data.toString();
  console.log('output was generated: ' + output);
});
 res.end('end');
});

app.get('/cam/left', function(req, res) {
  const { spawn } = require('child_process');	
  const pyProg = spawn('python', ['../piRobot-Core/stepmotor_left.py']);
  res.end('end');
  /* pyProg.stdout.on('data', function(pydata) {
	const output = pydata;	
        console.log(pydata.toString());
        res.write('data' + output); 
   });	*/	
});

app.get('/comtest', function(req, res) {
  console.log('a request')
  const { spawn } = require('child_process');	
  let output="";
  const pyProg = spawn('python', ['../piRobot-Core/comtest.py']);
  
  pyProg.stdout.on('data', (data) => {
    console.log('onData')
   output += data.toString();
   console.log('output was generated: ' + output);
 });
  res.end('end');
 });


app.listen(9003);
