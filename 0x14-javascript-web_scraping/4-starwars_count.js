#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedgeAntilles = '18';
let numMovies = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    for (const movieInfo in films) {
      const characters = films[movieInfo].characters;
      for (const characterId in characters) {
        if (characters[characterId].includes(wedgeAntilles)) {
          numMovies++;
        }
      }
    }
    console.log(numMovies);
  }
});
