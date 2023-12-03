#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const length = list.length;
  for (let x = 0; x < length; x++) {
    if (list[x] === searchElement) {
      count++;
    }
  }
  return count;
};
