import os

BASIC_URL = "http://pdd.ua/"

def make_url(i):
    url = BASIC_URL + str(i)
    print(url)
    return url

def make_fname(i):
    fname = "pdfs/{}.pdf".format(i)
    return fname

def main():
    for i in range(34):
        try:
            os.system("wkhtmltopdf --print-media-type {} {}".format(make_url(i+1), make_fname(i+1)))
            # client.convertUrlToFile(make_url(i+1), '{}.pdf'.format(i+1))
        except OSError as err:
            # report the error
            sys.stderr.write('SystemError: {}\n'.format(err))
            raise

main()
