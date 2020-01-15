#!/usr/bin/python
# Peter Lindee - 
#  
#	
# ** Sources ** :
# - bigramModel()  - rstudio-pubs-static.s3.amazonaws.com/115676_ab6bb49748c742b88127e8b5ce3e1298.html, github.com/karanmotani/bigram-probabilities

from collections import Counter 

def main():

	test1 = "<s> i would like to eat </s>"
	test2 = "<s> i am sam </s>"

	file1 = open('test.txt','r')
	file2 = open('lindee-peter-assgn2-unigram-out.txt', 'w')
	file3 = open('lindee-peter-assgn2-bigram-out.txt', 'w')

	for line in file1:
		x = bigramModel(line)
		y = unigramModel(line)
		x = str(x)
		y = str(y)
		print x
		file2.write(x)
		file2.write('\n')
		file3.write(y)
		file3.write('\n')


	print bigramModel(test1)
	print unigramModel(test1)

def unigramModel(sentence):

	data = open("berp-training.txt").read()
	words = data.split()

	if len(words) == 0:
		return 'no data in file'

	sentences = sentence.split()

	freqs = Counter(words)
	input_ = Counter(sentences)

	unk = "<unk>"

	for count in freqs.copy():						#handle unknown words from training data
		if freqs[count] == 1:
			freqs.pop(count)
			freqs[unk] += 1

	for word in input_.copy():										#handle unknown words from user input
		if freqs[word] <2:
			input_.pop(word)
			input_[unk] += 1

	uniprob = 1
	for word in input_:			
		if word in freqs:		
			uniprob = uniprob * (freqs[word]/float(sum(freqs.values()))) #calculate unigram probability
		else:
			uniprob = uniprob * 0.00

	if(uniprob == 0.000000):
		return 'String Not Found'

	return uniprob

def bigramModel(sentence): #note to grader: I couldn't get <unk> preprocessing to work with so it was not included					
	file = open("berp-training.txt").read().split()
	if len(file) == 0:
		return 'no data in file'
	unk = "<unk>"
	contents = []
	for words in file:									#handle training data
		contents.append(words)

	unicounts = Counter(file)							#creat unigram counts -> used for bigram probability 
	corpus_size = len(unicounts)
	#unigram counts

	bigrams = []
	bicounts = {}

	for i in range(len(contents)-1):					#create a list of bigrams and dictionary of bigram counts from file data
		bigrams.append((contents[i], contents[i+1]))
		if contents[i] not in bicounts:
			bicounts[contents[i], contents[i+1]] = 1
		else:  
			bicounts[contents[i], contents[i+1]] += 1

	biprobs = {}
	for bigram in bigrams:								#collect probabilities of given bigrams - Count(w-1, w) / Count(w-1)
		w1 = bigram[0]
		biprobs[bigram] = (bicounts[bigram]+1)/(float(unicounts[w1]+corpus_size)) 	#add-k smoothing
	#print biprobs

	userinput = []		
	sentences = sentence.split()						#handle user input
	for i in range(len(sentences)-1):
		userinput.append((sentences[i], sentences[i+1]))

	biprob = 1.0										
	for i in range(len(userinput)):
		if userinput[i] in biprobs:
			biprob = biprob * biprobs[userinput[i]]		#find bigram probability of user input
		else:
			biprob = biprob * 0.00

	return biprob

	

if __name__ == "__main__":
	main()












