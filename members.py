from collections import namedtuple
from secrets import client
from trello import ResourceUnavailable
Person = namedtuple("Person", ["spreadsheet_name", "full_name", "trello_username"], verbose=False)

admins = [
    Person("George", "George Griffin", "georgegriffin"),
    Person("Peter", "Peter McLaughlin", "petermclauglin")
    ]

members = [
    Person("Anup", "Anup Dhabarde", "anupdhabarde1"),
    Person("Enrica", "Enrica Beccalli", "enrica17"),
    Person("Evan", "Evan Bederman", "evanbederman"),
    Person("Harris", "Harris Pittinsky", "harrispittinsky1"),
    Person("Hemant", "Hemant Kumar", "hemant90"),
    Person("Himanshu", "Himanshu Chaubey", "himanshuchaubey"),
    Person("Isatou", "Isatou Sanneh", "isatousanneh1"),
    Person("Peter", "Peter McLaughlin", "petermclaughlin"),
    Person("Raghav", "Raghav Palekar", "raghavp"),
    Person("Rajnish", "Rajnish Kumar", "rajnishkumar5"),
    Person("Shaojun", "Shaojun Zhu", "shaojun2"),
    Person("Travis", "Travis Kempbell", "travis_kempbell"),
    Person("Tushar", "Tushar Thantharate", "tushar35"),
    Person("Vikas", "Vikas Pagar", "vikaspagar"),
    Person("Vivek", "Vivek Joshi", "vivek_verificient")
    ]

# Simple tests for now just to keep moving
# @todo: move this into a proper test setup
def validate_usernames():
    error_count = 0
    for member in members:
        try:
            client.get_member(member.trello_username)
        except ResourceUnavailable:
            print member.full_name, "has a bad username: ", member.username
            error_count += 1

    print "validate_usernames completed with %d errors" % error_count

if __name__ == "__main__":
    validate_usernames()
