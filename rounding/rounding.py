def rd(number, decimal_places=2, decimal_separator='.', minus_sign='-', separate_thousands=False, thousands_separator=' ') -> str:
    """Cerny rounding"""
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
    '''
    if abs(decimal_places) > dec_place and decimal_places < 0:
        #sem ještě přidat doplnění nul
        decimal_places = -1*dec_place
    if abs(decimal_places) == dec_place and decimal_places < 0: #and raw_string[0] in ('5', '6', '7', '8', '9'):
        raw_string = '0' + raw_string
        dec_place += 1
    if decimal_places < 0:
        decimal_places += 1
    if abs(decimal_places) >= dec_place and decimal_places < 0:
        raw_string = '0'*(abs(decimal_places) - dec_place + 1) + raw_string
        dec_place += abs(decimal_places) - dec_place + 1
    '''
    do_round_up = False
    # musim to iterovat pozadu a postupne pridat cisla, kdyz zaokrouhluju nahoru a dalsi je 9
    # at to nemusim delat nadvakrat
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
                    do_round_up = True
            else:
                ret_string += raw_string[i]
            break
    # repair if round up and all numbers are 9
    if do_round_up:
        rett_string = ''
        for i in range(len(ret_string)-1, -1, -1):
            if ret_string[i] == '9':
                rett_string += 0
                if i == 0: ret_string = '1' + rett_string
            else:
                rett_string += round_up[ret_string[i]]
                break
    if len(ret_string) < dec_place:
        ret_string += '0' * (dec_place - (len(ret_string)))
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
        print ('Using rounding to 0 decimal places')
        y = 0
    print(f'{x} rounded to {y} decimal places: {rd(x, y)}')
    #print(rd(x, int(y), kwargs={'separate_thousands':True}))

if __name__ == '__main__':
    main()