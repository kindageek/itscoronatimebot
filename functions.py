from urllib.request import urlopen
from datetime import datetime
from emoji import emojize
import json
import manager

def get_str_num(num):
    string = str('{:,}'.format(num))
    return string


def get_month_name(num):
    months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    return months[num]


def get_proper_name(country_name):
    proper_name = ''
    country_name = country_name.lower()
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


def get_dict_name(country_name):
    dict_name = ''
    if type(country_name) is list:
        country_name  = country_name.join(' ').lower()

    country_name  = country_name.lower()

    if country_name == 'usa' or country_name == 'united states of america':
        dict_name = 'us'
    elif country_name == 'kz':
        dict_name = 'kazakhstan'
    elif country_name == 'hong kong':
        dict_name = 'china-hong-kong-sar'
    elif country_name == 'macao':
        dict_name = 'china-macao-sar'
    elif country_name == 'vatican' or country_name == 'vatican city':
        dict_name = 'holy-see'
    elif country_name == 'hong kong':
        dict_name = 'china-hong-kong-sar'
    elif country_name == 'eswatini':
        dict_name = 'swaziland'
    elif country_name == 'north macedonia':
        dict_name = 'macedonia'
    else:
        dict_name = '-'.join(country_name.split(' '))
    
    return dict_name


def get_total():
    data = manager.get_all_data()
    date = '{} {}, {}'.format(get_month_name(datetime.date(datetime.now()).month), str(datetime.date(datetime.now()).day), str(datetime.date(datetime.now()).year))
    msg = 'Date: {}'.format(date)
    msg += '\n\n{}{} {} ({})'.format(emojize(':exclamation:', True),'Total Cases:', get_str_num(data['reports'][0]['cases']), str(data['reports'][0]['table'][0][0]['NewCases']))
    msg += '\n\n{}{} {} ({})'.format(emojize(':skull:', True),'Total Deaths:', get_str_num(data['reports'][0]['deaths']), str(data['reports'][0]['table'][0][0]['NewDeaths']))
    msg += '\n\n{}{} {}'.format(emojize(':v:', True),'Total Recovers:', get_str_num(data['reports'][0]['recovered']))
    
    total_active_cases = get_str_num(data['reports'][0]['active_cases'][0]['currently_infected_patients'] + data['reports'][0]['active_cases'][0]['inMidCondition'] + data['reports'][0]['active_cases'][0]['criticalStates'])
    
    msg += '\n\n{}{} {}'.format(emojize(':mask:', True), 'Total active cases:', get_str_num(data['reports'][0]['active_cases'][0]['currently_infected_patients']))
    msg += '\n\n{}{} {}'.format(emojize('       :small_red_triangle:', True), 'In mid condition:', get_str_num(data['reports'][0]['active_cases'][0]['inMidCondition']))
    msg += '\n\n{}{} {}'.format(emojize('       :small_red_triangle:', True), 'Critical states:', get_str_num(data['reports'][0]['active_cases'][0]['criticalStates']))
    
    msg += '\n\n{}{} {}'.format(emojize(':lock:', True), 'Total closed cases:',  get_str_num(data['reports'][0]['closed_cases'][0]['cases_which_had_an_outcome']))
    msg += '\n\nSource: www.worldometers.info'
    # print(msg)
    return msg


