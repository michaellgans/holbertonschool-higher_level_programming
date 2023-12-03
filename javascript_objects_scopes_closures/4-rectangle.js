#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    let temp = null;
    temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      for (let y = 0; y < this.width; y++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}

module.exports = Rectangle;
