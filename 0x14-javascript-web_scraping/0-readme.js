#!/usr/bin/node
// Include fs module
const fs = require('fs');
// Use fs.readFile() method to read file
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  // Display file content or error content
  if (err === true) {
    console.log(err);
  }
  console.log(data);
});
