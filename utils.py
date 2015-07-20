from members import admins, members
from models import Person, Task, Project

def parse_tasksheet(ws):
    projects = []
    num_rows = ws.row_count
    empty_row_count = 0
    current_project = None
    current_task = None
    for r in xrange(2, num_rows):
        row = ws.row_values(r)
        if empty_row_count==10: # after 10 empty rows
            break              # consider this done
        
        if is_row_empty(row):
            empty_row_count += 1
            continue

        if is_row_project(row):
            if current_project != None:  # If we are already working with a project, we need to save it.
                projects.append(current_project)
                current_project = None
            current_project = Project(row[0], [], 0, set())
        else:
            member_spreadsheet_name = row[2]
            task_name = row[1]
            task_points = int(row[3])
            member = filter(lambda x: x.spreadsheet_name==member_spreadsheet_name, members)[0]
            current_project.members.add(member)
            current_project.total_points += task_points
            current_project.tasks.append(Task(task_name, member, task_points))

    return projects

def is_row_empty(row):
    empty = True
    
    for cell in row:
        if not is_cell_empty(cell):
            empty = False
            return empty

    return empty

def is_cell_empty(cell):
    return cell in [None, ""]

def is_row_project(row):
    return not is_cell_empty(row[0])

