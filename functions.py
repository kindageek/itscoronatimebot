from urllib.request import urlopen
from datetime import datetime
from emoji import emojize
import json
import manager
# import urllib to open urls, datetime to get current date, emoji, json libraries and manager.py file

# function to get string formatted number with commas
def get_str_num(num):
    string = str('{:,}'.format(num))
    return string

# function to get the name of the month by its number
def get_month_name(num):
    months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    return months[num]

def getDateTime(longDate):
    myNumber = float(longDate)
    return str(datetime.fromtimestamp(myNumber / 1e3).strftime('%d.%m.%Y %H:%M:%S'))

# function to get proper name of the country
# used when sending country name from API
def get_proper_name(country_name):
    proper_name = ''

    # lower the country name first
    country_name = country_name.lower()

    # check different cases for unique names
    # otherwise, split the name by hyphen, and join it to one string, capitalizing the words except several ones
    if country_name == 'us' or country_name == 'usa':
        proper_name = 'USA'
    elif country_name == 'uk':
        proper_name = 'UK'
    elif country_name == 'uae':
        proper_name = 'United Arab Emirates'
    elif country_name == 'china-hong-kong-sar':
        proper_name = 'Hong Kong'
    elif country_name == 'china-macao-sar':
        proper_name = 'Macao'
    elif country_name == 'macedonia':
        proper_name = 'North Macedonia'
    elif country_name == 'swaziland':
        proper_name = 'Eswatini'
    elif country_name == 'holy-see':
        proper_name = 'Vatican City'
    else:
        str_list = country_name.split('-')
        for i in range(len(str_list)):
            if str_list[i] not in ['and', 'the', 'of'] and len(str_list[i]) != 1:
                proper_name += str_list[i].capitalize()
            else:
                proper_name += str_list[i]
            if i != len(str_list)-1:
                proper_name += ' '

    return proper_name


# function to get the api name of the country
# used when user inputs country name and the program needs to use it to access its API data
def get_api_name(country_name):
    api_name = ''

    # if the input is list of words, join them with a space beetween
    if type(country_name) is list:
        country_name  = country_name.join(' ').lower()

    # lower the country name
    country_name  = country_name.lower()

    # check different unique cases
    # otherwise, split the words by space and join them with hyphen
    if country_name == 'usa' or country_name == 'united states of america':
        api_name = 'us'
    elif country_name == 'kz':
        api_name = 'kazakhstan'
    elif country_name == 'hong kong':
        api_name = 'china-hong-kong-sar'
    elif country_name == 'macao':
        api_name = 'china-macao-sar'
    elif country_name == 'vatican' or country_name == 'vatican city':
        api_name = 'holy-see'
    elif country_name == 'hong kong':
        api_name = 'china-hong-kong-sar'
    elif country_name == 'eswatini':
        api_name = 'swaziland'
    elif country_name == 'north macedonia':
        api_name = 'macedonia'
    else:
        api_name = '-'.join(country_name.split(' '))

    return api_name


# function to get total statistics from the API
def get_total():
    #get data of total statistics from manager.py file
    data = manager.get_all_data()

    # get the current date in formatted string
    # date = '{} {}, {}'.format(get_month_name(datetime.date(datetime.now()).month), str(datetime.date(datetime.now()).day), str(datetime.date(datetime.now()).year))
    date = getDateTime(data['updated'])

    # initialize message and add all necessary data
    msg = 'Date: {}'.format(date)
    msg += '\n\n{} {} {} (+{})'.format(emojize(':exclamation:', True),'Cases:', get_str_num(data['cases']), get_str_num(data['todayCases']))
    msg += '\n\n{} {} {} (+{})'.format(emojize(':skull:', True),'Deaths:', get_str_num(data['deaths']), get_str_num(data['todayDeaths']))
    msg += '\n\n{} {} {} (+{})'.format(emojize(':v:', True),'Recovered:', get_str_num(data['recovered']), get_str_num(data['todayRecovered']))

    msg += '\n\n{} {} {}'.format(emojize(':mask:', True), 'Active cases:', get_str_num(data['active']))
    msg += '\n\n{} {} {}'.format(emojize('       :small_red_triangle:', True), 'Critical:', get_str_num(data['critical']))

    msg += '\n\n{} {} {}'.format(emojize(':chart_with_upwards_trend:', True), 'World population:',  get_str_num(data['population']))
    msg += '\n\nSource: www.worldometers.info'
    # print(msg)
    return msg


