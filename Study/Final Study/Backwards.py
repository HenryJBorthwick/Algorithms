def backwards(s):
    if len(s) == 0:
        return ""
    else:
        return backwards(s[1:]) + s[0]


print(backwards("Hi there!"))
# !ereht iH