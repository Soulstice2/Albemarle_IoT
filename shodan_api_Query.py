import shodan
CSV_FILE = "IP,PORT"

SHODAN_API_KEY = ''

api = shodan.Shodan(SHODAN_API_KEY)

results = api.search('city:Albemarle')

print 'Results found: %s' % results['total']

for result in results['matches']:
    IP = result['ip_str']
    Port = result['port']
    Port = str(Port)
    CSV_FILE = CSV_FILE + "\n" + IP + "," + Port


f = open('Shodan_Data.csv','w')
f.write(CSV_FILE)
f.close()
