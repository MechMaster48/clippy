#!/usr/bin/env python3
import re
import pyperclip

## OUTLINE ON USAGE
# Step 1: Copy large amount of text from somewhere
# Step 2: Trigger script
# Step 3: Script filters out all valid emails and phone numbers
# Step 4: Script sends that list to the clipboard and prints to CLI (Will make printing to CLI optional in the future)
# Step 5: Any text found will be able to be pasted

# TODO Dial in regular expression for phone number. It works 9/10 times, but still some numbers trigger a match

def grab_text(): # Takes all text currently stored in clipboard and returns it
    clipboard = pyperclip.paste()
    return clipboard

def filter_text(text): # Finds all valid emails and phone numbers and adds them to a list
    contact_list = []
    email_regex = re.compile(r'\w*@\w*\.\w*')
    phone_regex = re.compile(r'''(
     (\+\d\s)? # Country code  
     (\d{3}|\(\d{3}\))? # First 3 digits (area code)
     (-|\s*|\.)? # Seperator (if any)
     (\d{3}) # Next set of 3 digits
     (-|\s*|\.) # Seperator (if any)
     (\d{4,7}) # Last 4 digits (up to 7 if number did not have any spaces)
     )''', re.VERBOSE)
    filter_email = email_regex.findall(text)
    filter_phone = phone_regex.findall(text)
    for address in filter_email:
        contact_list.append(address)
    for number in filter_phone:
        contact_list.append(number[0])
    return contact_list

def format_text(list_text): # Takes the list from the filtered text and both adds it to clipboard and prints to CLI (CLI printing will be optional in future)
    if len(list_text) == 0:
        print('No phone numbers or emails found.')
    else:
        pyperclip.copy('\n'.join(list_text))
        print('Here is the contact info found:\n')
        for contact in list_text:
            print(contact)
    

if __name__ == "__main__": # Make it all happen
    grab_text()
    filter_text(grab_text())
    format_text(filter_text(grab_text()))