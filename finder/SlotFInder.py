import requests
import datetime

class SlotFinder(object):
    def __init__(self, postcode, age = None, date = datetime.datetime.today(), maxdays = 20):
        self.__code = postcode
        self.__age = age
        self.__date = date
        date_list = [self.__date + datetime.timedelta(days=x) for x in range(maxdays)]
        self.date_str = [x.strftime("%d-%m-%Y") for x in date_list]
        self.__url =  "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}"

    def slotchecker(self):
        slot_avail = {}
        for date in self.date_str:
            req_str = self.__url.format(self.__code, date)
            response = requests.get(req_str)
            
            hospital_list = []
            
            if response.ok:
                resp_json = response.json()
                
                if(self.__age  == None):
                    slot_avail[date] = resp_json
                    continue
                
                #print(resp_json)
                for center in resp_json["centers"]:
                    for session in center["sessions"]:
                        if session["min_age_limit"] <= self.__age:
                            vaccine =  session["vaccine"] if session["vaccine"] != '' else "COVISHIELD"
                            hospital_list.append({"Centre Name" : center["name"],
                                                     "Block Name" : center["block_name"],
                                                     "Price" : center["fee_type"],
                                                     "Capacity" : session["available_capacity"],
                                                     "slot" : session["slots"],
                                                     "Vaccine" : vaccine
                                                     })
                
                if(len(hospital_list) > 0):
                   slot_avail[str(date)] = [i for n, i in enumerate(hospital_list) if i not in hospital_list[n + 1:]]
                            
            else:
                print("No available slot on Date : "+str(date))
                
        return(slot_avail)


#slot = SlotFinder(751015, 32)
#resp = slot.slotchecker()




