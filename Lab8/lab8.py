###################################################
# APS106 - Winter 2022 - Lab 8 - Corner Detection #
###################################################

from lab8_image_utils import display_image, image_to_pixels
from operator import itemgetter


################################################
# PART 1 - RGB to Grayscale Conversion         #
################################################


def rgb_to_grayscale(rgb_img):
    """
    (tuple) -> tuple

    Function converts an image of RGB pixels to grayscale.
    Input tuple is a nested tuple of RGB pixels.

    The intensity of a grayscale pixel is computed from the intensities of
    RGB pixels using the following equation

        grayscale intensity = 0.3 * R + 0.59 * G + 0.11 * B

    where R, G, and B are the intensities of the R, G, and B components of the
    RGB pixel. The grayscale intensity should be *rounded* to the nearest
    integer.
    """

    # Generate Empty List
    # loop through input indices
    # find the gray value of each sub-tuple
    # round and add to output, convert to tuple and return

    grayscale_values = []
    for i in range(len(rgb_img)):
        grayscale_value = 0.3 * rgb_img[i][0] + 0.59 * rgb_img[i][1] + 0.11 * rgb_img[i][2]
        grayscale_values.append(round(grayscale_value))
    return tuple(grayscale_values)


############################
# Part 2b - Dot Product    #
############################

def dot(x, y):
    """
    (tuple, tuple) -> float

    Performs a 1-dimensional dot product operation on the input vectors x
    and y.
    """
    # set initial value to zero
    # loop through inputs with indices

    dot_product = 0
    for i in range(len(x)):
        dot_product += x[i] * y[i]
    return dot_product


######################################
# Part 2c - Extract Image Segment    #
######################################

