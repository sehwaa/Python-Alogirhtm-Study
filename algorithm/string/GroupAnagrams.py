from collections import defaultdict

group = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram = defaultdict(list)
for st in group:
    anagram[''.join(sorted(st.lower()))].append(st)

print([v for v in anagram.values()])