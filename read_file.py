# modes: "r" = read, "w" = write, "a" = append, "r+" = read and write
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
