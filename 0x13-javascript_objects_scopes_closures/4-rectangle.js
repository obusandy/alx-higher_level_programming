#!/usr/bin/node
//  a class Rectangle that defines a rectangle:
//  The constructor must take 2 arguments: w and h
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
// print - prints the rectangle using the character X
// return: void

  print () {
    for (let j = 0; j < this.height; j++) console.log('X'.repeat(this.width));
  }

//  rotate - makes changes of the width and the height of the rectangle

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
