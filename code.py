def are_valid_groups (studentNums, groups):
    for x in groups:
        for y in x:
            if not (y in studentNums):
                return False
    return True
