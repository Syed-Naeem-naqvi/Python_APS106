###############################################
# APS106  2022 - Lab 5 - Measurement Parser   #
###############################################

############################
# Part 1 - Email to Name   #
############################

def email_to_name(email):
    """
    (str) -> str

    Given a string with the format "first_name.last_name@domain.com",
    return a string "LAST_NAME,FIRST_NAME" where all the characters are upper
    case


    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'CONDA,ANNA'
    >>> email_to_name('ada.lovelace@emaildomain.com')
    'LOVELACE,ADA'
    >>> email_to_name('guido.vanrossum@companyX.com')
    'VANROSSUM,GUIDO'

    >>> email_to_name('Joe.bobson@utmail.ca')
    'BOBSON,JOE'
    >>> email_to_name('naeem.naqvi@mail.utoronto.ca')
    'NAQVI,NAEEM'
    >>> email_to_name('firstname.lastname@domain.com')
    'LASTNAME,FIRSTNAME'
    >>> email_to_name('Gabe.newell@valvesoftware')
    'NEWELL,GABE'
    >>> email_to_name('Mike.tyson@mail.utoronto.ca')
    'TYSON,MIKE'
    """

    # TODO: YOUR CODE HERE
    output_str = ''

    first_period_index = email.find('.')  # Locate the first period
    first_at_index = email.find('@')  # Locate the first @
    first_name = email[:first_period_index].upper()  # Slice the input form the start to the first period index-1 and make it uppercase
    last_name = email[first_period_index + 1:first_at_index].upper()  # The last name can be found by slicing form the location of the first period + 1 to the index of the @
    output_str += last_name + ',' + first_name  # combine the last and first names, separated by a comma
    return output_str  # return output to user


###############################
# Part 2 - Count Measurements #
###############################


def count_measurements(s):
    """
    (str) -> int

    Given s, a string representation of comma separated site-measurement
    pairs, return the total number of measurements

    >>> count_measurements("B, 5.6, Control, 5.5, Db, 3.2")
    3
    >>> count_measurements("Control, 7.5")
    1
    >>> count_measurements("B, 5.6, Control, 5.5, Db, 3.2")
    3
    >>> count_measurements("Control, 7.5")
    1

    >>> count_measurements('B, 1')
    1
    >>> count_measurements("A, 3.4, B, 9.5")
    2
    >>> count_measurements("A, 5, B, 8, C, 9.9")
    3
    >>> count_measurements("North, 5, South, 8, West, 4, East, 9")
    4
    >>> count_measurements("Site_1, 3.333, site_B, 2/5, site_3, 9.999999, four, 10.001, site_5, 2.222222")
    5
    """

    # TODO: YOUR CODE HERE

    count_commas = 0  # initialize container
    for i in s:  # traverse the input
        if i == ',':
            count_commas += 1  # count the number of commas
    number_of_measurements = (count_commas + 1) // 2  # use a relationship between the number of commas and measurements to count the measurements
    return number_of_measurements  # return number of measurements to user


######################################
# Part 3 - Calculate Site Average    #
######################################

def calc_site_average(measurements, site):
    """
    (str, str) -> float

    Given s, a string representation of comma separated site-measurement
    pairs, and the name of a site,
    return the average of the site measurements to one decimal place


    >>> calc_site_average("A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    7.2
    >>> calc_site_average("Control, 7.4, Control, 7.2, Control, 7.6", 'Control')
    7.4
    >>> calc_site_average("Control, 10.2, Control, 11.2, Control,9.6", "Control")
    10.3
    >>> calc_site_average("A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "A")
    4.0

    >>> calc_site_average("A, 5, B, 5, C, 5, A, 6",'A')
    5.5
    >>> calc_site_average("one, 4, two, 6, three, 8, one, 3, one, 2",'one')
    3.0
    >>> calc_site_average("one, 4, two, 6, three, 8, one, 3, one, 2",'two')
    6.0
    >>> calc_site_average("one, 4, two, 6, three, 8, one, 3, one, 2",'three')
    8.0

    """

    # TODO: YOUR CODE HERE
    measurements = measurements.replace(' ', '')  # Remove all whitespace from string
    data = measurements.split(',')  # use split() to transform into a list, break at ,'s

    count_instances = 0  # We want to know how many measurements were taken from the site for the avg
    site_sum = 0  # find the sum of site readings for the avg

    for index in range(len(data)):  # Generate indices for list traversal
        if data[index] == site:  # if an item in the list is the site
            count_instances += 1  # increase site instances by 1
            site_sum += float(data[index + 1])  # add the next item in the list (the site's reading) to the total

    site_average = site_sum / count_instances  # Calculate the arithmetic mean for the site
    site_average = round(site_average, 1)  # round the site's avg to one decimal place

    return site_average  # return the result


###############################
# Part 4 - Generate Summary   #
###############################

def generate_summary(measurement_info, site):
    """
    (str, str) -> str

    Extract technician name, number of measurements, and average of control
    site pH level measurements from string of technician measurements. Input
    string is formatted as

        firstname.lastname@domain.com, date, sitename, measurement, sitename, measurement, ...

    returns a string with the extracted information formatted as

        LASTNAME,FIRSTNAME,number of measurements,average pH of specified site

    >>> generate_summary("dina.dominguez@company.com, 01/11/20, A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    'DOMINGUEZ,DINA,7,7.2'
    >>> generate_summary("jamie.riggs@company.com, 14/12/20, B, 5.6, Control, 5.5, Db, 3.2, B, 6.1, B, 5.9", "B")
    'RIGGS,JAMIE,5,5.9'

    >>> generate_summary("Bob.Bobson@utmail.ca, 4/20/96, A, 10, B, 9, B, 8", "B")
    'BOBSON,BOB,3,8.5'
    >>> generate_summary("Fat.Wadil@mail.utoronto.ca, 3/13/20, C, 9, D, 2, D, 3, D, 4", "D")
    'WADIL,FAT,4,3.0'
    >>> generate_summary("First.Last@Some_bullshit_domain, 09/03/13, A, 9, B_site, 4, B_site, 9", "B_site")
    'LAST,FIRST,3,6.5'

    """

    # TODO: YOUR CODE HERE

    output_string = ''  # Initialize empty output string

    first_comma = measurement_info.find(',')  # find the first comma
    function_one_input = measurement_info[:first_comma]  # cut the input up to the first comma, extracting the email
    full_name = email_to_name(function_one_input)  # send the email to the first function to get the full name
    output_string += full_name  # add the name to the output

    email_removed = measurement_info[first_comma + 1:]  # remove the email from the input
    second_comma = email_removed.find(',')  # Now find the next comma
    date_removed = email_removed[second_comma + 1:]  # Slice from the next comma till the end of the input, removing the date
    site_average = count_measurements(date_removed)  # Send the dateless string to the second function
    output_string += ',' + str(site_average)  # add a comma and string-converted output of the second function to the output string

    site_average_result = calc_site_average(date_removed, site)
    output_string += ',' + str(site_average_result)  # Send the same input for the second function to the third one, and add the result to the output

    return output_string  # return the output string

