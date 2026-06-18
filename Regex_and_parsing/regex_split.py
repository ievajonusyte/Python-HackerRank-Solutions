'''
The task is to split a string on commas and dots. 
You just need to fill in the regex pattern.
'''



regex_pattern = r"[,.]"	

import re
print("\n".join(re.split(regex_pattern, input())))
