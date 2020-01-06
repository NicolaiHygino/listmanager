from datetime import date
import sys


def read_file():
	file = open('list.txt', 'r')
	content = file.readlines()
	file.close()
	return content


def write_file(changes):
	file = open('list.txt', 'w')
	if changes:
		file.writelines(changes)
	file.close()


def today_date():
	date_today = date.today()
	date_format = ('{}/{}/{}'.format(date_today.day, date_today.month, date_today.year))
	return date_format


def add_word(word):
	try: 
		content = read_file()

	except:
		write_file()
		content = read_file()

	last_number = str(len(content) + 1)
	content.append('{}. {} - {}\n'.format(last_number, word, today_date()))
	
	write_file(content)
	print('{} added with sucsess!'.format(word))
	display_words()


def enumerate_lines():
	content = read_file()
	
	content_enumerated = []
	for index, value in enumerate(content):
		splited_line = value.split()
		del splited_line[0]
		splited_line.append('\n')
		pos = '{}.'.format(index + 1)
		content_enumerated.append(' '.join([pos, ' '.join(splited_line)]))

	write_file(content_enumerated)
	print('renumerated with success!')


def display_words():
	content = read_file()
	for line in content:
		print(line)


def del_word(pos):
	content = read_file()
	
	position = int(pos) - 1
	confirmation = input('Are you sure you want to delete {}? [yes/no]: '.format(content[position]))

	if confirmation == 'yes':
		del content[position]

	else:
		sys.exit(1)

	write_file(content)
	enumerate_lines()
	display_words()


def help():
	print(
"""
--addword word

--displaywords

--delword position

--enumeratelines

"""
)


def main():
	if len(sys.argv) < 2:
		print('use --help for help')
		sys.exit(1)

	option = sys.argv[1]

	if option == '--addword':
		word = sys.argv[2]
		add_word(word)
	
	elif option == '--displaywords':
		display_words()

	elif option == '--delword':
		position = sys.argv[2]
		del_word(position)
	
	elif option == '--enumeratelines':
		enumerate_lines()

	elif option == '--help':
		help()

	else:
		print(
"""
Warning: {} is not a command.
Run help for a list of a available commands.""".format(sys.argv[1])
)


if __name__ == '__main__':
	main()
	