#!/usr/bin/env python3
import re
import pyperclip # Can put stuff into the clipboard

# TODO grab all email addresses
email_regex = re.compile(r'\w*@\w*\.\w*')
mo = email_regex.findall('zfoster777@gmail.com k8hoxie@gdfg.net dogcatmouse@pie.com beepbopbooe@sdfsdef.edu 12334234@34234.gov DOGBEARMOUdse@gmail.com')
print(mo)
# TODO grab all phone numbers
#phone_regex = re.compile(r'''(
    

# TODO Put all of them into the clipboard
# TODO Paste them off of the clipboard