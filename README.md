# VirAm - Your Virtual Friend
The Virtual Friend made by team of Mount Carmel School for the competition **Ignite**. You can visit this on [https://mcs-vf.herokuapp.com](https://mcs-vf.herokuapp.com)  
[![Introductory Video](https://github.com/Nalin-2005/VirAm/blob/main/media/Thumbnail.jpg?raw=1)](https://www.youtube.com/watch?v=xKLleKGzPuQ)  
*Click to view the video*

## About
VirAm is a virtual chatbot designed to help Indian students studying abroad, to help them understand their surroundings, and to make them feel at home. This bot was made keeping simplicity in mind, and to make the user feel comfortable using this.   

To make this chatbot effective in helping you adapt to the new places you are going to, VirAm has a number of features that make it easy to use. You can get these features listed here: https://mcs-vf.herokuapp.com/features.   

## Instructions on how to set it up
1. Create a Dialogflow agent, and put it's service account JSON file in the root directory by the name: `viram.json`
2. Create it's commands and responses as per your requirements.
3. Install python if not installed.
4. Make sure you can run `pip --version` and `python --version` in the Terminal
5. Run `pip install -r requirements.txt` with the terminal opened in the project's root directory
6. Run `python main.py` to start the app server.
7. Open [`http://localhost:2000`](http://localhost:2000) in your browser.

## Which files are for what purposes
- `media/*`: Graphics and Video used in the official YouTube demonstration for the project.   
- `static/*`: Static files for the web interface like images, css, js, etc.   
- `templates/*`: HTML templates.   
- `.env`: Sets the path of dialogflow credentials.   
- `Procfile`: The file for providing instructions to Heroku on how to run the app.   
- `commands.py`: Specialized commands to interpret dialogflow reponses and evaluate dynamic content (Currency conversion, Translation).   
- `features.py`: A file containing a list of features, and some of it's dynamic content generators for feature pages.   
- `main.py`: Starts the app server.   
- `predict.py`: Predicts the output of a given text.   
- `requirements.txt`: The python libraries required by the app.   

## How do commands work?
When we wish to implement dynamic content in the response, we make the dialogflow agent respond with a special command whose syntax is like: `cmd:function_name <space separated or "--arg val" type arguments>`   

## Credits
This project was made collaboratively by 2 students of [Mount Carmel School](https://mountcarmelchd.org/):  
- [Nalin Angrish](https://www.nalinangrish.me/) (XI-A) 
- [Arnab Jena](https://github.com/arnabjena007) (XII-A)