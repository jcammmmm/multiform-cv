from jinja2 import Environment, PackageLoader, select_autoescape

def decorate_task_descr(task):
    descr = task['descr']

    # TODO: apply decorations in one pass
    if 'heres' in task.keys():
        i = 0
        for _ in task['heres']:
            descr = descr.replace('HERE', '\\textbf{\\href{%s}{here}}'%task['heres'][i], 1)
            i += 1
    if 'bolds' in task.keys():
        for b in task['bolds']:
            descr = descr.replace(b, '\\textbf{%s}'%b)
    if 'italics' in task.keys():
        for it in task['italics']:
            descr = descr.replace(it, '\\textit{%s}'%it)
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

    template = env.get_template('cv-template.tex')
    return template.render(cv=cv_data)