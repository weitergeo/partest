import csv
with open('Test_1.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('Test_new.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)

        for line in csv_reader:
            csv_writer.writerow(line)
