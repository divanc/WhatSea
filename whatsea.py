#!/usr/bin/python -tt
import database as db
import questions


print('Был запущен алгоритм фасетного поиска среди определенных '+str(db.length)+' морей: '+db.seaNames+'\n Вам будет задана серия вопросов, пожалуйста, дайте ответ в форме "Да","Нет" или "Не знаю"\n')


questions.DefiningQuestionAt('ocean')