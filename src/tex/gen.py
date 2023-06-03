from re import compile
from jinja2 import Environment, PackageLoader, select_autoescape
from utils.formmating import format_date_period

def decorate_task_descr(task):
    descr = task['descr']
    if descr == None:
        raise NotImplementedError('Job tasks/activities cannot be empty! Please remove the dash without text.')

    # bold and italics
    def itbold(matchobj):
        return '\\textit{\\textbf{%s}}'%matchobj.group(0)[3:-3]
    p = compile(r'_\*\*.*?\*\*_')
    descr = p.sub(itbold, descr)

    # italics
    def it(matchobj):
        return '\\textit{%s}'%matchobj.group(0)[1:-1]
    p = compile(r'_.*?_')
    descr = p.sub(it, descr)

    # bold
    def bold(matchobj):
        return '\\textbf{%s}'%matchobj.group(0)[2:-2]
    p = compile(r'\*\*.*?\*\*')
    descr = p.sub(bold, descr)

    # heres
    def here(matchobj):
        data = matchobj.group(0)[1:-1].split(', ')
        return '\\textbf{\\href{%s}{%s}}'%(data[1].strip(), data[0].strip())
    p = compile(r'\[.*?\]')
    descr = p.sub(here, descr)

    return descr

def latex_generator(cv_data):
    env = Environment(
        loader=PackageLoader('tex'),
        autoescape=select_autoescape(),
        variable_start_string='==',
        variable_end_string='==',
        block_start_string='=%',
        block_end_string='%=',
        trim_blocks=True,
    )
    env.filters['decorate_task_descr'] = decorate_task_descr
    env.filters['format_date_period'] = format_date_period

    template = env.get_template('cv-template.tex')
    return template.render(cv=cv_data)