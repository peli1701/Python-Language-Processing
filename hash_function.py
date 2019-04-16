	
	# ****** SOURCES *******: #
	# hash function resource: https://stackoverflow.com/questions/26292487/python-hashing-with-string
	# matplotlib resource: https://stackoverflow.com/questions/32541659/plotting-histogram-with-given-x-and-y-values
	#																										
import csv
import random
import matplotlib.pyplot as plt
import numpy as np
import math

def char_to_index(name):
	sum_ = 0
	a = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R' ,'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	for i in range(len(name)):
		for j in range(len(a)):
			if(name[i] == a[j]):
				sum_ += (j+1)
	return sum_%170

def max_bucket(hash_list):
	return max(hash_list)

names = []
num_buckets = 175							

with open('data.csv', mode='r') as csv_file:		#read in data
	csvReader = csv.reader(csv_file)
	for row in csvReader:
		names.append(row[0])

random.shuffle(names)								#randomize data
size = (len(names))/2

rand_names = []
for i in range((size)):								#grab half of randomized data
	rand_names.append(names[i])

hash_list = [0 for x in range(175)]
max_ = 0
max_list = []
max_depth = []
uniform_max = []
cn = []
for name in rand_names:
	x = char_to_index(name)
	hash_list[x] += 1
	y = max_bucket(hash_list)
	if y > max_:
		max_list.append(y)

c = 1
for i in range(len(rand_names)):
	max_depth.append(math.log(c,2))
	print math.log(c,2)
	c += 1
	cn.append(.01*i)


plt.title("Hash Table")						#build histogram, x coords = num buckets, y coords = list of hashed-values
plt.xlabel("buckets")
plt.ylabel("bucket cardinality")
x1 = plt.bar(range(0,num_buckets), hash_list, color = 'green')

x = range(0, size)
y=plt.plot(x, max_list, color = 'red')
y=plt.plot(x, max_depth, color = 'blue')
y= plt.plot(x, cn, color = 'purple')

plt.show(x1) 
plt.show(y)




