# Secret santa project

## Files
Both files are independent from each other. 
### announcement_email.py
Code to simply send an annoucement and ask recipients if they want to participate. 
### pairing_email.py
Code to generate Secret Santa pairs and inform recipients about their assigned person.

It also contains a constraint bit in case some people should not be paired with each other. 

## Which email adress can work? 
This project is specifically designed for **Gmail adresses where 2-step verification is enabled**. 

Organization gmails may not work... 

## Which credentials should be given to the Python code? 
- the gmail address that will send the messages
- not the gmail address usual password, but an app password that is found following these **steps:**
  - manage your google account → security → 2-step verification (it should be enabled beforehand) → app passwords → create app name
- after following these steps, an app password should be available, it is the one that should be used in the code

  



