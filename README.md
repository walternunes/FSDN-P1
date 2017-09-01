# FSDN-P1
This project is part of Full Stack Developer Nanodegree


### About
Project 1: Develop a website that show movies and play trailers
This application uses the TMDB API to fetch the movie data if an account Key were provided. In case of not providing API key the movie data will be loaded by static CSV file. 

### Objective
Write an application using object-oriented Python. Make this application serve HTML via a web server.

### How to run the project
* Clone the repo using ```git clone https://github.com/walternunes/FSDN-P1.git``` and ```cd``` into the folder
* Install tmbd3 dependency by using ```pip install tmdb3``` in shell
* If you want to fetch movie data from the TMDB API it is necessary to aquire an API Key first. It is free and you can aquire signing up at https://www.themoviedb.org/account/signup?language=en. After you get the key, please edit the file ```entertainment_center.py``` and ADD it at ```API_KEY```
* In no API Key scenario, movie data will be loaded from a static CSV file
* Run ```entertainment_center.py```

### Output
A result demo can be checked [here](https://walternunes.github.io/FSDN-P1/fresh_tomatoes.html)
