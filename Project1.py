import re
import requests

rootURL = 'http://www.mosigra.ru/'
allURLs = [rootURL]
allMails = []
RecursionDepth = 0

def findAllMails(URLParameter):
	global allURLs, allMails, RecursionDepth
	RecursionDepth += 1
#parsing the URL
	URLVariable = requests.get(URLParameter)
	allURLsNew = list(set(re.findall('href="(.*?)"',URLVariable.text)))
	allMailsNew = list(set(re.findall(r'mailto:[a-zA-Z0-9-\.@_]+',URLVariable.text)))
#recursive call + result formation
	for mail in allMailsNew:
		mail = mail[7:]
		allMails.append(mail)
	for URL in allURLsNew:
		if URL not in allURLs:
			allURLs.append(URL)
			if URL[:len(rootURL)] == rootURL and RecursionDepth < 3:
				findAllMails(URL)

findAllMails(allURLs[0])
print(len(set(allMails)))
print(set(allMails))