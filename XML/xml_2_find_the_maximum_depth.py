import xml.etree.ElementTree as etree
# this variable will hold the deepest level found anywhere in the tree
# it needs to be declared outside the function so it can be updated from inside it
maxdepth = 0
# tell python we want to modify the global maxdepth, not create a new local one
def depth(elem, level):
    global maxdepth
    
    # we've gone one level deeper than the call before
    level += 1

    # if this is the deepest we've seen so far, update maxdepth
    if level >= maxdepth:
        maxdepth = level

    # go through every direct child of the current element
    for child in elem:
        # call depth again on each child, one level deeper than this one
        depth(child, level)

if __name__ == '__main__':
    # read the first line of input and convert it to an integer
    # this tells us how many lines the xml document has
    n = int(input())
    # start with an empty string, we will build the full xml text here
    xml = ""
    # loop n times, once for each line of the xml document
    for i in range(n):
        # read one line of input and add it to xml, plus a newline character
        # the newline is needed because input() strips it off automatically
        xml =  xml + input() + "\n"
    # parse the xml string into a tree structure
    # etree.fromstring(xml) turns the text into an Element object
    # etree.ElementTree(...) wraps that element into a full tree
    tree = etree.ElementTree(etree.fromstring(xml))
    # call our depth function starting at the root of the tree
    # we pass -1 as the starting level, so the root itself becomes level 0
    depth(tree.getroot(), -1)
    # print the final answer, which depth() has stored in maxdepth
    print(maxdepth)
