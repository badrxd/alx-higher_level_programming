#!/usr/bin/node
exports.esrever = function (list) {
  const List = [];
  for (let i = list.length - 1; i > -1; i--) {
    List[i - list.length] = list[i];
  }
  return list.reverse();
};
