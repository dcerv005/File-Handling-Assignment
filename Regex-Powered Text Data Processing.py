#Question 2
import re

with open('contacts.txt', 'r') as file:
    email_list=[]
    for line in file:
        emails = re.search(r"(\S+@\S+)", line)
        if emails:
            email_list.append(emails.group())
print(email_list)

