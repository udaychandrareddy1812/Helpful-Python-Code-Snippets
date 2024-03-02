# this python code snippet break out from two for loops at once

found = False

for i in range(5):
    for j in range(5):
        if some_condition:
            found = True
            break
    if found:
        break
