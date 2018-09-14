from collections import Counter
import operator
import database as db
import random
database = db.initStandartSetDb()
exPopular = []
exTypes = []

def initialQuestionAt(qType):
	'''
	Easier the question - easier the awnser. You don't want to ask 10 questions about islands in this sea,
	 if this sea doesn't have any islands at all
	So these questions are to be asked at first
	'''
	if qType == 'islands': print('В этом море есть острова?\n')
	elif qType == 'rivers': print('Какие-либо реки впадают в это море?\n')
	elif qType == 'gulfs': print('Какие-либо заливы впадают в это море?\n')
	elif qType == 'govBorders': print('Это море имеет какие-либо сухопутные границы?\n')
	elif qType == 'ports': print('У этого моря есть порты?\n')
	AskAnswer(qType,'initial')


def ApproximateQuestionAt(qType):
	'''
	Initialises maths kind of questions which engage some counting within itself 
	'''
	if qType == 'depth': ## Maybe in the future
		nextQuestion(qType)
	elif qType == 'size':
		nextQuestion(qType)
	elif qType == 'temperature':
		nextQuestion(qType)
	elif qType == 'saltiness':
		nextQuestion(qType)


def DefiningQuestionAt(qType):
	'''
	These questions are designed to put on a narrow filter, so one can find
	 the desired sea, even there are so much in common 
	'''

	## It would be strange if we try to find the most popular among bool, no?  
	if type(database[0][qType]) != type(True): PopularElement = maximiseSliceBy(qType)
	else: PopularElement = 'Bool'

	######## Questions, which require initial to be asked first
	if qType == 'govBorders':
		if CheckNewType(qType) == True:
	  		initialQuestionAt(qType)
	  		return True
		else: print('Оно граничит с государством '+PopularElement+'?\n')

	elif qType == 'ports': 
		if CheckNewType(qType) == True:
	  		initialQuestionAt(qType)
	  		return True
		else: print('У этого моря есть порт в городе '+PopularElement+'?\n')

	elif qType == 'islands':
		if CheckNewType(qType) == True:
	  		initialQuestionAt(qType)
	  		return True
		else: print('Есть ли  остров '+PopularElement+' в водах этого моря?\n')

	elif qType == 'gulfs': 
		if CheckNewType(qType) == True:
	  		initialQuestionAt(qType)
	  		return True
		else: print('Залив '+PopularElement+' впадает в это море?\n')
	elif qType == 'rivers': 
		if CheckNewType(qType) == True:
	  		initialQuestionAt(qType)
	  		return True
		else: print('Река '+PopularElement+' впадает в это море?\n')
	
	######## Boolean questions
	elif qType == 'volcanos': 		print('Есть ли известные вулканы поблизости этого моря?')
	elif qType == 'attraction': 	print(' Можно ли сказать, что это море туристически-популярное?\n')
	elif qType == 'warFactor':		print('Есть ли известные полигоны военных испытаний в этом море?\n')
	elif qType == 'extraction': 	print('Добывают ли нефть в этом море?\n')
	elif qType == 'routes': 		print('Есть ли в этом море крупные торговые пути?\n')

	######## Common Defining Questions
	elif qType == 'waterBorders': 	print('Загаданное море граничит с морем '+PopularElement+'?\n')		
	elif qType == 'color': 			print('Вода в этом море '+PopularElement+'?\n'); 
	elif qType == 'fauna': 			print('Там водится '+PopularElement+'?\n')
	elif qType == 'facts': 			print('Были ли известные истории сражения с участием государств '+PopularElement+' в этом море?\n')
	elif qType == 'discoverer': 	nextQuestion(qType); return True #It is hard info, u kno
	elif qType == 'litos': 			print('Это море находится на '+PopularElement+' литосферное плите?\n')
	elif qType == 'ocean': 			print('Это море впадает в '+PopularElement+' океан?\n')
	elif qType == 'position':
		if PopularElement == 'юг': side = 'южной'
		elif PopularElement == 'север': side = 'северной'
		elif PopularElement == 'запад': side = 'западной'
		elif PopularElement == 'восток': side = 'восточной'
		print("Можно ли сказать, что море находится в "+side+" части света?\n")
	
	######## Math Questions
	elif qType == ('depth' or 'size' or 'temperature' or 'saltiness'): ApproximateQuestionAt(qType)

	else: nextQuestion(qType)

	AskAnswer(qType,PopularElement)
	
	
def CheckNewType(qType):
	'''
	It  checks wether the type of question wasn't asked before
	In case it wasn't, initialises initialQuestionAt()
	'''
	if db.newType.get(qType) == True: 
		db.newType[qType] = False
		return True
	else: return False
		

