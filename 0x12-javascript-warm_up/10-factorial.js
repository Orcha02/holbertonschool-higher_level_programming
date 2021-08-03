#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(factorial(arg));
}

function factorial (n) {
  return (n < 2) ? 1 : n * factorial(n - 1);
}
