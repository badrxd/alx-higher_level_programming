#!/usr/bin/node
exports.converter = function (base) {
  const conv = (n) => {
    return n.toString(base);
  };
  return conv;
};
