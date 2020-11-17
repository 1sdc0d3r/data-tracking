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

# load in csv file
with open(path) as fp:
    reader = csv.reader(fp, delimiter=",")
    # del[data[0]]
    for row in reader:
        data.append(Day(row[0], row[1], row[2], row[3], row[4]))

del data[0]
# sort data by date w/ range at 1 to keep headers
for j in range(1, len(data) - 1):
    for i in range(1, len(data) - 1):
        if data[i].date > data[i+1].date:
            data[i], data[i+1] = data[i+1], data[i]


for day in data:
    # day.up = int(float(day.up)*.001)
    # day.down = int(float(day.down)*.001)
    # day.total = int(float(day.total)*.001)
    print(day)
    print(int(float(day.up)))
    # print(day.total)
    # print(data[1])
