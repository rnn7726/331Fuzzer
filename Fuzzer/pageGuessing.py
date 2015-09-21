# Attempts to access unlinked web pages given a text file
# containing one word per line. Will print out all URLs
# that actually exist from the common word file.
def guessPages(txtFile):
    extensions = ['.php', '.jsp', '.html']
    with open(txtFile) as f:
        for line in f:
            for ext in extensions:
                response = requests.get('http://127.0.0.1/' + line.strip() + ext)
                if (response.status_code < 400):
                    print('http://127.0.0.1/' + line.strip() + ext)
