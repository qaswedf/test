data = []
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)

sum_len = 0
for d in data:
	sum_len = len(d) + sum_len
avg = sum_len / len(data)
print(avg)
