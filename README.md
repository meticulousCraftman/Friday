# Friday
An assistant that does things elegantly.


> The assistant is being redesigned from ground up.
>
> The program is not working right now.


<hr/>

## Overview
You send voice commands using Google Assistant, the commands are then relayed to the python scripts using IFTTT. An IFTTT applet is used to
send Google Assistant voice command over telegram. 
The scripts keep looking for incoming commands and finally run whatever
command that was recieved.

## Installation 
### Create a Virutal Env
```console
foo@bar:~$ virutalenv -p python3 venv
foo@bar:~$ source venv/bin/activate
```

### Install requirements
```console
foo@bar:~$ pip install -r requirements.txt
```


### IFTTT Setup (with telegram)
Open [this](https://ifttt.com/applets/71095871d-if-you-say-pirate-popular-then-send-message-to-private-chat-with-ifttt) applet with a Google Account. Authorize google assistant and telegram. Go ahead to edit the IFTTT applet and remove the text "to Telegram" to ""Friday".

### Telegram API Keys
Open [this](my.telegram.org) link and login with your telegram account.
Put the image here
Click the link where it says "Create a new application". Fill the form and submit it to get the API ID and API HASH for your telegram app. Copy the API ID and API HASH from the telegram's website to `commander.py` file .

## Usage
`python3 daemon.py`
First time when running the application the, it would ask for your telegram phone number and telegram code. Enter those and continue.

## Project structure
The project is designed to be plug and play with any service. All the modules that are designed to be a service are placed in the `services` folder.  
You are welcome to add any service as long as it follows the API.

Here is a quick run-down of the function of each script. 

##### Docstrings are yet to written for some file.
+ **daemon** - runs commander and passes the command to service handler
+ **commander** - gets the command from wherever, whether it is flask server or telegram message or even command line. API : `get_command`

