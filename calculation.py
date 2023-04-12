def score_course(mid_score, overall_mid_weight, final_score, overall_final_weight, CO_mid_weight, CO_final_weight, quiz_score, overall_quiz_weight, CO_quiz_weight, contribution):
    score = 0
    for i in range(10):
        try:
            score += (mid_score*overall_mid_weight/100*CO_mid_weight[i]/100+final_score*overall_final_weight/100*CO_final_weight[i]/100+quiz_score*overall_quiz_weight/100*CO_quiz_weight[i]/100)/(contribution[i]/5)
        except ZeroDivisionError:
            score += 0
    return score

def score_subcourse(mid_score,overall_mid_weight, mid_weight, final_score, overall_final_weight, final_weight, quiz_score, overall_quiz_weight, quiz_weight, performance, overall_perform_weight, CO_perform_weight, AKHLAK):
    midScore = ((mid_score+AKHLAK)/2*overall_mid_weight/100*mid_weight/100)
    finalScore = ((final_score+AKHLAK)/2*overall_final_weight/100*final_weight/100)
    quizScore = ((quiz_score+AKHLAK)/2*overall_quiz_weight/100*quiz_weight/100)
    performanceScore = (performance*overall_perform_weight/100*CO_perform_weight/100)
    midContribution = overall_mid_weight/100*mid_weight/100
    finalContribution = overall_final_weight/100*final_weight/100
    quizContribution = overall_quiz_weight/100*quiz_weight/100
    performContribution = overall_perform_weight/100*CO_perform_weight/100
    score = (midScore+finalScore+quizScore+performanceScore)/(midContribution+finalContribution+quizContribution+performContribution)
    return score

def score_grouping(mid_score, overall_mid_weight, CO_mid_weight, final_score, overall_final_weight, CO_final_weight, quiz_score, overall_quiz_weight, CO_quiz_weight, performance, overall_perform_weight, CO_perform_weight, AKHLAK, contribution):
    score = 0
    for i in range(10):
        try:
            score += ((mid_score+AKHLAK)/2*overall_mid_weight/100*CO_mid_weight[i]/100+(final_score+AKHLAK)/2*overall_final_weight/100*CO_final_weight[i]/100+(quiz_score+AKHLAK)/2*overall_quiz_weight/100*CO_quiz_weight[i]/100+(performance)*overall_perform_weight/100*CO_perform_weight[i]/100)/(contribution[i]/5)
        except ZeroDivisionError:
            score += 0
    return score

def ipk(credit, course):
    total = 0
    for i in range(len(credit)):
        total += credit[i]*course[i]
    final = total/sum(credit)
    if final >= 86 and final <= 100:
        return "A"
    elif final >= 76 and final <= 85:
        return "AB"
    elif final >= 66 and final <= 75:
        return "B"
    elif final >= 61 and final <= 65:
        return "BC"
    elif final >= 56 and final <= 60:
        return "C"
    elif final >= 41 and final <= 55:
        return "D"
    else:
        return "E"
