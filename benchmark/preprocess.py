#!/usr/bin/python3

import sys
import xml.etree.ElementTree as xml
import csv
import json

## Example top 500 data
ns = { 'top500': 'http://www.top500.org/xml/top500/1.0'}
config = None

"""
<top500:list xmlns:top500="http://www.top500.org/xml/top500/1.0" authors="Martin Meuer, Erich Strohmaier, Jack Dongarra, Horst D. Simon" date="2019/11/18">
  <top500:site>
    <top500:rank>1</top500:rank>
    <top500:system-id>179397</top500:system-id>
    <top500:system-name>Summit</top500:system-name>
    <top500:manufacturer>IBM</top500:manufacturer>
    <top500:computer>IBM Power System AC922, IBM POWER9 22C 3.07GHz, NVIDIA Volta GV100, Dual-rail Mellanox EDR Infiniband</top500:computer>
    <top500:system-address>http://www.olcf.ornl.gov/olcf-resources/compute-systems/summit/</top500:system-address>
    <top500:r-max>148600000.0</top500:r-max>
    <top500:power>10096.0</top500:power>
    <top500:r-peak>200794880.0</top500:r-peak>
    <top500:n-max>16473600</top500:n-max>
    <top500:n-half>0</top500:n-half>
    <top500:installation-site>
      <top500:installation-site-name>DOE/SC/Oak Ridge National Laboratory</top500:installation-site-name>
      <top500:installation-site-address>http://computing.ornl.gov</top500:installation-site-address>
      <top500:site-id>48553</top500:site-id>
    </top500:installation-site>
    <top500:town>Oak Ridge</top500:town>
    <top500:state>TN</top500:state>
    <top500:country>United States</top500:country>
    <top500:year>2018</top500:year>
    <top500:area-of-installation>6</top500:area-of-installation>
    <top500:number-of-processors>2414592</top500:number-of-processors>
  </top500:site>
"""

def setColumn(row,site,attribute):
    # store data in the row dictionary
    row[attribute]=site.find("top500:%s" % attribute ,ns).text

def main(columns):

    tree = xml.parse(config['topdataxml'])
    root = tree.getroot()

    count=0
    with open(config['topdatacsv'],'w', newline='') as f:
        writer = csv.DictWriter(f, delimiter=',', quotechar='"', fieldnames=columns)
        writer.writeheader()

        # write out columns
        for r in root:
            count+=1
            row={}
            for a in columns:
                setColumn(row,r,a)
            writer.writerow(row)

    return count

if __name__=='__main__':
    if len(sys.argv)!=2:
        print("./preprocess.py JSON configfile not specified")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        config=json.load(f)
    print(config['topdataxml'])
    print(main(['rank','system-name','computer']))

