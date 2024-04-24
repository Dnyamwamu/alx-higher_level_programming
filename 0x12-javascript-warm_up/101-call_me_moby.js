#!/usr/bin/node

const { executeXTimes } = require('./executeXTimes');

function myFunction() {
  console.log('Executing my function');
}

executeXTimes(5, myFunction);
