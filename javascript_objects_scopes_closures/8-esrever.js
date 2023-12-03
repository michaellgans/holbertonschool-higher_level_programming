#!/usr/bin/node

exports.esrever = function (list) {
  const length = list.length;

  for (let x = 0; x < (length / 2); x++) {
    let temp = null;
    temp = list[x];
    list[x] = list[length - 1 - x];
    list[length - 1 - x] = temp;
  }
  return list;
};
