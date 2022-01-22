from django import template

register = template.Library()

@register.filter(name='multiply')
def myltiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int):
        return str(value) * arg
    else:
        raise ValueError(f'нельзя умножить {type(value)} на {type (arg)}')

@register.filter(name='censor')
def censor(value):
    censor_list = ['Козел',
                   'коза',
    ]
    value1 = (str(value)).split()
    for i in censor_list:
        for j in value1:
            if j == i:
                value1.remove(i) # delete
    value = ' '.join(value1)
    return str(value)