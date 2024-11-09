import csv
import sys

with open ('_csv_reader_data/Export_Sekce.txt', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter='\t', quotechar='"') #, quoting=csv.QUOTE_NONNUMERIC)
    while True:
        try:
            row = next(reader)
            print(row)
            print(len(row))
        except Exception as e:
            print(e)
            sys.exit()
        input('Press enter ...')

