from yaml import load
from pprint import pprint
from dotenv import load_dotenv
import tex.gen
import html.gen
import os

load_dotenv()

def main():
    print("Before running this script please be sure that the following environment")
    print("variables are correctly set within the .env file: ")
    print("- CV_PERSONAL_EMAIL")
    print("- CV_PERSONAL_PHONE")

    data = open('../cv/cv.yml', 'r').read()
    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Loader

    cv_data = load(data, Loader=Loader)
    cv_data['email'] = os.getenv('CV_PERSONAL_EMAIL')
    cv_data['phone'] = os.getenv('CV_PERSONAL_PHONE')

    generate_then_write('cv.tex', lambda: tex.gen.latex_generator(cv_data))
    generate_then_write('cv.html', lambda: html.gen.html_generator(cv_data))
    generate_then_write('cv.mob.html', lambda: html.gen.html_generator_mob(cv_data))

def generate_then_write(out_filename, cv_filler):
    cv = cv_filler()
    open('../cv/' + out_filename, 'w').write(cv)
    
if __name__ == '__main__':
    main()