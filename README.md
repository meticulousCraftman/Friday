# multiflix
A content download system that accepts commands in natural language (e.g. `download some popular movies`)

## Installation 
### Basic functionality
```
git clone https://github.com/devxpy/multiflix.git
pip install -r requirements.txt
pip install git+https://github.com/mwalercz/TPB.git@fix-403-forbidden
```

### Deluge download setup

```
sudo apt install deluge deluged deluge-console
deluged
```
### IFTTT Setup (with telegram)
Add [this](https://ifttt.com/applets/71095871d-if-you-say-pirate-popular-then-send-message-to-private-chat-with-ifttt) applet 
     
Authorize google assistant and telegram

## Usage
`python3 daemon.py`

## Project structure
The project is designed to be plug and play with any service other than the default.   
You are welcome to add any service as long as it follows the api 

Here is a quick run-down of the function of each script. 

##### You will find complete explaination in the docstring at the top of each file
+ daemon - runs commander, content_retriever, content_provider and downloader in that order
+ commander - gets the command from wherever, wheteher it is flask server or telegram message or even command line. API : `get_command`
+ content_retriever - get a content search query from somewhere (calls the TMDB api by default). API : `get_content`
+ content_provider - get content download link from somewhere (uses TPB by default). API : `get_download_url`
+ downloader - download the content from the download link. API : `start_download`
