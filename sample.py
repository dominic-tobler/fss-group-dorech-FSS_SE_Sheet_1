import pydriller

cnt = 0
for commit in pydriller.Repository('transformers/').traverse_commits():
    cnt += 1
    print('Hash {}, author {}, commiter date {}'.format(commit.hash, commit.author.name, commit.committer_date))
print(f'Iterated over {cnt} commits total.')