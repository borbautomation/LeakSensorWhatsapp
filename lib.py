#!/usr/bin/python3

"""
  ____   ____  _____  ____   ____  _      _                                _    _ _______ ____  __  __       _______ _____ ____  _   _ 
 |  _ \ / __ \|  __ \|  _ \ / __ \| |    | |        /\                /\  | |  | |__   __/ __ \|  \/  |   /\|__   __|_   _/ __ \| \ | |
 | |_) | |  | | |__) | |_) | |  | | |    | |       /  \              /  \ | |  | |  | | | |  | | \  / |  /  \  | |    | || |  | |  \| |
 |  _ <| |  | |  _  /|  _ <| |  | | |    | |      / /\ \            / /\ \| |  | |  | | | |  | | |\/| | / /\ \ | |    | || |  | | . ` |
 | |_) | |__| | | \ \| |_) | |__| | |____| |____ / ____ \          / ____ \ |__| |  | | | |__| | |  | |/ ____ \| |   _| || |__| | |\  |
 |____/ \____/|_|  \_\____/ \____/|______|______/_/    \_\        /_/    \_\____/   |_|  \____/|_|  |_/_/    \_\_|  |_____\____/|_| \_|
                                                                                                                                       
 +------------------------------------------------------------------------------------------------------------------------------------+
 |                                                                                                                                    |
 |  Module Name    : LibLEAK                                                                                                          |
 |  Module Purpose : Detect RLE leak sensor alarm , and send whatsapp message to user                                                 |
 |  Inputs  : Alarm relay                                                                                                             |
 |  Outputs : Whatsapp message to defined numbers                                                                                     |
 |  Author : Borbolla Automation Inc                                                                                                  |
 |  Email : ingenieria@borbolla-automation.com                                                                                        |
 |  webpage : www.borbolla-automation.com                                                                                             |
 +------------------------------------------------------------------------------------------------------------------------------------+
"""

import csv
import os
from twilio.rest import Client
import time
#import RPi.GPIO as GPIO

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
            GPIO.cleanup([self.pin])
    

class WhatsApp():
    def __init__(self,):
        print(os.getcwd()+'credentials.txt')
        cred = csv.reader(open(os.getcwd()+'/credentials.txt',newline=''),delimiter=' ',quotechar='|')
        for value in cred:
            self.SID,self.AUTH = value[0].split(',')[0],value[0].split(',')[1],    
        

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