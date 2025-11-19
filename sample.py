import pydriller, datetime, re, seaborn, pandas as pd

cnt = 0
data = []
for commit in pydriller.Repository('transformers/').traverse_commits():
    if commit.author_date.date() >= datetime.date(2023, 1, 1):
        if re.search(r'(fix|bug|error|issue)', commit.msg, re.IGNORECASE):
            data.append({'hash': commit.hash, 'author_date': commit.author_date.date()})
            cnt += 1
print(f'Iterated over {cnt} commits total.')
print(data)