def convFrac2Text(frac):
    for i in frac:
      if i == "/":
          topeval = frac.split("/")[0]
          bottomeval = frac.split("/")[1]
          return "\\frac{%s}{%s}" % (topeval, bottomeval)
    return frac


def baseCaseTopBottom(top, bottom, middle, evaluating, basecase):    
    if len(top) > 1:
        topdata = top.split("=")
        topdata = topdata[0]
    else:
        topdata = top
    if len(bottom) > 1:
        bottomdata = bottom.split("=")
        bottomdata = bottomdata[0]
    else:
        bottomdata = bottom
    evaluating = evaluating.replace(topdata,str(basecase))
    middle = middle.replace(bottomdata, str(basecase))
    return evaluating, middle

def extractTop(top):
    if len(top) > 1:
        topdata = top.split("=")
        topdata = topdata[0]
        return topdata
    else:
        topdata = top
        return topdata

def baseCaseLast(top, randomVar, middle, evaluating):
    for element in middle:
        if element == top:
            middle = middle.replace(top, randomVar)
    for i in evaluating:
        if i == top:
            evaluating = evaluating.replace(top, randomVar)
    return middle, evaluating

