def summation(top, bottom, middle, evaluating, basecase):
    consumed = []
    extracted = []
    for data in top:
        if data.isalpha():
            consumed.append(data)
    for data in bottom:
        if data.isalpha():
            consumed.append(data)   
    top = top.replace(" ", "")
    bottom = bottom.replace(" ", "")
    if len(top) > 1:
        #above = top.split("=")[1]
    if len(bottom) > 1:
        #below = bottom.split("=")[1]
    extracted.insert(0, top)
    extracted.insert(1, bottom)
    extracted.insert(2, middle)
    extracted.insert(3, evaluating)
    extracted.insert(4, basecase)
    return extracted