#!/usr/bin/python3

import csv
import os
from twilio.rest import Client
import time

class Alarm(object):
    """docstring for Alarm"""
    def __init__(self,pin):
        self.pin = pin
        

    def callback(self):
        wp = WhatsApp()
        wp.send_from_csv()   
        
    def setup_rising(self,bouncetime):
        GPIO.setup(pin,GPIO.IN)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=self.callback, bouncetime=bouncetime)

    def wait(self):
        try:
            while True:
                pass # your code

        except KeyboardInterrupt:
            pass
        finally:
            print("\nRelease the used pin(s)")
            GPIO.cleanup([Input_Sig])
    

class WhatsApp():
    def __init__(self,):
        self.SID = 'AC7b9834684161ec5cc333fcb4ca7037fb'
        self.AUTH = 'cf063fe28994876cd960f55c916be110'
        self.client = Client(self.SID,self.AUTH)
        self.from_whatsapp = 'whatsapp:+14155238886'

    def send_from_csv(self):
        self.csvObject = BorCSV()
        self.numbers = self.csvObject.get_whatsapp()

        for number in self.numbers:
            self.client.messages.create(body = "*An alarm in leak detector has been triggered* please check alarm in *Borbolla Automation's* site panel " , from_ = self.from_whatsapp,to='whatsapp:%s'%number)
            time.sleep(1)



class BorCSV():
    """docstring for BorCSV"""

    def __init__(self,):
        self.cwd = os.getcwd()
        print(self.cwd)
        self.file = self.cwd+'/whatsapp.bor'
        print(self.file)
        self.csv = csv

    def get_whatsapp(self):
        self.read = csv.reader(open(self.file,newline=''),delimiter=' ',quotechar='|')
        matrix = []

        for row in self.read:
            for value in row:
                matrix.append(value.split(","))
        print(matrix)
        matrix2 = []
        for subm in matrix:
            for value in subm:
                matrix2.append(value)
        
        return matrix2
        

if __name__ == '__main__':
    

    #read = csv.reader(open('KMEX\whatsapp.bor',newline=''),delimiter=' ',quotechar='|')
    a = WhatsApp()
    a.send_from_csv()