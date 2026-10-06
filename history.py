import json

def save(data):
	with open("CalcX_history.json","w") as file:
		json.dump(data, file , indent=4)
	
def load():
	try:
		with open("CalcX_history.json","r") as file:
			return json.load(file)
	except FileNotFoundError:
		return {}