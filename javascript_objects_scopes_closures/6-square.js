#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
    for (let x = 0; x < this.height; x++) {
      for (let y = 0; y < this.width; y++) {
        if (c === undefined) {
          process.stdout.write('X');
        } else {
          process.stdout.write(c);
        }
      }
      console.log();
    }
  }
}

module.exports = Square;
