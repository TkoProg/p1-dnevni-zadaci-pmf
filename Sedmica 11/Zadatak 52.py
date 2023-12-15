def sad_datum(d,m,g):
    if d < 10:
        d = str(d)
        d = "0" + d
    if m < 10:
        m = str(m)
        m = "0" + m
    return f"Datum u SAD formatu je: {m}/{d}/{g}"


print(sad_datum(8, 1, 2003))
