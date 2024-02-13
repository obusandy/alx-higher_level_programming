#!/usr/bin/node
// a function that returns the number of occurrences in a list:
// Prototype: exports.nbOccurences = function list, searchElement

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((num, j) => (j === searchElement ? num + 1 : num), 0);
};
