#!/usr/bin/python3

import re

# (314) 555-1212


def getAreacode(phonenumber):
    p=re.compile("\((\d{3})\)")
    m=p.search(phonenumber)
    if(m!=None):
        areacode=m.group(1)
        return int(areacode)
    p=re.compile("^(\d{3})-")
    m=p.search(phonenumber)
    if(m!=None):
        areacode=m.group(1)
        return int(areacode)
    return None


phonenumber="(314) 555-1212"
assert getAreacode(phonenumber)==314
assert getAreacode("314-555-1212")==314
