import json
#чтение файла

with open('news2.json', encoding='utf-8') as f:
    data = json.load(f)
    #data.byte.decode('utf-8')
    print(data)