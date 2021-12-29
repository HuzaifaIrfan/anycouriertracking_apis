import grequests

import datetime
import json
urls = [
]

# host='server.skiie.com'
host='localhost:8000'
# host='localhost'



for i in range(0,9):


    url=f'http://{host}/track/madhurcouriers_in_scraper_api?tnum=P50168710{i}'



    urls.append(url)

start=datetime.datetime.now()

print(start)

rs = (grequests.get(u) for u in urls)




responses = grequests.map(rs)



for res in responses:
    # print(res.content)
    try:
        d = json.loads(res.content)
        print(d.keys())
        # print(d)
    except:
        print(res)
        print('json error')
    
end=datetime.datetime.now()
print(end-start)

