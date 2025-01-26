# WEB-Summarizer
This project is about an AI agent which will take URL of an website as an input then generate its summary.
Main.py and summarizer.py are two different codes they are not interconnected. 


## REQUIREMENTS for running main.py
Virtual environment
1) Open your favorite IDE like VSCode, and create a new folder.
2) cd into your folder, open terminal, and type python -m venv venv
3) Type source venv/bin/activate and activate your virtual environment

Install newspaper3k
1) cd into your folder, open terminal, and type pip install newspaper3k

Install NLTK
1) cd into your folder, open terminal, and enter make sure venv is activated.
2) type pip install nltk
3)once completed type python,then enter
>>> import nltk
>>> nltk.download('punkt')
## REQUIREMENTS for running summarizer.py

Virtual environment
1) Open your favorite IDE like VSCode, and create a new folder.
2) cd into your folder, open terminal, and type python -m venv venv
3) Type source venv/bin/activate and activate your virtual environment

OpenAI API key
Generate a OpenAI API key. Copy and paste the link in the .env file provided in the repository
