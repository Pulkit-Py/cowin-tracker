import requests
import datetime
import json
from fake_useragent import UserAgent
from pynotifier import Notification
import  time


while(True):
    temp_user_agent = UserAgent()
    browser_header = {'User-Agent': temp_user_agent.random}
    POST_CODE = "247667"
    age = 19
# Print details flag
    print_flag = 'Y'
    time.sleep(1)
    INP_DATE = "21-05-2021"
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(POST_CODE, INP_DATE)
    response = requests.get(URL, headers=browser_header)
    if response.ok:
        resp_json = response.json()
        # print(json.dumps(resp_json, indent = 1))
        flag = False
        if resp_json["centers"]:
            print("Available on: {}".format(INP_DATE))
            if(print_flag=='y' or print_flag=='Y'):
                for center in resp_json["centers"]:
                    for session in center["sessions"]:
                        if session["min_age_limit"] <= age:
                            print("\t", center["name"])
                            print("\t", center["block_name"])
                            print("\t Price: ", center["fee_type"])
                            print("\t Available Capacity: ", session["available_capacity"])
                            if session["available_capacity"] > 0:
                                Notification(title='Notification Title',description='Slot avalible',urgency='normal').send()
                            else:
                                pass
                            if(session["vaccine"] != ''):
                                print("\t Vaccine: ", session["vaccine"])
                            print("\n\n")
                            
        else:
            print("No available slots on {}".format(INP_DATE))
















#

	
