import time

def clear_idle_window():

        print("\n" * 100) 

clear_idle_window()

print('-----------------------------------------------------')
print('Hello, and welcome to the Employee Management System!')
print('-----------------------------------------------------')
employeesinfo = []
while True:
    print('----------------------------------------------- \n')
    print('There are currently', len(employeesinfo), 'employees in the system.')
    print('\n-----------------------------------------------')
    print('Which would you like to do? \n')
    print('1. Add New Employee \n')
    print('2. View All Employees \n')
    print('3. Edit an Employee \n')
    print('4. Search employee by SSN \n')
    print('5. Import employees information from text file \n')
    print('6. Export employees information from text file \n')
    choice = int(input('Please Enter The Desiered Choice:'))

#Functionality 1: Add New Employee
    if choice == 1:
        print('Adding Employee...')
        name = input("Please Enter The Name: ")
        email = input("Please Enter The Email: ")
        phone = input("Please Enter The Phone Number: ")
        ssn = input("Please Enter The Social Security Number: ")
        salary = input("And last but not least, Please Enter Their Salary: $")
        employeesinfo.append((name, email, phone, ssn, salary))

#Functionality 2: View All Employees
    elif choice == 2:
        if not employeesinfo:
            clear_idle_window()
            print('No employees to display.')
            time.sleep(1)
        else:    
            print('Employee Information:')
        for employee in employeesinfo:
            print(f'---------------------------- {employee[0]} -----------------------------')
            print(f'Email: {employee[1]}')
            print(f'Phone: {employee[2]}')
            print(f'SSN: {employee[3]}')
            print(f'Salary: ${employee[4]}')
            print('----------------------------------------------------------------------------')

#Functionality 3: Edding SSN of an Employee
    elif choice == 3:
        ssn_to_edit = input("What is the SSN of the employee you want to edit: ")
        for index, employee in enumerate(employeesinfo):
            if employee[3] == ssn_to_edit:
                print(f'Editing Employee: {employee[0]}')
                name = input("New Name (leave blank to keep current): ") or employee[0]
                email = input("New Email (leave blank to keep current): ") or employee[1]
                phone = input("New Phone Number (leave blank to keep current): ") or employee[2]
                salary = input("New Salary (leave blank to keep current): $") or employee[4]
                employeesinfo[index] = (name, email, phone, ssn_to_edit, salary)
                print("Employee information updated successfully!")
                break
        else:
            print('--------------------------------')
            print("No employee found with that SSN.")
            print('--------------------------------')

#Functionality 4: Search Employee By SSN
    elif choice == 4:
        search_ssn = input("Please Enter the SSN of the Employee to Search: ")
        found = False
        for employee in employeesinfo:
            if employee[3] == search_ssn:
                print(f'---------------------------- {employee[0]} -----------------------------')
                print(f'Email: {employee[1]}')
                print(f'Phone: {employee[2]}')
                print(f'SSN: {employee[3]}')
                print(f'Salary: ${employee[4]}')
                print('----------------------------------------------------------------------------')
                found = True
                break
        if not found:
            print('--------------------------------')
            print("No employee found with that SSN.")
            print('--------------------------------')

#Functionallity 5: Importing Info
    elif choice == 5:
        print('Importing employees from file...')
        confirm = input('Are you sure you want to import the employee data from employee.txt? This will delete all data entered within the program! (yes/no): ').strip().lower()
        if confirm != 'yes':
            print('Import canceled.')
            continue
        try:
            with open('employees.txt', 'r') as f:
                employeesinfo.clear()
                for line in f:
                    parts = line.strip().split(', ')
                    if len(parts) == 5: 
                        name = parts[0].split(': ')[1]
                        email = parts[1].split(': ')[1]
                        phone = parts[2].split(': ')[1]
                        ssn = parts[3].split(': ')[1]
                        salary = parts[4].split(': $')[1]
                        employeesinfo.append((name, email, phone, ssn, salary))
                print('-------------------------------')
                print('Employee imported successfully!')
                print('-------------------------------')
        except FileNotFoundError:
            print('The file employees.txt does not exist.')
        except Exception as e:
            print(f'An error occurred: {e}')

#Functionallity 6: Exporting Info
    elif choice == 6:
        if not employeesinfo:
            print('No employees to export.')
            continue
        else:
            print('Exporting...')
        try:
            with open('employees.txt', 'w') as f:
                for employee in employeesinfo:
                    f.write(f'Name: {employee[0]}, Email: {employee[1]}, Phone: {employee[2]}, SSN: {employee[3]}, Salary: ${employee[4]}\n')  
            print('-----------------------------------------')
            print('Exported Successfully in "employees.txt"!')
            print('-----------------------------------------')
        except FileNotFoundError:
            print('The file employees.txt does not exist.')

            
#Error Handling for First List
    elif choice <= 5:
        print('Please Enter any number from 1 to 6.')


# Im not just a detective im a time traveler! Watch This!

        