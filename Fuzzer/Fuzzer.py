import requests
import textwrap
import operator
from lxml import html
from urlparse import urlparse
from datetime import timedelta

#test purposes
def links():
    link = raw_input('Insert Link Here: ')
    r = requests.get(link)
    reqhtml =  html.fromstring(r.text)
    ahreflist = reqhtml.xpath("//a/@href")
    for x in ahreflist:
        print (link + x)


#test purposes
def parse():
    link = raw_input('Insert Link Here: ')
    r = requests.get(link)
    reqhtml =  html.fromstring(r.text)
    ahreflist = reqhtml.xpath("//a/@href")
    for x in ahreflist:
        result = urlparse(x)
        print (result)


#test purposes
def cookies():
    session = requests.session()
    link = raw_input('Insert Link To Look For Cookies: ')
    session.get(link)
    print('Cookies: ', requests.utils.dict_from_cookiejar(session.cookies))


def getLinksAuth():
    link = raw_input('Insert Link Here: ')
    r = requests.get(link, auth=('admin', 'password'))
    reqhtml =  html.fromstring(r.text)
    ahreflist = reqhtml.xpath("//a/@href")
    for x in ahreflist:
        print (link + x)


def getLinks(theLink):
    r = requests.get(theLink)
    reqhtml =  html.fromstring(r.text)
    ahreflist = reqhtml.xpath("//a/@href")
    for x in ahreflist:
        print (theLink + x)


def getInputs(theLink):
    r = requests.get(theLink)
    reqhtml =  html.fromstring(r.text)
    inputnamelist = reqhtml.xpath("//input/@type")
    for x in inputnamelist:
        print ('Type: ' + x)
    return inputnamelist


def parseURL(theLink):
    r = requests.get(theLink)
    reqhtml =  html.fromstring(r.text)
    ahreflist = reqhtml.xpath("//a/@href")
    for x in ahreflist:
        result = urlparse(x)
        print (result)


def getCookies(theLink):
    session = requests.session()
    session.get(theLink)
    print('Cookies: ', requests.utils.dict_from_cookiejar(session.cookies))


def custAuth(name):
    session = requests.session()
    if operator.eq(name, 'dvwa'):
        # Fill in your details here to be posted to the login form.
        payload = {
            'username': 'admin',
            'password': 'password',
            'Login': 'Login'
        }

        # Use 'with' to ensure the session context is closed after use.

        p = session.post('http://127.0.0.1/dvwa/login.php', data=payload)

        return session

    if operator.eq(name, 'bodgeit'):
        # Fill in your details here to be posted to the login form.
        payload = {
            'username': 'test@thebodgeitstore.com',
            'password': 'password',
            'submit': 'Login'
        }

        # Use 'with' to ensure the session context is closed after use.

        p = session.post('http://127.0.0.1:8080/bodgeit/login.jsp', data=payload)

        return session



def guessPages(txtFile, url):
    extensions = ['.php', '.jsp', '.html']
    with open(txtFile, 'r') as f:
        for line in f:
            for ext in extensions:
                response = requests.get(url + line.strip() + ext)
                if response.status_code < 400:
                    print(url + line.strip() + ext)

def senseData(theLink, vectors):
    print ('Sensitive Data')
    r = requests.get(theLink)
    reqhtml =  html.fromstring(r.text)
    ahreflist = reqhtml.xpath("//a/@href")
    with open(vectors, 'r') as f:
        for line in f:
            for x in ahreflist:
                #result = urlparse(x)
                content = requests.get(theLink+x)
                if (content.text).find(line) == -1:
                    print (line + ' is not in location ' + x)
                # print(content.text)
                print('Potential security concern for ' + line + ' in ' + theLink + x)

def lackSanitize(theLink, escape_chars):
    print ('Discovering Sanitization:')

    if theLink == 'http://127.0.0.1/dvwa/login.php':
        custAuth('dvwa')

    if theLink == 'http://127.0.0.1:8080/bodgeit/login.jsp':
        custAuth('bodgeit')

    r = getInputs(theLink)
    size = len(r) #gets the size of the amount of inputs based on myLink.
    with open(escape_chars, 'r') as f:
        for line in f:
