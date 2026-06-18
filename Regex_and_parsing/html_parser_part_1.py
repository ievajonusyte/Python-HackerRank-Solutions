from html.parser import HTMLParser
'''
Task:
You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.

Format your results in the following way:
Start : Tag1
End   : Tag1
Start : Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Start : Tag3
-> Attribute3[0] > None
Empty : Tag4
-> Attribute4[0] > Attribute_value4[0]
End   : Tag3
End   : Tag2

The -> symbol indicates that the tag contains an attribute.
The > symbol acts as a separator between the attribute name and value.
If an HTML tag has no attribute then simply print the name of the tag.
If an attribute has no value then simply print the attribute name with None as value.

Note: Do not detect any HTML tag, attribute or attribute value inside
HTML comment tags (<!-- Comments -->). Comments can be multiline.

Input Format:
The first line contains integer N, the number of lines in a HTML code snippet.
The next N lines contain HTML code.

Constraints:
0 < N < 100

Output Format:
Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.
'''

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs): # Print the opening tag name
        print("Start :", tag) # Print each attribute and its value
        for attr_name, attr_value in attrs:
            if attr_value is None:
                print("-> {} > None".format(attr_name))
            else:
                print("-> {} > {}".format(attr_name, attr_value))

    def handle_endtag(self, tag): # Print the closing tag name
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs): 
        print("Empty :", tag) # Print each attribute and its value
        for attr_name, attr_value in attrs:
            if attr_value is None:
                print("-> {} > None".format(attr_name))
            else:
                print("-> {} > {}".format(attr_name, attr_value))


n = int(input()) # reads the first line of input, the number N telling us how many lines of HTML are coming
html_lines = [] # creates an empty list that will hold the HTML lines one by one
for _ in range(n): 
    html_lines.append(input()) # loops exactly N times, and each iteration reads one line of HTML and adds it to the list

parser = MyHTMLParser() # MyHTMLParser inherits from Python's built-in HTMLParser, so You get an object that already knows how to scan HTML
parser.feed("\n".join(html_lines)) # joins all the list items back into one big string separated by newlines, and feeds it to the parser as if it were one continuous HTML document
