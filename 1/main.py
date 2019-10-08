filename = "input.txt"
delimiter = '-'

def CreateDictByFile(file):
	dict = {}

	for line in file:

		i = 0
		key = ''

		while line[i] != delimiter:
			i += 1

		i += 2

		while line[i] != ' ':
			key += line[i]
			i += 1

		dict[key] = line

	return dict


def SortAndRewrite(file, dict):
	file.seek(0)

	for k in sorted(dict):
		file.write(dict[k])

f = open(filename, mode="r+", encoding="utf-8")

phonebook = CreateDictByFile(f)

SortAndRewrite(f, phonebook)

f.close()