def maximiseSliceBy(qType):
	'''
	Defines the maximum amount of similar characters by type, so we can slice the maximum, while
	composing questions, if there is a list of characters chooses most popular among them
	Must have operator and collections libraries imported
	'''
	SumStack = []
	if type(database[0].get(qType)) == type([]):
		
		for sea in database:
			for character in sea[qType]:
				SumStack.append(character)

	else:
		for sea in database:
			SumStack.append(sea[qType])


	ElementCounter = dict(Counter(SumStack))

	for character in ElementCounter.copy():
		if character in exPopular:
			ElementCounter.pop(character)

	MostPopular = max(ElementCounter.items(), key=operator.itemgetter(1))[0]
	return MostPopular


def AskAnswer(qType,subject):
	'''
	Ask user to enter the answer, checking wether it is correct
	'''
	i = 0
	while i < 1: 
		Data = str(input()).lower()
		if Data == "да" or Data == "yes": SubtractiveFilter(qType, subject,'yes'); i+=1;
		elif Data == "нет" or Data == "no": SubtractiveFilter(qType, subject,'no'); i+=1
		elif Data == "не знаю" or Data == "незнаю" or Data == "don't know" or Data == "dont know":
			nextQuestion(qType)
		else:
			print("Пожалуйста, введите ответ в форме \"Да\",\"Нет\" или \"Не знаю\"")
			

def ChangePopularBy(qType,subject):
	'''
	If we leave a list of seas wich have something in common by certain type
	This element will remain most popular, thus we want to change it 
	'''
	if maximiseSliceBy(qType) == subject:
		exPopular.append(subject)

	if type(database[0][qType]) == type(True):
		exTypes.append(qType)

def SubtractiveFilter(qType,subject,response):
	'''
	Removes uncorrect seas from database (which may be easily restored) Thus we 
	won't search by needed characters, but unneeded seas (which were excluded in other questions)
	'''
	tempType = type(database[0][qType])
	unrelevant = []

	if subject is 'initial':
		for sea in database:
			if response is 'yes':
				if len(sea[qType]) is 0:
					unrelevant.append(sea['name'])

			elif response is 'no':
				if len(sea[qType]) is not 0:
					unrelevant.append(sea['name'])
	
	else: ## If question is not initial
		if tempType is type([]):
			for sea in database:
				if response is 'no':
					if subject in sea[qType]:
						unrelevant.append(sea['name'])

				elif response is 'yes':
					if subject not in sea[qType]:
						unrelevant.append(sea['name'])

		elif tempType is type('str'):
			for sea in database:
				if response is 'no':
					if subject is  sea[qType]:
						unrelevant.append(sea['name'])

				elif response is 'yes':
					if subject is not sea[qType]:
						unrelevant.append(sea['name'])
		
		elif tempType is type(True):
			for sea in database:
				if response is 'no':
					if sea[qType] is True:
						unrelevant.append(sea['name'])

				elif response is 'yes':
					if sea[qType] is False:
						unrelevant.append(sea['name'])

	print("Db len before SFilter: "+str(len(database)))			#TEMP
	print("Unwanted seas are:")
	print(unrelevant)
	i = 0
	for sea in database.copy():
		print('DB Sea: '+str(i)+".) "+str(sea['name']))
		if sea['name'] in unrelevant:
			print("deleting sea: "+str(i)+". "+str(sea['name']))
			database.remove(sea)
		i+=1	

	if len(database) == 0: Restart(); return True ## cuz this happens sometimes, right?

	print("Db len after SFilter: "+str(len(database)))			#TEMP
	print("How many should we subtract: "+ str(len(unrelevant)))#TEMP
	ChangePopularBy(qType,subject)
	CheckAnswer(qType)


def CheckAnswer(qType):
	'''
	Makes sure answer is far away, so module won't ask you billion questions,
	while there is just 1 sea left 
	'''
	FitableAnswers = []
	tempBool = False

	if len(database) > 1:
		nextQuestion(qType)
	else: 
		CompleteQuiz()


def nextQuestion(qType = 'ocean'):
	SeaNamesTemp = []
	for i in range(0,len(database)):
		SeaNamesTemp.append(database[i]['name'])
	
	print("Before Next Question db includes: ")
	print(SeaNamesTemp)
	print("Before Next Question db counts: "+str(len(database)))
	
	keyList = []
	print(exPopular)
	for key in database[0]:
		if key not in exTypes:
			keyList.append(key)

	rkey = random.choice(keyList)
	print(rkey)
	DefiningQuestionAt(rkey)


def Restart():
	'''
	If player manages to get an empty list of options, program is to be restarted 
	'''
	print("Вы меня совсем запутали. Давайте сначала...")
	database = db.initStandartSetDb()
	exPopular = []
	exTypes = []
	nextQuestion('ocean')


def CompleteQuiz():
	'''
	Checks wether answer is correct and finishes module
	'''
	print("Это "+database[0]['name']+"?")
	print("Если да, просто нажмите Enter")
	Response = input()
	if len(Response) != 0: Restart()
	else:
		print("Ну, это было просто!\nСпасибо за игру!")
		exit()


if __name__ == '__main__':
	exit()
