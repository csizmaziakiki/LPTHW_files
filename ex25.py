def split(string):
	words = string.split(' ')
	return words

def sort(words):
	return sorted(words)

def print_first(words):
	word = words.pop(0)
	print word

def print_last(words):
	word = words.pop(-1)
	print word

def main():
	print split("asd fgh jkl")
	sorted_words = sort('abc', 'cde', 'fgh')
	print sorted_words
	print_first('abc', 'cde', 'fgh')
	print_last("abc", "cde", "fgh")

if __name__=="__main__":
	main()
