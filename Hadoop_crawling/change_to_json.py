import json
a = []
with open('BTS.txt', 'r',encoding="utf-8") as file:
    for line in file:
        # a=json.loads(line)
        # print(a['text'])
        a.append(json.loads(line)['text'])
output_file_name = "BTS_1.txt"
print(a)

with open(output_file_name, 'w',encoding="utf-8") as out_file:
    for line in a:
        print(line, file=out_file, flush=True)