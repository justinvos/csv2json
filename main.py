import csv
import json

def convert(csv_file_path, json_file_path):
    objs = []
    with open(csv_file_path) as input_file:
        csv_reader = csv.reader(input_file)

        headers = csv_reader.__next__()
        for line in csv_reader:
            obj = {}
            for index in range(len(line)):
                header,value = headers[index],line[index]
                obj[header] = value
            objs += [obj]

    with open(json_file_path, 'w') as output_file:
        output_file.write(json.dumps({ 'output': objs }))

convert('panels.csv', 'panels.json')
