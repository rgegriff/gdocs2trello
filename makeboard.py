from trello import TrelloClient


TRELLO_API_KEY = "86071be5a684e67f3fc2d166cb461d9c"
TRELLO_API_SEC = "d2c12f949b4b7546c2c633919f4d746a61fb2fad908d4898e6951d27377e9676"
OAUTH_TOKEN = "ca79cb6695c5e80818a2b50bca5fe240be7523d9179b9807117d4d91024ed4fc"
OAUTH_TOKEN_SEC = "cf51e5f666908e612f241de7e752f23a"

client = TrelloClient(api_key=TRELLO_API_KEY, api_secret=TRELLO_API_SEC, token=OAUTH_TOKEN, token_secret=OAUTH_TOKEN_SEC)
the_goddamn_batman = client.get_board('55a69f0465c199a77b692421')
admins = the_goddamn_batman.admin_members()
members = the_goddamn_batman.get_members()

