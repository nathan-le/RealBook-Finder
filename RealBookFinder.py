import sys, re, os


offset = {'colorado' : 3,
		  'jazzfake': -1,
		  'jazzltd' : 7,
		  'evansbk' : 3,
		  'library' : 4,
		  'newreal1' : 15,
		  'newreal2' : 12,
		  'newreal3' : 10,
		  'realbk1' : 13,
		  'realbk2' : 7,
		  'realbk3' : 5}


args = sys.argv
#For now limit only to one requested title
if len(args) > 2:
	print("Requested too many titles. Please try again.")
	exit()

#Our Master Index Text File
file = open("Master_index.txt", "r")

#Entry Processing
for entry in file.readlines():

	#Confirming our entry
	if args[1].lower() in entry.lower():
		#removes in between whitespace
		parsedEntry = re.split(r'\s{2,}', entry)
		print(parsedEntry)

		#text entry for our apple script
		book = "{}.PDF".format(parsedEntry[1].upper())
		filepath = os.getcwd()
		page = parsedEntry[2].rstrip()
		#re-index due to page offset 
		page = int(page) + offset[parsedEntry[1].lower()]

		#call upon apple script for pdf page pull up
		request = "osascript pagefinder.scpt '{}/RealBooks/{}' {}"
		# print(request.format(filepath, book, page))
		os.system(request.format(filepath, book, page))


file.close()

