#COMPSCI 2XC3 Lab 1

def are_valid_groups(studentNumbers, Groups):
    array = []
    for studentNumber in studentNumbers:
        array.append(str(studentNumber))
    studentNumbers.clear()

    studentNumbers = array

    array2 = []
    array3 = []

    for i in range (0, len(Groups)):
        array3 = []

        for stdNum in Groups[i]:
            array3.append(str(stdNum))

        Groups[i] = array3

    foundNumbers = []
    for studentNumber in studentNumbers:
        found = False
        for group in Groups:
            for studentNumber2 in group:
                if (studentNumber == studentNumber2):
                    if studentNumber not in foundNumbers:
                        found = True
                        foundNumbers.append(studentNumber)
                    else:
                        found = False
        if (found):
            pass
        else:
            return False
    return True