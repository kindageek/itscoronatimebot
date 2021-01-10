from urllib.request import urlopen, Request
import json
import ast
# import urllib to open urls and json library

# url of the api
URL = 'https://corona.lmao.ninja/v3/covid-19'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

# api path extensions
all_reports = '/all'
by_country = '/countries/'

# list of the countries, 205 entries
countries = [
    'afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'anguilla', 'antigua-and-barbuda', 'argentina', 'armenia', 'aruba', 'australia', 'austria', 'azerbaijan',
    'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bermuda', 'bhutan', 'bolivia', 'bosnia-and-herzegovina', 'botswana', 'brazil', 'british-virgin-islands', 'brunei-darussalam', 'bulgaria', 'burkina-faso', 'burundi',
    'cabo-verde', 'cambodia', 'cameroon', 'canada', 'caribbean-netherlands', 'cayman-islands', 'central-african-republic', 'chad', 'channel-islands', 'chile', 'china', 'china-hong-kong-sar', 'china-macao-sar', 'colombia', 'congo', 'costa-rica', 'cote-d-ivoire', 'croatia', 'cuba', 'curacao', 'cyprus', 'czech-republic',
    'democratic-republic-of-the-congo', 'denmark', 'djibouti', 'dominica', 'dominican-republic',
    'ecuador', 'egypt', 'el-salvador',  'swaziland', 'equatorial-guinea', 'eritrea', 'estonia', 'ethiopia',
    'faeroe-islands', 'falkland-islands-malvinas', 'fiji', 'finland', 'france', 'french-guiana', 'french-polynesia',
    'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'gibraltar', 'greece', 'greenland', 'grenada', 'guadeloupe', 'guatemala', 'guinea', 'guinea-bissau', 'guyana',
    'haiti', 'holy-see', 'honduras', 'hungary',
    'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'isle-of-man', 'israel', 'italy',
    'jamaica', 'japan', 'jordan',
    'kazakhstan', 'kenya', 'kuwait', 'kyrgyzstan',
    'laos', 'latvia', 'lebanon', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg',
    'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'martinique', 'mauritania', 'mauritius', 'mayotte', 'mexico', 'moldova', 'monaco', 'mongolia', 'montenegro', 'montserrat', 'morocco', 'mozambique', 'myanmar',
    'namibia', 'nepal', 'netherlands', 'new-caledonia', 'new-zealand', 'nicaragua', 'niger', 'nigeria', 'macedonia', 'norway',
    'oman',
    'pakistan', 'panama', 'papua-new-guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal',
    'qatar',
    'reunion', 'romania', 'russia', 'rwanda',
    'saint-barthelemy', 'saint-kitts-and-nevis', 'saint-lucia', 'saint-martin', 'saint-vincent-and-the-grenadines', 'san-marino', 'saudi-arabia', 'senegal', 'serbia', 'seychelles', 'sierra-leone', 'singapore', 'sint-maarten', 'slovakia', 'slovenia', 'somalia', 'south-africa', 'south-korea', 'south-sudan', 'spain', 'sri-lanka', 'state-of-palestine', 'sudan', 'suriname', 'sweden', 'switzerland', 'syria',
    'taiwan', 'tanzania', 'thailand', 'timor-leste', 'togo', 'trinidad-and-tobago', 'tunisia', 'turkey', 'turks-and-caicos-islands',
    'uganda', 'uk', 'ukraine', 'united-arab-emirates', 'uruguay', 'us', 'uzbekistan',
    'venezuela', 'vietnam',
    'zambia', 'zimbabwe'
]

# function to get url of the API data of the given country


def get_url_by_country(country_name):
    by_country_url = URL + by_country + country_name
    return by_country_url


# function to get url of the API data of total statistics
def get_url_all_reports():
    all_reports_url = URL + all_reports
    return all_reports_url


# function to get the list of countries
def get_list_of_countries():
    return countries


# function to check if the given country is in the list
def in_countries(country_name):
    return country_name in countries


def get_request(url):
    return Request(url=url, headers=HEADERS)


def get_object_data(data_str):
    return ast.literal_eval(data_str.decode('utf-8'))


# function to get the data of total statistics
def get_all_data():
    url = get_url_all_reports()
    request = get_request(url)
    data = urlopen(request).read()
    data = get_object_data(data)
    return data


def get_all_countries():
    url = URL + by_country
    request = get_request(url)
    data = urlopen(request).read()
    data = data.decode('utf-8')
    # data = json.dumps(data)
    # data = json.loads(data)
    # print(len(data))
    data = data.strip('][').split('},{')
    print(data[0])

# function to get the data of top statistics
def get_top_data():
    return get_country_data('usa')

# function to get the data of specific country statistics
def get_country_data(country_name):
    url = get_url_by_country(country_name)
    request = get_request(url)
    data = urlopen(request).read()
    data = get_object_data(data)
    return data
