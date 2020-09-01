import json

json_format = {'data': []}
quote_list = []
with open("Quote_1.txt") as in_file, open("Quote_1.json") as in_json_file:
    lines = in_file.readlines()
    for line in lines:
        quote, author = line.split('-')
        quote_list.append({'quote':quote.capitalize().strip(),'author':author.title().strip()})

    try:
        json_quotes = json.load(in_json_file)
    except:
        json_format['data'].extend(quote_list)
    else:      
        json_quotes['data'].extend(quote_list) 
        json_format['data'].extend(json_quotes['data'])

with open("Quote_1.json", "w") as out_file:
    json.dump(json_format,out_file,indent= 4)


    


