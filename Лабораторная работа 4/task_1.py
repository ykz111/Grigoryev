import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
        sumF = sum(item["score"] * item["weight"] for item in data)
        return round(sumF, 3)
print(task())
