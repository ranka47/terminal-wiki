import wikipedia
import sys
if(len(sys.argv) < 2):
    print "No input to search"
    exit()

results = wikipedia.search(sys.argv[1])

if(len(results) > 0):
    print "Here are the results"
else:
    print "No results found"
    exit()
for i in range(0, len(results)): 
    print ("%2d: %s" % (i+1, results[i]))
choice = input("Choose which result you want to see: ")

if choice in range(1, len(results) + 1):
    page = wikipedia.page(results[choice - 1])
else:
    print "Sorry, wrong choice!"
    exit()

print "-------------------Summary-------------------"
print page.summary
print "---------------------------------------------"
file = open(page.title + ".txt", 'w')
file.write(page.content.encode('utf-8'))
file.close()
print "If you want more details, check out this file: " + page.title + ".txt"