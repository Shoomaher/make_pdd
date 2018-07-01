import os

COMMAND = "pdfunite"

#pdfs must be in "pdfs" dit!
for i in range(34):
    COMMAND += " {}.pdf".format(i+1)

COMMAND += " pdd.pdf"

print(COMMAND)

os.system(COMMAND)
