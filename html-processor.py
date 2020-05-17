#Created by Alexandra Paramytha (Π2017001)

import re

#Replacement Function
def replacement(matchobj):
    if matchobj.group(0) == '&amp;': return '&'
    if matchobj.group(0) == '&gt;': return '>'
    if matchobj.group(0) == '&lt;': return '<'
    if matchobj.group(0) == '&nbsp;': return ' '

#Opens and stores the testpage.txt in testpage
testpage = open("testpage.txt",'r', encoding="utf8").read()
#Creates an output file
output = open("output.txt", 'w', encoding="utf8")


#Task 1 in assignment
output.write("Task 1\n-------------------------------------------\n")
reTitle = re.compile(r'<title>(.+)</title>')
for m in reTitle.finditer(testpage):
    output.write(m.group(1))

output.write("\n\n============================================================\n\n")


#Task 2 in assignment
output.write("Task 2\n-------------------------------------------\n")
noCommentRexp = re.sub('<!--.+-->', '', testpage)
output.write(noCommentRexp)
output.write("\n\n============================================================\n\n")


#Task 3 in assignment
output.write("Task 3\n-------------------------------------------\n")
noScriptOrStyleRexp = re.sub('(<script.*?>.*?</script>)|(<style.*?>.*?</style>)', '', testpage, flags=re.DOTALL)
output.write(noScriptOrStyleRexp)
output.write("\n\n============================================================\n\n")


#Task 4 in assignment
output.write("Task 4\n-------------------------------------------\n")
reLinks = re.compile(r'<a(.*?href="(.+?)".*?)?>(.*)?</a>')
for m in reLinks.finditer(testpage):
    output.write(m.group(2))
    output.write(m.group(3))
output.write("\n\n============================================================\n\n")


#Task 5 in assignment
output.write("Task 5\n-------------------------------------------\n")
tagRexp = re.compile('<.+?>.*?</.+?>')
noStartTagRexp = re.sub('<.+?>', '', testpage, flags=re.DOTALL)
noTagRexp = re.sub('</.+?>', '', noStartTagRexp, flags=re.DOTALL)
output.write(noTagRexp)
output.write("\n\n============================================================\n\n")


#Task 6 in assignment
#The following converts &amp;, &gt;, &lt;, &nbsp;
#into &, >, <, [space] accordingly
output.write("Task 6\n-------------------------------------------\n")
convertedRexp = re.sub(r'&.+;', replacement , testpage)
output.write(convertedRexp)
output.write("\n\n============================================================\n\n")


output.close()
