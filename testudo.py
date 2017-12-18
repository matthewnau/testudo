import requests
from bs4 import BeautifulSoup
from time import sleep, strftime, gmtime
from random import randint

#returns the unique semester identifier
def getSemester():
	#start a new web scraping session
	s = requests.session()

	#download the main page of classes
	html = s.get("https://ntst.umd.edu/soc")

	#parse the html of the class page
	options = BeautifulSoup(html.text,"html.parser")
	options = options.find("select", {"id":"term-id-input"})
	options = str(options).split("</option>")

	#find the option with the semester code in it
	for option in options:
		if '"selected"' in option:
			semester = option

	#extract the semester code
	semester = semester[semester.index('value="')+7:]
	semester = semester[:semester.index('"')]

	#close the session
	s.close()

	return semester

#returns a list of sections
def getSections(course):
	#start a new web scraping session
	s = requests.session()

	#begin composing the url
	url = "https://ntst.umd.edu/soc/search"
	url += "?courseId=" + course
	url += "&sectionId="
	url += "&termId="+getSemester()
	url += "&_openSectionsOnly=on"
	url += "&creditCompare="
	url += "&credits="
	url += "&courseLevelFilter=ALL"
	url += "&instructor="
	url += "&_facetoface=on"
	url += "&_blended=on"
	url += "&_online=on"
	url += "&courseStartCompare="
	url += "&courseStartHour="
	url += "&courseStartMin="
	url += "&courseStartAM="
	url += "&courseEndHour="
	url += "&courseEndMin="
	url += "&courseEndAM="
	url += "&teachingCenter=ALL"
	url += "&_classDay1=on"
	url += "&_classDay2=on"
	url += "&_classDay3=on"
	url += "&_classDay4=on"
	url += "&_classDay5=on"

	#download the list of classes
	html = s.get(url).text

	#parse the html with bs4
	courses = BeautifulSoup(html,"html.parser").find_all("div", {"class":"section"})

	#make an empty list to contain all sections
	sections = []

	#loop through every section in the course list
	for course in courses:

		#declare a blank list to hold section and time info
		section = []
		times = []

		#get the times avaiable
		slots = course.find("div", {"class":"class-days-container"})
		slots = slots.find_all("div", {"class":"row"})

		#loops thorugh and add all time to the list
		for slot in slots:
			time = slot.find("div", {"class":"section-day-time-group"})
			time = " ".join(time.text.strip().split("\n"))
			times.append(time)

		#get the name of the course
		name = str(course.find("div", {"class":"section-action-links-container"}))
		name = name[name.index('value="')+7:]
		name = name[:name.index('"')]

		#append the name of the course to the list
		section.append(name)

		#get the amount of open seats
		openSeatsCount = int(course.find("span", {"class":"open-seats-count"}).text)

		#say whether class is open
		if openSeatsCount > 0:
			section.append("open")
		else:
			section.append("closed")

		#get the section number, and the instructor
		section.append(course.find("span", {"class":"section-id"}).text.strip())
		section.append(course.find("span", {"class":"section-instructor"}).text)

		#add the section information and the times
		sections.append(section)
		section.append(times)

	#close the current session
	s.close()

	#return all sections
	return sections

#returns if a section is open
def isOpen(section):
	if section[1] != "open":
		return False
	else:
		return True

#main function, continuously checks for openings
def testudo(course):

	#get all sections for the course
	sections = getSections(course)

	#loop through and list all sections
	for index, value in enumerate(sections):
		if index < 9:
			print("(0"+str(index+1)+") "+str(value))
		else:
			print("("+str(index+1)+") "+str(value))

	#get the section wanted, and check if open
	section = int(input("Type the list number for the section wanted: "))-1
	output = isOpen(sections[section])

	#if section not open, continuously check
	while output == False:
		output = isOpen(getSections(course)[section])
		print("["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] (section closed)")
		sleep(randint(35, 45))
	if output == True:
		print("["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] (section open)")
		'''
		Place custom notification code in this area!
		'''

#define the command line arguments
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        sys.stderr.write('usage: python3 testudo.py <course>\n')
        sys.exit(1)
    else:
        testudo(sys.argv[1].lower())