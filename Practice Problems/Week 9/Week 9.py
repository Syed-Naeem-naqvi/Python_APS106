# # Q1
# # Open file for reading
# # Method 1: loop through file
# f = open('grades.txt', 'r')
#
# # Create file for writing
# f2 = open('grades_copy.txt', 'w')
#
# # Go through reading file, read line by line and add
# # to the writing file
# for line in f:
#     f2.write(line)
#
# # Close both files when done
# f.close()
# f2.close()
#
# # Method 2: .read()
# f = open('grades.txt', 'r')
# f3 = open('grades2.txt', 'w')
# file_contents = f.read()
# f3.write(file_contents)
# f.close()
# f3.close()
#
# # Method 3: .readlines()
# f = open('grades.txt', 'r')
# f4 = open('grades3.txt', 'w')
# content_list = f.readlines()
# # print(content_list)
# for item in content_list:
#     f4.write(item)
#
# f.close()
# f4.close()
#
# # # Method 4
# # f = open('grades.txt', 'r')
# # f5 = open('grades4.txt', 'w')
# # contents = ''
# # line = f.readline()
# # contents = contents + line
# # while line != ' ':
# #     contents += f.readline()
# # print(contents)
# # f.close()
# # f5.close()
#
# # Q2
#
# f = open('onetwo.txt', 'r')
# contents = f.readlines()
# # print(contents)
# string_form = ''
# for i in contents:
#     string_form += i.replace('\n',' ')
# print(string_form)

# Q3a

#
# def make_copy(file=None):
#     data = open(file, 'r')
#     lines = data.read()
#     file_copy = open('copy','w')
#     file_copy.write(lines)
#     data.close()
#     file_copy.close()
#
#
# make_copy('test1.txt')

# Q5 Correct


def convert_to_binary(x):
    """
    Convert some {XEZ+} to a base 2 number
    """
    max_value = 1
    num_list = [max_value]
    while max_value*2 <= x:
        max_value *= 2
        num_list.append(max_value)

    num_list = num_list[::-1]
    out = ''
    for i in num_list:
        if (x - i ) >= 0:
            out += str(1)
            x = x - i
        else:
            out += str(0)
    return out


print(convert_to_binary(999))

