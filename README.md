****************
* Gemini Explorer
* 06/17/24
* Max Hartel
**************** 

OVERVIEW:

Gemini Explorer is a project that introduces google's gemini interactive large language model and how to begin working with it. The main focus of this exercise was to connect to gemini with a python script such that we could use the streamlit service to interact with gemini under the custom interface of ReX. 


INCLUDED FILES:

 gemini_explorer.py - source file
 README - this file


COMPILING AND RUNNING:
 
 From the directory containing all source files run the script with the command:
 $ streamlit run gemini_explorer.py

 The window will then switch over to streamlit, where you can interact with the AI model.


PROGRAM DESIGN AND IMPORTANT CONCEPTS:

The ReX AI interface that was designed in this project uses google's gemini as its brain and informational database when responding to user questions. This was an essential resource to be able to take advantage of because the creation and maitnence of a large scale natural language model was not feasable for this project from scratch. The main focus of this project was to become familiar with interfacing with gemini and passing along user requests to it, I became accustomed to accessing the google cloud API as well as working with the Google Clout and Streamlit CLI's. The extent of this project's functionalitity was to create a custom istance of google's gemini, and teach it how to great a custom user after gathering their name as a designated input. I think with these basic building blocks there is a bright future for further work on this project. 


TESTING:
This was tested manually by human use of the streamlit interface of the ReX model. 


DISCUSSION:
 
 Development Journal:

The first few tasks were relatively simple in just that I had to download software and make the correct intalls of dependencies of the project, there were no major issues here, but the guiding videos seemed to be out of sync with the guiding slide deck, so this led me to just have to figure some things out entirely on my own. The confusion in the instructional materials slowed me down a little bit, but progress overall moved along at a good pace. 

After the installs and sign-ups fpr online services were finished, I was finally able to get to the actual code, I liked this part of the development much better, as I was able to lean on my experience as a software engineer to speed things along. The code itself was not very complicated, only using fundamental datastructures, but there were many unfamiliar pieces with the streamlit and gemini api's and their functions being new to me. 

After getting used to how the Api's worked and how gemini accepted and returned input, I created an custom welcom messege for the user that took in the user's name as input and returned a welcome messege with a create and unique AI personality for ReX as well. 