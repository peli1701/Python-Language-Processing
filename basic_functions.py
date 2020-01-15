#Peter Lindee

def compute_census(list_of_rates, current_population):
	seconds = 31536000
	birth_rate = list_of_rates[0]
	death_rate = list_of_rates[1]
	new_immigrants_rate = list_of_rates[2]

	birth_rate = seconds / birth_rate
	death_rate = seconds / death_rate
	new_immigrants_rate = seconds / new_immigrants_rate

	future_pop = current_population + birth_rate - death_rate + new_immigrants_rate 
	return future_pop

#convert_seconds is a function that does not take in any parameters. Instead, it converts
#a user inputted value for seconds that will be converted into the corresponding days, hours, 
#minutes, and seconds. For example, if 1,000,000 seconds are entered, the function will calculate
#the amount of days by dividing that amount by how many seconds there are in a day and so on.
def convert_seconds():
	input = raw_input()
	input = int(input)
	seconds = input % 60
	minutes = (input % 3600) / 60
	hours = input / (3600)
	hours = hours % (24)
	days = input / (60 * 60 * 24)
	print("{} corresponds to: {} days, {} hours, {} minutes, {} seconds.".format(input, days, hours, minutes, seconds))

#Part 2:

#my generate_story function takes in a list of strings as parameters and uses them along with
#prompts to generate a story for the user. The parameter given starts with a story followed by 
#a prompt so we can iterate the index twice each run through in order to compensate for multiple
#strings or prompts. This function is very simple because once we iterate the index correctly all 
#that is left is to concatenate the string and print its value outside of the while loop.
def generate_story(list_to_story):
	i = 0 
	string = " "
	while i < len(list_to_story):
		str = list_to_story[i]
		prompt = list_to_story[i+1]
		banana = raw_input(prompt + " ")
		i = i+2
		string = string + str + " " + banana + " "
	print(string)
	return string

#Part 3:

#similarity_score is a function that serves to calculate a hamming distance between two sequences 
#that are given as parameters. In order to calculate the hamming distance, we must first check that 
#the two sequences are the same length. Then we must check for characters that are not equal in the 
#given sequences. If they arent equal, that means there is mistmatch and the counter rises in value. 
#lastly, the hamming distance is calculated by subtracting the amount of mistmatches in a sequence
#and dividing it by the length of the sequence iself. For example, if a string is 10 characters long,
#and there are 3 mismathes, the hamming distance would be 0.7.
def similarity_score(seq1, seq2):
	i = 0;
	count = 0.0; 
	length1 = len(seq1)
	length2 = len(seq2)
	if (length1 == length2):
		while(i < length1):
			if (seq1[i] != seq2[i]):
				count = count + 1
			i = i + 1
		score = (length1 - count) / length1
		return score
	else:
		return 0	

#best_match takes in two parameters, a string genome, and a specific sequence of that genome. It serves
#to find the best similarity score of the genome by looping through the genome and calling upon our 
#similarity score functon which calculates the hamming distance for each sequence. Whichever sequence has
#the best score, or hamming distance, is returned in the form of the index at the position of that sequence. 
def best_match(string, seq):
	goodScore = 0.0
	x = 0 
	sim = 0
	for i in range(0, len(string)):
		substring = string[i:len(seq)+i]
		sim = similarity_score(substring, seq)
		if sim > goodScore:
			goodScore = sim
			x = i 
	return x

#Part 4:

#My calc_stats function is very simple. It serves to calculate the average and median value for a given list of 
#values which are passed in as parameters. The average value is calculated by dividing the sum of the list by 
#the length of the list. Python has built in functions for sum and length which make this calculaion easy. To 
#calculate the median value, sorting the list is essential. After we use the built in sort function, we calculate
#the median value by dividing the length of the string in half and finding where the length is evenly divisible by 2.
#Once the median is calculated, we add the avg and median values to a new list and return that list. 
def calc_stats(list_of_values): 
	sum1 = 0.0
	median = 0.0
	avg = 0.0
	x = sorted(list_of_values)
	avg = float(sum(x))/float(len(x))
	for i in range(len(x)):
		length = len(x)
		k = length / 2
		if length % 2 == 0:
			median = (x[k] + x[k-1]) / 2.0
		else:
			median = x[k]
	newList = [avg, float(median)]
	return newList

#Part 5:

#the parse_ratings function involves file I/O in order to create a list containing usernames and book ratings
#of students. The function takes one parameter, the file containing the students information. We first must open
#the file and read in its contents line by line. Next, we must split the lines and remove commas and spaces. From here,
#we can place the students names and ratings into appended lists. We know that its a students vs a rating because
#students are always the first index of a line while the ratings are the next index positions. We must append our lists
#when putting in the values or else the lists would be overwritten for each iteration through the line loop. 
def parse_ratings(file_name):
	myList = []
	myFile = open(file_name, 'r')
	if (myFile.closed):
		return "File is closed. Open it!"
	else:
		for i in myFile:
			ze_list = i.split(',')
			nameList = []
			nameList.append(ze_list[0])
			numberList = [] 
			new = ze_list[1].split(' ')
			for x in new:
				if x != '':
					numberList.append(int(x))

			nameList.append(numberList)
			myList.append(nameList)

		myFile.close()
		return myList

def main(): 
#The following functions serve as testers to validate that each of my 8 functions are working as intended
#involving different any different test parameter given. 

	#print(compute_census([8, 12, 33], 1000000))
	#convert_seconds()
	#generate_story(["I went skiing to", "Enter a location", "hours", "and I stayed in line for "])
	#print(similarity_score("CCGCCGCCGA", "CCTCCTCCTA"))
	#print(best_match("GTGCCGCCGA", "CCC"))
	#(calc_stats([2,1,5,3,4]))
	parse_ratings('mynamejeff.txt')


if __name__ == "__main__" :
	main()
		

