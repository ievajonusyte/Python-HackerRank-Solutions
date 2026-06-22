import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    '''
    Count the total number of attributes in the given node and all of its descendant nodes (recursively).
    
    Example: 
    <feed xml:lang='en'> has 1 attribute (lang)
    <title> has 0
    <subtitle lang='en'> has 1
    <link rel='alternate' type='text/html' href='...'> has 3
    <updated> has 0
    
    Total: 1 + 0 + 1 + 3 + 0 = 5
    '''
    # start with the number of attributes on this node itself
    count = len(node.attrib)

    # add the attribute counts from every child node, recursively
    for child in node:
        count += get_attr_number(child)

    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
