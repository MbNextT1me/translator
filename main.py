import requests
import argparse
import json
import sys
import re

# Парсим командную строку
parser = argparse.ArgumentParser(description="Translator's manual!")
parser.add_argument("--file", default=1, type=str, help="Файл, который вы хотите перевести")
parser.add_argument("--lan", default=1, type=str, help="Выберите язык для перевода")
parser.add_argument("--out", default="output.txt", type=str, help="Выберите файл для вывода")

# Задаём аргументы
args = parser.parse_args()
text = args.file
toLan = args.lan
output = args.out
print(args.file, args.file)
# Проверка на ввод
if text == 1 or toLan == 1:
    print("Ошибка! Неверно заданы аргументы!")
    sys.exit()

# Считываем файл
with open(text, 'r', encoding="utf-8") as file:
    data = file.read()

# Делаем запрос
headers = {
    'Ocp-Apim-Subscription-Key': '9bf007a897f54e4a94203f8aa88cd2b1',
    'Ocp-Apim-Subscription-Region': 'westeurope',
    'Content-type': 'application/json'
}

url = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=' + toLan
body = [{
    'Text': data
}]

# Проверяем, выполнен ли запрос
try:
    response = requests.post(url, headers=headers, json=body)
except Exception:
    print("Ошибка! Запрос не был выполнен!")
    sys.exit()

# Если запрос выполнен
result = response.json()

# Запись в файл
f = open(output, 'w')
f.write(result[0]['translations'][0]['text'])
f.close()

print("\nПеревод успешно записан в файл!")
