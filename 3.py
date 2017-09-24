from ast import literal_eval

def tipo(x):
    try:
        return type(literal_eval(x))
    except (ValueError, SyntaxError):
        return str

print ("'1' pertence ao conjunto: "+ str(tipo("1")))
print ("\n'1.234' pertence ao conjunto: "+ str(tipo("1.234")))
print ("\n'True' pertence ao conjunto: "+ str(tipo("True")))
print ("\n'abcd' pertence ao conjunto: "+ str(tipo("abcd")))
