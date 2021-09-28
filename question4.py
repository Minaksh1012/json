# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?

# Example:

# Input :-
import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
# for i in sorted(a):
b=open("4.json","w")
# for i in sorted(a):
json.dump(a,b,sort_keys=True,indent=4)
b.close()





# Output:- JSON data:

# {
    # "1": 3,
    # "2": 4,
    # "4": 5,
    # "6": 7
# }
