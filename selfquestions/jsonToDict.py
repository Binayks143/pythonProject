json_data = '{"name":"binay","age":30,"city":"Bangalore"}'

content = json_data.strip('{}').strip()
print(content)
pairs = content.split(',')
print(pairs)

data = {}

for pair in pairs:
    print(pair)
    k, v = pair.split(':', 1)
    key = k.strip().strip('"')
    value = v.strip().strip('"')

    data[key] = value

print(data)

print("age=", data['age'])
