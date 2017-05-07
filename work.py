from collections import defaultdict
from csv import DictReader
import numpy as np
import matplotlib.pyplot as plt

reports_data = []
reports = []

"""
0: Record ID
1: Agency Code
2: Agency Name
3: Agency Type
4: Record Source
5: City
6: State
7: Month
8: Year
9: Incident
10: Crime Type
11: Weapon
12: Relationship
13: Perpetrator Age
14: Perpetrator Sex
15: Perpetrator Race
16: Perpetrator Ethnicity
17: Perpetrator Count
18: Victim Age
19: Victim Sex
20: Victim Race
21: Victim Ethnicity
22: Victim Count
23: Crime Solved
"""


def read_data(file_path, result):
    with open(file_path, "rt", encoding="utf-8") as file:
        reader = DictReader(file)
        for row in reader:
            result.append(row)


def histogram(data, title, x, y):
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.bar(list(data.keys()), list(data.values()))
    plt.show()


def barh(data, title, x, y):
    values, labels = ([a for a, b in data], [b for a, b in data])
    plt.figure()
    y_axis = np.arange(1, len(labels) + 1, 1)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.barh(y_axis, values, align='center')
    plt.yticks(y_axis, labels)
    plt.show()


read_data("data/database.csv", reports_data)

for report in reports_data:
    reports.append([report["Record ID"], report["Agency Code"], report["Agency Name"], report["Agency Type"],
                    report["Record Source"],
                    report["City"], report["State"], report["Month"], report["Year"], report["Incident"],
                    report["Crime Type"], report["Weapon"], report["Relationship"], report["Perpetrator Age"],
                    report["Perpetrator Sex"], report["Perpetrator Race"],
                    report["Perpetrator Ethnicity"], report["Perpetrator Count"], report["Victim Age"],
                    report["Victim Sex"], report["Victim Race"], report["Victim Ethnicity"],
                    report["Victim Count"], report["Crime Solved"]])
reports = np.array(reports)

years = set(reports[:, 8])
weapons = set(reports[:, 11])
solution = set(reports[:, 23])
state = "South Dakota"

###
# Zanimivi stati:
# California
# Sauth Dakota
# Hawaii
###

reports_by_year = {int(year): len(reports[reports[:, 8] == year, 1]) for year in years}
reports_by_year_in_state = {int(year): len(reports[(reports[:, 6] == state) & (reports[:, 8] == year), 1]) for year in
                            years}
reports_by_weapon = [(len(reports[reports[:, 11] == weapon, 1]), weapon) for weapon in weapons]
solutions = [(len(reports[reports[:, 23] == sol]), sol) for sol in solution]

print("Should be here")

histogram(reports_by_year, "Crimes per year in USA", "Year", "Number of crimes")
histogram(reports_by_year_in_state, "Crimes per year in USA in state of {}".format(state), "Year", "Number of crimes")
barh(sorted(reports_by_weapon), "Number of crimes committed by weapon", "# of crimes", "Weapon")
barh(sorted(solutions), "Difference between solved and unsolved crimes", "# of crimes", "Crime solved")
