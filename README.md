# twittoff-khislatz

# Installation 


'''sh 
git clone https://github.com/Khislatz/twitoff-khislatz.git
cd twioff-khislatz/

#Setup

'''sh
pipenv install
''''

#Usage 

'''sh

# Mac:
FLASK_APP=web_app flask run
# FLASK_APP=hello.py flask run  
# hello.py is the name of the file. Right now we use web_app directory, flask will look for the app that should be run in this directory.  

# Windows:
export FLASK_APP=web_app # one-time thing, to set the env var
flask run
# export doesn't work use set instead
set FLASK_APP=web_app