def enter_txt(lmin=0, lmax=100, msg=None):
    print(msg) if msg else None
    while True:
        etexto = input("> ")
        if len(etexto) >= lmin and len(etexto) <= lmax:
            return etexto
