##############################
# APS106 Winter 2022 - Lab 3 #
##############################
import math as m


def circle_overlap(circ1_centre_x, circ1_centre_y, circ1_radius,
                   circ2_centre_x, circ2_centre_y, circ2_radius):
    """
    (int, int, int, int, int, int) -> str

    Function determines whether two circles overlap. When circles
    overlap, the function checks for the following scenarios
        1. The two circles perfectly overlap
        2. The first circle is contained within the second
        3. The second circle is contained within the first
        4. The circle have overlapping area, but neither is completely
           contained within the other

    Function inputs represent x and y coordinates circle centres and their
    radii (see lab document)

    The function returns a string describing the overlap scenario

    >>> circle_overlap(0,1,3,6,4,1)
    'no overlap'

    >>> circle_overlap(0,1,3,0,1,3)
    'identical circles'

    >>> circle_overlap(1,1,10,6,7,1)
    'circle 2 is contained within circle 1'

    >>> circle_overlap(-1,-2,2,0,0,11)
    'circle 1 is contained within circle 2'

    >>> circle_overlap(1,-2,2,-4,0,5)
    'circles overlap'

    # Own tests
    >>> circle_overlap(-2,0,4,0,0,5)
    'circles overlap'
    >>> circle_overlap(0,0,10,0,0,12)
    'circle 1 is contained within circle 2'
    >>> circle_overlap(-2,4,4,4,-4,5)
    'no overlap'
    >>> circle_overlap(0,0,10,1,1,4)
    'circle 2 is contained within circle 1'
    >>> circle_overlap(0,0,4,0,0,4)
    'identical circles'
    >>> circle_overlap(-4,-4,2,-4,-4,10)
    'circle 1 is contained within circle 2'
    >>> circle_overlap(-6,-6,2,-6,-6,2)
    'identical circles'
    >>> circle_overlap(0,0,1,2,0,1)
    'no overlap'

    """
    # TODO your code here

    # Define the result string
    result = ''

    # Begin by calculating the distance between the two centers
    distance_between_centers = m.sqrt((circ2_centre_x - circ1_centre_x) ** 2 + (circ2_centre_y - circ1_centre_y) ** 2)

    # Next, define the distance 'a' as the distance between two centers plus
    a1 = circ1_radius + distance_between_centers
    a2 = circ2_radius + distance_between_centers

    if distance_between_centers == 0 and circ1_radius == circ2_radius:  # The easiest case to define
        result = 'identical circles'

    elif circ1_radius >= a2 and circ1_radius > circ2_radius:  # The next two use the previously defined a1 and a2 values
        result = 'circle 2 is contained within circle 1'

    elif circ2_radius >= a1 and circ2_radius > circ1_radius:
        result = 'circle 1 is contained within circle 2'

    elif distance_between_centers < circ1_radius + circ2_radius:
        result = 'circles overlap'

    elif distance_between_centers >= circ1_radius + circ2_radius:
        result = 'no overlap'

    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()


