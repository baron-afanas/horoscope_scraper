import json

years = [12,13,14,15,16,17,18,19]
total = []
for year in years:

    with open('datos20{}.json'.format(str(year))) as json_file:
        data = json.load(json_file)
        total.extend(data)

for entry in total:
    txt = entry['text']
    index = txt.index("\r\n")
    txt = txt[index+4:]
    txt = txt.lstrip()
    index = txt.index("\r\n")
    txt = txt[:index]
    entry['text'] = txt

    date = entry['date']
    entry['date'] = date[:4]+'-'+date[4:6]+'-'+date[6:8]

with open('clean_data.json', 'w') as outfile:
        json.dump(total, outfile)