import extraction as e
import hypothesis as h
import sumh as s
import randomgen as r

extracted = []
extracted = s.summation("n", "j=1", "j", "n(n+1)/2", 1)
top = extracted[0].strip()
bottom = extracted[1].strip().strip()
middle = e.convFrac2Text(extracted[2]).strip()
evaluating = e.convFrac2Text(extracted[3]).strip()
basecase = extracted[4]