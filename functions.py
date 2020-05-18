from urllib.request import urlopen
import json

url = 'https://covid19api.io/api/v1'
all_reports = '/AllReports'
by_country = '/ReportsByCountries/'

def get_total():
    request = urlopen(url + all_reports)
    data = json.load(request)
    msg = ''
    msg += 'Total cases: ' + str(data['reports'][0]['cases']) + ' (' + str(data['reports'][0]['table'][0][0]['NewCases']) + ')'
    msg += '\n\nTotal deaths: ' + str(data['reports'][0]['deaths']) + ' (' + str(data['reports'][0]['table'][0][0]['NewDeaths']) + ')'
    msg += '\n\nTotal recovers: ' + str(data['reports'][0]['recovered'])
    msg += '\n\nTotal active cases: ' + str(data['reports'][0]['active_cases'][0]['currently_infected_patients'] + data['reports'][0]['active_cases'][0]['inMidCondition'] + data['reports'][0]['active_cases'][0]['criticalStates'])
    msg += '\n\n    Currently infected: ' + str(data['reports'][0]['active_cases'][0]['currently_infected_patients'])
    msg += '\n\n    In mid condition: ' + str(data['reports'][0]['active_cases'][0]['inMidCondition'])
    msg += '\n\n    Critical states: ' + str(data['reports'][0]['active_cases'][0]['criticalStates'] + data['reports'][0]['closed_cases'][0]['recovered'] + data['reports'][0]['closed_cases'][0]['deaths'])
    msg += '\n\nTotal closed cases: ' + str(data['reports'][0]['closed_cases'][0]['cases_which_had_an_outcome']+data['reports'][0]['closed_cases'][0]['recovered']+ data['reports'][0]['closed_cases'][0]['deaths'])
    msg += '\n\n    Cases with outcome: ' + str(data['reports'][0]['closed_cases'][0]['cases_which_had_an_outcome'])
    msg += '\n\n    Recovered: ' + str(data['reports'][0]['closed_cases'][0]['recovered'])
    msg += '\n\n    Deaths: ' + str(data['reports'][0]['closed_cases'][0]['deaths']) + '\n'
    return msg


def get_deaths():
    request = urlopen(url + all_reports)
    data = json.load(request)
    return '\nTotal deaths: ' + str(data['reports'][0]['deaths']) + '\n'


def get_top():
    request = urlopen(url + all_reports)
    data = json.load(request)
    msg = ''
    for item in data['reports'][0]['table'][0][1]:
        msg += str(item) + ': ' + str(data['reports'][0]['table'][0][1][item]) + '\n\n'
    return msg


def to_string(list):
    str = ''
    for i in range(len(list)):
        str += list[i]
        if i != len(list)-1:
            str += '-'
    return str 


def get_country(country_name):
    if type(country_name) == list:
        country_name = to_string(country_name)
    
    country_name = country_name.lower()
    
    if country_name == 'usa':
        country_name = 'us'

    if country_name not in countries:
        return 'Incorrect input. Please try again!'
    
    request = urlopen(url + by_country + country_name)
    data = json.load(request)
    
    msg = ''
    msg += 'Country: ' + country_name.upper()
    msg += '\n\nCases: ' + str(data['report']['cases'])
    msg += '\n\nFlag: ' + str(data['report']['flag'])
    msg += '\n\nDeaths: ' + str(data['report']['deaths'])
    msg += '\n\nRecovers: ' + str(data['report']['recovered'])
    if len(data['report']['active_cases']) != 0:
        msg += '\n\nActive cases: ' + str(data['report']['active_cases'][0]['currently_infected_patients'] 
                                        + data['report']['active_cases'][0]['inMidCondition'] 
                                        + data['report']['active_cases'][0]['criticalStates'])
        msg += '\n\n    Currently infected: ' + str(data['report']['active_cases'][0]['currently_infected_patients'])
        msg += '\n\n    In mid condition: ' + str(data['report']['active_cases'][0]['inMidCondition'])
        msg += '\n\n    Critical states: ' + str(data['report']['active_cases'][0]['criticalStates'])

    if len(data['report']['closed_cases']) != 0:
        msg += '\n\nClosed cases: ' + str(data['report']['closed_cases'][0]['cases_which_had_an_outcome']
                                    + data['report']['closed_cases'][0]['recovered']
                                    + data['report']['closed_cases'][0]['deaths'])
        msg += '\n\n    Cases with outcome: ' + str(data['report']['closed_cases'][0]['cases_which_had_an_outcome'])
        msg += '\n\n    Recovered: ' + str(data['report']['closed_cases'][0]['recovered'])
        msg += '\n\n    Deaths: ' + str(data['report']['closed_cases'][0]['deaths'])

    return msg


