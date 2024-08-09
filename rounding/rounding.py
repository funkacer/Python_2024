def rd(number, decimal_places=2, **kwargs) -> str:
    """Cerny rounding"""
    decimal_separator='.'
    minus_sign='-'
    separate_thousands=False
    thousands_separator=' '
    # parse kwargs
    #print(kwargs)
    #('decimal_separator', 'minus_sign', 'thousands_separate', 'thousands_separator'):
    if 'kwargs' in kwargs.keys():
        kwargs = kwargs['kwargs']
    for key in kwargs:
        if key == 'decimal_separator':
            decimal_separator = kwargs[key]
        elif key == 'minus_sign':
            minus_sign = kwargs[key]
        elif key == 'separate_thousands':
            separate_thousands = kwargs[key]
        elif key == 'thousands_separator':
            thousands_separator = kwargs[key]
        elif key == '':
            xxx = kwargs[key]
        else:
            raise Exception(f"Key argument {key} not accepted!")
    round_up = {'0':'1', '1':'2', '2':'3', '3':'4', '4':'5', '5':'6', '6':'7', '7':'8', '8':'9', '9':'0'}
    ret_string = ''
    raw_string = str(number)
    raw_string = raw_string.replace(thousands_separator, '')
    minus_place = raw_string.find(minus_sign)
    raw_string = raw_string.replace(minus_sign, '')
    dec_place = raw_string.find(decimal_separator)
    raw_string = raw_string.replace(decimal_separator, '')
    if dec_place == -1:
        dec_place = len(raw_string)
    for i, num in enumerate(raw_string):
        #-1 kvůli chybějícímu decimal_separator
        if i == (dec_place + decimal_places -1) or i == len(raw_string)-1:
            ret_string += raw_string[:i]
            if len(raw_string[i:]) > 1:
                decision_number = raw_string[(i+1)]
                #print(decision_number)
                if decision_number in ('0', '1', '2', '3', '4'):
                    ret_string += raw_string[i]
                else:
                    ret_string += round_up[raw_string[i]]
            else:
                ret_string += raw_string[i]
            break
    if len(ret_string) > dec_place - decimal_places:
        ret_string=ret_string[:dec_place] + decimal_separator + ret_string[dec_place:]
        if len(ret_string) - dec_place <= decimal_places:
            ret_string += '0' * (decimal_places - (len(ret_string) - dec_place) + 1)
    if separate_thousands:
        for i, j in enumerate(range(dec_place -1, -1, -1)):
            #print(ret_string[j])
            if i % 3 == 2 and j > 0:
                ret_string=ret_string[:j] + thousands_separator + ret_string[j:]
    if minus_place > -1:
        ret_string = minus_sign + ret_string
    return ret_string

def main():
    x=input("Zadejte číslo:")
    y=input("Des. místa:")
    try:
        y = int(y)
    except Exception as e:
        print (e)
        y = 0
    print(f'{x} rounded to {y} decimal places: {rd(x, y)}')
    #print(rd(x, int(y), kwargs={'separate_thousands':True}))

if __name__ == '__main__':
    main()