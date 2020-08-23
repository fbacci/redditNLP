import os
import logging, requests, praw
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from reddit import getReddit
from preprocessing import clean
from classification import classification

TOKEN = os.environ['TELEGRAM_TOKEN']

reddit = getReddit()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def start(update, context):
    # start message
    update.message.reply_text('Hello! This is the Reddit Post Classification bot. To get the right subreddit of a post, '
                                'please send its link and you will get your response.\n\nTo stop the bot just type \"/stop\".')

def stop(update, context):
    user = update.message.from_user
    logger.info("Stopped conversation by %s", user.first_name)
    update.message.reply_text('See you soon :)',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def checkPost(post):
    cleanedPost = clean(post)
    return classification(cleanedPost)

def getSubreddit(update, context):
    update.message.reply_text("Got it! You will get your response very soon.")
    submission = reddit.submission(url=update.message.text)
    prediction = checkPost(submission.selftext)
    update.message.reply_text("I think this post should belong to " + prediction[0] + " subreddit.")

    return 1

def main():
    # start the bot
    updater = Updater(TOKEN, use_context=True)

    # dispatcher
    dp = updater.dispatcher

    # other commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(MessageHandler(Filters.regex("^[https]|^[http]|^[www]"), getSubreddit))

    # start bot
    updater.start_polling()

    # run the bot until Ctrl-C is pressed
    updater.idle()

if __name__ == '__main__':
    main()