import datetime
try:
	import webbrowser
except:
	pass


christmas = [359,360]
year = 2018

def checkforleapyear(currentYear): #this function checks if the current year is a leap year
	if(int(str(currentYear)[-1])%2==0 and int(str(currentYear)[-2:])%4==0): 
		return True
	else:
		return False

def getAmountOfDaysPassed(months):
	days = 0
	currentMonth,currentDay = datetime.datetime.now().month,datetime.datetime.now().day
	for i in range(currentMonth-1):
		days += months[i]
	days += currentDay
	return days

def main():
	if(checkforleapyear(datetime.datetime.now().year) == False):
		months = [31,28,31,30,31,30,31,31,30,31,30,31]
		christmas = 359
	else:
		months = [31,29,31,30,31,30,31,31,30,31,30,31]
		christmas = 360

	days = getAmountOfDaysPassed(months)
	if(christmas-days==0):
		print("Merry Christmas!!")
		try:
			webbrowser.open('https://youtu.be/GETHJ-vQGwI')#plays jingle bells 10 hour version
		except:
			pass
	else:	
		print("There are only {} days left before christmas!".format(christmas-days))


main()

