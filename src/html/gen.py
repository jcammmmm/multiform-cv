from re import compile
from jinja2 import Environment, PackageLoader
from utils.formmating import format_date_period

def separate_into_paragraphs(string):
    formmated_text = ''
    for paragraph in string.strip().split('\n'):
        formmated_text += '<p>'
        formmated_text += paragraph
        formmated_text += '</p>'
    return formmated_text

def to_valid_id(string):
    return '_'.join(string.split(' '))

def decorate_task_descr(task):
    descr = task['descr']
    if descr == None:
        raise NotImplementedError('Job tasks/activities cannot be empty! Please remove the dash without text.')

    # bold and italics
    def itbold(matchobj):
        return '<strong><i>{}</i></strong>'.format(matchobj.group(0)[3:-3])
    p = compile(r'_\*\*.*?\*\*_')
    descr = p.sub(itbold, descr)

    # italics
    def it(matchobj):
        return '<i>{}</i>'.format(matchobj.group(0)[1:-1])
    p = compile(r'_.*?_')
    descr = p.sub(it, descr)

    # bold
    def bold(matchobj):
        return '<strong>{}</strong>'.format(matchobj.group(0)[2:-2])
    p = compile(r'\*\*.*?\*\*')
    descr = p.sub(bold, descr)

    # heres
    def here(matchobj):
        data = matchobj.group(0)[1:-1].split(', ')
        return '<i><a href="{}">{}</a></i>'.format(data[1].strip(), data[0].strip())
    p = compile(r'\[.*?\]')
    descr = p.sub(here, descr)

    return descr

def generator(cv_data, template_name):
    env = Environment(
        loader=PackageLoader('html'),
        autoescape=False,
        trim_blocks=True,
    )
    env.filters['to_valid_id'] = to_valid_id
    env.filters['format_date_period'] = format_date_period
    env.filters['decorate_task_descr'] = decorate_task_descr
    env.filters['separate_into_paragraphs'] = separate_into_paragraphs

    template = env.get_template(template_name)
    return template.render(cv=cv_data)

def html_generator(cv_data):
    return generator(cv_data, 'cv-template.html')

def html_generator_mob(cv_data):
    return generator(cv_data, 'cv-template.mob.html')

