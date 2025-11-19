import pydriller

for commit in pydriller.Repository('transformers/').traverse_commits():
    print('Hash {}, author {}'.format(commit.hash, commit.author.name))