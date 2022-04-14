from jinja2 import Environment, PackageLoader
from utils.formmating import format_date_period

def to_valid_id(string):
    return '_'.join(string.split(' '))

def decorate_task_descr(task):
    descr = task['descr']
    if descr == None:
        raise NotImplementedError('Job tasks/activities cannot be empty! Please remove the dash without text.')

    # TODO: apply decorations in one pass
    if 'heres' in task.keys():
        i = 0
        for _ in task['heres']:
            descr = descr.replace('HERE', '<i><a href="%s">here</a></i>'%task['heres'][i], 1)
            i += 1
    if 'bolds' in task.keys():
        for b in task['bolds']:
            descr = descr.replace(b, '<strong>%s</strong>'%b)
    if 'italics' in task.keys():
        for it in task['italics']:
            descr = descr.replace(it, '<i>%s</i>'%it)
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

    template = env.get_template(template_name)
    return template.render(cv=cv_data)

def html_generator(cv_data):
    return generator(cv_data, 'cv-template.html')

def html_generator_mob(cv_data):
    return generator(cv_data, 'cv-template.mob.html')

