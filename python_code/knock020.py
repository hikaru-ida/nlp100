import json

def get_text(country):
    f = open('../data/jawiki-country.json', 'r')
    json_data = []
    for line in f:
        json_data.append(json.loads(line))

    f.close()
    for data in json_data:
        if data['title'] == country:
            return data['text']

if __name__ == '__main__':
    print (get_text("イギリス"))
