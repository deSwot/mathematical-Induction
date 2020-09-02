import random
import extraction as e
import hypothesis as h
import sumh as s
import randomgen as r
import calc as c

outFile= open("index.html","w")
outFile.write("""<!DOCTYPE html>
<html>
<head>
  <title>Proof by Abdullah Mujahid  </title>
   <link rel="stylesheet" href="styles.css">
</head>
<center><h1>Mathematical Induction Proof <br> Abdullah Mujahid </h1></center>
<hr class="style-three">
<body class="output">
<p>
""")


#below code snip sets up the question for execution
outFile.write("Question" )
module1 = """\[\sum_{%s}^%s %s = %s \]""" % (c.bottom, c.top, c.middle, c.evaluating)
outFile.write(module1)

#this piece of code snip checks the base case where n is 1 
temp = e.extractTop(c.top)
outFile.write("Base case {} = {}".format(temp, c.basecase))
extractionBaseCase, intermediate = e.baseCaseTopBottom(c.top, c.bottom, c.middle, c.evaluating, c.basecase)
module2 = """\[\sum_{%s}^%s %s = %s \]""" % (c.bottom, c.basecase, intermediate, extractionBaseCase)
outFile.write(module2)
outFile.write("\[" + intermediate  + "=" + extractionBaseCase + "\]<br>")

#this piece of code is responsible for the inductive hypotesis setup

consumed = []
randomVar = r.generator(consumed)
topdata = e.extractTop(c.top)
outFile.write("Assume for some {} = {}".format(randomVar, topdata))

lastEnd, evaluateP3 = e.baseCaseLast(c.top, randomVar, c.middle, c.evaluating)
module3 = """\[\sum_{%s}^%s %s = %s \]""" % (c.bottom, randomVar, lastEnd, evaluateP3)
outFile.write(module3)

#evaluate and store into the file
outFile.write("Show true for {} + 1".format(randomVar))
firstP, evaluateP4, midTier = h.inductiveHypothesis(c.top, randomVar, c.middle, c.evaluating)
module4 = """\[\sum_{%s}^{%s} %s = %s \]""" % (c.bottom, firstP, midTier, evaluateP4)
outFile.write(module4)



outFile.write("""</p>
  <script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML">
</script></body></html>""")

outFile.close()
