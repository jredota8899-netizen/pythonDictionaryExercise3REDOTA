fname = input('Enter the file name: ')
fhand = open(fname)
counts = dict()
count = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    emails = words[1]
    counts[emails] = counts.get(emails, 0) + 1

print(counts)


