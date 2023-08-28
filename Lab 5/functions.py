# 1)

def email_to_name(email):
    """
    (str) -> str

    Given a string with the format "first_name.last_name@domain.com",
    return a string "LAST_NAME,FIRST_NAME" where all the characters are upper
    case


    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'CONDA,ANNA'
    """
    output_str = ''

    first_period_index = email.find('.')
    first_at_index = email.find('@')
    first_name = email[:first_period_index].upper()
    last_name = email[first_period_index+1:first_at_index].upper()
    output_str += last_name + ',' + first_name
    return output_str


# print(email_to_name('anna.conda@mail.utoronto.ca'))
# print(email_to_name('guido.vanrossum@companyX.com'))

# Q2


def count_measurements(s):
    """
    (str) -> int

    Given s, a string representation of comma separated site-measurement
    pairs, return the total number of measurements

    >>> count_measurements("B, 5.6, Control, 5.5, Db, 3.2")
    3

    >>> count_measurements("Control, 7.5")
    1
    """

    # TODO: YOUR CODE HERE
    count_commas = 0
    for i in s:
        if i == ',':
            count_commas += 1
    number_of_measurements = (count_commas + 1)//2
    return number_of_measurements


# print(count_measurements("Control, 7.5"))
# print(count_measurements('B, 5.6, Control, 5.5, Db, 3.2'))

# Q3

def calc_site_average(measurements, site):
    """
    (str, str) -> float

    Given s, a string representation of comma separated site-measurement
    pairs, and the name of a site,
    return the average of the site measurements to one decimal place

    >>> calc_site_average("A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    7.2
    """
    # TODO: YOUR CODE HERE
    to_iterate = measurements.split(',')
    print(to_iterate)
    relevant_measurements = []
    for i in range(len(to_iterate)):
        print(i)
        if to_iterate[i] == site:
            relevant_measurements.append(to_iterate[i + 1])
    print(relevant_measurements)
    return relevant_measurements

# Do something with split()




print(calc_site_average("A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control"))


