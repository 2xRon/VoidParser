import re, requests, os, sys



class VoidGame(object):
	playersDict = {}
	gameID = 0
	date = ""
	length = 0
	winner = ""
	def __init__(self, gameID =0, names=[], score=[], kda=[], creep=[], team=[], date=0, length=0 ,winner =""):
		for id in range(len(names)):
			temp = {"playername": names[id],"zscore": score[id], "killscore": kda[id], "creepscore": creep[id], "teamname": team[id]}
			self.playersDict.update({names[id]: temp})
		self.gameID = gameID
		self.date = date
		self.length = length
		self.winner = winner
		
	def getter(self, playername, property="playername"):
		return self.playersDict[playername][property]

def parseFile(filename):
	f = open(filename,'r')
	game_id_list =[]
	for line in f:
		x = re.findall("(?<=gameid\=)\d{6}",line)
		if x:
			game_id_list.append(int(x[0]))
	return game_id_list
		

def getPage(gameID):
	requestURL = "http://www.dota-void.com/game.php?gameid="+str(gameID)
	return requests.get(requestURL).text
	
def numberStringParse(numberString):
	temp = [re.findall('\d+', x) for x in numberString]
	return [[int(ix) for ix in x] for x in temp]
	
def parsePage(gamePage, gameID):
	names = re.findall('(?<=playername=)\w+',gamePage)
	score = list(map(float,re.findall('[\+|\-]\d{1}\.\d{3}', gamePage)))
	numberString = re.findall('\d+\|\d+\|\d+',gamePage)
	kdaString = numberString[0::2]
	creepString = numberString[1::2]
	kda = numberStringParse(kdaString) 
	creep = numberStringParse(creepString)
	team = [0,0,0,0,0,1,1,1,1,1] # Sentinel = 0, Scourge = 1
	#winner = re.findall('Winner\: \<span class\=\"text_scourge\"\>Scourge',gamePage)
	winner = re.findall('(Scourge|Sentinal)(?=\<\/span\>)',gamePage)[0][-1] == 'e'
	date = re.findall('(?<=Date\: )\w+ \d{1,2}, \d{4}',gamePage)
	glength = re.findall('(?<=Length\: )\d+:\d+',gamePage)
	return VoidGame(gameID, names,score,kda,creep,team,date,glength,winner)
	
def main():
	gameIDList = parseFile(sys.argv[1])
	#for gameID in gameIDList:
	#	page = getPage(gameID)
	#	parsedGame = parsePage(page)
	firstGID = gameIDList[0]
	firstpage = getPage(firstGID)
	parsedGame = parsePage(firstpage, firstGID)
	print(parsedGame.getter("iGoOcH","zscore"))

if __name__ == '__main__':
	main()