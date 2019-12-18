#!/usr/bin/python3

#!/usr/bin/python3

import os
from twilio.rest import Client

SID = 'AC7b9834684161ec5cc333fcb4ca7037fb'
AUTH = 'cf063fe28994876cd960f55c916be110'
client = Client(SID,AUTH)
from_whatsapp = 'whatsapp:+14155238886'

client.messages.create(body = "body!!" , from_ = from_whatsapp,to='whatsapp:+5218110087616')
client.messages.create(body = "*Prueba de mensaje de whatsapp desde programa* no contestar a este numero" , from_ = from_whatsapp,to='whatsapp:+5218115432706')