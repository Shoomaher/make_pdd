import os

COMMAND = "pdfunite"

#pdfs must be in "pdfs" dit!
os.chdir("pdfs")

for i in range(34):
    COMMAND += " {}.pdf".format(i+1)

COMMAND += " pdd.pdf"

os.system(COMMAND)
