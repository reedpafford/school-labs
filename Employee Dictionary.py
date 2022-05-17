# File: L8q1.py
# Author: Reed Pafford
# Date: 03/30/2022
# Section: 599
# Email: reedpafford@tamu.edu
# Description: This program is a program that adds and searches emplyees

from Employee import Employee
def main():
    print('\nMenu')
    print('----------------------------------------')
    print('''1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit the program
''')
    employees={}
    choice=0
    while choice !=5:
        choice_in=int(input('Enter your choice: '))
        if choice_in==1:
            lookup(employees)
            print()
        elif choice_in==2:
            add(employees)
            print()
        elif choice_in==3:
            change(employees)
            print()
        elif choice_in==4:
            delete(employees)
            print()
        elif choice==5:
            print('Shutting down program')
        else:
            print('invalid option')
              
        
def lookup(employees):
    ID=input('Enter an employee ID: ')
    if ID in employees.keys():
        employees[ID].display()
    else:
        print('Employee not found')

def add(employees):
    name=input('Enter employee name: ')
    ID=input('Enter employee ID: ')
    department=input('Enter employee department: ')
    title=input('Enter employees job title: ')

    newEmp=Employee(name,ID,department,title)
    employees[newEmp.getID()] = newEmp
    print('New employee has been added')

def change(employees):
    ID=input('Enter employee ID number: ')
    if ID in employees:
        name=input('Enter employee name: ')
        ID=input('Enter employee ID: ')
        department=input('Enter employee department: ')
        title=input('Enter employees job title: ')

        employees[ID]=Employee(name,ID,department,title)
        print('Employee updated')
    else:
        print('Employees ID not found')

def delete(employees):
    ID = input('Enter employees ID number: ')
    if ID in employees.keys():
        del employees[ID]
        print('Employee info deleted')
    else:
        print('ID not found')
    
    
main()    
