from django import template

register = template.Library()


@register.filter(name='ru_suffix')
def ru_suffix(number, arg):
    nom_sing, gen_sing, gen_plur = arg.split(',')
    if 10 <= number % 100 <= 20:
        return f'{ number } { gen_plur }'
    if number % 10 == 1:
        return f'{ number } { nom_sing }'
    if 2 <= number % 10 <= 4:
        return f'{ number } { gen_sing }'
    return f'{number} {gen_plur}'


@register.filter(name='chg_sep')
def chg_sep(string, sep):
    words = [word.strip() for word in string.split(',')]
    return sep.join(words)
