def solution(survey, choices): 
    score = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    for s,c in zip(survey, choices):
        c = c - 4
        if c < 0:
            score[s[0]] -= c
        elif c > 0 :
            score[s[1]] += c
    
    answer = ''
    test_type = [('R','T'),('C','F'),('J','M'),('A','N')]
    for type1, type2 in test_type:
        if score[type1] >= score[type2]:
            answer += type1
        else:
            answer += type2

    return answer