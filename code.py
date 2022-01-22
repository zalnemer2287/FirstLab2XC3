<<<<<<< Updated upstream
def are_valid_groups (studentNums, groups):
    for x in groups:
        for y in x:
            if not (y in studentNums):
                return False
    return True
=======
def are_valid_groups(student_nums, groups):
    for i in student_nums:
        found = False
        for j in groups:
            for k in j:
                if (i == k):
                    found = True
        if (found):
            pass
        else:
            return False

    return True
>>>>>>> Stashed changes
