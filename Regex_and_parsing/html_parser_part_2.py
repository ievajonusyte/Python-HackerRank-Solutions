from html.parser import HTMLParser

'''
Given N lines of HTML, detect and print:
- single-line comments: >>> Single-line Comment followed by the comment text
- multi-line comments: >>> Multi-line Comment followed by each line directly
- data (text content): >>> Data followed by the data text
Skip data that is just a newline character.
'''

class MyHTMLParser(HTMLParser): # creates your own parser by inheriting from HTMLParser, you get all its HTML-reading ability and just define what to do when it finds things

    def handle_comment(self, data): # HTMLParser automatically calls this method when it finds a commen
        lines = data.split('\n') # Splits the comment text on newlines
        if len(lines) == 1: # Checks if there is only one line meaning it's a single line comment
            print('>>> Single-line Comment')
            print(data) # Prints the label and then the comment text
        else:
            print('>>> Multi-line Comment')
            for line in lines:
                print(line) # Prints the label, then loops through each line of the comment and prints it

    def handle_data(self, data): # HTMLParser automatically calls this when it finds text content between tags
        if data != '\n': # Skips pure newline data 
            print('>>> Data')
            print(data) # Prints the label and then the text content


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n' 
    # Reads N lines one by one. rstrip() removes trailing spaces from each line, then \n is added back so the HTML structure stays intact. All lines are joined into one big string.

parser = MyHTMLParser()
parser.feed(html)
parser.close()
# Creates the parser, feeds it the full HTML string so it starts reading and calling your methods, then close() flushes any remaining unprocessed data
