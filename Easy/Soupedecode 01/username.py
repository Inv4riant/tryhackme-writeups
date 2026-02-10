import re

target = ''
output = ''

usernames = set()
pattern = re.compile(r"\\([^ ]+)")

while not target.endswith(".txt"):
    target = input("'target.txt' file: ")
while not output.endswith(".txt"):
    output = input("'output.txt' file: ")

with open(target, "r") as f:
    for line in f:
        if "(SidTypeUser)" not in line or "$" in line:
            continue
        match = pattern.search(line)
        if match:
            usernames.add(match.group(1))

with open(output, "w") as f:
    for user in sorted(usernames):
        f.write(user + "\n")

print(f"Extracted {len(usernames)} valid usernames.")
