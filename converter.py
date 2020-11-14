import csv
from pathlib import Path

path = Path("History.csv")
# for file in path.glob("*"):
#     print(file)


class Day:
    def __init__(self, date, network, down, up, total):
        self.date = date
        self.network = network
        self.down = down
        self.up = up
        self.total = total

    def __str__(self):
        return f"date: {self.date}, network: {self.network}, down: {self.down}, up: {self.up}, total: {self.total}"


data = []


def dataReader():
    with open(path) as fp:
        reader = csv.reader(fp, delimiter=",")
        for row in reader:
            data.append(Day(row[0], row[1], row[2], row[3], row[4],))


dataReader()
print(data[1])
# print
