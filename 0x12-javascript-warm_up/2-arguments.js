#!/usr/bin/node
const args = process.argv.length;

if (args < 3) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

// Arg(0)-> Process execution path
// Arg(1)-> Executable file
// Arg(2)-> 1st Argument
