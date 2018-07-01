import pdfcrowd
import sys

BASIC_URL = "http://pdd.ua/"
LOGIN = "Shoomaher"
API_KEY = "41099c73cfffa6cedc0180c0029b889c"

def make_url(i):
    url = BASIC_URL + str(i)
    print(url)
    return url

def main():
    for i in range(34):
        try:
            # create the API client instance
            client = pdfcrowd.HtmlToPdfClient(LOGIN, API_KEY)

            # run the conversion and write the result to a file
            client.convertUrlToFile(make_url(i+1), '{}.pdf'.format(i+1))
        except pdfcrowd.Error as why:
            # report the error
            sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

            # handle the exception here or rethrow and handle it at a higher level
            raise

main()
