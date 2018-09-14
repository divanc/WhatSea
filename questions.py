from collections import Counter
import operator
import database as db
import WhatSea #Check wether it updates info over time 
import random
database = db.initStandartSetDb()
dunno = 0

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
	if qType == 'depth':
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
	PopularElement = maximiseSliceBy(qType)

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
	
	######## Common Defining Questions
	elif qType == 'waterBorders': 	print('Загаданное море граничит с морем '+PopularElement+'?\n')		
	elif qType == 'color': 			print('Вода в этом море '+PopularElement+'?\n'); 
	elif qType == 'fauna': 			print('Там водится '+PopularElement+'?\n')
	elif qType == 'attraction': 	print(' Можно ли сказать, что это море туристически-популярное?\n')
	elif qType == 'warFactor':		print('Есть ли известные полигоны военных испытаний в этом море?\n')
	elif qType == 'extraction': 	print('Добывают ли нефть в этом море?\n')
	elif qType == 'routes': 		print('Есть ли в этом море крупные торговые пути?\n')
	elif qType == 'facts': 			print('Были ли известные истории сражения с участием государств '+PopularElement+' в этом море?\n')
	elif qType == 'discoverer': 	nextQuestion(); return True #It is hard info, u kno
	elif qType == 'litos': 			print('Это море находится на '+PopularElement+' литосферное плите?\n')
	elif qType == 'volcanos': 		print('Есть ли известные вулканы поблизости этого моря?')
	elif qType == 'ocean': 			print('Это море впадает в '+PopularElement+' океан?\n')
	elif qType == 'position':
		if PopularElement == 'юг': side = 'южной'
		elif PopularElement == 'север': side = 'северной'
		elif PopularElement == 'запад': side = 'западной'
		elif PopularElement == 'восток': side = 'восточной'
		print("Можно ли сказать, что море находится в "+side+" части света?\n")
	
	######## Math Questions
	elif qType == ('depth' or 'size' or 'temperature' or 'saltiness'):
		ApproximateQuestionAt(qType)

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
	else:
		return False
		

def maximiseSliceBy(qType):
	'''
	Defines the maximum amount of similar characters by type, so we can slice the maximum, while
	composing questions, if there is a list of characters chooses most popular among them
	Must have operator and collections libraries imported
	'''
	SumStack = []
	if type(database[0].get(qType)) == type([]):
		
		for i in range(0,len(database)):
			for j in range(0,len(database[i].get(qType))):
				SumStack.append(database[i].get(qType)[j])

	else:

		for i in range(0,len(database)):
			SumStack.append(database[i].get(qType))

	ElementCounter = dict(Counter(SumStack))
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
			dunno += 1; nextQuestion(qType)
		else:
			print("Пожалуйста, введите ответ в форме \"Да\",\"Нет\" или \"Не знаю\"")
			

def SubtractiveFilter(qType,subject,response):
	'''
	Removes uncorrect seas from database (which may be easily restored) Thus we 
	won't search by needed characters, but unneeded seas (which were excluded in other questions)
	'''
	print("Im here") 				#TEMP

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

		elif tempType is (type('str') or type(True)):
			for sea in database:
				if response is 'no':
					if subject is  sea[qType]:
						unrelevant.append(sea['name'])

				elif response is 'yes':
					if subject is not sea[qType]:
						unrelevant.append(sea['name'])

	for sea in database:
		if sea['name'] in unrelevant:
			database.remove(sea)	

	print("Db len after SFilter: "+str(len(database)))			#TEMP
	print("How many should we subtract: "+ str(len(unrelevant)))#TEMP
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


def nextQuestion(qType):
	SeaNamesTemp = []
	for i in range(0,len(database)):
		SeaNamesTemp.append(database[i]['name'])
	
	print("Before Next Question db includes: ")
	print(SeaNamesTemp)
	print("Before Next Question db counts: "+str(len(database)))
	
	keyList = []
	for key in database[0]:
		keyList.append(key)
	rkey = random.choice(keyList)
	print(rkey)
	DefiningQuestionAt(rkey)

def CompleteQuiz():
	print("u win, boy")
#closeType (func will ensure no question at qType will be asked) 
DefiningQuestionAt('fauna')
