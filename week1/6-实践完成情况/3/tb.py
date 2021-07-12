def lcs(series1, series2):
    s1 = ""
    s2 = ""

    if len(series1) < len(series2):
        s1 = series1
        s2 = series2
    else:
        s1 = series2
        s2 = series1
    Lcs = []
    for i in s1:
        for j in s2:
            if i == j:
                Lcs.append(i)
                break

    return Lcs

if __name__ == '__main__':
    str1 = "12345678"
    str2 = "45679"
    LCS = lcs(str1, str2)
    print(LCS)