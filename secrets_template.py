from trello import TrelloClient

TRELLO_API_KEY = ""
TRELLO_API_SEC = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SEC = ""

client = TrelloClient(api_key=TRELLO_API_KEY, api_secret=TRELLO_API_SEC, token=OAUTH_TOKEN, token_secret=OAUTH_TOKEN_SEC)
