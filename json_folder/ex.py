import json

people_string = '''
{
"const profiles" : [
  {
    "name": "Jane Doe",
    "favorite-game": "Stardew Valley",
    "subscriber": false
  }
 ]
}
'''

data = json.loads(people_string)
print(data)


