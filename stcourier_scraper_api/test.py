import grequests

import datetime
import json
urls = [
]



url='http://0.0.0.0:5000/track/stcourier_scraper_api?q=63346811006'



for i in range(0,5):

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
    except:
        print(res.content)
        print('json error')
    
end=datetime.datetime.now()
print(end-start)

