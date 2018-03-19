def greet2(name):
	print 'How are you, %s?'% name


def bye():
	print 'Okay, bye!'


def greet(name):
	print 'Hello, %s!'% name
	greet2(name)
	print 'Getting ready to say goodbye'
	bye()


if __name__ == '__main__':
	greet('Yuci')

