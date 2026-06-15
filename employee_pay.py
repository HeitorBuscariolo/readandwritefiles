import csv

employee_file = csv.reader(open('employee_data.csv', 'r'),delimiter=',')

next(employee_file)

for rec in employee_file:
    print(f"ID: {rec[0]}")
    print(f"Name: {rec[1]}")
    print(f"Age: {rec[2]}")
    print(f"Salary: ${float(rec[3]):,.2f}")
    print(f"HoursWorked: {rec[4]}")
    print(f"Productivity: {rec[5]}")
    print(f"Team: {rec[6]}")
    
    bonus = int(rec[3]) * float(rec[7])
    print(f"Bonus Amount: {bonus:,.2f}")

    total_pay = int(rec[3]) + bonus

    print(f"Total pay: {total_pay:,.2f}")

    input()
        
