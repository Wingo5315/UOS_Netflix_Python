import csv
with open('../data/netflix_data.csv', newline='') as csvfile:
    the_reader = csv.reader
    for row in the_reader:
        print(', '.join(row))
