''' JavaScript Object Notation '''
import json

with open('c:\\Users\\Sanjay\\Documents\\python\\python-learning\\json_folder\\states.json') as f:
  data = json.load(f)

for state in data['states']:
#   print(state)
  print(state['name'], state['abbreviation'])
#   del state['area_codes']

# with open('c:\\Users\\Sanjay\\Documents\\python\\python-learning\\json_folder\\new_states.json', 'w') as f:
#   json.dump(data, f, indent=2)