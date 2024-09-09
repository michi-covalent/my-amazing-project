import csv
import sys
from collections import defaultdict


def process_csv(path):
    with open(path, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        actions = []

        # Process each row
        row: dict[str, str]
        for row in csv_reader:
            if row['Product'] == 'Actions':
                row['name'] = row['Repository Slug'] + ":" + row['Actions Workflow']
                row['price'] = str(float(row['Quantity']) * float(row['Price Per Unit ($)']))
                del row['Quantity']
                del row['SKU']
                del row['Price Per Unit ($)']
                del row['Date']
                del row['Product']
                del row['Owner']
                del row['Username']
                del row['Repository Slug']
                del row['Actions Workflow']
                del row['Unit Type']
                del row['Notes']
                del row['Multiplier']
                # 'Quantity': '293', 'Price Per Unit ($)': '0.008
                actions.append(row)
        aggregated_data = defaultdict(float)
        for row in actions:
            name = row['name']
            price = float(row['price'])
            aggregated_data[name] += price
        result = dict(aggregated_data)
        for stuff in sorted(result.items(), key=lambda item: item[1], reverse=True):
            print("{:s} {:.2f}".format(stuff[0], stuff[1]))
        total = 0
        for stuff in sorted(result.items(), key=lambda item: item[1], reverse=True):
            total += stuff[1]
        print("{:.2f}".format(total))


def main() -> int:
    # Example usage
    file_path = sys.argv[1]
    process_csv(file_path)
    return 0


if __name__ == '__main__':
    sys.exit(main())

