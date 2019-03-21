import json

class JsonDict():

    def jsonToDict(self):
        city_dict = {}
        f  = open('utils/city_code.json', encoding='utf-8')
        results = json.load(f)
        for result in results:
            #print(type(result))
            city_code = result['city_code']
            city_name = result['city_name']
            if city_code != '':
                city_dict[city_name] = city_code
        return city_dict
