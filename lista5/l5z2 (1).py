from json.encoder import INFINITY

polski = [9.90, 1.47, 4.36, 3.25, 8.77, 0.3, 1.42, 1.08, 8.21, 2.28, 3.51, 2.10, 2.80, 5.52, 8.60, 3.13, 0.14, 4.69, 4.98, 3.98, 2.5, 0.04, 4.65, 0.02, 3.76, 6.53]
angielski = [8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 5.03, 2.41, 6.75, 7.51, 1.93, 0.10, 5.99, 6.33, 9.05, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07]
niemiecki = [7.10, 1.89, 2.73, 5.08, 16.40, 1.66, 3.01, 4.58, 6.55, 0,27, 1.42, 3.44, 2.53, 9.78, 3.03, 0.67, 0.02, 7.00, 7.58, 6.15, 5.17, 0.85, 1.92, 0.03, 0.04, 1.13]

samo = "aeiouy"
pol_samo = 41.74
ang_samo = 40.08
nie_samo = 38.25

def Analyse(s):
    s = s.lower()
    dlg = len(s)
    wystepowanie = [0] * 26
    for i in range(0, dlg):
        diff = ord(s[i])-ord('a')
        if diff < 0 or diff >= 26:
            continue
        wystepowanie[diff] += 1
    wspP = wspA = wspN = 0
    for i in range(0,25):
        proc = wystepowanie[i]/100.0
        wspP += proc - polski[i]
        wspA += proc - angielski[i]
        wspN += proc - niemiecki[i]

    wspP = abs(wspP)
    wspA = abs(wspA)
    wspN = abs(wspN)

    if wspP <= wspA and wspP <= wspN:
        return "polski"
    elif wspA <= wspP and wspA <= wspN:
        return "angielski"
    elif wspN <= wspP and wspN <= wspA:
        return "niemiecki"

def ModifiedAnalyse(s):
    s = s.lower()
    dlg = len(s)
    wystepowanie = 0
    for i in range(0, dlg):
        diff = ord(s[i])-ord('a')
        if diff < 0 or diff >= 26:
            continue
        if samo.find(s[i]) != -1:
            wystepowanie += 1

    wspP = abs(wystepowanie/dlg - pol_samo)
    wspA = abs(wystepowanie/dlg - ang_samo)
    wspN = abs(wystepowanie/dlg - nie_samo)

    if wspP <= wspA and wspP <= wspN:
        return "polski"
    elif wspA <= wspP and wspA <= wspN:
        return "angielski"
    elif wspN <= wspP and wspN <= wspA:
        return "niemiecki"

s = "sadflhjasdfhhfdsjkadfsh"
print(Analyse(s))
print(ModifiedAnalyse(s))