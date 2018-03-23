from pprint import pprint


def find_lowest_cost(costs,to_process):
	lowest_cost_node = to_process[0]
	lowest_cost = costs[lowest_cost_node]
	if len(to_process)>1:
		for node in to_process[1:]:
			new_cost = costs[node]
			if new_cost < lowest_cost:
				lowest_cost = new_cost
				lowest_cost_node = node
	return lowest_cost_node


def set_up_graph():
	graph = {}
	graph['start'] = {"A":6,"B":2}
	graph["A"] = {'fin':1}
	graph["B"] = {"A":3,"fin":5,"C":1}
	graph["C"] = {"B":1}
	graph['fin'] = {}
	return graph


def initialize_costs_n_fathers(graph):
	costs, fathers ={},{}
	for node in graph:
		if node is "start":
			costs[node] = 0
			fathers[node] = None
		else:
			costs[node] = float('inf')
	return costs,fathers


def get_shortest_path(fathers):
	path = []
	father = 'fin'
	path.append(father)
	while father != 'start':
		father = fathers[father]
		path.append(father)
	print 'Shortest path is:',
	for i in path[-1:-len(path):-1]:
		print '{}-->'.format(i),
	print path[0]


def main():
	graph = set_up_graph()
	print 'Graph as below:'
	pprint(graph)
	print '\n'
	costs, fathers = initialize_costs_n_fathers(graph)
	to_process = [i for i in graph.keys()]
	to_process.remove('fin')
	while to_process:
		node = find_lowest_cost(costs,to_process)
		neighbors = graph[node]
		for neighbor in neighbors:
			new_cost = costs[node] + graph[node][neighbor]
			if new_cost < costs[neighbor]:
				costs[neighbor] = new_cost
				fathers[neighbor] = node
		to_process.remove(node) # keys donnot share names
	get_shortest_path(fathers)
	print 'The lowest cost is {}.'.format(costs['fin'])
	
	
if __name__=='__main__':
	main()
