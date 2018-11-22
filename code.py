
def isValid(stringOfSequence):
    for i in range(len(stringOfSequence)):
        if i % 4 == 1 and stringOfSequence[i] not in ["A", "T", "G", "C", "U"]:
            return False
        if i % 4 == 2 and stringOfSequence[i] not in ["r", "d", "m"]:
            return False
        if i % 4 == 3 and stringOfSequence[i] not in ["o", "s"]:
            return False
    return True

def lengthOfSequence(stringOfSequence):
    if not isValid(stringOfSequence):
        return -1
    return len(stringOfSequence) // 4 + 1 

def getProductTypes(stringOfSequence):
    if not isValid(stringOfSequence):
        return -1
    myset = set()
    for i in range(2, len(stringOfSequence), 4):
        myset.add(stringOfSequence[i])
        if stringOfSequence[i] == 'm':
            if stringOfSequence[i + 1] != 's':
                return -1
    if len(myset) == 1 and list(myset)[0] == 'r':
        return "vanilla RNA"
    if len(myset) == 2:
        if 'd' in myset and 'r' in myset:
            return "chimera"
        if 'm' in myset and 'r' in myset:
            return "mod RNA"
    return -1


if __name__ == "__main__":
    s1 = "-Uro-Uro-Aro-Gro-Cro-Uro-Aro-Aro-Cro-Gro-Gro-Uro-Ur"
    s2 = "-Uro-Uro-Aro-Gdo-Cdo-Tdo-Ado-Aro-Cro-Gro-Gro-Uro-Ur"
    s3 = "-Ums-Ums-Ams-Gro-Cro-Uro-Aro-Aro-Cro-Gro-Gms-Ums-Um"
    print(isValid(s1))
    print(isValid(s2))
    print(isValid(s3))
    print(lengthOfSequence(s1))
    print(getProductTypes(s2))


