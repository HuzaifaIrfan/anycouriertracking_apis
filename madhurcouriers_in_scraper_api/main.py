from typing import Optional

from fastapi import FastAPI, HTTPException

from madhurcouriers_in_chrome_selenium import track

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/track/madhurcouriers_in_scraper_api")
def track_query(tnum: Optional[str] = None):

    try:
        tracking_number=tnum
        print(tracking_number)
        if len(str(tracking_number)) == 10:
            print('Valid tnum')
        else:
            raise HTTPException(status_code=404, detail="Please Enter valid Tracking Number")
            # return {'msg':'Please Enter valid Tracking Number'}

    except:
        raise HTTPException(status_code=404, detail="Please Enter valid Tracking Number")
        # return {'msg':'Please Enter valid Tracking Number'}


    try:
        response=track(tracking_number)
    except:
        
        raise HTTPException(status_code=404, detail="Not Found")
        # response={'msg':'Internal Server Error'}


    return  response