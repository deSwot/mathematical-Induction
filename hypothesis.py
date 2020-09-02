
def inductiveHypothesis(top, Random_variable, middle, evaluating):
    temp = top
    top = top.replace(top, Random_variable + " + 1")
    middle = middle.replace(temp, "("+top+")")
    evaluating = evaluating.replace(temp, "("+top+")")
    return top, evaluating, middle