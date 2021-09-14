#!/usr/bin/node
// Include fs module
const fs = require('fs');
// Use fs.writeFile method to write file
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err) {
  // Dsiplay file content or error content
  if (err) {
    console.log(err);
  }
});
