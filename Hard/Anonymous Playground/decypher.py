alphabet = [None] + [chr(i) for i in range(ord('a'),ord('z')+1)]

cypher = ["hE","zA","dC","fH","zA","::","hE","zA","dC","fH","zA","hA","iJ","zA","eI","aD","jB","cB","hH","gA","zA","fH","fN"]
result = ""

for pair in cypher:
    if len(pair) != 2 or not pair[0].isalpha() or not pair[1].isalpha():
        result += pair
        continue

    shift = pair[0].lower()
    target = pair[1].lower()

    shift_number = alphabet.index(shift)
    target_index = alphabet.index(target)

    index = ((target_index - 1 + shift_number) % 26) + 1 
    result += alphabet[index]

print (result)
