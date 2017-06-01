import pandas
import xlwt

df = pandas.read_excel(r'rand_10.xlsx')

f = open('classes.txt', 'w')

rez = ""

for column in df:
	values = df.get(column)
	discrete_values = dict()
	rez += column.upper() + "\n"
	for i, value in enumerate(set(values)):
		if type(values[0]) is str:
			discrete_values[value] = i
			rez += str(value) + " -> " + str(i) + "\n"
	rez += "------------------\n\n"
	if type(values[0]) is str:
		for row in range(len(values)):
			modified = discrete_values[df.loc[row, column]]
			df.loc[row, column] = modified
f.write(rez)
f.close()

writer = pandas.ExcelWriter('numerized.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()