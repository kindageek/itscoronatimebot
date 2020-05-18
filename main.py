import logging
import config
import telegram
from emoji import emojize
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from functions import get_total, get_deaths, get_top, get_country, list_countries

TOKEN = config.token

updater = Updater(token = TOKEN, use_context = True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def start(update, context):
    msg = 'Hello! It\'s corona time ' + emojize(' :ghost:') + '\n\n'
    msg += 'Get the most recent COVID-19 updates in an easier way with me.\n\n'
    msg += 'Available commands:\n'
    msg += '/total - get the total statistics of the world for today\'s date\n'
    msg += '/country + [country_name] - input a country name to get the data for this country\n'
    msg += '/top - get the country statistics with the largest number of cases\n'
    msg += '/deaths - get the statistics for total deaths\n'
    msg += '/list - list all country names'
    context.bot.send_message(chat_id = update.effective_chat.id, text = msg, parseMode = 'MARKDOWN')

def total(update, context):
    msg = get_total()
    context.bot.send_message(chat_id = update.effective_chat.id, text = msg)

def country(update, context):
    country_name = " ".join(context.args)
    msg = get_country(country_name)
    context.bot.send_message(chat_id = update.effective_chat.id, text = msg)

def top(update, context):
    msg = get_top()
    context.bot.send_message(chat_id = update.effective_chat.id, text = msg)

def deaths(update, context):
    msg = get_deaths()
    context.bot.send_message(chat_id = update.effective_chat.id, text = msg)

def options(update, context):
    msg = 'Available commands:\n'
    msg += '/total - get the total statistics of the world for today\'s date\n'
    msg += '/country + [country_name] - input a country name to get the data for this country\n'
    msg += '/top - get the country statistics with the largest number of cases\n'
    msg += '/deaths - get the statistics for total deaths\n'
    msg += '/list - list all country names'
    context.bot.send_message(chat_id = update.effective_chat.id, text = msg)

def list(update, context):
    msg = list_countries()
    context.bot.send_message(chat_id = update.effective_chat.id, text = msg)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def main():
    start_handler = CommandHandler('start', start)
    total_handler = CommandHandler('total', total)
    country_handler = CommandHandler('country', country)
    top_handler = CommandHandler('top', top)
    deaths_handler = CommandHandler('deaths', deaths)
    options_handler = CommandHandler('options', options)
    list_handler = CommandHandler('list', list)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(total_handler)
    dispatcher.add_handler(country_handler)
    dispatcher.add_handler(top_handler)
    dispatcher.add_handler(deaths_handler)
    dispatcher.add_handler(options_handler)
    dispatcher.add_handler(list_handler)
    dispatcher.add_handler(echo_handler)

    dispatcher.add_error_handler(error)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)
    
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()