import requests
from bs4 import BeautifulSoup
from lxml import etree
# Session setup
session = requests.Session()

# Set the base URL for the request
base_url = 'https://teledeclaration.cnas.dz'
demande_url = f'{base_url}/ui/secu01.xhtml'

# Ensure that cookies from the login are included in the session
session.cookies.set('JSESSIONID', '932BE04B8390FCF043531351168A2F8E.worker_8155')  # Example, set your JSESSIONID here
session.cookies.set('SESSIONID', '1157753866.63775.0000')  # Example, set your SESSIONID here
session.cookies.set('TSa1b21acf027', '0885e72d1fab2000db87ef39701f16e5304e839b2220de9651ae35e3634f50bc3a1d1c45298bbcf808e0faffd6113000d681cfc6a2b76d0000d9a4ed3c366481ee1d34583434a8b017ecc19616ed6a1b9c2058d7d8d330ceaad9e141a2d7b6f7')  # Example, set your cookie here

# Request the page to get the ViewState
response = session.get(demande_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the 'javax.faces.ViewState' value
view_state = soup.find('input', {'name': 'javax.faces.ViewState'}).get('value')
print(view_state)
# Define the form data, including all necessary fields
form_data = {





    'javax.faces.partial.ajax': 'true',
    'javax.faces.source': 'finit:numass',
    'javax.faces.partial.execute': 'finit:numass',
    'javax.faces.partial.render': 'finit:precherche',
    'javax.faces.behavior.event': 'blur',
    'javax.faces.partial.event': 'blur',
    'finit:ipt_sexe': '1',
    'finit:numass': 942153003350,
    'finit:nom': '',
    'finit:nomRr': '',
    'finit:prenom': '',
    'finit:prenomRr': '',
    'finit:hide': 'H',
    'finit:prenomPere_ar': '',
    'finit:nomMere_ar': '',
    'finit:prenomMere_ar': '',
    'finit:nationalite_filter': '',
    'finit:pays_de_naissance_filter': '',
    'finit:stf_focus': '',
    'finit:stf_input': '0',
    'finit:gs_focus': '',
    'finit:gs_input': '0',
    'finit:haveCard_focus': '',
    'finit:haveCard_input': 'true',
    'finit:handicap_focus': '',
    'finit:handicap_input': 'false',
    'finit:tel': '',
'javax.faces.ViewState': view_state
}

# Headers for the request
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Faces-Request': 'partial/ajax',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': demande_url,
    'Origin': base_url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'application/xml, text/xml, */*; q=0.01',
}

# Send the AJAX request with the form data and headers
submit_response = session.post(demande_url, data=form_data, headers=headers)

# Check if the request was successful
if submit_response.status_code == 200:
    print("Form submitted successfully!")
else:
    print("Failed to submit the form. Status code:", submit_response.status_code)

# Optional: Print the response content for debugging purposes
print(submit_response.text)
print(response.headers["Content-Type"])

