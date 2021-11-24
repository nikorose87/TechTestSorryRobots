"""
This class is set up to process the data that comes from the Appsync
"""
import os

class resfun():
    def __init__(self, event, list_):
        self.event = event
        self.fieldName = event['info']['fieldName'] 
        self.list_ = list_
        self.results = []
        self.apis = {"contacts": self.contacts,
                     "addcontact": self.addcontact,
                     "delcontact": self.delcontact} #the 1st key are the function strings and the values are the values
        
    def contacts(self):
        # this is where all code goes with contacts
        self.results = self.list_
        
    def addcontact(self):
        # this is where all code goes with contacts.
        self.list_.append(self.event['arguments'])
        self.results = self.event["arguments"]
        
    def delcontact(self):
        # this is where all code goes with contacts
        self.results = self.event["arguments"] #Me van a dar un ID
        self.list_.pop()
        # To do
        
        
    def result(self):
        
        apifunc = self.apis[self.fieldName]
        
        return self.results
