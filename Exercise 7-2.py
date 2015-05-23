# prompt for file name
fname = raw_input('Enter the file name: ')

# checks to see if file name is valid
try:
	fhandle = open(fname)
except:
	print 'File cannot be opened: ', fname
	exit()

# set count and total to 0
count = 0
total = 0


for line in fhandle:
# searches for desired line
	if line.startswith('X-DSPAM-Confidence:'):
# ups the count by 1
		count = count + 1
# pulls out the floating point number
		colpos = line.find(':')
		spam = line[colpos+1: ]
		spam = spam.lstrip()
		spam = float(spam)
# pulls out the floating point number
# adds the floating point number to the total
		total = total + spam

# prints the average at the end of the file
print 'Average spam confidence: ', total / count