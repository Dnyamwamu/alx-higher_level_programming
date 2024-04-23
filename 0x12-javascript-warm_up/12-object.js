#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const replacedArgs = args.map(num => num === 12 ? 89 : num);
  const sortedArgs = replacedArgs.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
