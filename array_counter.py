numbers="4 11 3 12 2 12 13 11 6 11 8 2 6 7 2 2 12 7 11 13 5 8 6 7 4 6 10 5 13 11 12 3 8 1 1 10 12 1 7 4 12 2 6 4 9 7 6 8 1 3 7 5 10 13 12 13 5 8 5 5 5 3 7 13 4 8 9 3 8 3 6 6 4 12 10 12 6 2 6 6 5 13 11 1 12 9 1 4 3 6 8 8 8 2 7 12 9 3 1 3 6 7 9 9 5 6 8 10 7 1 2 12 13 13 12 11 8 13 2 11 5 9 6 13 10 13 11 5 2 11 8 8 5 4 3 9 9 11 5 3 11 7 1 10 6 13 8 1 12 9 12 4 5 4 3 1 3 1 6 5 11 1 12 3 5 2 11 13 12 3 3 9 10 3 6 3 3 13 3 2 9 1 5 13 5 7 1 7 8 7 11 6 7 10 8 11 11 5 11 9 7 13 5 4 3 10 6 5 9 8 6 5 9 11 4 13 4 4 7 12 11 5 4 4 1 11 2 12 2 13 7 9 12 11 12 2 8 5 6 4 13 12 8 9 9 11 9 13 2 2 11 12 6 1 3 7 11 4 5 13"
array_of_numbers=numbers.split(" ")

results=[0]*13

for number in array_of_numbers:
	i=int(number)
	results[i-1] +=1
print results