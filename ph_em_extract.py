#!/usr/bin/env python3
import re
import pyperclip # Can put stuff into the clipboard

contact_list = []
# TODO grab all email addresses (For now just create the proper expression that will grab what we need)
email_regex = re.compile(r'\w*@\w*\.\w*')
mo = email_regex.findall('zfoster777@gmail.com k8hoxie@gdfg.net dogcatmouse@pie.com beepbopbooe@sdfsdef.edu 12334234@34234.gov DOGBEARMOUdse@gmail.com')
for i in mo:
    contact_list.append(i)


# TODO grab all phone numbers (For now just create the proper expression that will grab what we need)
phone_regex = re.compile(r'''(
     (\d{3}|\(\d{3}\))? # First 3 digits (area code)
     (-|\s*|\.)? # Seperator (if any)
     (\d{3}) # Next set of 3 digits
     (-|\s*|\.) # Seperator (if any)
     (\d{4,7})
     )''', re.VERBOSE)
moph = phone_regex.findall('505-967-8766, (242) 566 4567, 456 789 3455, 456-789-1010, 5053455678')
index = len(moph)

for i in moph:
    contact_list.append(i[0])
print(contact_list)

# TODO Put all of them into the clipboard
# TODO Paste them off of the clipboard