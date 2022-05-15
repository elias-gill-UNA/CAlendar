import requests
import json
apiKey = '43bd49af-15b8-4d69-95ed-e2c1d327b876' 

country = 'PY'
respuesta = requests.get(f'https://holidayapi.com/v1/holidays?pretty&key=43bd49af-15b8-4d69-95ed-e2c1d327b876&country=PY&year=2021')._content
print(json.loads(respuesta)) #ignorar error (si, ironico)
