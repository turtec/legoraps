
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

app.get('/move/forward', function(req, res) {
  Shell.send(JSON.stringify({command:'mf'}))
  res.end('hs')
});

app.get('/move/left', function(req, res) {
  Shell.send(JSON.stringify({command:'ml'}))
  res.end('hs')
});

app.get('/move/right', function(req, res) {
  Shell.send(JSON.stringify({command:'mr'}))
  res.end('hs')
});

app.get('/move/stop', function(req, res) {
  Shell.send(JSON.stringify({command:'ms'}))
  res.end('hs')
});

app.get('/move/backward', function(req, res) {
  Shell.send(JSON.stringify({command:'mb'}))
  res.end('hs')
});

app.listen(9006);
