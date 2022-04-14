def format_date_period(exp_period):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    period_descr = ''
    period_descr += months[int(exp_period['from'].month) - 1]
    period_descr += ' '
    period_descr += str(exp_period['from'].year)
    period_descr += ' - '
    if exp_period['to'].year == 2999:
        period_descr += 'Current'
    else:
        period_descr += months[int(exp_period['to'].month) - 1]
        period_descr += ' '
        period_descr += str(exp_period['to'].year)
    return period_descr