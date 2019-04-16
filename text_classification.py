#Peter Lindee : 104757978
#CSCI 3832 - Natural Language Processing
#James Martin
#HW 3 - Text Classification

from collections import Counter
import math


def main():

	pos_file = open("hotelPosT-train.txt").read().split()			#open training data.
	neg_file = open("hotelNegT-train(1).txt").read().split()
	input_file = open("testdata.txt").read().split()
	outfile = open("hw3sol.txt",'w')								#open output file.

	N = len(input_file)
	pos_freqs = Counter(pos_file)									#dictionary of pos file.
	neg_freqs = Counter(neg_file)
	#print neg_freqs
	print neg_freqs['the']	
	neg_size = float(sum(neg_freqs.values()))
	pos_size = float(sum(pos_freqs.values())) 							# 			   neg file

	with open("testdata.txt", 'r') as f:
								
		for line in f:
			words = line.split()
			pos_prob = 1.0
			neg_prob = 1.0	
			pos_val = 1.0
			neg_val = 1.0						
			for i in range(len(words)):														
				if words[i] in pos_freqs:											
					#continue
					pos_val = (pos_freqs[words[i]] + 1)
					pos_val = math.log(pos_val, 10)
					pos_prob += pos_val  						#calculate unigram prob for each line using pos training data.
				
				if words[i] in neg_freqs:
					#continue
					neg_val = (neg_freqs[words[i]] + 1) 
					neg_val = math.log(neg_val, 10)
					neg_prob += neg_val							#unigram unigram prob for each line using neg training data.

			pos_prob = pos_prob / pos_size
			neg_prob = neg_prob / neg_size
			if pos_prob > neg_prob :															
				outfile.write(line[0:7] + '\t' + 'POS' + '\n')	
				#print 'pos'									#whichever prob is higher, output ID and classificatiion to outputfile.
			if neg_prob > pos_prob :
				#print 'neg'
				outfile.write(line[0:7] + '\t' + 'NEG' + '\n')
         
	outfile.close()

if __name__ == "__main__":
	main()