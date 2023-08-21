# TODOS
[ ] Add 4 audio recordings in each language    
[ ] Link your English certificate to your profile description    
[ ] Link something (e.g. youtube vid) in order to demo. your speaking    
[ ] Rearrange your skillset more comprehesively    
[ ] Link the companies names with their web pages
[ ] Add side _projects_ to your ***curriculum***

About  
===========================================================
Python script that generate Juan Camilo's CV in several template formats and languages 
but with the same content.
The formats are:
- LaTeX
- HTML for desktop browsers
- HTML for mobile browsers

This script does not provide you with the entire html o latex document, 
only provides well formated content that should be placed by hand (at least
for this version) in your templates.


Environment setup 
===========================================================
1. Install `python`
2. Install `pip`
3. Install `venv`

Usage  
===========================================================
Edit the YAML files in each language. Then execute the provided python script as follows:

Linux/Debian
---------------------------------------
1. Create your environment if you did not create already one:
	 ```$ python3 -m venv env```
2. Activate your environment:    
	```$ source env/bin/activate```
3. Install script dependencies:
	```pip install -r requirements.txt```
4. Run the script:
	```cd src```
	```python3 multiform-gen.py```
5. Look for output results in ```../cv``` folder.
6. Deactivate your environment:    
	```$ deactivate```

MacOS
---------------------------------------
3. Create your environment:    
	`$ python3 -m venv env`
4. Activate your environment:     
	`$ source env/bin/activate`
5. Deactivate your environment: 
	`$ deactivate`

Windows
---------------------------------------
2. `$> cd multiform-cv`
3. `$> python -m venv env`
4. `$> env\Scripts\activate.bat`
5. `$> pip install -r requirements.txt`
6. `$> cd src`
7. `$> python3 multiform-gen.py`
8. output in ../cv folder

## How to run
`$ python3 src/multiform-gen.py`

## How to update deps.
`$ pip freeze > requirements.txt`

# Docs's docs
## venv
https://docs.python.org/3/library/venv.html#how-venvs-work
## Jinja2
https://jinja.palletsprojects.com/en/3.1.x/api/#custom-filters
https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters
## PyYAML
https://pyyaml.org/wiki/PyYAMLDocumentation