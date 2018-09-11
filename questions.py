from collections import Counter
import operator
import webbrowser


database = [{"name":"Баренцево","age":30},{"name":"УстьКусть","age":30},{"name":"УстьКусть","age":40},{"name":"УстьКусть","age":30}]
side = ''


def DefiningQuestionAt(qType):
	'''
	Unlike BSQ (Big-Slice Question) these questions are designed to put on a narrow filter, so one can find the desired sea, even there are so much in common 
	'''
	PopularElement = maximiseSliceBy(qType)

	if qType == 'waterBorders': print("Загаданное море граничит с {PopularElement}?\n")
	if qType == 'govBorders': print("Оно граничит с государством {PopularElement}?\n")
	if qType == 'depth': print("Noooooooo")	#only bigslicequestion
	if qType == 'size': print("Noooooooo") #only bigslicequestion
	if qType == 'color': print('Вода в этом море {PopularElement}?\n')
	if qType == 'fauna': print('Там водится {PopularElement}?\n')
	if qType == 'temperature': print("Noooooooo") #onlybsq
	if qType == 'saltiness': print('Вода в этом море {PopularElement}?\n')
	if qType == 'position':
		if PopularElement == 'юг': side = 'южной'
		if PopularElement == 'север': side = 'северной'
		if PopularElement == 'запад': side = 'западной'
		if PopularElement == 'восток': side = 'восточной'
		print("Можно ли сказать, что море находится в {side} части света?\n")
	if qType == 'attraction': print(' Можно ли сказать, что это море туристически-популярное?\n')
	if qType == 'warFactor': print('Есть ли известные полигоны военных испытаний в этом море?\n')
	if qType == 'extraction': print('Добывают ли {PopularElement} в этом море?\n')
	if qType == 'routes': print('{PopularElement}, случаем, не проходит через это море?\n')
	if qType == 'facts': print('Мне кажется, что {PopularElement} происходило именно в этом море\n')
	if qType == 'discoverer': print('{PopularElement} как-либо связан с историей этого моря?\n')
	if qType == 'ports': print('Порт {PopularElement} находится в этом море?\n')
	if qType == 'islands': print('Есть ли {PopularElement} в водах этого моря?\n') #+bsq
	if qType == 'litos': print('Ваше море находится на плите {PopularElement}?\n')
	if qType == 'volcanos': print('Вулкан {PopularElement} находится поблизости этого моря?')
	if qType == 'gulfs': print('Залив {PopularElement} впадает в это море?\n')
	if qType == 'rivers': print('Река {PopularElement} впадает в это море?\n')
	if qType == 'ocean': print('Это море впадает в {PopularElement} океан?\n')
	else: return False

	AskAnswer(qType,PopularElement)
	
def maximiseSliceBy(qType):
	'''
	Defines the maximum amount of similar characters by type, so we can slice the maximum, while
	composing questions
	Must have operator and collections libraries imported
	'''
	SumStack = []
	for i in range(0,len(database)):
		SumStack.append(database[i].get(qType))

	ElementCounter = dict(Counter(SumStack))
	MostPopular = max(ElementCounter.items(), key=operator.itemgetter(1))[0]
	return MostPopular

def BigSliceQuestionAt(qType):
	'''
	Big-Slice Question (BSQ) are designed to be asked first, as they typically will cut the searcharea in the strongest way
	RELEVANT()?
	'''
	if qType == 'depth': print("Средняя глубина моря больше 200м?\n")
	if qType == 'size': print("Считается ли это море большим?\n")
	if qType == 'temperature': print("Средняя температура воды этого моря летом ниже 20 градусов Цельсия?\n")
	if qType == 'govBorders': print("Море имеет границу с больше, чем 9 государствами?\n")
	if qType == 'islands': print('В этом море больше 10 островов?\n')


def AskAnswer(qType,subject):
	'''
	Ask user to enter the answer, checking wether it is correct
	'''
	i = 0
	while i < 1: 
		Data = str(input()).lower()
		if Data == "да" or Data == "yes": FulfillData(qType,subject); i+=1; return True
		if Data == "нет" or Data == "no": TrimDatabase(1,qType, subject); i+=1
		if Data == "не знаю" or Data == "незнаю" or Data == "don't know" or Data == "dont know":
			webbrowser.open('http://wikipedia.org')
		else:
			print("Пожалуйста, введите ответ в форме \"Да\",\"Нет\" или \"Не знаю\"")
			
def FulfillData():
	return True
def TrimDatabase():
	return True

DefiningQuestionAt('ocean')