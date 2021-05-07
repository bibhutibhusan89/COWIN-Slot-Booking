


import requests

class StateIDFinder(object):
    def __init__(self):
        self.__url = "http://cdn-api.co-vin.in/api/v2/admin/location"
         
    def listStateIDs(self, locatecode = "hi_IN"):
           
        try:
            resp_json = None
            req_str = self.__url+"/states?Accept-Language={}".format(locatecode)
            response = requests.get(req_str)
            if response.ok:
                resp_json = response.json()
        except Exception as error:
            print(error)
        
        return(resp_json)
    
    
    def listDistrictsByState(self, stateID):
       try:
            resp_json = None
            req_str = self.__url + "/districts/{}".format(stateID)
            response = requests.get(req_str)
           
            if response.ok:
                resp_json = response.json()
       except Exception as error:
            print(error)
       return(resp_json)
   
        
        
    
#sid = StateIDFinder()
#states = sid.listStateIDs("hi_IN")
#dist = sid.listDistrictsByState(16)
        
        
        

