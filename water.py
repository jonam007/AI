def pour(ja, jb):
    max1, max2, final = 5, 7, 4
    print("%d\t%d" % (ja, jb))  

    if jb == final:
        return
    elif jb == max2:
        pour(0, ja)
    elif ja != 0 and jb == 0:
        pour(0, jb)
    elif ja == final:
        pour(ja, 0)
    elif ja < max1:
        pour(max1, jb)
    elif jb < (max2 - jb):  # Changed to (max2 - ja) for correct subtraction
        pour(0, (ja + jb))
    else:
        pour(ja - (max2 - jb), (max2 - jb) + jb)

print("A \t B")
pour(0,0)