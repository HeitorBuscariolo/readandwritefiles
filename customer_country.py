import csv

customers = open('customers.csv', 'r')

csv_file = csv.reader(customers,delimiter=',')

next(csv_file)

outfile = open('customer_country.csv', 'w')

customer_count = 0

for row in csv_file:
    full_name = row[1] + ' ' + row[2]
    country = row[4]

    outfile.write(full_name + ',' + country + '\n')

    customer_count += 1

print(f'Total customer: {customer_count}')

customers.close()
outfile.close()
input()