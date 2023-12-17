import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests
from io import BytesIO


# URL der Excel-Datei auf GitHub
url = 'https://raw.githubusercontent.com/RomanHaak/streamlit-example/master/CBAM_Estimator_Default_Values.xlsx'


# Anfordern der Datei von GitHub
response = requests.get(url)
response.raise_for_status()  # Stellt sicher, dass der Request erfolgreich war

# Verwendung von Pandas, um die Excel-Datei zu lesen
# Passen Sie 'sheet_name' und Zellenbereich nach Bedarf an
data_frame = pd.read_excel(BytesIO(response.content), sheet_name='Alle_Default_Values_Mit_Nullen', skiprows=5, usecols='A:DR', nrows=277)



st.title('CBAM-Kostenschätzerlo')

countries = [
    'AD - Andorra', 'AE - Vereinigte Arabische Emirate', 'AF - Afghanistan', 
    'AG - Antigua und Barbuda', 'AI - Anguilla', 'AL - Albanien', 
    'AM - Armenien', 'AN - Niederländische Antillen', 'AO - Angola', 
    'AQ - Antarktis', 'AR - Argentinien', 'AS - Amerikanisch-Samoa', 
    'AT - Österreich', 'AU - Australien', 'AW - Aruba', 
    'AX - Ålandinseln', 'AZ - Aserbaidschan', 'BA - Bosnien und Herzegowina', 
    'BB - Barbados', 'BD - Bangladesch', 'BE - Belgien', 
    'BF - Burkina Faso', 'BG - Bulgarien', 'BH - Bahrain', 
    'BI - Burundi', 'BJ - Benin', 'BL - Saint-Barthélemy', 
    'BM - Bermuda', 'BN - Brunei Darussalam', 'BO - Bolivien', 
    'BQ - Bonaire, Sint Eustatius und Saba', 'BR - Brasilien', 'BS - Bahamas', 
    'BT - Bhutan', 'BV - Bouvetinsel', 'BW - Botswana', 
    'BY - Belarus', 'BZ - Belize', 'CA - Kanada', 
    'CC - Kokosinseln', 'CD - Demokratische Republik Kongo', 'CF - Zentralafrikanische Republik', 
    'CG - Kongo', 'CH - Schweiz', 'CI - Elfenbeinküste', 
    'CK - Cookinseln', 'CL - Chile', 'CM - Kamerun', 
    'CN - China', 'CO - Kolumbien', 'CR - Costa Rica', 
    'CS - Serbien und Montenegro', 'CU - Kuba', 'CV - Kap Verde', 
    'CW - Curaçao', 'CX - Weihnachtsinsel', 'CY - Zypern', 
    'CZ - Tschechien', 'DE - Deutschland', 'DJ - Dschibuti', 
    'DK - Dänemark', 'DM - Dominica', 'DO - Dominikanische Republik', 
    'DZ - Algerien', 'EC - Ecuador', 'EE - Estland', 
    'EG - Ägypten', 'EH - Westsahara', 'ER - Eritrea', 
    'ES - Spanien', 'ET - Äthiopien', 'EU - Europäische Gemeinschaft', 
    'FI - Finnland', 'FJ - Fidschi', 'FK - Falklandinseln', 
    'FM - Mikronesien', 'FO - Färöer', 'FR - Frankreich', 
    'GA - Gabun', 'GB - Vereinigtes Königreich', 'GD - Grenada', 
    'GE - Georgien', 'GF - Französisch-Guayana', 'GG - Guernsey', 
    'GH - Ghana', 'GI - Gibraltar', 'GL - Grönland', 
    'GM - Gambia', 'GN - Guinea', 'GP - Guadeloupe', 
    'GQ - Äquatorialguinea', 'GR - Griechenland', 'GS - Südgeorgien und die Südlichen Sandwichinseln', 
    'GT - Guatemala', 'GU - Guam', 'GW - Guinea-Bissau', 
    'GY - Guyana', 'HK - Hongkong', 'HM - Heard- und McDonald-Inseln', 
    'HN - Honduras', 'HR - Kroatien', 'HT - Haiti', 
    'HU - Ungarn', 'ID - Indonesien', 'IE - Irland', 
    'IL - Israel', 'IM - Isle of Man', 'IN - Indien', 
    'IO - Britisches Territorium im Indischen Ozean', 'IQ - Irak', 'IR - Iran', 
    'IS - Island', 'IT - Italien', 'JE - Jersey', 
    'JM - Jamaika', 'JO - Jordanien', 'JP - Japan', 
    'KE - Kenia', 'KG - Kirgisistan', 'KH - Kambodscha', 
    'KI - Kiribati', 'KM - Komoren', 'KN - St. Kitts und Nevis', 
    'KP - Nordkorea', 'KR - Südkorea', 'KW - Kuwait', 
    'KY - Kaimaninseln', 'KZ - Kasachstan', 'LA - Laos', 
    'LB - Libanon', 'LC - St. Lucia', 'LI - Liechtenstein', 
    'LK - Sri Lanka', 'LR - Liberia', 'LS - Lesotho', 
    'LT - Litauen', 'LU - Luxemburg', 'LV - Lettland', 
    'LY - Libyen', 'MA - Marokko', 'MC - Monaco', 
    'MD - Moldawien', 'ME - Montenegro', 'MF - Saint-Martin', 
    'MG - Madagaskar', 'MH - Marshallinseln', 'MK - Nordmazedonien', 
    'ML - Mali', 'MM - Myanmar', 'MN - Mongolei', 
    'MO - Macau', 'MP - Nördliche Marianen', 'MQ - Martinique', 
    'MR - Mauretanien', 'MS - Montserrat', 'MT - Malta', 
    'MU - Mauritius', 'MV - Malediven', 'MW - Malawi', 
    'MX - Mexiko', 'MY - Malaysia', 'MZ - Mosambik', 
    'NA - Namibia', 'NC - Neukaledonien', 'NE - Niger', 
    'NF - Norfolkinsel', 'NG - Nigeria', 'NI - Nicaragua', 
    'NL - Niederlande', 'NO - Norwegen', 'NP - Nepal', 
    'NR - Nauru', 'NU - Niue', 'NZ - Neuseeland', 
    'OM - Oman', 'PA - Panama', 'PE - Peru', 
    'PF - Französisch-Polynesien', 'PG - Papua-Neuguinea', 'PH - Philippinen', 
    'PK - Pakistan', 'PL - Polen', 'PM - Saint-Pierre und Miquelon', 
    'PN - Pitcairninseln', 'PR - Puerto Rico', 'PS - Palästinensische Autonomiegebiete', 
    'PT - Portugal', 'PW - Palau', 'PY - Paraguay', 
    'QA - Katar', 'QP - Hohe See', 'RE - Réunion', 
    'RO - Rumänien', 'RS - Serbien', 'RU - Russische Föderation', 
    'RW - Ruanda', 'SA - Saudi-Arabien', 'SB - Salomonen', 
    'SC - Seychellen', 'SD - Sudan', 'SE - Schweden', 
    'SG - Singapur', 'SH - St. Helena, Ascension und Tristan da Cunha', 'SI - Slowenien', 
    'SJ - Svalbard und Jan Mayen', 'SK - Slowakei', 'SL - Sierra Leone', 
    'SM - San Marino', 'SN - Senegal', 'SO - Somalia', 
    'SR - Suriname', 'SS - Südsudan', 'ST - São Tomé und Príncipe', 
    'SV - El Salvador', 'SX - Sint Maarten', 'SY - Syrien', 
    'SZ - Eswatini', 'TC - Turks- und Caicosinseln', 'TD - Tschad', 
    'TF - Französische Süd- und Antarktisgebiete', 'TG - Togo', 'TH - Thailand', 
    'TJ - Tadschikistan', 'TK - Tokelau', 'TL - Osttimor', 
    'TM - Turkmenistan', 'TN - Tunesien', 'TO - Tonga', 
    'TP - Osttimor', 'TR - Türkei', 'TT - Trinidad und Tobago', 
    'TV - Tuvalu', 'TW - Taiwan', 'TZ - Tansania', 
    'UA - Ukraine', 'UG - Uganda', 'UM - Amerikanisch-Ozeanien', 
    'US - Vereinigte Staaten', 'UY - Uruguay', 'UZ - Usbekistan', 
    'VA - Vatikanstadt', 'VC - St. Vincent und die Grenadinen', 'VE - Venezuela', 
    'VG - Britische Jungferninseln', 'VI - Amerikanische Jungferninseln', 'VN - Vietnam', 
    'VU - Vanuatu', 'WF - Wallis und Futuna', 'WS - Samoa', 
    'XA - Amerikanisch-Ozeanien', 'XC - Ceuta', 'XI - Vereinigtes Königreich (Nordirland)', 
    'XK - Kosovo', 'XL - Melilla', 'XM - Montenegro', 
    'XO - Australisch-Ozeanien', 'XP - Westjordanland und Gazastreifen', 'XR - Polarregionen', 
    'XS - Serbien', 'XZ - Neuseeland-Ozeanien', 'YE - Jemen', 
    'YT - Mayotte', 'YU - Bundesrepublik Jugoslawien', 'ZA - Südafrika', 
    'ZM - Sambia', 'ZR - Zaire', 'ZW - Simbabwe'
]


