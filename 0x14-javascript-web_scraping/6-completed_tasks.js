#!/usr/bin/node
/**
 * Write a script that computes the number of tasks completed by user id.
 * Arguments:
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only print users with completed task
 */

const request = require('request');
const url = process.argv[2];

request(url, function (errr, response, body) {
  if (errr) {
    console.log(errr);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const intg in tasks) {
      const task = tasks[intg];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
