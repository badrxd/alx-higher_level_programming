#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(`${url}?completed=true`, function (err, body) {
    if (err) {
      console.error(err);
    } else {        
      let obj = {}

      const data = JSON.parse(body.body)
      data.forEach(element => {
        if (obj[element.userId] == undefined) {
            obj[element.userId] = 1          
        } else {
            obj[element.userId] = obj[element.userId] + 1
        }
      });
        console.log(obj);
    }
  });