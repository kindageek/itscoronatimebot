from urllib.request import urlopen
import json

url = 'https://covid19api.io/api/v1'
all_reports = '/AllReports'
by_country = '/ReportsByCountries/'

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

def get_url_by_country(country_name):
    by_country_url = url + by_country + country_name
    return by_country_url


def get_url_all_reports():
    all_reports_url = url + all_reports
    return all_reports_url


def get_list_of_countries():
    return countries


def in_countries(country_name):
    return country_name in countries


def get_all_data():
    url = get_url_all_reports()
    request = urlopen(url)
    data = json.load(request)
    return data


def get_country_data(country_name):
    url = get_url_by_country(country_name)
    request = urlopen(url)
    data = json.load(request)
    return data