
import PySimpleGUI as sg
import json
from employee import Employee
from quicksort import Quicksort as qs
import re

#Load contents of json file into employee_list.
#If file doesn't exist, create it.
def load_json():
    try:
        with open('employees.json', 'r') as openfile:
            json_object = json.load(openfile)
            if json_object == None:
                json_object = []
    except:
        f = open('employees.json', 'w+')
        f.close()
        json_object = []
    return json_object

#Update what is displayed in the window's Listbox.
def update(window, employee_list):
    msg = []
    if len(employee_list) > 0:
        for emp in employee_list:
            n = emp["name"]
            i = emp["id"]
            t = emp["title"]
            h = emp["hire_date"]
            msg.append(f'Name: {n} | ID Number: {i} | Job Title: {t} | Hire Date: {h}')

        window['-DIS-'].update(msg)

#Employees are sorted by their data fields.
def sort(values, employee_list):
    if values['-S_NAME-']:
        qs.quicksort(employee_list, 'name', 0, len(employee_list)-1)

    elif values['-S_ID-']:
        qs.quicksort(employee_list, 'id', 0, len(employee_list)-1)

    elif values['-S_TITLE-']:
        qs.quicksort(employee_list, 'title', 0, len(employee_list)-1)

    elif values['-S_DATE-']:
        qs.quicksort(employee_list, 'date', 0, len(employee_list)-1)

#Make sure information entered by the user is properly formatted.
def check_format(name, date):

    #Check for valid name format.
    found = name.find(', ')
    name = name.replace(', ', '')
    matches = name.isalpha()
    name_valid = False

    if found > 0 and matches:
        name_valid = True

    #Check for valid date format.
    r = re.compile('.{2}/.{2}/.{4}')
    date_valid = False

    if len(date) == 10 and r.match(date):
        date_valid = True
    
    return name_valid, date_valid

def main():

    search_layout = [
            [sg.Text('Name Format: Last, First | Hire Date Format: XX/XX/XXXX (month/date/year)', size =(60, 1))],
            [sg.Text('Employee Name:', size =(15, 1)), sg.InputText('', size=30, key='-NAME-')],
            [sg.Text('Employee ID:', size =(15, 1)), sg.InputText('', size=30, key='-ID-')],
            [sg.Text('Employee Title:', size =(15, 1)), sg.InputText('', size=30, key='-TITLE-')],
            [sg.Text('Employee Hire Date:', size =(15, 1)), sg.InputText('', size=30, key='-DATE-')], 
             
            [sg.Button('Add Employee')],
            [sg.Text('_____'  * 30, size=(124, 1))],

            [sg.Radio('Sort By Name', 'RADIO1', default=True, key='-S_NAME-')], 
            [sg.Radio('Sort By ID', 'RADIO1', default=False, key='-S_ID-')],
            [sg.Radio('Sort By Title', 'RADIO1', default=False, key='-S_TITLE-')],
            [sg.Radio('Sort By Hire Date', 'RADIO1', default=False, key='-S_DATE-')],
            [sg.Button('Sort Employees')],
            [sg.Text('_____'  * 30, size=(124, 1))],
            [sg.Listbox('', size=(200, 10), key='-DIS-')],
            [sg.Button('Update List'), sg.Button('Exit')]
            ]

    window = sg.Window('Company Employees',
                search_layout,
                size=(600, 650), finalize=True)

    employee_list = load_json()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):                   #Exit window
            break

        if event in ('Add Employee',):
            name = values['-NAME-']
            date = values['-DATE-']
            valid_input = check_format(name, date)
            
            if not valid_input[0] and not valid_input[1]:
                sg.popup_error('ERROR', 'Name and hire date do not conform to format.')

            elif not valid_input[0]:
                sg.popup_error('ERROR', 'Name does not conform to format.')

            elif not valid_input[1]:
                sg.popup_error('ERROR', 'Hire date does not conform to format.')

            else:
                employee = Employee(name, values['-ID-'], values['-TITLE-'], date)
                employee = employee.create()
                if employee is not None:
                    employee_list.append(employee)
                    with open('employees.json', 'w') as outfile:
                        json.dump(employee_list, outfile, indent=4)

                window['-NAME-'].update('')
                window['-ID-'].update('')
                window['-TITLE-'].update('')
                window['-DATE-'].update('')  

        if event in ('Sort Employees',) and len(employee_list) > 0:                
            sort(values, employee_list)

        if event in ('Update List',) and len(employee_list) > 0:                
            update(window, employee_list)

    with open('employees.json', 'w') as outfile:
        json.dump(employee_list, outfile, indent=4)

    window.close()    

if __name__ == "__main__":
    main()

