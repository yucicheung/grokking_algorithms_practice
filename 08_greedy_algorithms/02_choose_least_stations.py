def set_up_all():
	states_needed = set(['WA','MT','ID','OR','NV','UT','CA','AZ'])
	states_of_stations = {}
	states_of_stations['kone'] = set(['ID','NV','UT'])
	states_of_stations['ktwo'] = set(['WA','ID','MT'])
	states_of_stations['kthree'] = set(['OR','NV','CA'])
	states_of_stations['kfour'] = set(['NV','UT'])
	states_of_stations['kfive'] = set(['CA','AZ'])

	return states_needed, states_of_stations


def main():
	states_needed, states_of_stations = set_up_all()
	final_stations = set()
	while states_needed:
		most_covered = set()
		for station, states in states_of_stations.items():
			covered = states_needed & states
			if len(covered) > len(most_covered):
				best_station = station
				most_covered = covered
		
		final_stations.add(best_station)
		states_needed -= most_covered
	
	print "Final stations are:\n{}".format(final_stations)


if __name__=='__main__':
	main()
