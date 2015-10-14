from datetime import timedelta # this is required for delayed response time checking

# checks for delayed responses or HTTP response error codes on the website
# if an error or delay is found => prints human readable error message
# if no error or delay is found => prints nothing
# theLink => URL of the home page we are fuzzing
def checkHTTPResponses(theLink):
    r = requests.get(theLink)
    reqhtml =  html.fromstring(r.text)
    ahreflist = reqhtml.xpath("//a/@href")
    for x in ahreflist:
        response = requests.get(url + line.strip() + ext)
        if response.status_code == 408 or response.elapsed.seconds >= 5:
            # response took longer than 5 seconds or timed out
            print("Delayed response: " + url + line.strip() + ext)
        else if response.status_code == 404:
            # response told us that the page does not exist
            print("Page not found: " + url + line.strip() + ext)
        else if response.status_code == 400:
            # response told us it was a bad request
            print("Bad request: " + url + line.strip() + ext)
        else if response.status_code == 401 or response.status_code == 403:
            # response told us we are unauthorized to access the page
            print("Unauthorized access: " + url + line.strip() + ext)
        else if response.status_code >= 500:
            # response told us there was a server error
            print("Server error: " + url + line.strip() + ext)
