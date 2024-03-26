#!/usr/bin/node
/**
 * Below is a script that display the status code of a GET request.
 * arguments:
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 */
const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
