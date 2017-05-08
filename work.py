import calendar
from collections import defaultdict, Counter
from csv import DictReader
from time import strptime

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


def gender_by_race():
	rasa_napadalca = set(reports[:, 15])
	print(rasa_napadalca)
	d = dict()
	for rasa in rasa_napadalca:
		d[rasa] = {
			'm': 0,
			'z': 0
		}
	for line in reports:
		if line[14] == 'Male':
			d[line[15]]['m'] += 1
		elif line[14] == 'Female':
			d[line[15]]['z'] += 1

	male = [d[rasa]['m'] for rasa in rasa_napadalca]
	female = [d[rasa]['z'] for rasa in rasa_napadalca]

	fig, ax = plt.subplots(1, 1)
	plt.title("Razmerje moških proti ženskam glede na raso")
	plt.xlabel("Rasa morilca")
	plt.ylabel("Število umorov")
	plt.bar(range(len(rasa_napadalca)), male, color="cyan", align="center", label="Moški")
	plt.bar(range(len(rasa_napadalca)), female, bottom=male, color="magenta", align="center", label="Ženske")
	ax.xaxis.set_ticks(np.arange(0, len(rasa_napadalca), 1))
	ax.set_xticklabels(rasa_napadalca)
	plt.legend()
	plt.show()


def solved_by_states():
	drzave = set(reports[:, 6])
	d = dict()
	for state in drzave:
		d[state] = {
			'da': 0,
			'ne': 0
		}

	for line in reports:
		if line[23] == 'Yes':
			d[line[6]]['da'] += 1
		elif line[23] == 'No':
			d[line[6]]['ne'] += 1

	solved = [d[drzava]['da'] for drzava in drzave]
	unsolved = [d[drzava]['ne'] for drzava in drzave]

	fig, ax = plt.subplots(1, 1)
	plt.title("Razmerje rešenih primerov po državah")
	plt.xlabel("Države")
	plt.ylabel("Število umorov")
	plt.bar(range(len(drzave)), solved, color="cyan", align="center", label="Rešeni")
	plt.bar(range(len(drzave)), unsolved, bottom=solved, color="magenta", align="center", label="Nerešeni")
	ax.xaxis.set_ticks(np.arange(0, len(drzave), 1))
	plt.gca().set_xticklabels(drzave, rotation=90)
	plt.tight_layout()
	plt.legend()
	plt.show()


def murders_by_month():
	meseci = reports[:, 7]
	c = Counter(meseci)
	meseci_ime_n = [strptime(x, '%B').tm_mon for x in list(c.keys())]
	meseci_num = list(c.values())
	tup = list(zip(meseci_ime_n, meseci_num))
	tup.sort(key=lambda tup: tup[0])
	tup = list(zip(*tup))
	meseci_ime = [calendar.month_name[x] for x in tup[0]]

	fig, ax = plt.subplots(1, 1)
	plt.title("Število umorov skozi mesece")
	plt.xlabel("Meseci")
	plt.ylabel("Število umorov")
	ax.xaxis.set_ticks(np.arange(1, 13, 1))
	ax.set_xticklabels(meseci_ime)
	plt.bar(tup[0], tup[1])
	plt.ylim([40000, 60000])
	plt.show()


def age_distribution():
	attacker = []
	victim = []
	for line in reports:
		if reports[13] == ' ' or line[18] == ' ':
			continue
		if int(line[13]) in (998, 0, ' ') or int(line[18]) in (998, 0, ' '):
			continue
		victim.append(int(line[18]))
		attacker.append(int(line[13]))

	plt.subplot(211)
	plt.hist(attacker)
	plt.yticks([])
	plt.title("Porazdelitev starosti napadalcev")
	plt.xlabel("Starost napadalca")

	plt.subplot(212)
	plt.hist(victim)
	plt.title("Porazdelitev starosti žrtev")
	plt.xlabel("Starost žrtve")
	plt.yticks([])
	plt.tight_layout()
	plt.show()


age_distribution()
murders_by_month()
solved_by_states()
gender_by_race()
barh(sorted(solutions), "Difference between solved and unsolved crimes", "# of crimes", "Crime solved")
