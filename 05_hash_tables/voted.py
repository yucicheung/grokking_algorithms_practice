voted = {} # voted = dict()


def check_voter(name):
	print '{} wants to vote!'.format(name)
	if voted.get(name):
		print "kick {} out!".format(name)
	else:
		voted[name] = True
		print "Let {} vote!".format(name)

check_voter('Yuci')
check_voter('Yuci')