def get_top():
    data = manager.get_all_data()
    date = '{} {}, {}'.format(get_month_name(datetime.date(datetime.now()).month), str(datetime.date(datetime.now()).day), str(datetime.date(datetime.now()).year))
    msg = 'Date: {}'.format(date)
    msg += '\n\n{}{} {}'.format(emojize(':round_pushpin:', True), 'Country:', get_proper_name(data['reports'][0]['table'][0][1]['Country']))
    msg += '\n\n{}{} {} ({})'.format(emojize(':exclamation:', True), 'Total Cases:', (data['reports'][0]['table'][0][1]['TotalCases']),(data['reports'][0]['table'][0][1]['NewCases']))
    msg += '\n\n{}{} {} ({})'.format(emojize(':skull:', True), 'Total Deaths:', (data['reports'][0]['table'][0][1]['TotalDeaths']), (data['reports'][0]['table'][0][1]['NewDeaths']))
    msg += '\n\n{}{} {}'.format(emojize(':v:', True), 'Total Recovers:', (data['reports'][0]['table'][0][1]['TotalRecovered']))
    msg += '\n\n{}{} {}'.format(emojize(':mask:', True), 'Active Cases:', (data['reports'][0]['table'][0][1]['ActiveCases']))
    msg += '\n\n{}{} {}'.format(emojize(':chart_with_upwards_trend:', True), 'Population:', (data['reports'][0]['table'][0][1]['Population']))
    msg += '\n\n{}{} {}'.format(emojize(':syringe:', True), 'Total Tests:', (data['reports'][0]['table'][0][1]['TotalTests']))
    msg += '\n\nSource: www.worldometers.info'
    # print(msg)
    return msg


def get_country(country_name):
    country_name = get_dict_name(country_name)

    if not manager.in_countries(country_name):
        return emojize(':anger: ', True) + 'Incorrect input. Please try again!'
    
    
    data = manager.get_country_data(country_name)

    date = '{} {}, {}'.format(get_month_name(datetime.date(datetime.now()).month), str(datetime.date(datetime.now()).day), str(datetime.date(datetime.now()).year))
    msg = 'Date: {}'.format(date)
    
    if data['report']['country'] is not None: 
        msg += '\n\n{}{} {}'.format(emojize(':round_pushpin:', True), 'Country:', get_proper_name(data['report']['country']))
    
    if data['report']['cases'] is not None: 
        msg += '\n\n{}{} {}'.format(emojize(':exclamation:', True), 'Cases:', get_str_num(data['report']['cases']))
    
    if data['report']['deaths'] is not None: 
        msg += '\n\n{}{} {}'.format(emojize(':skull:', True), 'Deaths:', get_str_num(data['report']['deaths']))
    
    if data['report']['recovered'] is not None: 
        msg += '\n\n{}{} {}'.format(emojize(':v:', True), 'Recovers:', get_str_num(data['report']['recovered']))
    
    if len(data['report']['active_cases']) != 0:
        active = 0 
        midCondition = 0 
        critical = 0
        
        if data['report']['active_cases'][0]['currently_infected_patients'] is not None:
            active = data['report']['active_cases'][0]['currently_infected_patients']
        if data['report']['active_cases'][0]['inMidCondition'] is not None:
            midCondition = data['report']['active_cases'][0]['inMidCondition']
        if data['report']['active_cases'][0]['criticalStates'] is not None:
            critical = data['report']['active_cases'][0]['criticalStates']
        
        msg += '\n\n{}{} {}'.format(emojize(':mask:', True), 'Active cases: ', get_str_num(active))
        
        if midCondition != 0:
            msg += '\n\n{}{} {}'.format(emojize('       :chart_with_upwards_trend:', True), 'In mid condition: ', get_str_num(midCondition))
        else:
            msg += '\n\n{}{} {}'.format(emojize('       :chart_with_upwards_trend:', True), 'In mid condition: N/A')
        
        if critical != 0:
            msg += '\n\n{}{} {}'.format(emojize('       :chart_with_upwards_trend:', True), 'Critical states: ', get_str_num(critical))
        else:
            msg += '\n\n{}{}'.format(emojize('       :chart_with_upwards_trend:', True), 'Critical states: N/A')
    
    msg += '\n\nSource: www.worldometers.info'
    # print(msg)
    return msg


def list_countries():
    msg = '{}{}\n'.format(emojize(':round_pushpin:', True), 'Countries:')
    
    countries = manager.get_list_of_countries()
    for i in range(len(countries)):
        country = get_proper_name(countries[i])
        msg += '\n{:>3}: {}'.format(i + 1, country)
    
    msg += '\n\n{}{}'.format('Please choose /country and enter country\'s name', emojize(':point_down:', True))
    # print(msg)
    return msg