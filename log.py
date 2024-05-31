from safeconvert import convert

printdebug = True
printinfo = False
printmessage = True

def combine_args(message):
    comb = ""
    for m in message:
        comb += convert(m, str) + " "
    comb = comb[:-1]
    return comb


def d(*message: str) -> None:
    if printdebug:
        comb_message = combine_args(message)
        print("D: " + comb_message)

def i(*message: str) -> None:
    if printinfo:
        comb_message = combine_args(message)
        print("I: " + comb_message)

def m(*message: str) -> None:
    if printmessage:
        comb_message = combine_args(message)
        print("M: " + comb_message)
    