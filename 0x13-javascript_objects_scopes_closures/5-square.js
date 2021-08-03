#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;

// super-> Calls the parent class's constructor with lengths
// provided from the Rectangle's width and height
