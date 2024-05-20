import json
import csv


with open('data.json', 'r') as json_file:
    data = json.load(json_file)


with open('output.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)


    csv_writer.writerow(['reel', 'imaginaire'])


    for complex_number in data:
        csv_writer.writerow(complex_number)
print(data)