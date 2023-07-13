
## Python Item Sort for Apartment Moving
# Broken into three categories: Need, Want, Have
# Used to keep track of what we are bringing, what we want and need

# import for the CSV file
import csv

def parse_data(filename):
    total_price_mark = 0  # Variable to store the total price for Mark
    total_price_tanishq = 0  # Variable to store the total price for Tanishq

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            item = row['Item']
            price = float(row['Price'].replace('$', ''))
            mark = row['Mark']
            tanishq = row['Tanishq']

            print(f"Item: {item}")
            print(f"Price: ${price:.2f}")

            if mark == 'True' and tanishq == 'False':
                total_price_mark += price  # Add the price to Mark's total
            elif mark == 'False' and tanishq == 'True':
                total_price_tanishq += price  # Add the price to Tanishq's total
            elif mark == 'True' and tanishq == 'True':
                total_price_mark += price / 2  # Add half the price to each person
                total_price_tanishq += price/2

            print()

    print(f"Total Price (Mark): ${total_price_mark:.2f}")
    print(f"Total Price (Tanishq): ${total_price_tanishq:.2f}")


filename = 'ApartmentItemsUpdated.csv'
parse_data(filename)
