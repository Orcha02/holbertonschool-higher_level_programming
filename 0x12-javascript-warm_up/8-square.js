#!/usr/bin/node
const size = process.argv[2];
const square = parseInt(size);
if (isNaN(square)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < square; i++) {
    console.log('X'.repeat(size));
  }
}

// repeat() returns string with specified number of copies of the string it was called on
