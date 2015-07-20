class Person:
    def __init__(self, spreadsheet_name, full_name, trello_username):
        self.spreadsheet_name = spreadsheet_name
        self.full_name = full_name
        self.trello_username = trello_username

class Project:
    def __init__(self, name='', tasks=[], total_points=0, members=set()):
        self.name = name
        self.tasks = tasks
        self.total_points = total_points
        self.members = members

    def __unicode__(self):
        return "(%d)%s"%(self.points, self.name)

class Task:
    def __init__(self, name, member, points):
        self.name = name
        self.member = member
        self.points = points
