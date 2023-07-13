
## Python Item Sort for Apartment Moving
# Broken into three categories: Need, Want, Have
# Used to keep track of what we are bringing, what we want and need

# import for the CSV file
import csv

def parse_data(filename):
    total_price_mark = 0  # Variable to store the total price for Mark
    total_price_tanishq = 0  # Variable to store the total price for Tanishq
    
    mark_items = ""
    tanishq_items = ""
    both_items = ""

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
                total_price_mark += price           # Add the price to Mark's total
                mark_items += (item + "\n")         # Add the item to Mark's items
            elif mark == 'False' and tanishq == 'True':
                total_price_tanishq += price        # Add the price to Tanishq's total
                tanishq_items += (item + "\n")      # Add the item to Tanishq's items
            elif mark == 'True' and tanishq == 'True':
                total_price_mark += price / 2       # Add half the price to each person
                total_price_tanishq += price/2
                both_items += (item + "\n")         # Items that are being split


    print(f"Total Price (Mark): ${total_price_mark:.2f}")
    print(f"Total Price (Tanishq): ${total_price_tanishq:.2f}")
    print("\n\n") #spacing
    print(f"Mark's Item List\n---------------------\n{mark_items}")
    print(f"\nTanishq's Item List\n---------------------\n{tanishq_items}")
    print(f"\nShared Items\n---------------------\n{both_items}")


filename = 'ApartmentItemsUpdated.csv'
parse_data(filename)
