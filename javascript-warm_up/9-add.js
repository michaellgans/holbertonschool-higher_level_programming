#!/usr/bin/node

function add(a, b) {

    a = Number(process.argv[2]);
    b = Number(process.argv[3]);

    if (!a && !b) {
      return NaN;
    }
    return a + b;
}

let result = add();

console.log(result);
