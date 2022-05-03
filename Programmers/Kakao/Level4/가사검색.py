from collections import deque

def insert(s, root, mode):
  cur_node = root
  if mode:
    for i in range(len(s)):
      token = s[i]
      if token not in cur_node:
        cur_node[token] = {}
      else:
        cur_node[token][1] += 1
      cur_node = cur_node[token]
    cur_node["*"] = [s]
  else:
    for i in reversed(range(len(s))):
      token = s[i]
      if token not in cur_node:
        cur_node[token] = [{}, 1]
      else:
        cur_node[token][1] += 1
      cur_node = cur_node[token]
    cur_node["*"] = [s]

def front_search(s, root):
  cur_node = root
  count = 0
  for i in range(len(s)):
    token = s[i]
    if token != "?":
      if token in cur_node:
        cur_node = cur_node[token]
      else:
        return 0
    else:
      count += cur_node[1]
      break
  return count

def back_search(s, root):
  cur_node = root
  count = 0
  for i in reversed(range(len(s))):
    token = s[i]
    if token != "?":
      if token in cur_node:
        cur_node = cur_node[token]
      else:
        return 0
    else:
      count += cur_node[1]
      break
  return count

def solution(words, queries):
  answer = []

  front_trie = {}
  back_trie = {}
  length = []

  for word in words:
    insert(word, front_trie, length, True)
    insert(word, back_trie, length, False)
  
  for query in queries:
    if query[-1] == "?":
      answer.append(front_search(query, front_trie))
    elif query[0] == "?":
      answer.append(back_search(query, back_trie))

  return answer

words = ["frodo", "frozz", "frozz", "frozen", "frame", "kakao"]
queries = ["fro??"]
print(solution(words, queries))