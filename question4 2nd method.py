import json

a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
for i in a:
    json.dumps(a)
    b=sorted(a)
    # json.dumps(b)
print(b)
