from collections import deque


def set_up_graph():
	graph = {}
	graph['you'] = ['alice','bob','claire']
	graph['alice'] = ['peggy']
	graph['bob'] = ['anuj','peggy']
	graph['claire'] = ['thom','jonny']
	graph['anuj'] = []
	graph['peggy'] = []
	graph['jonny'] = []
	graph['thom'] = []
	return graph


def set_up_close_graph():
	graph = {}
	graph['you'] = ['alice']
	graph['alice'] = ['you']
	return graph


def check_is_seller(name):
	return name[-1] == 'm'


def bfs(graph):
	searched = []
	search_que = deque()
	search_node = 'you'
	neighbors = graph[search_node]
	search_que += neighbors
	while search_que:
		name = search_que.popleft()
		if name not in searched:
			if check_is_seller(name):
				return name
			else:
				search_que += graph[name]
			searched.append(name)
	return None


def main():
	for graph_type in ['set_up_graph','set_up_close_graph']:
		graph = eval(graph_type)()
		seller = bfs(graph)
		print 'Graph is {}'.format(graph)
		if seller:
			print 'The mango seller is {}.'.format(seller.title())
		else:
			print "You don't know any mango seller."
	

if __name__ == '__main__':
	main()
