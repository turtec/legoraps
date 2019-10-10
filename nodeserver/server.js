const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'legorasp-control/build')));

app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname, 'legorasp-control/build', 'index.html'));
});

app.listen(9000);
