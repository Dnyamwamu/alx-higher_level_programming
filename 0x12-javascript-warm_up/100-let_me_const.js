#!/usr/bin/node

const fs = require('fs');

// Define the new value of myVar
const newValue = 333;

// Update the value of myVar in the file
const content = `const myVar = ${newValue};`;

// Write the updated content to the file
fs.writeFileSync('myfile.js', content);

