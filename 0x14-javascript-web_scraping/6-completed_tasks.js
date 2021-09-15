#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const empTasksDict = {};

request(url, function (error, data, body) {
  if (error) {
    console.log(error);
  } else {
    const response = JSON.parse(body);
    for (let i = 0; response[i]; i++) {
      if (response[i].completed === true) {
        if (response[i].userId in empTasksDict) {
          empTasksDict[response[i].userId] += 1;
        } else {
          empTasksDict[response[i].userId] = 1;
        }
      }
    }
  }
  console.log(empTasksDict);
});