countries = [
                'afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'anguilla', 'antigua-and-barbuda', 'argentina', 'armenia', 'aruba', 'australia', 'austria', 'azerbaijan',
                'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bermuda', 'bhutan', 'bolivia', 'bosnia-and-herzegovina', 'botswana', 'brazil', 'british-virgin-islands', 'brunei-darussalam', 'bulgaria', 'burkina-faso', 'burundi',
                'cabo-verde', 'cambodia', 'cameroon', 'canada', 'caribbean-netherlands', 'cayman-islands', 'central-african-republic', 'chad', 'channel-islands', 'chile', 'china', 'china-hong-kong-sar', 'china-macao-sar', 'colombia', 'congo', 'costa-rica', 'cote-d-ivoire', 'croatia', 'cuba', 'curacao', 'cyprus', 'czech-republic',
                'democratic-republic-of-the-congo', 'denmark', 'djibouti', 'dominica', 'dominican-republic',
                'ecuador', 'egypt', 'el-salvador', 'equatorial-guinea', 'eritrea', 'estonia', 'ethiopia',
                'faeroe-islands', 'falkland-islands-malvinas', 'fiji', 'finland', 'france', 'french-guiana', 'french-polynesia',
                'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'gibraltar', 'greece', 'greenland', 'grenada', 'guadeloupe', 'guatemala', 'guinea', 'guinea-bissau', 'guyana',
                'haiti', 'holy-see', 'honduras', 'hungary',
                'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'isle-of-man', 'israel', 'italy',
                'jamaica', 'japan', 'jordan',
                'kazakhstan', 'kenya', 'kuwait', 'kyrgyzstan',
                'laos', 'latvia', 'lebanon', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg',
                'macedonia', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'martinique', 'mauritania', 'mauritius', 'mayotte', 'mexico', 'moldova', 'monaco', 'mongolia', 'montenegro', 'montserrat', 'morocco', 'mozambique', 'myanmar',
                'namibia', 'nepal', 'netherlands', 'new-caledonia', 'new-zealand', 'nicaragua', 'niger', 'nigeria', 'norway',
                'oman',
                'pakistan', 'panama', 'papua-new-guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal',
                'qatar',
                'reunion', 'romania', 'russia', 'rwanda',
                'saint-barthelemy', 'saint-kitts-and-nevis', 'saint-lucia', 'saint-martin', 'saint-vincent-and-the-grenadines', 'san-marino', 'saudi-arabia', 'senegal', 'serbia', 'seychelles', 'sierra-leone', 'singapore', 'sint-maarten', 'slovakia', 'slovenia', 'somalia', 'south-africa', 'south-korea', 'spain', 'sri-lanka', 'state-of-palestine', 'sudan', 'suriname', 'swaziland', 'sweden', 'switzerland', 'syria',
                'taiwan', 'tanzania', 'thailand', 'timor-leste', 'togo', 'trinidad-and-tobago', 'tunisia', 'turkey', 'turks-and-caicos-islands',
                'uganda', 'uk', 'ukraine', 'united-arab-emirates', 'uruguay', 'us', 'uzbekistan',
                'venezuela', 'vietnam',
                'zambia', 'zimbabwe'
            ]

def list_countries():
    msg = 'Countries: '
    for i in range(len(countries)):
        country = countries[i].capitalize()
        msg += '\n' + str(i + 1) + ': ' + country
    msg += '\nPlease choose a country and enter its name'
    return msg