class Trie:
	def __init__(self):
		self.front_root = {'len': []}
		self.back_root = {'len': []}
	
	def insert(self, s, front):
		cur_node = self.front_root if front else self.back_root
		cur_node['len'].append(len(s))

		for c in s:
			if c not in cur_node:
				cur_node[c] = {'len': []}
			cur_node = cur_node[c]
			cur_node['len'].append(len(s))
		
		cur_node['len'].append(len(s))
	
	def search(self, s, front):
		cur_node = self.front_root if front else self.back_root
		s = s if front else s[::-1]

		for c in s:
			if c == '?':
				return cur_node['len'].count(len(s))
			elif c in cur_node:
				cur_node = cur_node[c]
			else:
				break


def solution(words, queries):
	answer = []
	wordTree = Trie()

	for word in words:
		wordTree.insert(word, True)
		wordTree.insert(word[::-1], False)
	
	for query in queries:
		result = wordTree.search(query, query[0] != '?')
		answer.append(result if result else 0)

	return answer