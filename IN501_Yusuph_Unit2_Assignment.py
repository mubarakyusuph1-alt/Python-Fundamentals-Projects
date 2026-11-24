# Fundamentals of Computer Programming

# Project Data
projects = {
    101: {
        "name": "Website Redesign",
        "hours": {"Alice": 25, "Bob": 40, "Charlie": 30, "Diana": 35, "Eve": 20}
   },
    102: {
        "name": "Mobile App Development",
        "hours": {"Alice": 15, "Frank": 50, "Grace": 40, "Bob": 20, "Hank": 45}
    },
    103: {
        "name": "Marketing Campaign",
        "hours": {"Diana": 20, "Ivy": 35, "Charlie": 15, "Eve": 25, "Grace": 30}
    },
    104: {
        "name": "Data Analysis",
        "hours": {"Hank": 50, "Frank": 35, "Ivy": 40, "Bob": 25, "Charlie": 20}
    },
    105: {
        "name": "Product Launch",
        "hours": {"Alice": 30, "Diana": 25, "Eve": 40, "Grace": 20, "Hank": 35}
     }
}

#Introduction
print("Enter a project number and employee name to find logged hours.")

# Get project number from the user
project_number = input("Enter a project number: ")

# Check if the project number is valid
if project_number.isdigit():
    project_number = int(project_number)
    if project_number in projects:
        # Get employee name
        employee_name = input("Enter employee name: ").strip().capitalize()

        project = projects[project_number]
        project_name = project["name"]

        # Check if the employee exists for the project
        if employee_name in project["hours"]:
            hours = project["hours"][employee_name]
            print(f"{employee_name} has worked {hours} hours on project {project_number}, {project_name}")
        else:
            print(f"{employee_name} is not listed for projct {project_number}")
    else:
        print("That is not a valid project number.")
else:
    print("Please enter a valid numeric project number.")


project_number = input("Enter a project number: ")

if project_number == "101":
    print( "Website Redesign")

if project_number == "102":
    print( "Mobile App Development")

if project_number == "103":
    print( "Marketing Campaign")

if project_number == "104":
    print( "Data Analysis")

if project_number == "105":
    print( "Product Launch")

else:
    print("WARNING!! Project number not found.")