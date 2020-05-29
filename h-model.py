import requests
import json

URL_API = "https://alpha-vantage.p.rapidapi.com/query"
HEADERS = {
	'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
	'x-rapidapi-key': "5a92d6730emsh553b07f7c37825cp1ac400jsn86bb3d1d6f0f"
}

# REMEMBER - FREE API == 500 CALLS / DAY 
def GetStock(symb):
	q = {
		"symbol":symb,
		"datatype":"json",
		"function":"GLOBAL_QUOTE"
	}

	r = requests.get(URL_API, headers=HEADERS, params=q)
	'''
	Structure:
	{
	"Global Quote":{
		"01. symbol":"TSLA"
		"02. open":"777.8700"
		"03. high":"789.7500"
		"04. low":"770.7700"
		"05. price":"771.8426"
		"06. volume":"6995867"
		"07. latest trading day":"2020-02-12"
		"08. previous close":"774.3800"
		"09. change":"-2.5374"
		"10. change percent":"-0.3277%"
		}
	}
	'''
	if r:
		r = json.loads(r.text)

		#Rename key for easy access
		p = dict()
		for i in r["Global Quote"]:
			p[i[4:]] = r["Global Quote"][i]

		return p
	return None

def main():
	#Testing unit
	print(GetStock("MSFT"))

if __name__ == '__main__':
	main()
