#!/usr/bin/python3

# Examples derived from
# https://docs.python.org/3.7/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
# https://docs.python.org/3.7/library/csv.html#module-csv

import xml.etree.ElementTree as xml
import csv

tree = xml.parse('input.xml')
root = tree.getroot()

for c in root:
    print(c.tag, c.text)

with open('output.csv','w', newline='') as f:
    writer = csv.DictWriter(f, delimiter=',', quotechar='"', fieldnames=['tag','text'])
    writer.writeheader()
    for r in root:
        writer.writerow({'tag':c.tag, 'text':r.text})

