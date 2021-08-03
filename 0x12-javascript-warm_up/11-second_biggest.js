#!/usr/bin/node
const argSize = process.argv.length;
if (argSize < 2) {
  console.log(0);
} else {
  argSize.sort((a, b) => a - b);
  console.log(parseInt(num[num.length - 2]));
}
