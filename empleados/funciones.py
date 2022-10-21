



def validar_dato(consulta):
    for digito in consulta:
        if digito in '0123456789':
            continue
        else:
            return False
    return True



