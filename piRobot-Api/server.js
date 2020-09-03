
const ps = require  ('python-shell');
const express = require('./node_modules/express');
const app = express();
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
  Shell.send(JSON.stringify({command:'f'}))
  res.end('hs')
});

app.get('/move/left', function(req, res) {
  Shell.send(JSON.stringify({command:'l'}))
  res.end('hs')
});

app.get('/move/right', function(req, res) {
  Shell.send(JSON.stringify({command:'r'}))
  res.end('hs')
});

app.get('/move/stop', function(req, res) {
  Shell.send(JSON.stringify({command:'s'}))
  res.end('hs')
});

app.get('/comtest', function(req, res) {
  Shell.send(JSON.stringify({command:'f'}))
  res.end('hs')
});


app.listen(9006);
