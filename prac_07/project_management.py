"""
CP1404 Prac 7 Jack Kerlin
Estimate: ~3 hours
Actual: 2.5 hours
"""

import datetime
from project import Project

MENU_MESSAGE = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date "
                "\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>> ")
DEFAULT_FILE_NAME = "projects.txt"


def main():
    projects = []
    projects = load_project(DEFAULT_FILE_NAME, projects)
    user_input = input(MENU_MESSAGE).upper()
    while user_input != "Q":
        if user_input == "L":
            file_name = get_text("Enter file name to load from: ")
            projects = load_project(file_name, projects)
        elif user_input == "S":
            file_name = get_text("Enter file name to save to: ")
            save_project(file_name, projects)
        elif user_input == "D":
            # find all projects that are unfinished and finished and display them
            unfinished_projects = [project for project in projects if not project.is_complete()]
            finished_projects = [project for project in projects if project.is_complete()]
            print("Incomplete projects: ")
            display_projects(unfinished_projects)
            print("Complete projects: ")
            display_projects(finished_projects)
        elif user_input == "F":
            filter_date = get_date("Show projects that start after date (dd/mm/yy): ")
            # find projects with date larger than the filter date and sort by date
            filtered_projects = sorted([project for project in projects if project.date >= filter_date],
                                       key=lambda x: x.date)
            display_projects(filtered_projects)
        elif user_input == "A":
            # get new attributes of Project and then append them to projects
            name = get_text("Name: ")
            start_date = get_date("Start date (dd/mm/yy): ")
            priority = get_number("Priority: ")
            cost_estimate = get_number("Cost estimate: $")
            percent_complete = get_percentage("Percent complete: ")
            projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))
        elif user_input == "U":
            indices = [i for i in range(len(projects))]
            display_projects(projects, True)
            index = get_number("Project choice: ")
            while index not in indices:
                print("Invalid project index.")
                index = get_number("Project choice: ")
            print(projects[index])
            projects[index].completion = get_percentage("New Percentage: ")
            projects[index].priority = get_number("New Priority: ")
        else:
            print("Invalid input.")
        user_input = input(MENU_MESSAGE).upper()
    print("Goodbye.")
    save_project(DEFAULT_FILE_NAME, projects)


def load_project(file_name, projects):
    """Load lines from a file and adds them as project objects to the project list"""
    in_file = open(file_name, "r")
    # readline to remove header
    in_file.readline()
    parts = [line.strip().split('	') for line in in_file]
    print(parts)
    in_file.close()
    projects += [
        Project(part[0], datetime.datetime.strptime(part[1], "%d/%m/%Y").date(), int(part[2]), float(part[3]),
                int(part[4]))
        for part in parts]
    return projects


def get_date(input_message):
    """Return a valid date"""
    is_valid_input = False
    while not is_valid_input:
        try:
            date = datetime.datetime.strptime(input(input_message), "%d/%m/%Y").date()
            is_valid_input = True
        except ValueError:
            print("Invalid input, enter a valid date.")
    return date


def display_projects(projects, display_index=False):
    """Display every project in projects with optional index"""
    indices = [" " for _ in range(len(projects))]
    if display_index:
        indices = [i for i in range(len(projects))]
    for i, project in enumerate(sorted(projects)):
        print(f"{indices[i]}", project)


def get_number(input_message):
    """Return a valid integer greater or equal to than zero"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(input_message))
            if number < 0:
                print("Number must be >= 0.")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input, enter a valid integer.")
    return number


def get_percentage(input_message):
    """Return a valid integer greater or equal to than zero and less than or equal to 100"""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(input_message))
            if number < 0:
                print("Percentage must be >= 0.")
            if number > 100:
                print("Percentage must be <= 100.")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input, enter a valid integer.")
    return number

def get_text(input_message):
    """Return a non-blank string"""
    text = input(input_message)
    while text == "":
        print("Input cannot be blank.")
        text = input(input_message)
    return text


def save_project(file_name, projects):
    out_file = open(file_name, "w")
    out_file.write("\n".join(
        [" ".join([project.name, str(project.date), str(project.priority), str(project.cost), str(project.completion)])
         for project in projects]))
    out_file.close()


main()
