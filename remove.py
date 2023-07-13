
import csv

input_file = 'ApartmentItems.csv'
output_file = 'ApartmentItemsUpdated.csv'

with open(input_file, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

header = data[0]
need_index = header.index('Need')
want_index = header.index('Want')
have_index = header.index('Have')

for row in data:
    del row[need_index]
    del row[want_index]
    del row[have_index]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print('Columns removed successfully. Output file:', output_file)
