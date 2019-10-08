filename = "input.txt"	# Имя файла, с которым будешь работать
delimiter = '-'		# Разделитель-----(см. файл с номерами телефонов)----┑
			# Общий формат файла с номерами: Номер - ФИО - Адрес ┃
			#				       ┕----┶------┙

# Можно было сделать все без функций, но они нужны, исходя из условия
# Задача этой функции - прочитать файл по строкам и сформировать словарь со всеми номерами, именами, адресами, которые были в файле
# Параметры:
#	file - объект открытого файла для чтения из него
def CreateDictByFile(file):
	dict = {}	# Объявляем словарь(локальную переменную; эта переменная видна только в этой функции)
	uuid = 0	# Уникальный id нужен для создания уникального ключа в случае совпадения фамилий

	for line in file:	# Читаем по строчке файл, объект которого мы получили через парамерты

		i = 0
		key = ''	# Ключ, который будет использоваться в словаре; в нашем случае им будет являться фамилия

		while line[i] != delimiter:	# Номер телефона идет первым, поэтому скипаем его, т.к. нам нужна фамилия
			i += 1			# В этом цикле просто перемещаемся по строке и ищем первый разделитель(-)

		i += 2	# Перемещаемся вперед еще на 2 символа, чтобы оказаться ровно на первой букве фамилии в считаной строке

		while line[i] != ' ':	# Читаем фамилию
			key += line[i]	# Записываем фамилию по символу(буковке) в переменную
			i += 1

		# Есть один момент: что, если встретятся одинаковые фамилии?
		# Весь этот код слегка поломается
		# Захочешь показаться умнее - оставь следующие 3 строки кода и оставь 10 строку
		# Это учтение того, что в списке будут одинаковые фамилии
		
		if (dict.get(key) != None):	# Если в словаре уже есть запись с этим ключем(т.е. с этой фамилией)
			key += str(uuid)	# То прибавляем к ключу уникальный id, чтобы можно было создать запись в словаре с инфой именно об этом человеке,
						# а не перезаписать инфу про однофамильца
			uuid += 1		# Сохраняем уникальность идентификатора, просто инкрементируя его

		#

		dict[key] = line	# Добавляем запись в словарь. line - это строка из файла, key - это фамилия
		# Если первая строка в файле input.txt будет: 88005553531 - Еремин Иван Иванович - г. Санкт-Петербург, пр. Свободы
		# Тогда: line = '88005553531 - Еремин Иван Иванович - г. Санкт-Петербург, пр. Свободы'
		#	 key = 'Еремин'
		# В качестве ключа используется фалимия, т.к. нужно отсортировать по фамилии

	# Возвращаем сформираваный словарь
	return dict

# Сортируем по фамилии и перезаписываем отсортированный вариант обратно в файл
# Параметры:
#	file - объект открытого файла для записи в него
#	dict - словарь, который отсортируеся по ключам и из которого значения запишутся в файл
def SortAndRewrite(file, dict):
	file.seek(0)	# Перемещаем курсор на начало файла
	
	# Сортируем и перемещаемся от начала до конца уже по сортированному словарю
	for k in sorted(dict):	# k - это ключ
		file.write(dict[k])	# Пишем в файл

# Выше были функции, их ты будешь вызывать в своем коде, они выполнятся только тогда, когда ты их вызовешь, ниже - твой код

# Открываем файл с именем filename, режимом чтения и записи 'r+' и юникод кодировкой, т.к. ФИО на руссом языке
f = open(filename, mode="r+", encoding="utf-8")

# Вызываем нашу функцию для создания словаря, передаем аргументом объект нашего файла с номерами, который мы уже открыли
phonebook = CreateDictByFile(f)

# Вызываем нашу вторую функцию для записи в файл f отсортированных по фамилии значений из словаря phonebook
SortAndRewrite(f, phonebook)

# Закрываем файл
f.close()
