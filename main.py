import logging
import config
import telegram
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from emoji import emojize
from telegram.ext import Updater, RegexHandler, CommandHandler, MessageHandler, ConversationHandler, Filters
from functions import get_total, get_top, get_country, list_countries
# import telegram, telegram.ext, logging, emoji libraries and config, functions files

# get token from config.py file
TOKEN = config.token

# initialize logging and logger to see logs in terminal in case of error
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# initialize two states
MAIN, COUNTRY = range(2)

# initialize custom keyboard list for reply markup
custom_keyboard = [['/total'], ['/top'], ['/country'], ['/list'], ['/help']]

# MAINTENANCE = "WARNING!" + emojize(':warning:', True) + "\n\nThis Telegram Bot is under repair, but it will be back soon :)\n\nThank you!"

# function for handling /start command
def start(update, context):
    # send 'typing ...' action to the chat before doing the work
    context.bot.send_chat_action(chat_id = update.message.chat_id ,
                                action = telegram.ChatAction.TYPING)

    # initialize the message with welcome and option list
    msg = emojize(' :ghost:', True) + 'Hello! It\'s corona time '
    msg += '\n\nGet the most recent COVID-19 updates in an easier way with me.'
    msg += '\n\n' + emojize(':round_pushpin:', True) + 'Available commands:'
    msg += '\n\n/total - get the total statistics of the world for today\'s date'
    msg += '\n\n/country - input a country name to get the data for this country'
    msg += '\n\n/top - get the country statistics with the largest number of cases'
    msg += '\n\n/list - list all country names'
    msg += '\n\n/help - list all available commands'
    # msg += '\n\n' + MAINTENANCE

    # send message to the chat with custom keyboard
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = msg,
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True),
                             parse_mode = telegram.ParseMode.MARKDOWN)

    # remove keyboard after user response
    reply_markup = ReplyKeyboardRemove()


# function to handle /total command
def total(update, context):
    # send 'typing ...' action to the chat before doing the work
    context.bot.send_chat_action(chat_id = update.message.chat_id ,
                                 action = telegram.ChatAction.TYPING)

    # initialize message text by using get_total() command from functions.py file
    msg = get_total()

    # send message to the chat with custom keyboard
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = msg,
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True),
                             parse_mode = telegram.ParseMode.MARKDOWN)

    # remove keyboard after user response
    reply_markup = ReplyKeyboardRemove()


# function to handle /country command
def country(update, context):
    # send 'typing ...' action to the chat before doing the work
    context.bot.send_chat_action(chat_id=update.message.chat_id ,
                                 action = telegram.ChatAction.TYPING)

    # initialize message text and prompt for country name
    msg = 'Please enter a country name: ' + emojize(':point_down:', True)

    # send message to the chat with regular keyboard
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = msg,
                             parse_mode = telegram.ParseMode.MARKDOWN)
    # return COUNTRY


# function to handle /country command name input
def get_country_data(update, context):
    # send 'typing ...' action to the chat before doing the work
    context.bot.send_chat_action(chat_id=update.message.chat_id ,
                                 action = telegram.ChatAction.TYPING)

    # initialize message text by using get_country() command from functions.py file
    msg = get_country(update.message.text)

    # send message to the chat with custom keyboard
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = msg,
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True),
                             parse_mode = telegram.ParseMode.MARKDOWN)

    # remove keyboard after user response
    reply_markup = ReplyKeyboardRemove()
    # return MAIN


# function to handle /top command name input
def top(update, context):
    # send 'typing ...' action to the chat before doing the work
    context.bot.send_chat_action(chat_id=update.message.chat_id ,
                                 action = telegram.ChatAction.TYPING)

    # initialize message text by using get_top() command from functions.py file
    msg = get_top()

    # send message to the chat with custom keyboard
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = msg,
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True),
                             parse_mode = telegram.ParseMode.MARKDOWN)

    # remove keyboard after user response
    reply_markup = ReplyKeyboardRemove()


# function to handle /help command name input
def help(update, context):
    # send 'typing ...' action to the chat before doing the work
    context.bot.send_chat_action(chat_id=update.message.chat_id ,
                                 action = telegram.ChatAction.TYPING)

    # initialize message text
    msg = emojize(':round_pushpin:', True) + 'Available commands:'
    msg += '\n\n/total - get the total statistics of the world for today\'s date'
    msg += '\n\n/country - input a country name to get the data for this country'
    msg += '\n\n/top - get the country statistics with the largest number of cases'
    msg += '\n\n/list - list all country names'
    msg += '\n\n/help - list all available commands'
    # msg += '\n\n' + MAINTENANCE

    # send message to the chat with custom keyboard
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = msg,
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True),
                             parse_mode = telegram.ParseMode.MARKDOWN)

    # remove keyboard after user response
    reply_markup = ReplyKeyboardRemove()


# function to handle /list command name input
def list_all(update, context):
    # send 'typing ...' action to the chat before doing the work
    context.bot.send_chat_action(chat_id=update.message.chat_id ,
                                 action = telegram.ChatAction.TYPING)

    # initialize message text by using list_countries() command from functions.py file
    msg = list_countries()
    # msg += '\n\n' + MAINTENANCE

    # send message to the chat with custom keyboard
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = msg,
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True),
                             parse_mode = telegram.ParseMode.MARKDOWN)

    # remove keyboard after user response
    reply_markup = ReplyKeyboardRemove()


# functiomn to handle errors and print warnings
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# function to handle unknown text and commands from user
def unknown(update, context):
    # send 'typing ...' action to the chat before doing the work
    context.bot.send_chat_action(chat_id=update.message.chat_id ,
                                 action = telegram.ChatAction.TYPING)

    # send message to the chat with custom keyboard
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text = emojize(':sweat_smile: ', True) + "Unknown command, try /help",
                             reply_markup=ReplyKeyboardMarkup(custom_keyboard),
                             parse_mode = telegram.ParseMode.MARKDOWN)

    # remove keyboard after user response
    reply_markup = ReplyKeyboardRemove()


# function to cancel the conversation handler
def cancel(update, context):
    return ConversationHandler.END


# main function
def main():
    # create updater and dispatcher with bot's api token
    updater = Updater(token = TOKEN, use_context = True)
    dispatcher = updater.dispatcher

    # create and add command and message handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('total', total))
    dispatcher.add_handler(CommandHandler('country', country))
    dispatcher.add_handler(CommandHandler('top', top))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('list', list_all))
    # dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    dispatcher.add_handler(MessageHandler(Filters.text, get_country_data))
    # conv_handler = ConversationHandler(
    #     entry_points = [CommandHandler('start', start)],
    #     states = {
    #         MAIN: [CommandHandler('start', start)],
    #         COUNTRY: [MessageHandler(Filters.text, get_country_data)]
    #     },
    #     fallbacks=[CommandHandler('cancel', cancel)]
    # )
    # dispatcher.add_handler(conv_handler)

    # add error handler
    dispatcher.add_error_handler(error)

    # start the bot
    updater.start_polling()
    updater.idle()


# call main function when program has run
if __name__ == '__main__':
    main()