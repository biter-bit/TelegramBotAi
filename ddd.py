import json

a = {'system': [{'system': 'user', 'content': 'text'}], '1': [{"role": "user", "content": 'text'}], '2': [{"role": "user", "content": 'text'}]}

out_file = open("my_file.json", "w")
print(c)
json.dump(a, out_file, indent=6)

out_file.close()