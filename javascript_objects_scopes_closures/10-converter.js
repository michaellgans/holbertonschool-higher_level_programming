#!/usr/bin/node

exports.converter = function (base) {
  return function toBeConverted (number) {
    return number.toString(base);
  };
};
