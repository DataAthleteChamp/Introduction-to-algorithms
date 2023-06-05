from json.encoder import INFINITY


def Hamming(s, t):
    s = s.lower()
    t = t.lower()
    ans = 0
    for i in range(0,len(s)):
        if s[i] != t[i]:
            ans+=1
    
    return ans

def ModifiedHamming(s, t):
    s = s.lower()
    t = t.lower()
    ans=0
    mx = ["qwsz","vghn","xdfv","serfcx","wsdr","drtgvc","ftyhbv","gyujnb","ujko","huikmn","jiolm","kop","njk","bhjm","iklp","ol","asw","edft","awedxz","rfgy","yhji","cfgb","qase","zsdc","tghu","asx"]
    for i in range(0,len(s)):
        if (s[i] != t[i]):
            if (mx[ord(s[i])-ord('a')].find(t[i]) != -1):
                ans += 1
            else:
                ans += 2
    return ans

dicti = ["a", "about", "all", "also", "and", "as", "at", "be", "because", "but", "by", "can", "come", "could", "day", "do", "even", "find", "first", "for", "from", "get", "give", "go", "have", "he", "her", "here", "him", "his", "how", "I", "if", "in", "into", "it", "its", "just", "know", "like", "look", "make", "man", "many", "me", "more", "my", "new", "no", "not", "now", "of", "on", "one", "only", "or", "other", "our", "out", "people", "say", "see", "she", "so", "some", "take", "tell", "than", "that", "the", "their", "them", "then", "there", "these", "they", "thing", "think", "this", "those", "time", "to", "two", "up", "use", "very", "want", "way", "we", "well", "what", "when", "which", "who", "will", "with", "would", "year", "you", "your"]

def FindInDict(s):
    s.lower()
    lista = []
    for i in range(0,len(dicti)):
        mn = s
        wk = dicti[i].lower()
        if len(mn) > len(wk):
            mn, wk = wk, mn
        best_temp = INFINITY
        diff = len(wk)-len(mn)
        for j in range(0,diff+1):
            best_temp = min(best_temp, Hamming(mn,wk)+diff)
        lista.append((best_temp,dicti[i]))
    lista.sort()
    if lista[0][0] == 0:
        return "OK"
    else:
        ans = []
        for i in range(0, min(len(lista),3)):
            ans.append(lista[i][1])
        return ans

print(Hamming("abccba", "accbba"))
print(ModifiedHamming("abccba", "avbbva"))
print(FindInDict("fdsagfd"))