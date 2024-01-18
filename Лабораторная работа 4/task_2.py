import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, newline='') as cf:
        cr = csv.DictReader(cf)
        data = [row for row in cr]


    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as of:
        for line in of:
            print(line, end="")
