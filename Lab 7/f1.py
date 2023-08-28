
def mol_form(compound_formula):
    """(str) -> dictionary
    When passed a string of the compound formula, returns a dictionary
    with the elements as keys and the number of atoms of that element as values.

    >>> mol_form("C2H6O")
    {'C': 2, 'H': 6, 'O': 1}
    >>> mol_form("CH4")
    {'C': 1, 'H': 4}
    >>> mol_form('H2O')
    {'H': 2, 'O': 1}
    >>> mol_form('KFe4')
    {'K': 1, 'Fe': 4}
    >>> mol_form('C2H6O')
    {'C': 2, 'H': 6, 'O': 1}
    >>> mol_form('HNO3')
    {'H': 1, 'N': 1, 'O': 3}
    >>> mol_form('MnO3')
    {'Mn': 1, 'O': 3}
    >>> mol_form('BH3')
    {'B': 1, 'H': 3}
    >>> mol_form('HCNO')
    {'H': 1, 'C': 1, 'N': 1, 'O': 1}
    >>> mol_form('NaBrH3')
    {'Na': 1, 'Br': 1, 'H': 3}
    >>> mol_form('C3H5N3O9')
    {'C': 3, 'H': 5, 'N': 3, 'O': 9}
    >>> mol_form('C5H11OH')
    {'C': 5, 'H': 12, 'O': 1}
    """

    # TODO your code here

    # Add periods to separate atoms
    with_pers = ''
    for i in compound_formula:
        if i.isupper():
            with_pers += '.'
        with_pers += i
    with_pers = with_pers[1:]
    print(with_pers)

    # Split it
    list_form = with_pers.split('.')
    print(list_form)

    # Add Ones where needed
    for i in range(len(list_form)):
        if list_form[i].isalpha():
            list_form[i] = list_form[i] + '1'

    print(list_form)

    # cut each substring to separate names and counts
    # Add periods between letters and numbers

    for i in range(len(list_form)):
        inserted = False
        for j in range(len(list_form[i])):
            if list_form[i][j].isnumeric() and not inserted:
                revised = list_form[i][:j]+'.'+list_form[i][j:]
                list_form[i] = revised
                inserted = True

    print(list_form)

    # Split the substrings
    for k in range(len(list_form)):
        list_form[k] = list_form[k].split('.')

    print(list_form)
    out = {}
    for n in range(len(list_form)):
        key = list_form[n][0]
        # print(key)
        value = list_form[n][1]
        # print(value)
        if key not in out:
            out[key] = int(value)
        else:
            old_val = out[key]
            out[key] = old_val + int(value)

    return out


print(mol_form('C2HC'))





