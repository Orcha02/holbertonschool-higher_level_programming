#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedge_antilles = '18';
let num_movies = 0;

request(url, function (error, response, body) {
    if (error) {
	console.log(error);
    } else {
	const films = JSON.parse(body).results;
	for (const movie_info in films) {
            const characters = films[movie_info].characters;
            for (const character_id in characters)
		if (characters[character_id].includes(wedge_antilles)) {
                    num_movies++;
		}
	}
	console.log(num_movies);
    }
});
