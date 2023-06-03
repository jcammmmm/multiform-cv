from yaml import load
from pprint import pprint
from dotenv import load_dotenv
import tex.gen
import html.gen
import os

import re

load_dotenv()

def main():
    print("Before running this script please be sure that the following environment")
    print("variables are correctly set within the .env file: ")
    print("- CV_PERSONAL_EMAIL")
    print("- CV_PERSONAL_PHONE")


    langava = ['en', 'es', 'pt', 'de']
    for lang in langava:
        data = open('../cv/{}/cv.yml'.format(lang), 'r', encoding='utf-8').read()
        try:
            from yaml import CLoader as Loader
        except ImportError:
            from yaml import Loader

        cv_data = load(data, Loader=Loader)
        cv_data['email'] = os.getenv('CV_PERSONAL_EMAIL')
        cv_data['phone'] = os.getenv('CV_PERSONAL_PHONE')

        generate_then_write(lang, 'cv.tex', lambda: tex.gen.latex_generator(cv_data))
        generate_then_write(lang, 'cv.html', lambda: html.gen.html_generator(cv_data))
        generate_then_write(lang, 'cv.mob.html', lambda: html.gen.html_generator_mob(cv_data))

def generate_then_write(lang, out_filename, cv_filler):
    cv = cv_filler()
    open('../cv/{}/{}'.format(lang, out_filename), 'wb+').write(cv.encode('utf8'))
    
if __name__ == '__main__':
    main()
    exit
    def it(matchobj):
        return 'xxxx'
    p = re.compile(r'_\w*_')
    ms = p.sub(it, 'buah _aha_ hahab _ds_')
    print('_buahahahahah_'[1:-1])
    exit
