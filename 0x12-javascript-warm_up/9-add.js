#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));

// parseInt-> Accepts string to convert it into an integer
// process.argv[]-> Gets the arguments to add
