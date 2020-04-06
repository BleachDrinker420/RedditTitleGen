# RedditTitleGen

A quick-ish project i made to generate [arabfunny](https://www.reddit.com/r/arabfunny/ "arabfunny") titles, but that can be used on any subreddit to replicate titles.

## Requirements
[`Python 3.5 - 3.7`](https://www.python.org/downloads/release/python-377/ "Python 3.7") 3.8 or above is not supported by tensorflow currently.

[`Tensorflow >= 2.1.0`](https://www.tensorflow.org/install/pip "Tensorflow >= 2.1.0") (Preferably with GPU support)

[`textgenrnn`](https://github.com/minimaxir/textgenrnn "textgenrnn") The main library the code is built on.

[`requests`](https://pypi.org/project/requests/ "requests") Used to scrape the reddit api to get the titles

## Usage

All of the files can just be clicked on to run without any parameters
### Scraper
The scraper is used to get all the titles from a subreddit.

The settings are:
* `Subreddit` is the subreddit you want to scrape, just the name, without r/
* `Filter Removed Posts` is used to remove deleted or removed posts
* `Date Search` is used to change if you are searching for the "beginning -> now" or "now -> beginning" of the subbreddit
* `Add Flair To Title` is used to add a flair in the post to the title, for example:

*`Example Post`* -> *`[Example Flair] Example Post`*

After you've put in the settings it will start scraping. You can use `Ctrl+C` to stop the scraper after that page and save the titles

---
### Train
The *train.py* File is the file that trains the rnn on the texts you scraped

The settings are:
* `Model File To Load` is the model file that will be loaded, if left black it creates a new model in a new file. If you want to retrain a file, out the model filename in this field, it should be `Model-<unix-timestamp>_weights.hdf5` by default
* `Text File To Train On` is the file to file with titles that you scraped on, (*it will automatically search for text files so you can just press enter if its already found the file*)
* `Epochs To Run` is how many times it will train the rnn, on a decent gpu it will take ~30 sec-5 min/epoch depending on how many lines you have

***TODO: Add batch setting***

Then it will train on the text (*it might take a while loading all the text in*). It will give some example texts after each epoch so you can see when its trained enough

---
### Generator
After you are done training, you can use the generator to generate new texts

The settings are:
* `Model File To Load` is the model file with the trained data, you should find it in the directory when you trained the model
* `Texts To Output` is how many texts out create (*It takes a signifigant amount of time to create each text (2-3 sec/text on a decent gpu)*)
* `Creativity` is how much the ai should guess when creating texts (*0.5-0.8 is usually good*)

Then it will create the texts and output them to output.txt