def extract_image_segment(img, width, height, centre_coordinate, N):
    """
    (tuple, int, int, tuple, int) -> tuple

    Extracts a 2-dimensional NxN segment of a image centred around
    a given coordinate. The segment is returned as a tuple of pixels from the
    image.

    img is a tuple of grayscale pixel values
    width is the width of the image
    height is the height of the image
    centre_coordinate is a two-element tuple defining a pixel coordinate
    N is the height and width of the segment to extract from the image

    """
    # Reshape the 1D array into a 2D one
    # 1) Create an empty 2D array
    two_d_array = []
    for i in range(height):
        two_d_array.append([0] * width)
    # print(two_d_array)

    # 2) Now, fill in the 2D array
    count = 0
    for i in range(height):
        for j in range(width):
            two_d_array[i][j] = img[count]
            count += 1
    # print(two_d_array)

    # 3) Create ranges for the x and y values, for extracting the segment.
    x = centre_coordinate[0]
    y = centre_coordinate[1]
    x_range = list(range(x - ((N - 1) // 2), x + ((N + 1) // 2)))  # These were never the problem
    y_range = list(range(y - ((N - 1) // 2), y + ((N + 1) // 2)))  # fx and fy were the issue beforehand

    # 4) Create empty segment array
    extracted_segment = []
    for i in range(N):
        extracted_segment.append([0] * N)

    # 5) Define some change of coordinate factors
    fx = x - (N - 1) // 2  # The second term used to be 1, worked for 3x3 but nothing else
    fy = y - (N - 1) // 2  # How did I come up with it? Shear chance

    # 6) Extract the segment
    for i in x_range:
        for j in y_range:
            extracted_segment[j - fy][i - fx] = two_d_array[j][i]

    # 7) Convert into a 1D tuple
    output_tuple = []
    for sublist in extracted_segment:
        for item in sublist:
            output_tuple.append(item)
    return tuple(output_tuple)


######################################
# Part 2d - Kernel Filtering         #
######################################

def kernel_filter(img, width, height, kernel):
    """
    (tuple, int, int, tuple) -> tuple

    Apply the kernel filter defined within the two-dimensional tuple kernel to
    image defined by the pixels in img and its width and height.

    img is a 1 dimensional tuple of grayscale pixels
    width is the width of the image
    height is the height of the image
    kernel is a 2 dimensional tuple defining a NxN filter kernel, n must be an odd integer

    The function returns the tuple of pixels from the filtered image
    """

    # 1) Create ranges to use to loop through the image and process each pixel
    n = len(kernel[0])
    extract_x_range = list(range((n - 1) // 2, width - (n - 1) // 2))
    extract_y_range = list(range((n - 1) // 2, height - (n - 1) // 2))
    # print(extract_x_range)
    # print(extract_y_range)

    # 2) Create empty 2D array for filtered image
    processed_image = []
    for i in range(height):
        processed_image.append([0] * width)
    # print(processed_image)

    # 3) Convert the kernel into a 1D array
    kernel_1d = []
    for sublist in kernel:
        for item in sublist:
            kernel_1d.append(item)
    kernel_1d = tuple(kernel_1d)

    # 4) Process each pixel, add to the result
    for i in extract_x_range:
        for j in extract_y_range:
            extract = extract_image_segment(img, width, height, (i, j), n)
            result = dot(extract, kernel_1d)
            processed_image[j][i] = int(result)
    # print(processed_image)

    # 5) Convert the processed image into a 1D tuple
    output_processed_image = []
    for sublist in processed_image:
        for item in sublist:
            output_processed_image.append(item)

    return tuple(output_processed_image)


# picture = [ 4, 87, 233, 245, 227, 209, 190,
#             2, 59, 235, 246, 229, 219, 200,
#            17, 99, 230, 220, 211, 210, 201,
#            46, 58, 196, 165, 201, 179, 150,
#            82, 63,  41, 169, 190, 188, 145,
#            99, 55,  54,  55,  74,  23,  12,
#            45, 55,  56,  45, 155, 145, 156]
#
# gaussian_blur = ((1/16, 1/8, 1/16),
#                  ( 1/8, 1/4,  1/8),
#                  (1/16, 1/8, 1/16))
#
# horizontal_sobel = ((-1, -2, -1),
#                      (0, 0, 0),
#                      (1, 2, 1))
#
#
# print(kernel_filter(picture, 7, 7, gaussian_blur))  # Passed
# print(kernel_filter(picture, 7, 7, horizontal_sobel))  # Passed

###############################
# PART 3 - Harris Corners     #
###############################

def harris_corner_strength(Ix, Iy):
    """
    (tuple, tuple) -> float

    Computes the Harris response of a pixel using
    the 3x3 windows of x and y gradients contained
    within Ix and Iy respectively.

    Ix and Iy are  lists each containing 9 integer elements each.

    """

    # calculate the gradients
    Ixx = [0] * 9
    Iyy = [0] * 9
    Ixy = [0] * 9

    for i in range(len(Ix)):
        Ixx[i] = (Ix[i] / (4 * 255)) ** 2
        Iyy[i] = (Iy[i] / (4 * 255)) ** 2
        Ixy[i] = (Ix[i] / (4 * 255) * Iy[i] / (4 * 255))

    # sum  the gradients
    Sxx = sum(Ixx)
    Syy = sum(Iyy)
    Sxy = sum(Ixy)

    # calculate the determinant and trace
    det = Sxx * Syy - Sxy ** 2
    trace = Sxx + Syy

    # calculate the corner strength
    k = 0.03
    r = det - k * trace ** 2

    return r


def harris_corners(img, width, height, threshold):
    """
    (tuple, int, int, float) -> tuple

    Computes the corner strength of each pixel within an image
    and returns a tuple of potential corner locations. Each element in the
    returned tuple is a two-element tuple containing an x- and y-coordinate.
    The coordinates in the tuple are sorted from highest to lowest corner
    strength.
    """

    # perform vertical edge detection
    vertical_edge_kernel = ((-1, 0, 1),
                            (-2, 0, 2),
                            (-1, 0, 1))

    Ix = kernel_filter(img, width, height, vertical_edge_kernel)

    # perform horizontal edge detection
    horizontal_edge_kernel = ((-1, -2, -1),
                              (0, 0, 0),
                              (1, 2, 1))
    Iy = kernel_filter(img, width, height, horizontal_edge_kernel)

    # compute corner scores and identify potential corners
    border_sz = 1
    corners = []
    for i_y in range(border_sz, height - border_sz):
        for i_x in range(border_sz, width - border_sz):
            Ix_window = extract_image_segment(Ix, width, height, (i_x, i_y), 3)
            Iy_window = extract_image_segment(Iy, width, height, (i_x, i_y), 3)
            corner_strength = harris_corner_strength(Ix_window, Iy_window)
            if corner_strength > threshold:
                # print(corner_strength)
                corners.append([corner_strength, (i_x, i_y)])

    # sort
    corners.sort(key=itemgetter(0), reverse=True)
    corner_locations = []
    for i in range(len(corners)):
        corner_locations.append(corners[i][1])

    return tuple(corner_locations)


###################################
# PART 4 - Non-maxima Suppression #
###################################

def non_maxima_suppression(corners, min_distance):
    """
    (tuple, float) -> tuple

    Filters any corners that are within a region with a stronger corner.
    Returns a tuple of corner coordinates that are at least min_distance away from
    any other stronger corner.

    corners is a tuple of two-element coordinate tuples representing potential
        corners as identified by the Harris Corners Algorithm. The corners
        are sorted from strongest to weakest.

    min_distance is a float specifying the minimum distance between any
        two corners returned by this function
    """
    # 1) Follow the lab worksheet algorithm
    unsuppressed = [corners[0]]
    corners = list(corners)
    corners.pop(0)
    for corner in corners:
        for another_corner in unsuppressed:
            # print('first corner: ', corner)
            # print('second corner: ', another_corner)
            list_of_distances = []
            distance = ((corner[0] - another_corner[0]) ** 2 + (corner[1] - another_corner[1]) ** 2) ** (1 / 2)
            # print('distance: ', distance)
            list_of_distances.append(distance)
        if min(list_of_distances) >= min_distance:
            unsuppressed.append(corner)
        # print(list_of_distances)
        # print('unsuppressed: ', unsuppressed)

    return tuple(unsuppressed)

