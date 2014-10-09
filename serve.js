var express = require('express');
var bodyParser = require('body-parser')

// Constants
var PORT = 80;
var ROOT = 'repos';

// Child Process
var exec = require('child_process').exec;
var spawn = require('child_process').spawn;

// File System
var fs = require('fs');

// App
var app = express();
app.use(bodyParser.json());

app.get('/', function (req, res) {
    res.sendfile('index.html');
});

app.post('/', function (req, res) {
    var url = req.body.repository.clone_url;
    console.log(url);
    var parts = url.split('/').reverse();
    var user = parts[1];
    var repo = parts[0];
    var parent = ROOT + '/' + user;
    var rm_cmd = 'rm -rf ' + parent + '/' + repo.replace(/\.git$/, '');
    var git_cmd = 'git clone ' + url

    fs.mkdir(parent, null, function() {});
    
    exec(rm_cmd, {}, function(error, stdout, stderr) {
        console.log('old repo removed via', rm_cmd, error);
    });

    exec(git_cmd, { cwd: parent }, function(error, stdout, stderr) {
        console.log('repo cloned via', git_cmd, error);
    });

    res.status(200).end();
});

app.listen(PORT);
console.log('Running on port ' + PORT);
