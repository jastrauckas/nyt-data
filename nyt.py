import requests
import json
import pprint

print "\n\n\n\n\n\n\n\n\n\n\n\n\n"

key = ''
with open('key.txt', 'rb') as f:
	key = f.readline().strip()

payload = {'q': 'gun', 'begin_date': '20160226', 'end_date': '20160228', 'api-key': key}
payload = {'q': 'gun', 'api-key': key}
payload['fq'] = 'headline:("gun")'
r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)
print r.url
pp = pprint.PrettyPrinter(indent=4)
json = r.json()
content = json['response']['docs']

for article in content:
	print article['headline']['main']
#pp.pprint(content)
