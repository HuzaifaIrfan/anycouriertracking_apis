from typing import Optional

from fastapi import FastAPI, HTTPException

import uvicorn as uvicorn
from uvicorn.workers import UvicornWorker



from selenium_scraper import track as return_details
 

class MyUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {
        "log_config": "logging.yaml",
    }


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/track/intelcom_ca_scraper_api")
def track_query(tnum: Optional[str] = None):
    # logger.info("logging from the root logger")

    try:
        tracking_number=tnum
        print(tracking_number)
        # INTLCMC413042332
        if len(str(tracking_number)) == 16 or len(str(tracking_number)) == 20 :
            print('Valid tnum')
        else:
            raise HTTPException(status_code=404, detail="Please Enter valid Tracking Number")
            # return {'msg':'Please Enter valid Tracking Number'}

    except:
        raise HTTPException(status_code=404, detail="Please Enter valid Tracking Number")
        # return {'msg':'Please Enter valid Tracking Number'}

    try:
        response=return_details(tracking_number)
    except:
        
        raise HTTPException(status_code=404, detail="Not Found")
        # response={'msg':'Internal Server Error'}


    return  response



if __name__ == '__main__':
      uvicorn.run(app, port=5000)

# import json
# from flask import Flask, render_template, request, jsonify, redirect

# app = Flask(__name__)





# # @app.route('/docs',methods = ['GET'])
# # def index():
# #     return render_template('index.html')



# @app.route('/track/madhurcouriers_in_scraper_api',methods = ['GET'])
# def madhurcouriers_in_track():

#     # tnum=int(tnum_str)

#     try:

#         tnum = request.args.get('tnum')
#         print(f'madhurcouriers_in tnum: {tnum}')

#     except:
        
#         return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422


#     if not tnum:
#         return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422



#     if not (len(str(tnum)) == 10):
#         return jsonify({'tnum':tnum, 'message':'Invalid Tracking Number'}), 422



    

#     try:
#         tracking_details=return_details(tnum)
#     except:
#         return jsonify({'tnum':tnum, 'message':'Tracking Details Not Found'}), 404

#     return jsonify(tracking_details), 200

# if __name__ == '__main__':
# 	app.run(debug=True)