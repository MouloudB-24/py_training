def get_value(dictionnaire, *args):
    args = list(args)
    default = args.pop(-1)

    for arg in args:
        dictionnaire = dictionnaire.get(arg)
        if not dictionnaire:
            return default

    return dictionnaire


dictionnaire = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
a = print(get_value(dictionnaire, "01", "identite", "prenom", "valeur inconnue"))
