import logging
import config
import telegram
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from emoji import emojize
from telegram.ext import Updater, RegexHandler, CommandHandler, MessageHandler, ConversationHandler, Filters
from functions import get_total, get_top, get_country, list_countries

TOKEN = config.token

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

MAIN, COUNTRY = range(2)
custom_keyboard = [['/total'], ['/top'], ['/country'], ['/list'], ['/help']] 

def start(update, context):
    context.bot.send_chat_action(chat_id = update.message.chat_id , 
                                action = telegram.ChatAction.TYPING)
    
    msg = emojize(' :ghost:', True) + 'Hello! It\'s corona time '
    msg += '\n\nGet the most recent COVID-19 updates in an easier way with me.'
    msg += '\n\n' + emojize(':round_pushpin:', True) + 'Available commands:'
    msg += '\n\n/total - get the total statistics of the world for today\'s date'
    msg += '\n\n/country - input a country name to get the data for this country'
    msg += '\n\n/top - get the country statistics with the largest number of cases'
    msg += '\n\n/list - list all country names'
    msg += '\n\n/help - list all available commands'

    context.bot.send_message(chat_id = update.effective_chat.id, 
                             text = msg,  
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True), 
                             parse_mode = telegram.ParseMode.MARKDOWN)    
    reply_markup = ReplyKeyboardRemove()
    # return MAIN


def total(update, context):
    context.bot.send_chat_action(chat_id = update.message.chat_id , 
                                 action = telegram.ChatAction.TYPING)
    msg = get_total()
    context.bot.send_message(chat_id = update.effective_chat.id, 
                             text = msg,  
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True), 
                             parse_mode = telegram.ParseMode.MARKDOWN)    
    reply_markup = ReplyKeyboardRemove()
    # return MAIN


def country(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id , 
                                 action = telegram.ChatAction.TYPING)
    msg = 'Please enter a country name: ' + emojize(':point_down:', True)
    context.bot.send_message(chat_id = update.effective_chat.id, 
                             text = msg, 
                             parse_mode = telegram.ParseMode.MARKDOWN)    
    reply_markup = ReplyKeyboardRemove()
    # return COUNTRY


def get_country_data(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id , 
                                 action = telegram.ChatAction.TYPING)
    msg = get_country(update.message.text)
    context.bot.send_message(chat_id = update.effective_chat.id, 
                             text = msg,  
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True), 
                             parse_mode = telegram.ParseMode.MARKDOWN)    
    reply_markup = ReplyKeyboardRemove()  
    # return MAIN


def top(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id , 
                                 action = telegram.ChatAction.TYPING)
    msg = get_top()
    context.bot.send_message(chat_id = update.effective_chat.id, 
                             text = msg,  
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True), 
                             parse_mode = telegram.ParseMode.MARKDOWN)    
    reply_markup = ReplyKeyboardRemove()
    # return MAIN


def help(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id , 
                                 action = telegram.ChatAction.TYPING)
    
    msg = emojize(':round_pushpin:', True) + 'Available commands:'
    msg += '\n\n/total - get the total statistics of the world for today\'s date'
    msg += '\n\n/country - input a country name to get the data for this country'
    msg += '\n\n/top - get the country statistics with the largest number of cases'
    msg += '\n\n/list - list all country names'
    msg += '\n\n/help - list all available commands'
    
    context.bot.send_message(chat_id = update.effective_chat.id, 
                             text = msg,  
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True), 
                             parse_mode = telegram.ParseMode.MARKDOWN)    
    reply_markup = ReplyKeyboardRemove()
    # return MAIN


def list_all(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id , 
                                 action = telegram.ChatAction.TYPING)
    msg = list_countries()
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id = update.effective_chat.id, 
                             text = msg,  
                             reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True), 
                             parse_mode = telegram.ParseMode.MARKDOWN)    
    reply_markup = ReplyKeyboardRemove()
    # return MAIN


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def unknown(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id , 
                                 action = telegram.ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text = emojize(':sweat_smile: ', True) + "Unknown command, try /help", 
                             reply_markup=ReplyKeyboardMarkup(custom_keyboard), 
                             parse_mode = telegram.ParseMode.MARKDOWN)
    reply_markup = ReplyKeyboardRemove()
    return MAIN


def cancel(update, context):
    return ConversationHandler.END


def main():
    updater = Updater(token = TOKEN, use_context = True)
    dispatcher = updater.dispatcher

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
    
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()