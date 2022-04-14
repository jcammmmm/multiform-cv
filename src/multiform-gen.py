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

    data = open('../cv-data.yml', 'r').read()
    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Loader

    cv_data = load(data, Loader=Loader)
    cv_data['email'] = os.getenv('CV_PERSONAL_EMAIL')
    cv_data['phone'] = os.getenv('CV_PERSONAL_PHONE')

    cv_tex = tex.gen.latex_generator(cv_data)
    open('../cv.tex', 'w').write(cv_tex)

    cv_html = html.gen.html_generator(cv_data)
    open('../cv.html', 'w').write(cv_html)
    
if __name__ == '__main__':
    main()