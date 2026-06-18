"""
Given an HTML code snippet of N lines, detect and print all HTML tags, their attributes, and attribute values in order of occurrence.
Input: First line: integer N, the number of lines in the HTML snippet. Next N lines: the HTML code

Output: for each tag found (top to bottom):
- Print the tag name
- For each attribute of that tag, print:
--> attribute_name > attribute_value
Ignore any HTML tags, attributes, or values inside comment tags <!-- ... -->
Comments may be multiline. All attributes are guaranteed to have a value.
"""

from html.parser import HTMLParser # Importing the built-in HTML parser

class MyHTMLParser(HTMLParser): # Creating your own parser by inheriting from HTMLParser
  
    # Handling opening tags like <a href="x">
    def handle_starttag(self, tag, attrs):
        print(tag) 
        for attr_name, attr_value in attrs:
            print(f"-> {attr_name} > {attr_value}")
    # Handling self-closing tags like <br /> or <img />
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

n = int(input()) # Reading the input
html = "\n".join([input() for _ in range(n)])
parser = MyHTMLParser() # Running the parser
parser.feed(html) # Running the parser
