def rd(number: float, precision: int = 1) -> str:
    '''
    Returns rounded string with defined precicion.

    INPUT:
    number: float, to be rounded
    precision: int, precision used whe rounding

    OUTPUT:
    round_str: str
    '''
    
    num, prec = None, None

    if isinstance(number, float):
        num = number
    else:
        try:
            num = float(number)
        except Exception as e:
            traceback.print_exc()
            pass

    if isinstance(precision, int):
        if precision >= 0:
            prec = precision
        else:
            prec = abs(precision)
    else:
        try:
            prec = abs(int(precision))
        except Exception as e:
            traceback.print_exc()
            pass

    assert num is not None, '\nPlease specify valid number\n'
    assert prec is not None, '\nPlease specify valid precision\n'

    fin = 1
    if num < 0: fin = -1
    num1 = num*10**prec
    if abs(num1 - int(num1)) >= .5:
        num1 += fin
    round_float = int(num1)/10**prec
    round_str = '{num:.{prec}f}'.format(num=round_float,prec=prec)
    return round_str
