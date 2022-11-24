
from operator import ne
import pandas
df = pandas.read_excel("base.xlsx", engine="openpyxl")  # открываем файл base.xlsx 
word = ["анализ", "hadoop", "ml",  "машинное обучение", "big data",  "безопасность","бизнес","руков","управлять","этикет","информ","выступ","распр"] # не образщайте внимания на такие странные слова, это так, чтобы проще было искать
df['Название'] = df['Название'].str.lower()
df['Описание'] = df['Описание'].str.lower() # приводим столбцы к нижнему регистру
dict_of_names = {}
for i in word:
    titles = []
    new_df = str(df['Название'][df['Название'].str.contains(i)]).split('  ')[1::] # парсим табличку в строку чтобы было удобно и не было лишних пробелов
    for j in new_df:
        if j != "":
            index = j.find("\n")
            titles.append(j[0:index])  # добавил все названия курсов к их ключевым словам

    dict_of_names[i] = titles			

d1 = {'анализ':'Анализ данных','ml':'Машинное обучение', 'машинное обучение':'Машинное обучение', 'hadoop':'hadoop', 'big data':'Bigdata', 'бизнес':'для бизнеса','безопасность':'Информационная безопасность','управлять':'Управление сотрудниками','руков':'Руководителям','этикет':'Онлайн этикет','выступ':'Выступления на публике','информ':'Методы работы с информацией','распр':'Методы работы с информацией'}
# а вот тут я привел как раз таки все кривые ключи к нормальному виду
for old_key, new_key in d1.items():
    dict_of_names[new_key] = dict_of_names.pop(old_key)
dict_of_names['base knowledge'] = ['Вводный инструктаж по информационной безопасности', 'Правила информационной безопасности при работе с электронной почтой и сетью-Интернет', 'Превосходный сервис. Требования к внешнему виду', 'Превосходный сервис. Коммуникации с клиентами', 'Оказание первой помощи', 'Начну с понедельника', 'Кросс-культурная коммуникация', 'Креативное мышление', 'Как управлять стрессом', 'Как принимать решения в команде', 'Как делегировать задачи', 'Информационная безопасность', 'Добро пожаловать в РЖД!', 'Онлайн-курс Тотального диктанта', 'Самомотивация', 'Цифровой этикет, или как сделать онлайн-коммуникацию приятной и эффективной']

print(dict_of_names.items())