def backwards(s):
    """DOCSTIRING"""
    if len(s) == 0:
        return ""
    else:
        return backwards(s[1:]) + s[0]

print(backwards("Hi there!"))