# function to get the data for the country with the largest number of cases of COVID-19
def get_top():
    #get data of top statistics from manager.py file
    data = manager.get_top_data()

    # get the current date in formatted string
    date = getDateTime(data['updated'])

    # initialize message and add all necessary data
    msg = 'Date: {}'.format(date)
    msg += '\n\n{} {} {} ({})'.format(emojize(':round_pushpin:', True), 'Country:', get_proper_name(data['country']), data['continent'])
    msg += '\n\n{} {} {} (+{})'.format(emojize(':exclamation:', True), 'Cases:', get_str_num(data['cases']), get_str_num(data['todayCases']))
    msg += '\n\n{} {} {} (+{})'.format(emojize(':skull:', True), 'Deaths:', get_str_num(data['deaths']), get_str_num(data['todayDeaths']))
    msg += '\n\n{} {} {} (+{})'.format(emojize(':v:', True), 'Recovered:', get_str_num(data['recovered']), get_str_num(data['todayRecovered']))
    msg += '\n\n{} {} {}'.format(emojize(':mask:', True), 'Active Cases:', get_str_num(data['active']))
    msg += '\n\n{} {} {}'.format(emojize('       :small_red_triangle:', True), 'Critical:', get_str_num(data['critical']))
    msg += '\n\n{} {} {}'.format(emojize(':chart_with_upwards_trend:', True), 'Population:', get_str_num(data['population']))
    msg += '\n\n{} {} {}'.format(emojize(':syringe:', True), 'Tests:', get_str_num(data['tests']))
    msg += '\n\n{} {} {}'.format(emojize(':pushpin:', True), 'Flag:', data['countryInfo']['flag'])
    msg += '\n\nSource: www.worldometers.info'
    # print(msg)
    return msg


# function to get statistics for the specific country
def get_country(country_name):

    # get api name of the country
    country_name = get_api_name(country_name)

    # if the country name is not in the list of available countries, return error message
    if not manager.in_countries(country_name):
        return emojize(':anger: ', True) + 'Incorrect input. Please try again!'

    # get the data for the country from manager.py file
    data = manager.get_country_data(country_name)

    # get the current date in formatted string
    date = getDateTime(data['updated'])

    # initialize message and add all necessary data
    msg = 'Date: {}'.format(date)
    msg += '\n\n{} {} {} ({})'.format(emojize(':round_pushpin:', True), 'Country:', get_proper_name(data['country']), data['continent'])
    msg += '\n\n{} {} {} (+{})'.format(emojize(':exclamation:', True), 'Cases:', get_str_num(data['cases']), get_str_num(data['todayCases']))
    msg += '\n\n{} {} {} (+{})'.format(emojize(':skull:', True), 'Deaths:', get_str_num(data['deaths']), get_str_num(data['todayDeaths']))
    msg += '\n\n{} {} {} (+{})'.format(emojize(':v:', True), 'Recovered:', get_str_num(data['recovered']), get_str_num(data['todayRecovered']))
    msg += '\n\n{} {} {}'.format(emojize(':mask:', True), 'Active Cases:', get_str_num(data['active']))
    msg += '\n\n{} {} {}'.format(emojize('       :small_red_triangle:', True), 'Critical:', get_str_num(data['critical']))
    msg += '\n\n{} {} {}'.format(emojize(':chart_with_upwards_trend:', True), 'Population:', get_str_num(data['population']))
    msg += '\n\n{} {} {}'.format(emojize(':syringe:', True), 'Tests:', get_str_num(data['tests']))
    msg += '\n\n{} {} {}'.format(emojize(':pushpin:', True), 'Flag:', data['countryInfo']['flag'])
    msg += '\n\nSource: www.worldometers.info'
    # print(msg)
    return msg


# function to list all country names
def list_countries():
    # initialize message
    msg = '{}{}\n'.format(emojize(':round_pushpin:', True), 'Countries:')

    # get the list of countries from manager.py file
    countries = manager.get_list_of_countries()

    # traverse the list and get proper name of each country
    for i in range(len(countries)):
        country = get_proper_name(countries[i])
        msg += '\n{:>3}: {}'.format(i + 1, country)

    msg += '\n\n{}{}'.format('Please choose /country and enter country\'s name', emojize(':point_down:', True))
    # print(msg)
    return msg

print(get_country('kazakhstan'))