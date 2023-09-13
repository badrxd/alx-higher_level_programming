#!/usr/bin/node
const list = require('./100-data.js');
const List = [];
list.map((item, i) => {
  return (List[i] = item * i);
});
console.log(list);
console.log(List);
