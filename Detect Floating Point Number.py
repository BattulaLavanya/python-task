import re
for _ in range((input())):
	print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
