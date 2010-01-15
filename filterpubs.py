import re,sys

pub_start = re.compile('^@\w*{(.*?),')

#Read the publications data
inpub = False
currpub = ''
pubcode = ''
pubs = {}
for line in open('papers.bib','r').readlines():

    for match in pub_start.findall(line):
        pubcode = match
        inpub = True

    currpub += line

    if line.strip() == '}':
        inpub = False
        pubs[pubcode] = currpub
        currpub = ''


for line in open(sys.argv[1],'r'):
    print pubs[line.strip()]
