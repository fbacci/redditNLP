# redditNLP

## What is this?
The **redditNLP** project is the implementation of a telegram bot which is able to classify a reddit post, given its url, in the correct or most suitable subreddit based on the text content. The dataset used to train the classfier is [this](https://www.kaggle.com/mswarbrickjones/reddit-selfposts). Before developing the classifier and the bot, the dataset has been preprocessed using a series of functions, in order to reduce the dimensionality and to normalize the text of the examples it contains. In particular, only a subset of subreddit has been chose for the training, starting from a total of 1000 subreddit to a subset of 300 elements, and the text of each post has been cut to 550 characters, in order to speed up the execution.

This github project contains the version of the classifier implemented using *TF-IDF* and *Naive Bayes*. Out of all the implementations, this one was the most performing one.
The other implementations can be found in the [Google colab notebook](https://colab.research.google.com/drive/1JnbyLIioYVlLbxNfEX0ZXEUKF_ccyGG5?usp=sharing) I used to implement and test all the system. It also includes a brief evaluation table with the accuracy, precision and recall values for all the developed implementations.

### Implemented classifier
- TF-IDF + Naive Bayes
- TF-IDF + Logistic Regression
- Word2Vec + Naive Bayes
- Word2Vec + Logistic Regression

## Files
This project is composed by 4 main files:
- **bot.py**: contains all the codes needed to connect to the Telegram API and to analyze the messages the user sends, after applying all the clean function imported from the processing file. It also has the task to reply with the predicted subreddit;
- **preprocessing.py**: contains all the preprocessing and normalization functions needed to prepare the message to the classification step;
- **classification.py**: imports the TF-IDF and Naive Bayes classifier in order to predict the subreddit. The vectorizer and the classifier has been implemented and executed in the Google colab notebook. I saved the results and uploaded them in the *files* directory;
- **reddit.py**: contains the tokens for the reddit API.

## How to run redditNLP
### Packages needed for the bot:
- python-telegram-bot
- PRAW

### Packages needed for the classification task
- pandas
- nltk
- sklearn
- gensim

In order to execute the bot, you just need to run ```python bot.py```.
Remember to use your API tokens.
