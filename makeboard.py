from trello import TrelloClient
from secrets import client


the_goddamn_batman = client.get_board('55a69f0465c199a77b692421')
admins = the_goddamn_batman.admin_members()
members = the_goddamn_batman.get_members()


