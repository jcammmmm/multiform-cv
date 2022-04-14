# About
Python script that generate Juan Camilo's CV in several template formats    
but with the same content.
The formats are:
    - LaTeX
    - HTML for desktop browsers
    - HTML for mobile browsers

This script does not provide you with the entire html o latex document, 
only provides well formated content that should be placed by hand (at least
for this version) in your templates.

## Development setup
1. Install python
2. Install PIP
3. Create your environment: `$ python3 -m venv env`
4. Activate your environment: `$ source env/bin/activate`
5. Deactivate your environment: `$ deactivate`

## How to run
`$ python3 multiform-gen.py`

## How to update deps.
`$ pip freeze > requirements.txt`

# Docs's docs
## Jinja2
https://jinja.palletsprojects.com/en/3.1.x/api/#custom-filters
