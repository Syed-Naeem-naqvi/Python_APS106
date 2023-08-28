############################################################
# APS106 Winter 2022 - LAB 9 - Wind Turbine Placement OOP  #
############################################################

import csv


class Point:
    """
    A point in a two-dimensional coordinate plane
    """

    def __init__(self, x, y):
        """
        Create a point with an x and y coordinate
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Generate a string representation of a point
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"


############################
# Part 1 - Circle Class
############################
class Circle:
    """
    A circle in a two-dimensional coordinate plane
    """

    def __init__(self, centre_x, centre_y, radius):
        """
        Create a rectangle defined by its bottom left and top right corner
        coordinates
        """
        self.centre = Point(centre_x, centre_y)
        self.radius = radius

    def __str__(self):
        """
        Generate a string representation of a rectangle
        """
        return ("Circle with centre coordinate " +
                str(self.centre) + " and radius " + str(self.radius))

    def move(self, horizontal_translation, vertical_translation):
        """
        (Circle, int, int) -> None

        Alters the location of a circle by translating the coordinates
        of its centre coordinates.
        """
        self.centre.x += horizontal_translation
        self.centre.y += vertical_translation

    def overlap(self, circB):
        """
        (Circle, Circle) -> bool

        Checks whether two circles overlap, return true if they overlap, false otherwise
        """

        # compute the distance between the centres
        d = ((self.centre.x - circB.centre.x) ** 2 + (self.centre.y - circB.centre.y) ** 2) ** (1 / 2)
        return d < (self.radius + circB.radius)


##############################
# Part 2 - Wind Turbine Class
##############################
class WindTurbine:
    """
    A wind turbine placed in a two-dimensional area
    """

    def __init__(self, id_number, placement_centre_x, placement_centre_y, placement_radius):
        """
        Create a wind turbine
        """
        self.id_number = id_number
        self.placement = Circle(placement_centre_x, placement_centre_y, placement_radius)

        self.overlapping_turbines = []

    def __str__(self):
        """
        Generate a string representation of a WindTurbine object
        """
        return ("Wind Turbine ID: " + str(self.id_number) +
                ", Placement: " + str(self.placement))

    def move(self, horizontal_translation, vertical_translation):
        """
        (WindTurbine, int, int) -> None

        Alters the location of a wind turbine by translating the coordinates
        of its bottom left and top right corner coordinates. After moving the
        turbine, the overlapping turbine list should be reset to an empty
        list.

        The change in the x and y coordinates are specified by the
        horizontal_translation and vertical_translation parameters, respectively.
        """
        self.placement.move(horizontal_translation, vertical_translation)

    def overlap(self, turbineB):
        """
        (WindTurbine, WindTurbine) -> bool

        Checks for overlap between a wind turbine and another turbine (turbineB).
        """
        return self.placement.overlap(turbineB.placement)

    def validate_placement(self, turbines):
        """
        (WindTurbine, list of WindTurbines) -> None

        Check if the position of a wind turbine is valid by checking for
        overlapping areas with all other wind turbines.
        """
        for turbine in turbines:
            if self.overlap(turbine) is True and turbine.id_number != self.id_number:
                self.overlapping_turbines.append(turbine)


##########################################
# Part 3 - Load Wind Turbines from File
##########################################

def load_turbine_placements(turbine_filename):
    """
    (str) -> list of WindTurbines

    Opens a csv file containing wind turbine IDs, and placement
    info (centre coordinates and radius) and returns a list
    of WindTurbine objects for each turbine defined in the file
    """
    generated_turbines = []
    with open(turbine_filename, 'r') as csv_file:
        turbines_nested_list = csv.reader(csv_file)
        print(turbines_nested_list)
        for data_list in turbines_nested_list:
            print(data_list)
            new_turbine = WindTurbine(data_list[0], data_list[1], data_list[2], data_list[3])
            generated_turbines.append(new_turbine)
    return generated_turbines[1:]


# Test 1 Passed
turbines = load_turbine_placements('turbines1.csv')
print(turbines)
for i in turbines:
    print(i)

# Test 2 Passed
# more_turbines = load_turbine_placements('turbines2.csv')
# for i in more_turbines:
#     print(i)


##########################################
# Part 4 - Testing Wind Turbine Placement
##########################################

def check_turbine_placements(turbines):
    """
    (list of WindTurbines) -> int

    Checks a list of wind turbines to identify turbines with invalid (overlapping)
    placements. The function should return the number of turbines with
    invalid placements.

    All placements should be evaluated using the validate_placement method from
    the WindTurbine class.
    """
    invalid_placements_count = 0
    turbine_pairs = []
    for t in turbines:
        t.validate_placement(turbines)
        if len(t.overlapping_turbines) > 0:
            invalid_placements_count += 1
    return invalid_placements_count


# # circle move()
# c1 = Circle(0,1,4)
# print(c1)
# c1.move(3,-9)
# print(c1)
#
# # turbine move()
# t1 = WindTurbine(1, 4, 5, 10)
# print(t1)
# t1.move(-1,4)   # move one unit to the left and 4 units up
# print(t1)
#
# # Overlap()
# t2 = WindTurbine(2, 0, 0, 2)
# print(t1.overlap(t2))
# t3 = WindTurbine(3, -10, -5, 2)
# print(t1.overlap(t3))
#
# # validate()
# t1 = WindTurbine(1, 4, 5, 10)
# t2 = WindTurbine(2, 4, 6, 5)
# t3 = WindTurbine(3, -5, -9, 3)
# t4 = WindTurbine(4, 100, 2000, 44)
# turbine_list = [t1, t2, t3, t4]
# t1.validate_placement(turbine_list)
# print(len(t1.overlapping_turbines))  # print the number of turbines found to overlap with t1
# print(t1.overlapping_turbines[0])  # print the turbine that overlaps
#
# # Last function
# t1 = WindTurbine(1, 4, 5, 10)
# t2 = WindTurbine(2, 4, 6, 5)
# t3 = WindTurbine(3, -5, -9, 3)
# t4 = WindTurbine(4, 100, 2000, 44)
# turbine_list = [t1, t2, t3, t4]
# num_invalid = check_turbine_placements(turbine_list)
# print(num_invalid)

# Markus Tests

def equal(expected_result, submission_result, msg):
    """
    Return true if submission_result is equal to expected_result, false otherwise.
    If not equal, print error message.
    """
    if expected_result == None:
        # check for correct type
        if submission_result != None:
            print(msg)
            return False

    elif isinstance(expected_result, str):
        if not isinstance(submission_result, str):
            print(msg)
            return False

        if expected_result != submission_result:
            print(msg)
            return False

    elif isinstance(expected_result, bool):
        # check for correct type
        if not isinstance(submission_result, bool):
            print(msg)
            return False

        # check value
        if expected_result != submission_result:
            print(msg)
            return False

    elif isinstance(expected_result, int):
        # check for correct type
        if not isinstance(submission_result, int):
            print(msg)
            return False

        # check value
        if expected_result != submission_result:
            print(msg)
            return False

    elif isinstance(expected_result, list):
        # check for correct type
        if not isinstance(submission_result, list):
            print(msg)
            return False

        if len(expected_result) != len(submission_result):
            print(msg)
            return False

        for exp_res_item, sub_res_item in zip(expected_result, submission_result):
            if not equal(exp_res_item, sub_res_item, msg):
                return False
    else:
        print("MarkUS error, contact course head TA.")
        return False

    return True


def test_01():
    """
    (None) -> bool

    Run Circle.move test, return true if test passes, false otherwise
    """
    from lab9 import Circle
    sub_c = Circle(3, 4, 8)

    pre_move_pt_id = id(sub_c.centre)

    sub_out = sub_c.move(33, -19)

    post_move_pt_id = id(sub_c.centre)

    # test that method returns None
    returns_none = equal(None, sub_out, "Your Circle.move method does not return None")

    # test that the coordinates of the circle are updated correctly
    correct_coordinates = equal('Circle with centre coordinate (36,-15) and radius 8',
                                str(sub_c),
                                "Circle.move method does not modify circle objects as expected")

    # test that no new Point object was created
    update_centre = equal(pre_move_pt_id, post_move_pt_id,
                          "Your Circle.move method creates a new Point object. It should update the existing Point")

    return returns_none and correct_coordinates and update_centre


def test_02():
    """
    (None) -> bool

    Run WindTurbine.move test, return true if test passes, false otherwise
    """
    from lab9 import WindTurbine
    sub_t = WindTurbine(14, 22, -7, 29)

    pre_move_circ_id = id(sub_t.placement)
    pre_move_pt_id = id(sub_t.placement.centre)

    sub_out = sub_t.move(33, -19)

    post_move_circ_id = id(sub_t.placement)
    post_move_pt_id = id(sub_t.placement.centre)

    # test that the method returns none
    returns_none = equal(None, sub_out, "Your WindTurbine.move method does not return None")

    # test that the coordinates of the circle are updated correctly
    correct_coordinates = equal('Wind Turbine ID: 14, Placement: Circle with centre coordinate (55,-26) and radius 29',
                                str(sub_t),
                                "WindTurbine.move method does not modify circle objects as expected")

    # test that no new Point object was created
    update_centre = equal(pre_move_pt_id, post_move_pt_id,
                          "Your WindTurbine.move method creates a new Point object. It should update the existing Point")

    # test that no new Circle object was created
    update_placement = equal(pre_move_circ_id, post_move_circ_id,
                             "Your WindTurbine.move method creates a new Circle object. It should update the existing Circle")

    return returns_none and correct_coordinates and update_centre and update_placement


def test_03():
    """
    (None) -> bool

    Run WindTurbine.overlap test, return true if test passes, false otherwise
    """
    from lab9 import load_turbine_placements
    sub_out = load_turbine_placements("turbines1.csv")

    # convert list of turbines to list of string representations
    sub_out_strs = []
    if isinstance(sub_out, list):
        for t in sub_out:
            sub_out_strs.append(str(t))

    expected_out_strs = ['Wind Turbine ID: 1, Placement: Circle with centre coordinate (8,-9) and radius 8',
                         'Wind Turbine ID: 52, Placement: Circle with centre coordinate (-9,71) and radius 5',
                         'Wind Turbine ID: 5, Placement: Circle with centre coordinate (0,0) and radius 1',
                         'Wind Turbine ID: 8, Placement: Circle with centre coordinate (7,99) and radius 2']

    return equal(expected_out_strs, sub_out_strs, "load_turbine_placements returns the incorrect result")


def test_04():
    """
    (None) -> bool

    Run WindTurbine.validate_placement test, return true if test passes, false otherwise
    """
    from lab9 import WindTurbine

    t1 = WindTurbine(1, 1, 2, 5)
    t2 = WindTurbine(2, 0, 2, 4)
    t3 = WindTurbine(3, 11, 12, 5)
    sub_ret = t2.validate_placement([t1, t2, t3])

    t2_overlapping_strs = []
    for t in t2.overlapping_turbines:
        t2_overlapping_strs.append(str(t))

    return (equal(None, sub_ret, "Your method does not return None.") and
            equal(['Wind Turbine ID: 1, Placement: Circle with centre coordinate (1,2) and radius 5'],
                  t2_overlapping_strs,
                  "Your WindTurbine.validate_placement method does not identify the correct overlapping turbines"))


def test_05():
    """
    (None) -> bool

    Run check_turbine_placements test, return true if test passes, false otherwise
    """
    from lab9 import check_turbine_placements, WindTurbine

    t1 = WindTurbine(1, 1, 2, 5)
    t2 = WindTurbine(2, 0, 2, 4)
    t3 = WindTurbine(3, 11, 12, 5)
    t4 = WindTurbine(4, -1, 4, 1)
    sub_out = check_turbine_placements([t1, t2, t3, t4])
    exp_out = 3
    return equal(exp_out, sub_out,
                 "Your check_turbine_placement function does not return the correct number of overlapping turbines")


def run_tests():
    """
    Run all MarkUS test functions
    """
    if test_01():
        print("test 1 passed\n\n")
    else:
        print("test 1 failed, see error message above\n\n")

    if test_02():
        print("test 2 passed\n\n")
    else:
        print("test 2 failed, see error message above\n\n")

    if test_03():
        print("test 3 passed\n\n")
    else:
        print("test 3 failed, see error message above\n\n")

    if test_04():
        print("test 4 passed\n\n")
    else:
        print("test 4 failed, see error message above\n\n")

    if test_05():
        print("test 5 passed\n\n")
    else:
        print("test 5 failed, see error message above\n\n")


# if __name__ == '__main__':
#     run_tests()


