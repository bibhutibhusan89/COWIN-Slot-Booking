
import urllib3
import requests
import json
import hashlib
import uuid
import jsonpickle


class ManageAuth(object):
    def __init__(self,):
        self.__url = "http://cdn-api.co-vin.in/api"
        self.__http = urllib3.PoolManager()
        self.__uuid = uuid.uuid1()

    def authRequest(self, mobile):
        body = {"mobile" : str(mobile)}
        resp = None
        try:
            resp = self.__http.request("POST", self.__url + "/v2/auth/public/generateOTP",
                                    headers={'Content-Type': 'application/json'},
                                    body = json.dumps(body))
            self.__txnID = json.loads(resp.data)["txnId"]
           
        except Exception as error:
            print(error)
            
        return(resp)

    def authValidate(self, OTPValue):
        otp_encode =  hashlib.sha256(str(OTPValue).encode())
        #print(self.__txnID)
        body = {"otp" : otp_encode , "txnId" : self.__txnID}
        resp_json = None
        try:
            resp_json = self.__http.request("POST", self.__url + "/v2/auth/public/confirmOTP",
                                        headers={'Content-Type': 'application/json'},
                                        body=jsonpickle.encode(body))
            
            print("Response Received")
        except Exception as error:
            print(error)

        return(resp_json)

#m1 = ManageAuth()
#resp = m1.authRequest("7892902575")
#resp = m1.authValidate("576486")
#print(resp)








