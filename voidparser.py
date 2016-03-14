import re, requests, os, sys, statistics

class VoidGame(object):
	playersDict = {}
	gameID = 0
	date = ""
	length = 0
	winner = ""
	def __init__(self, gameID =0, names=[], score=[], kda=[], creep=[], team=[], date=0, length=0 ,winner ="", players=[]):
		# dict of dict of game-specific info
		for id in range(len(names)):
			temp = {"playername": names[id],"zscore": score[id], "killscore": kda[id], "creepscore": creep[id], "teamname": team[id] }
			self.playersDict.update({names[id]: temp})
		self.gameID = gameID
		self.date   = date
		self.length = length
		self.winner = winner
		# dict of player personal statistics
		playerstats = {x.playername:x for x in players}
		
	def getter(self, playername, property="playername"):
		return self.playersDict[playername][property]
		
	@property
	def players(self):
		return list(self.playersDict.keys())
		
	def teamscore(self, playername=False):
		sentinelTS = sum(x.zscore for x in playerstats.keys() if playersdict[x.playername]["teamname"] == 0)/5
		scourgeTS = sum(x.zscore for x in playerstats.keys() if playersdict[x.playername]["teamname"] == 1)/5
		if playername:
			if playersDict[playername][teamname]:
				return (sentinelTS, scourgeTS)
			else:
				return (scourgeTS, sentinelTS)
		else:
			return (sentinelTS, scourgeTS)
			
class VoidPlayer(object):
	playername = ""
	zscore = 0
	ngames = 0
	winpercent = 0.0
	killscore = []
	creepscore =[]
	staypercent = 0.0
	realm = 'x'
	def __init__(self, playername, zscore, ngames, winpercent, killscore, creepscore, staypercent, realm):
		self.playername  = playername
		self.zscore      = zscore
		self.ngames      = ngames
		self.winpercent  = winpercent
		self.killscore   = killscore
		self.creepscore  = creepscore
		self.staypercent = staypercent
		self.realm       = realm

def parseFile(filename):
	f = open(filename,'r')
	game_id_list =[]
	for line in f:
		x = re.findall("(?<=gameid\=)\d{6}",line)
		if x:
			game_id_list.append(int(x[0]))
	return game_id_list
		

def getGamePage(gameID):
	requestURL = "http://www.dota-void.com/game.php?gameid="+str(gameID)
	return requests.get(requestURL).text
	
def getPlayerPage(playerName, realm='e'):
	requestURL = "http://www.dota-void.com/player.php?playername=" +playerName + "&realm=" + realm
	return requests.get(requestURL).text
	
def numberStringParse(numberString): 
	# split kda/creep number triplets from string into list of ints
	temp = [re.findall('\d+', x) for x in numberString]
	return [[int(ix) for ix in x] for x in temp]
	
def playerNumberStringParse(numberString):
	temp = [re.findall('\d+.\d', x) for x in numberString]
	return [[float(ix) for ix in x] for x in temp]

def getGamePlayers(gamePage):
	players = list()
	for playerAndRealm in re.findall('playername=([a-zA-Z\.\_\(\)\-]+)\&amp\;realm\=(\w)',gamePage):
		playerPage = getPlayerPage(playerAndRealm[0], playerAndRealm[1])
		players.append(parsePlayerPage(playerPage,playerAndRealm[1]))
	return players
	
def parseGamePage(gamePage, gameID):

	# game info
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
	
	# get void player pages (find realms first)
	players = getGamePlayers(gamePage) #list of VoidPlayer
	
	return VoidGame(gameID, names,score,kda,creep,team,date,glength,winner, players)
	

def parsePlayerPage(playerPage, realm):
	playername = playername = re.findall('Init\(\'([a-zA-Z\.\_\(\)\-]+)\',\'',playerPage)[0]
	zscore = list(map(float,re.findall('[\+|\-]\d{1}\.\d{3}', playerPage)))[0]
	ngames = int(re.findall('Total Games: (\d+)',playerPage)[0])

	numberString = re.findall('\d+.\d/\d+.\d/\d+.\d',playerPage)
	kdaString = numberString[0]
	creepString = numberString[1]
	killscore = playerNumberStringParse(kdaString) 
	creepscore = playerNumberStringParse(creepString)

	winpercent = int(re.findall('(\d+)\%',playerPage)[1])
	staypercent = int(re.findall('(\d+)\%',playerPage)[2])
	#status = re.findall('blah',playerPage)
	return VoidPlayer(playername, zscore, ngames, winpercent, killscore, creepscore, staypercent, realm)
	
	
def main():
	gameIDList = parseFile(sys.argv[1])
	gameList = []
	for gameID in gameIDList:
		page = getGamePage(gameID)
		gameList.append(parseGamePage(page, gameID))
	scores = list()
	for game in gameList:
		score.append(game.teamscore(playername='ReadyToBrew'))

	goodScore = statistics.mean(x[0] for x in score)
	badScore = statistics.mean(x[1] for x in score)
	print(goodScore,badScore)
	
			
		
	#firstGID = gameIDList[0]
	#firstpage = getGamePage(firstGID)
	#parsedGame = parseGamePage(firstpage, firstGID)
	#print(parsedGame.getter("iGoOcH","zscore"))
	#print(parsedGame.players)

if __name__ == '__main__':
	main()