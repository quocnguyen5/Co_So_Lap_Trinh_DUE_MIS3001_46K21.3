import re
n = input()


def KiemTraMatKhau(n):
    if len(n) < 6 or len(n) > 17:
        return False
    else:
        pass
    if not re.search("[a-z]", n):
        return False
    elif not re.search("\d", n):
        return False
    elif not re.search("[A-Z]", n):
        return False
    elif not re.search("[$#@]", n):
        return False

    return True


print(KiemTraMatKhau(n))
