import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title('CBAM-Kostenschätzerli')

"""
# CBAM-Kostenschätzer

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
"""

countries = [
    "AD - Andorra", "AE - Vereinigte Arabische Emirate", "AF - Afghanistan", 
    "AG - Antigua und Barbuda", "AI - Anguilla", "AL - Albanien", 
    "AM - Armenien", "AN - Niederländische Antillen", "AO - Angola", 
    "AQ - Antarktis", "AR - Argentinien", "AS - Amerikanisch-Samoa", 
    "AT - Österreich", "AU - Australien", "AW - Aruba", 
    "AX - Ålandinseln", "AZ - Aserbaidschan", "BA - Bosnien und Herzegowina", 
    "BB - Barbados", "BD - Bangladesch", "BE - Belgien", 
    "BF - Burkina Faso", "BG - Bulgarien", "BH - Bahrain", 
    "BI - Burundi", "BJ - Benin", "BL - Saint-Barthélemy", 
    "BM - Bermuda", "BN - Brunei Darussalam", "BO - Bolivien", 
    "BQ - Bonaire, Sint Eustatius und Saba", "BR - Brasilien", "BS - Bahamas", 
    "BT - Bhutan", "BV - Bouvetinsel", "BW - Botswana", 
    "BY - Belarus", "BZ - Belize", "CA - Kanada", 
    "CC - Kokosinseln", "CD - Demokratische Republik Kongo", "CF - Zentralafrikanische Republik", 
    "CG - Kongo", "CH - Schweiz", "CI - Elfenbeinküste", 
    "CK - Cookinseln", "CL - Chile", "CM - Kamerun", 
    "CN - China", "CO - Kolumbien", "CR - Costa Rica", 
    "CS - Serbien und Montenegro", "CU - Kuba", "CV - Kap Verde", 
    "CW - Curaçao", "CX - Weihnachtsinsel", "CY - Zypern", 
    "CZ - Tschechien", "DE - Deutschland", "DJ - Dschibuti", 
    "DK - Dänemark", "DM - Dominica", "DO - Dominikanische Republik", 
    "DZ - Algerien", "EC - Ecuador", "EE - Estland", 
    "EG - Ägypten", "EH - Westsahara", "ER - Eritrea", 
    "ES - Spanien", "ET - Äthiopien", "EU - Europäische Gemeinschaft", 
    "FI - Finnland", "FJ - Fidschi", "FK - Falklandinseln", 
    "FM - Mikronesien", "FO - Färöer", "FR - Frankreich", 
    "GA - Gabun", "GB - Vereinigtes Königreich", "GD - Grenada", 
    "GE - Georgien", "GF - Französisch-Guayana", "GG - Guernsey", 
    "GH - Ghana", "GI - Gibraltar", "GL - Grönland", 
    "GM - Gambia", "GN - Guinea", "GP - Guadeloupe", 
    "GQ - Äquatorialguinea", "GR - Griechenland", "GS - Südgeorgien und die Südlichen Sandwichinseln", 
    "GT - Guatemala", "GU - Guam", "GW - Guinea-Bissau", 
    "GY - Guyana", "HK - Hongkong", "HM - Heard- und McDonald-Inseln", 
    "HN - Honduras", "HR - Kroatien", "HT - Haiti", 
    "HU - Ungarn", "ID - Indonesien", "IE - Irland", 
    "IL - Israel", "IM - Isle of Man", "IN - Indien", 
    "IO - Britisches Territorium im Indischen Ozean", "IQ - Irak", "IR - Iran", 
    "IS - Island", "IT - Italien", "JE - Jersey", 
    "JM - Jamaika", "JO - Jordanien", "JP - Japan", 
    "KE - Kenia", "KG - Kirgisistan", "KH - Kambodscha", 
    "KI - Kiribati", "KM - Komoren", "KN - St. Kitts und Nevis", 
    "KP - Nordkorea", "KR - Südkorea", "KW - Kuwait", 
    "KY - Kaimaninseln", "KZ - Kasachstan", "LA - Laos", 
    "LB - Libanon", "LC - St. Lucia", "LI - Liechtenstein", 
    "LK - Sri Lanka", "LR - Liberia", "LS - Lesotho", 
    "LT - Litauen", "LU - Luxemburg", "LV - Lettland", 
    "LY - Libyen", "MA - Marokko", "MC - Monaco", 
    "MD - Moldawien", "ME - Montenegro", "MF - Saint-Martin", 
    "MG - Madagaskar", "MH - Marshallinseln", "MK - Nordmazedonien", 
    "ML - Mali", "MM - Myanmar", "MN - Mongolei", 
    "MO - Macau", "MP - Nördliche Marianen", "MQ - Martinique", 
    "MR - Mauretanien", "MS - Montserrat", "MT - Malta", 
    "MU - Mauritius", "MV - Malediven", "MW - Malawi", 
    "MX - Mexiko", "MY - Malaysia", "MZ - Mosambik", 
    "NA - Namibia", "NC - Neukaledonien", "NE - Niger", 
    "NF - Norfolkinsel", "NG - Nigeria", "NI - Nicaragua", 
    "NL - Niederlande", "NO - Norwegen", "NP - Nepal", 
    "NR - Nauru", "NU - Niue", "NZ - Neuseeland", 
    "OM - Oman", "PA - Panama", "PE - Peru", 
    "PF - Französisch-Polynesien", "PG - Papua-Neuguinea", "PH - Philippinen", 
    "PK - Pakistan", "PL - Polen", "PM - Saint-Pierre und Miquelon", 
    "PN - Pitcairninseln", "PR - Puerto Rico", "PS - Palästinensische Autonomiegebiete", 
    "PT - Portugal", "PW - Palau", "PY - Paraguay", 
    "QA - Katar", "QP - Hohe See", "RE - Réunion", 
    "RO - Rumänien", "RS - Serbien", "RU - Russische Föderation", 
    "RW - Ruanda", "SA - Saudi-Arabien", "SB - Salomonen", 
    "SC - Seychellen", "SD - Sudan", "SE - Schweden", 
    "SG - Singapur", "SH - St. Helena, Ascension und Tristan da Cunha", "SI - Slowenien", 
    "SJ - Svalbard und Jan Mayen", "SK - Slowakei", "SL - Sierra Leone", 
    "SM - San Marino", "SN - Senegal", "SO - Somalia", 
    "SR - Suriname", "SS - Südsudan", "ST - São Tomé und Príncipe", 
    "SV - El Salvador", "SX - Sint Maarten", "SY - Syrien", 
    "SZ - Eswatini", "TC - Turks- und Caicosinseln", "TD - Tschad", 
    "TF - Französische Süd- und Antarktisgebiete", "TG - Togo", "TH - Thailand", 
    "TJ - Tadschikistan", "TK - Tokelau", "TL - Osttimor", 
    "TM - Turkmenistan", "TN - Tunesien", "TO - Tonga", 
    "TP - Osttimor", "TR - Türkei", "TT - Trinidad und Tobago", 
    "TV - Tuvalu", "TW - Taiwan", "TZ - Tansania", 
    "UA - Ukraine", "UG - Uganda", "UM - Amerikanisch-Ozeanien", 
    "US - Vereinigte Staaten", "UY - Uruguay", "UZ - Usbekistan", 
    "VA - Vatikanstadt", "VC - St. Vincent und die Grenadinen", "VE - Venezuela", 
    "VG - Britische Jungferninseln", "VI - Amerikanische Jungferninseln", "VN - Vietnam", 
    "VU - Vanuatu", "WF - Wallis und Futuna", "WS - Samoa", 
    "XA - Amerikanisch-Ozeanien", "XC - Ceuta", "XI - Vereinigtes Königreich (Nordirland)", 
    "XK - Kosovo", "XL - Melilla", "XM - Montenegro", 
    "XO - Australisch-Ozeanien", "XP - Westjordanland und Gazastreifen", "XR - Polarregionen", 
    "XS - Serbien", "XZ - Neuseeland-Ozeanien", "YE - Jemen", 
    "YT - Mayotte", "YU - Bundesrepublik Jugoslawien", "ZA - Südafrika", 
    "ZM - Sambia", "ZR - Zaire", "ZW - Simbabwe"
]

dropdown_countries = st.selectbox("Geben Sie das Herkunftsland Ihrer Ware an", contries)

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
