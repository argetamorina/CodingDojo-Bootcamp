// import dependencies
var express = require('express');
var path = require('path');

// import config
var config = require('./server/config');

// create express app
var app = express();

// setup bodyParser
var bodyParser = require('body-parser');
app.use(bodyParser.json());

// setup mongoose
require('./server/config/mongoose');

// setup routes
require('./server/config/routes')(app);

// static content
app.use(express.static(path.join(__dirname, './client')));

// start server
app.listen(config.port, function () {
  console.log(`Server running on port ${config.port}`);
});
