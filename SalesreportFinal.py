import csv

sales = open('sales.csv', 'r')

csv_file = csv.reader(sales, delimiter=',')

next(csv_file)

totals = {}

for row in csv_file:

    customer_id = row[0]

    subtotal = float(row[3])
    tax = float(row[4])
    freight = float(row[5])

    order_total = subtotal + tax + freight

    if customer_id in totals:
        totals[customer_id] += order_total
    else:
        totals[customer_id] = order_total

outfile = open('SalesreportFINAL.csv', 'w')

outfile.write('Customer_ID,Total\n')

for customer_id in totals:
    outfile.write(f'{customer_id},{totals[customer_id]:.2f}\n')

sales.close()
outfile.close()

print('SalesreportFINAL.csv created')

input()