#!/usr/bin/node
// class Rectangle that defines a rectangle:
// using the class notation for defining class
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let j = 0; j < this.height; j++) console.log('X'.repeat(this.width));
  }
};
