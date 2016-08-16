#
# Problem: given a string, compress repeating characters into <Character><Count> format.
#

def stringCompression(target):
    result = ""
    curChar = ""
    count = 0

    for char in target:

        if char != curChar:
            if count != 0:
                result += str(count)
            curChar = char
            result += char
            count = 1
        else:
            count += 1

    result += str(count)
    print result


string = "ABCCDDDEE"
stringCompression(string)