#I know these multiple if-statements arent the best but I was running into problems
# I couldnt get around related to the payload variable, on DVWA the number of input
# forms per page doesnt surpass 3 which is why I hardcoded in the if statements.
# So what happens is all the escape characters get entered into all available input pages on the page,
# and are then submitted if possible. The issue is that depending on the page, the forms have different
# submit values depending on the page. For example: this url has  (http://127.0.0.1/dvwa/vulnerabilities/brute/)
# has a submit value of 'Login', while this url (http://127.0.0.1/dvwa/vulnerabilities/xss_s/) has a submit value
# of 'Sign Guestbook'. So I am not too sure how to go about getting those values and plugging them into the payload
# for that page.
            if size == 2:
                payload = {
                r[0]: f,
                r[1]: '*VARIABLE*',
            }

            if size == 3:
                payload = {
                r[0]: f,
                r[1]: f,
                r[2]: '*VARIABLE*'
            }
                with requests.Session() as s:
                    p = s.post(theLink, data=payload)
                    text = p.text
                    if '&lt' not in text:
                        print '< is not sanitized.'

                    if '&gt' not in text:
                        print '> is not sanitized.'

                    if '&amp' not in text:
                        print '& is not sanitized.'

                    if '&quot' not in text:
                        print " ' is not sanitized."

                    if '&#39' not in text:
                        print '" is not sanitized.'




# checks for delayed responses or HTTP response error codes on the website
# if an error or delay is found => prints human readable error message
# if no error or delay is found => prints nothing
# theLink => URL of the home page we are fuzzing

def checkHTTPResponses(theLink):
    print ('Checking HTTP Responses: ')
    print ('Checking Now...')
    #r = requests.get(theLink)
    #reqhtml =  html.fromstring(r.text)
    #ahreflist = reqhtml.xpath("//a/@href")
    #for x in ahreflist:
        #response = requests.get(theLink + line.strip() + ext)
        #if response.status_code == 408 or response.elapsed.seconds >= 5:
            # response took longer than 5 seconds or timed out
        #    print("Delayed response: " + theLink + line.strip() + ext)
        #elif response.status_code == 404:
            # response told us that the page does not exist
        #    print("Page not found: " + theLink + line.strip() + ext)
        #elif response.status_code == 400:
            # response told us it was a bad request
        #    print("Bad request: " + theLink + line.strip() + ext)
        #elif response.status_code == 401 or response.status_code == 403:
            # response told us we are unauthorized to access the page
        #    print("Unauthorized access: " + theLink + line.strip() + ext)
        #elif response.status_code >= 500:
            # response told us there was a server error
        #    print("Server error: " + theLink + line.strip() + ext)

def discover():
    print textwrap.dedent(
        """
fuzz [discover | test] url OPTIONS

COMMANDS:
  discover  Output a comprehensive, human-readable list of all discovered inputs to the system. Techniques include both crawling and guessing.
  test      Discover all inputs, then attempt a list of exploit vectors on those inputs. Report potential vulnerabilities.

OPTIONS:
  --custom-auth=string     Signal that the fuzzer should use hard-coded authentication for a specific application (e.g. dvwa). Optional.

  Discover options:
    --common-words=file    Newline-delimited file of common words to be used in page guessing and input guessing. Required.

  Test options:
    --vectors=file         Newline-delimited file of common exploits to vulnerabilities. Required.
    --sensitive=file       Newline-delimited file data that should never be leaked. It's assumed that this data is in the application's database (e.g. test data), but is not reported in any response. Required.
    --random=[true|false]  When off, try each input to each page systematically.  When on, choose a random page, then a random input field and test all vectors. Default: false.
    --slow=500             Number of milliseconds considered when a response is considered "slow". Default is 500 milliseconds
        """
    )
    link = raw_input('Please Enter Command: ')
    info = link.split()
    command = info[0].lower()
    url = info[1].lower()
    options = info[2:]
    for x in options:
        if operator.contains(x, '--custom-auth='):
            print ('Custom Authentication: ')
            custAuth(x.split('=')[1])
        if operator.contains(x, '--common-words='):
            print('Searching Common Words: ')
            guessPages(x.split('=')[1], url)
    if operator.eq(command, 'discover'):
        #discover functionality
        print('Discovering Links: ')
        getLinks(url)
        print('Parse URLs: ')
        parseURL(url)
        print('Discovering Cookies: ')
        getCookies(url)
        print('Get Inputs: ')
        getInputs(url)
    else:
        #test functionality
        print ('Discovering All Inputs: ')
        getInputs(url)
        print ('Checking For Sensitive Data')
        for x in options:
            if operator.contains(x, '--vectors='):
                print('Looking For Potential Threats In Vectors: ')
                senseData(url, x.split('=')[1])
            if operator.contains(x, '--sensitive='):
                print('Looking For Potential Sensitive Information: ')
                senseData(url, x.split('=')[1])
        print ('Checking Forpul Sanitized Data: ')
        lackSanitize(url, '<')


discover()


# execfile('C:\\Users\\rnn7726\\PycharmProjects\\Fuzzer\\Fuzzer.py')





