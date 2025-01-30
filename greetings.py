from datetime import datetime

username = 'You name'
title = 'Title of note'
content = 'Body of note'
status = 'Status'
created_date = datetime.today()
issue_date = datetime.today()

print(username)
print(title)
print(content)
print(status)
print(created_date.strftime("%d-%m-%y"))
print(issue_date.strftime("%d-%m-%y"))
