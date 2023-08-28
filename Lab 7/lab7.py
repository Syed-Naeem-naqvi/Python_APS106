#####################################################
# APS106 Winter 2022 - Lab 7 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Complete the function below to decompose
#          a compound formula written as a string
#          in a dictionary
######################################################

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
    # print(with_pers)

    # Split it
    list_form = with_pers.split('.')
    # print(list_form)

    # Add Ones where needed
    for i in range(len(list_form)):
        if list_form[i].isalpha():
            list_form[i] = list_form[i] + '1'

    # print(list_form)

    # cut each substring to separate names and counts
    # Add periods between letters and numbers

    for i in range(len(list_form)):
        inserted = False
        for j in range(len(list_form[i])):
            if list_form[i][j].isnumeric() and not inserted:
                revised = list_form[i][:j]+'.'+list_form[i][j:]
                list_form[i] = revised
                inserted = True

    # print(list_form)

    # Split the substrings
    for k in range(len(list_form)):
        list_form[k] = list_form[k].split('.')

    # print(list_form)
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

######################################################
# PART 2 - Complete the function below that takes two
#          tuples representing one side of a
#          chemical equation and returns a dictionary
#          with the elements as keys and the total
#          number of atoms in the entire expression
#          as values.
######################################################


def expr_form(expr_coeffs, expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary

    This function accepts two input tuples that represent a chemical expression,
    or one side of a chemical equation. The first tuple contains integers that
    represent the coefficients for molecules within the expression. The second
    tuple contains dictionaries that define these molecules. The molecule
    dictionaries have the form {'atomic symbol' : number of atoms}. The order
    of the coefficients correspond to the order of molecule dictionaries.
    The function creates and returns a dictionary containing all elements within
    the expression as keys and the corresponding number of atoms for each element
    within the expression as values.

    For example, consider the expression 2NaCl + H2 + 5NaF

    >>> expr_form((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}

    """
    # TODO your code here
    out_dict = {}
    for i in range(len(expr_coeffs)):
        factor = expr_coeffs[i]
        subdict = expr_molecs[i]

        for key, value in subdict.items():
            if key not in out_dict:
                out_dict[key] = value * factor
            else:
                old_value = out_dict[key]
                out_dict[key] = old_value + value * factor

    return out_dict


########################################################
# PART 3 - Check if two dictionaries representing
#          the type and number of atoms on two sides of
#          a chemical equation contain different
#          key-value pairs
########################################################


def find_unbalanced_atoms(reactant_atoms, product_atoms):
    """
    (Dict,Dict) -> Set

    Determine if reactant_atoms and product_atoms contain equal key-value
    pairs. The keys of both dictionaries are strings representing the
    chemical abbreviation, the value is an integer representing the number
    of atoms of that element on one side of a chemical equation.

    Return a set containing all the elements that are not balanced between
    the two dictionaries.

    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}

    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()

    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """

    # TODO your code here

    unbalanced = set()
    for key, value in reactant_atoms.items():  # First check if there are any reactant atoms that aren't in products
        if key not in product_atoms:  # Also check if the numbers are the same for the atoms that are in both reactants and products
            unbalanced.add(key)
        else:
            if product_atoms[key] != value:
                unbalanced.add(key)
    for key in product_atoms:  # Now check if there are any product atoms that aren't in reactants
        if key not in reactant_atoms:
            unbalanced.add(key)

    return unbalanced


########################################################
# PART 4 - Check if a chemical equation represented by
#          two nested tuples is balanced
########################################################

def check_eqn_balance(reactants, products):
    """
    (tuple,tuple) -> Set

    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.

    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.

    For example, the following balanced equation
    C3H8 + 5O2 <-> 4H2O + 3CO2

    would be input as the following two tuples:
    reactants: ((1,5), ("C3H8","O2"))
    products: ((4,3), ("H2O","CO2"))

    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O","CO2")))
    set()

    Similarly, for the unbalanced equation

    C3H8 + 2O2 <-> 4H2O + 3CO2

    would be input as the following two tuples:
    reactants: ((1,2), ("C3H8","O2"))
    products: ((4,3), ("H2O","CO2"))

    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O","CO2")))
    {'O'}

    """

    # TODO your code here

    reactants_coefficients = reactants[0]
    string_form_reactants_tuple = reactants[1]

    products_coefficients = products[0]
    string_form_products_tuple = products[1]

    reactants = []
    products = []
    for formula in string_form_reactants_tuple:  # Get dict representations for every string in the reactants
        reactants.append(mol_form(formula))
    reactants = tuple(reactants)
    for formula in string_form_products_tuple:
        products.append(mol_form(formula))
    products = tuple(products)
    reactants_expr_form = expr_form(reactants_coefficients, reactants)
    products_expr_form = expr_form(products_coefficients, products)
    unbalanced = find_unbalanced_atoms(products_expr_form, reactants_expr_form)
    return unbalanced

