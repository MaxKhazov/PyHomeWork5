# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".\
#text = 'Вот это абв такое абв что я абветурентировался в абвох'
text = str(input())

data = list(map(str, text.split()))

newtext = list(filter(lambda data: 'абв' not in data, data))

print(data)
print(newtext)