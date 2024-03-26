#!/usr/bin/node
/**
 * a script that prints all characters of a Star Wars movie:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line
 */
const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const intg of dd) {
    req.get(intg, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
