
output = open("word_list.txt", "w")

def search_msgid():
	with open("django.po", "r") as ins:
		for line in ins:
			if str(line).startswith("msgid"):
				separator_pos = str(line).find(' ')
				word = str(line)[separator_pos:]
				output.write(word)
				print word

if __name__ == "__main__":
	print "Loading"
	search_msgid()