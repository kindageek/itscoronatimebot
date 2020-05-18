# README

# It's Corona Time Telegram Bot

[@its_corona_time_bot](https://t.me/its_corona_time_bot) is a beta version of a Telegram Bot which will help to get updated real-time data on coronavirus cases from the worldometers page and other important websites, provided by the most reputable organizations and statistical offices in the world. 

The bot is made using Python 3.7 and [python-telegram-bot](https://github.com/python-telegram-bot) API. 

The API for COVID-19 information is taken from [Chris Michael's GitHub page](https://github.com/ChrisMichaelPerezSantiago/covid19).

## How to use it?

Go to [@its_corona_time_bot](https://t.me/its_corona_time_bot)

Press `/start` and choose on of the available commands.

## Code

There are two significant .py files:

1. [`main.py`](http://main.py) is responsible for bot's operations and command handling
    - It connects to the bot using bot's unique token from [`config.py`](http://config.py) file
    - It uses python-telegram-bot API and telegram.ext for all necessary functionality of the bot
2. [`functions.py`](http://functions.py) is responsible for scraping data from coronavirus API and returning the text with a requested data
    - There are two major extensions for the coronavirus API url
        1. '/AllReports'
        2. '/ReportsByCountries/'
    - /AllReports is used to get data for total statistics of the current day
        - It is used in get_total(), get_death() and get_top() functions
    - /ReportsByCountries is used to get specific information of a country whose name was entered by a user

## Hosting

This telegram bot is being hosted on [Heroku.com](http://heroku.com) for non-stop performance
