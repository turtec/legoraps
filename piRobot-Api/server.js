
const ps = require  ('python-shell');
const express = require('./node_modules/express');
const path = require('path');

const app = express();

//const pyscript =  spawn('python3', ['../piRobot-Core/main.py']);
//let pyshell = new ps.PythonShell('../piRobot-Core/main.py');
//const pyProg = spawn('python', ['../piRobot-Core/main.py']);  

//pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
//  console.log(message);
//});

// sends a message to the Python script via stdin
var options = {
  //pythonPath: '/Users/zup/.local/share/virtualenvs/python_Shell_test-TJN5lQez/bin/python',
  pythonOptions: ['-u'], // get print results in real-time
  // make sure you use an absolute path for scriptPath
  //scriptPath: "./subscriber/",
  // args: ['value1', 'value2', 'value3'],
 // mode: 'json'
};

const Shell = new ps.PythonShell("../piRobot-Core/main.py", options);

/*setInterval(() => {
  console.log('interval')
  
}, 1000);*/

Shell.on("message", message => {
  console.log('js the message ' + message);
})


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
});

app.get('/move/forward', function(req, res) {
  console.log('api call to move forward');
  const { spawn } = require('child_process');	 
  const pyProg = spawn('python', ['../piRobot-Core/api-interface/moveforward.py']);
  res.end('end');
});

app.get('/comtest', function(req, res) {
  
  Shell.send('command')
  res.end('hs')
 /* pyProg.stdin.write('my data' + '\r\n');
  res.end('hs')
 
 pyProg.stdout.on('data', function (data) {
  //console.log('Pipe data from python script ...');
  dataToSend = data.toString();
  console.log(dataToSend)
  res.end(dataToSend)
 });
 
 pyProg.stderr.on('data', (data) => {
  console.log('error')
  console.log(data);
});*/




 // in close event we are sure that stream from child process is closed
 /*pyProg.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 // send data to browser
 res.send(dataToSend)
 });*/
 


 
 });


app.listen(9006);
