#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 04:16:47 2021

@author: bibhuti
"""

import requests

class DownloadPDF(object):
    
    def __init__(self, referenceID):
        self.__rid = referenceID
        self.__url = "https://cdn-api.co-vin.in/api/v2/registration/certificate/public/download?beneficiary_reference_id={}"
        
    
    def getCertificate(self):
        
        url = self.__url.formt(self.__rid)
        response = requests.get(url)
        pdf_content = None
        
        if response.ok:
            pdf_content = response.content()
            
            with open('metadata.pdf', 'wb') as f:
                f.write(pdf_content)
        
        return(pdf_content)        

        
        
    