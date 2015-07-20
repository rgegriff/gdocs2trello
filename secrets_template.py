import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from trello import TrelloClient

TRELLO_API_KEY = ""
TRELLO_API_SEC = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SEC = ""

GOOGLE_API = json.loads('''
    REPLACE THIS WITH THE CONTENTS OF YOUR GOOGLE API JSON FILE
''')

credentials = SignedJwtAssertionCredentials(GOOGLE_API['client_email'], GOOGLE_API['private_key'],
        scope = ['https://spreadsheets.google.com/feeds'])

google_client = gspread.authorize(credentials)
trello_client = TrelloClient(api_key=TRELLO_API_KEY, api_secret=TRELLO_API_SEC, token=OAUTH_TOKEN, token_secret=OAUTH_TOKEN_SEC)
