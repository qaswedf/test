data = []
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)

wc = {}
for d in data:
	words = d.split(" ")
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
# sum_len = 0
# for d in data:
# 	sum_len = len(d) + sum_len
# avg = sum_len / len(data)
# print(avg)
