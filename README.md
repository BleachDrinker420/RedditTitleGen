# RedditTitleGen

A quick-ish project i made to generate [arabfunny](https://www.reddit.com/r/arabfunny/ "arabfunny") titles, but that can be used on any subreddit to replicate titles.

## Requirements
[`Python 3.5 - 3.7`](https://www.python.org/downloads/release/python-377/ "Python 3.7") 3.8 or above is not supported by tensorflow currently.

[`Tensorflow >= 2.1.0`](https://www.tensorflow.org/install/pip "Tensorflow >= 2.1.0") (Preferably with GPU support)

[`textgenrnn`](https://github.com/minimaxir/textgenrnn "textgenrnn") The main library the code is built on.

[`requests`](https://pypi.org/project/requests/ "requests") Used to scrape the reddit api to get the titles

## Usage
#### Scraper
`Pretty straightforward, just run it and put in a subreddit, and it will return the titles in "titles.json"`

---
#### Train
`Once you collected the titles, you need to train the network, run train.py and it will ask for a model (leave blank if you are training for the first time, or put the file name of a previous model in that folder if you are retraining), then it will ask for epochs, which are how many times it will train on the data, then it will begin training`

---
#### Generator
`After you are done training, you can generate new texts, to do this run generator.py and put the filename of the model you trained as the model, the text setting is how many words it output and the creativity setting is how much "Generated" text is in the text. The text output should be in output.txt`


