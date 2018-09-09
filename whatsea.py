#!/usr/bin/python -tt

import json
'''
OOP made with json
#############################################################
Море относится к ... океану?								3
Оно примыкает к ... государству?							4
Большое?/Маленькое											6
Там обитают ...?											8
Морские границы...?											3
Средняя глубина больше 200м?								5
Средняя температура воды поверхности ...?					9
Гласная?													2
Соленость ...? Пресное?										10
Относительно России ..западнее..? 							11	
Цвет														7
Туристическое 												12
Военные испытания???????									13
Нефтедобыча													14
Морские пути 												15
Исторические факты											16
Первооткрыватель 											17
Порты 														18
Есть ли остров .... в море? 								19
Литосферные плиты 											20
Вулканы														21
Заливы														22
Реки														23
##############################################################

In order to filter faster, every filter will decide which question is more appropriate  for a deeper learning
One may add seas with another module
Seas in json?

'''

print('Был запущен алгоритм фасетного поиска среди определенных 20 морей:\n \n Японское,Азовское, Балтийское, Красное, Аравийское, Белое, Баренцево, Лазарево, Росса, Черное, Охотское, Желтое, Мраморное, Чукотское, Дюрвиля, Норвежское, Карское, Эгейское, Карибское, Северное \n Вам будет задана серия вопросов, пожалуйста, дайте ответ в форме "Да","Нет" или "Не знаю"\n')

def ScanForSea():
		'''Compares the given answer to the list of seas, decides wich character is better to be asked next'''
		pass
##1Start>2AskQuestion>3GetAnswer>4WriteAwnserinSecret>5CompareWithDB>if more than 1!!>6FilterAnswers>7FindDefiningQuestion(compareChosenDbSeas)>##### Ask>Get>Write>Compare> if 1> 8final
def startSequence():
	'''1)It executes the sequence of questions, forming the answers in filters, memorising them'''
	usedQuestions = []
	QuestionCounter = 0
	typ = ''
	
	Answer = dict(						#questionID 
	name = [],							#1		Название из цвета? 
	waterBorders = [],					#2		Граничит с морями
	govBorders = [],					#3		Граничит больше, чем с 6?/ С Бразилией?
	depth = [], 						#4		Средняя глубина больше 200?
	size = [], 							#5		Большое?
	color = [], 						#6		Вода Темная?
	fauna = [], 						#7		Водятся ли №карасики№?
	temperature = [], 					#8		Средняя температура
	saltiness = [], 					#9		Соленое или пресное? Соленость
	position = [], 						#10		Находится №восточнее№ РФ?/ 
	attraction = [], 					#11		Туризм
	warFactor = [], 					#12		Военные испытания
	extraction = [], 					#13		Нефть и тд
	routes = [], 						#14		Торговые пути
	facts = [], 						#15		История/битвы
	discoverer = [], 					#16		Основатель
	ports = [], 						#17		Известные порты
	islands = [], 						#18		Есть ли острова?/Есть ли такой остров
	litos = [], 						#19		На литосферной плите?
	volcanos = [], 						#20		Есть ли поблизости вулканы?
	gulfs = [], 						#21		Залив?
	rivers = [], 						#22		Река впадает?
	ocean = []  						#23		Море впадает в ?
	)


	def newQuestion():
		'''
		2)Decides which question is more appropriate to ask in order to reveal the answer faster
		'''
		print("Оно большое?\n");
		qType = 5
		GetAnswer(5,"большое")
		
	def GetAnswer(qType,subject):
		'''
		3)Gets the answer, checking its correction 
		'''
		Data = str(input()).lower
		if Data == ("да" or "yes" or "1" or "+"): FulfillData(qType,subject)
		if Data == ("нет" or "no" or "0" or "-"): TrimDatabase(1,qType, subject)
		if Data == ("не знаю" or "незнаю" or "don't know" or "?" or "dont know"):
		else:
			print("Пожалуйста, введите ответ в форме \"Да\",\"Нет\" или \"Не знаю\"")
			GetAnswer()#redo

	def FulfillData(ty, answer):
		'''
		4)Initialise secret object to search among given information
		ty - type of info we have acquired, ques.ID - ID, answerID - 0 for No, 1 for Yes, 2 for don't know
		'''
		QuestionCounter += 1

		if ty == 2: Answer['waterBorders'].append(answer); typ = 'waterBorders'
		if ty == 3: Answer['govBorders'].append(answer); typ = 'govBorders'
		if ty == 4: Answer['depth'].append(answer); typ = 'depth'
		if ty == 5: Answer['size'].append(answer); typ = 'size'
		if ty == 6: Answer['color'].append(answer); typ = 'color'
		if ty == 7: Answer['fauna'].append(answer); typ = 'fauna'
		if ty == 8: Answer['temperature'].append(answer); typ = 'temperature'
		if ty == 9: Answer['saltiness'].append(answer); typ = 'saltiness'
		if ty ==10: Answer['position'].append(answer); typ = 'position'
		if ty ==11: Answer['attraction'].append(answer); typ = 'waterBorders'
		if ty ==12: Answer['warFactor'].append(answer); typ = 'attraction'
		if ty ==13: Answer['extraction'].append(answer); typ = 'warFactor'
		if ty ==14: Answer['routes'].append(answer); typ = 'routes'
		if ty ==15: Answer['facts'].append(answer); typ = 'facts'
		if ty ==16: Answer['discoverer'].append(answer); typ = 'discoverer'
		if ty ==17: Answer['ports'].append(answer); typ = 'ports'
		if ty ==18: Answer['islands'].append(answer); typ = 'islands'
		if ty ==19: Answer['litos'].append(answer); typ = 'litos'
		if ty ==20: Answer['volcanos'].append(answer); typ = 'volcanos'
		if ty ==21: Answer['gulfs'].append(answer); typ = 'gulfs'
		if ty ==22: Answer['rivers'].append(answer); typ = 'rivers'
		if ty ==23: Answer['ocean'].append(answer); typ = 'ocean'
		else: newQuestion()
		TrimDatabase(0,ty, answer)
		return typ

	def ListCapitalize(listWithStr):
		'''
		In order to compare string elements of two lists, capitalization matters, so you want avoid different capitals in the same strings
		'''
		return CapList = [n.capitalize() in listWithStr]
	
	#LastChange = FulfillData(...)
	def FilterData(LastChange):
		'''
		Compares absorbed data to all seas
		database = import database
		'''
		set(ListCapitalize(database)).intersection(ListCapitalize(Answer))
