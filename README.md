# chatbot
hello
NOTE: The web app is deployed on a free server which goes into sleep mode and takes about 10s for boot up, once loaded the bot will work as expected.

Demo 2

Usage Guide
When a user asks for a recommendation, the bot activates the a module that handles such requests, following are commands to trigger that module

For Movie Recommendations enter "movies like movie-title" command.
>> movies like rockstar
For Movie Plots enter "about movie-title" command.
>> about zindagi na milegi dobara
Easter Eggs.
>> who are you?
>> what did you do all day?
Casual conversation.
>> how are you?
>> do you have friends?
>> you're mean
Architecture
This is an image

Extended Features
Feature     	Description
Unk Handler	Implemented a module to replace out of vocabulary words (words not seen in training) detected in a user request with 'unk' to gain maximum information out of the request, the UNK percent in the bot response refers to that.
Movie Title Spellings	To handle variations of movie title spelling, implemented a module that computes Levenstein distance between user input movie title and the ones in the database to capture appropriate movie title given by the user.
Profanity Handler	Implemented an intent that tries to detect swear words in a user's request.
Model Training
The model training part of the projects is in the moviebot-mike-training repository.

Setup Instructions
This repo is currently in a development state, I'm working on setting up an easy method to run this application on local machines, will update this section soon. In the meantime check out the moviebot-mike-training repository.