countries_EU = [
    "AT - Österreich",
    "BE - Belgien",
    "BG - Bulgarien",
    "CY - Zypern",
    "CZ - Tschechien",
    "DE - Deutschland",
    "DK - Dänemark",
    "EE - Estland",
    "ES - Spanien",
    "EU - Europäische Gemeinschaft",
    "FI - Finnland",
    "FR - Frankreich",
    "GR - Griechenland",
    "HR - Kroatien",
    "HU - Ungarn",
    "IE - Irland",
    "IT - Italien",
    "LT - Litauen",
    "LU - Luxemburg",
    "LV - Lettland",
    "MT - Malta",
    "NL - Niederlande",
    "PL - Polen",
    "PT - Portugal",
    "RO - Rumänien",
    "SE - Schweden",
    "SI - Slowenien",
    "SK - Slowakei"
]


countries_not_relevant = [
    "CH - Schweiz",
    "IS - Island",
    "LI - Liechtenstein",
    "NO - Norwegen",
    "XC - Ceuta",
    "XL - Melilla"
]


cn_codes = [
    "2601 12 00", "7201", "7202 11", "7202 19", "7202 41", "7202 49", "7202 60 00", "7203", "7205", "7206", 
    "7206 10 00", "7206 90 00", "7207", "7207 11 11", "7207 11 14", "7207 11 16", "7207 12 10", "7207 19 12", 
    "7207 19 80", "7207 20 11", "7207 20 15", "7207 20 17", "7207 20 32", "7207 20 52", "7207 20 80", "7207 11 90", 
    "7207 12 90", "7207 19 19", "7207 20 19", "7207 20 39", "7207 20 59", "7208", "7209", "7210", "7211", 
    "7211 13 00", "7211 14 00", "7211 19 00", "7211 23", "7211 29 00", "7211 90", "7212", "7213", "7214", 
    "7214 10 00", "7214 20 00", "7214 30 00", "7214 91", "7214 99", "7215", "7216", "7217", "7217 10", 
    "7217 20", "7217 30", "7217 90", "7218", "7218 10 00", "7218 99 19", "7218 99 80", "7218 91", "7218 99 11", 
    "7218 99 20", "7219", "7219 11 00", "7219 12", "7219 13", "7219 14", "7219 21", "7219 22", "7219 23 00", 
    "7219 24 00", "7219 31 00", "7219 32", "7219 33", "7219 34", "7219 35", "7219 90", "7220", "7220 11 00", 
    "7220 12 00", "7220 20", "7220 90", "7221", "7222", "7222 11", "7222 19", "7222 20", "7222 40", "7222 30", 
    "7223", "7223 00", "7224", "7224 10", "7224 90 18", "7224 90 90", "7224 90 02", "7224 90 03", "7224 90 05", 
    "7224 90 07", "7224 90 14", "7224 90 31", "7224 90 38", "7225", "7225 11 00", "7225 19 10", "7225 30", 
    "7225 40", "7225 19 90", "7225 50", "7225 91 00", "7225 92 00", "7225 99 00", "7226", "7226 11 00", 
    "7226 19 10", "7226 20 00", "7226 91", "7226 19 80", "7226 92 00", "7226 99", "7227", "7228", "7228 10 20", 
    "7228 10 90", "7228 20", "7228 30", "7228 50", "7228 60", "7228 70", "7228 80 00", "7228 10 50", "7228 40", 
    "7229", "7301", "7302", "7303", "7303 00", "7304", "7304 11 00", "7304 22 00", "7304 24 00", "7304 41 00", 
    "7304 49", "7304 51", "7304 59", "7304 19", "7304 23 00", "7304 29", "7304 31", "7304 39", "7304 90 00", 
    "7305", "7306", "7306 30 18", "7306 19 00", "7306 29 00", "7306 30 12", "7306 30 41", "7306 30 49", 
    "7306 30 72", "7306 30 77", "7306 30 80", "7306 61 92", "7306 61 99", "7306 69 90", "7306 90 00", 
    "7306 40 80", "7306 50 29", "7306 11 00", "7306 21 00", "7306 40 20", "7306 61 10", "7306 69 10", 
    "7306 50 21", "7306 50 80", "7307", "7307 11", "7307 19 10", "7307 19 90", "7307 21 00", "7307 22", 
    "7307 23", "7307 29", "7307 91 00", "7307 92", "7307 93", "7307 99", "7308", "7309", "7310", "7311", 
    "7311 00", "7318", "7318 11 00", "7318 12 90", "7318 13 00", "7318 14 91", "7318 14 99", "7318 19 00", 
    "7318 21 00", "7318 24 00", "7318 29 00", "7318 12 10", "7318 14 10", "7318 15", "7318 16", "7318 22 00", 
    "7318 23 00", "7326", "7326 11 00", "7326 19", "7326 90 92", "7326 90 94", "7326 90 96", "7326 20 00", 
    "7326 90 30", "7326 90 40", "7326 90 50", "7326 90 60", "7326 90 98", "7601", "7603", "7604 10 10", 
    "7604 10 90", "7604 21 00", "7604 29 10", "7604 29 90", "7605", "7606", "7607", "7608", "7609 00 00", 
    "7610 10 00", "7610 90", "7610 90 10", "7610 90 90", "7611 00 00", "7612", "7613 00 00", "7614", 
    "7615 10 10", "7615 10 30", "7615 10 80", "7615 20 00", "7616 10 00", "7616 91 00", "7616 99 10", 
    "7616 99 90", "2507 00 80", "2523 10 - weißer Klinker", "2523 10 - grauer Klinker", "2523 21", "2523 29", 
    "2523 90 - weißer Zement", "2523 90 - grauer Zement", "2523 30", "2808 00 00", "2814", "2834 21 00", 
    "3102", "3102 10", "3102 21 00", "3102 29 00", "3102 30", "3102 40", "3102 50 00", "3102 60 00", 
    "3102 80 00", "3105", "3105 20", "3105 30 00", "3105 40 00", "3105 51 00", "3105 59 00"
]



dropdown_cn_codes = st.selectbox(
    'Geben Sie den KN-Code Ihrer Ware an',
    cn_codes, index=None, placeholder='KN-Code')


dropdown_countries = st.selectbox(
    'Geben Sie das Herkunftsland Ihrer Ware an',
    countries, index=None, placeholder='Herkunftsland')

activity_data = st.number_input('Geben Sie die Menge der importierten Ware (in Tonnen) an', min_value=0, max_value=None, value=None, placeholder='Warenmenge in Tonnen')

st.write('Geschätzte Kosten:')

def calculate():
    if isinstance(activity_data,int):
        ans=activity_data*100
        st.success(f"{ans}")
   
    
calculate()
 
