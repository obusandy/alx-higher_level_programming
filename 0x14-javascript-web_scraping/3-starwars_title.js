#!/usr/bin/node
/**
 * Below is a script that prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 * The first argument is the movie ID
 * using the Star wars API with the endpoint
 * https://swapi-api.alx-tools.com/api/films/:id
 */

const request = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
