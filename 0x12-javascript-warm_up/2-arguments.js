#!/usr/bin/node
const totalno = process.argv.length;
console.log(totalno === 2 ? 'No argument' : totalno === 3 ? 'Argument found' : 'Arguments found');
