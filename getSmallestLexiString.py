def get_smallest_lexi_string(word: str, max_op: int):
    # First scenario where regardless of word, can transform to a.
    if max_op >= 25:
        return "a" * len(word)
    # Second scenario where largest character in word, can transform to a.
    largest_char_in_word = 0
    largest_char_from_start = 0
    for i in word:
        largest_char_in_word = max(largest_char_in_word, ord(i))
    for i in word:
        if ord(i) - ord("a") <= max_op:
            largest_char_from_start = max(largest_char_from_start, ord(i))
        else:
            break
    if largest_char_in_word <= max_op + ord("a"):
        return "a" * len(word)
    else: # Third scenario where operation not enough to transform all into a.
        for i in range(len(word) - 1):
            if (max_op > 0):
                op_needed_to_become_a = ord(word[i]) - ord("a")
                if op_needed_to_become_a >= max_op:
                    for j in range(max_op):
                        if word[i] == "a":
                            continue
                        print(f"[GTE] i: {i} j: {j} - Trying to replace: {chr(ord(word[i]))} with {chr(ord(word[i]) - 1)}")
                        max_op -= 1
                        word = word.replace((chr(ord(word[i]))), chr(ord(word[i]) - 1))
                else: 
                    for j in range(ord(word[i]) - ord("a")):
                        if word[i] == "a":
                            continue
                        print(f"[LT] i: {i} j: {j} - Trying to replace: {chr(largest_char_from_start - j)} with {chr(largest_char_from_start - j - 1)}")
                        max_op -= 1
                        word = word.replace(chr(largest_char_from_start - j), chr(largest_char_from_start - j - 1))
            else: 
                break

    return word

print(get_smallest_lexi_string('acbcecdba', 3))


def stored_word(word, max_operations):
    n = len(word)
    
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        if max_operations == 0:
            break
        
        count = word.count(ch)
        if count > 0:
            # Determine the replacement character
            if ch == 'a':
                replacement = 'z'
            else:
                replacement = chr(ord(ch) - 1)
            
            # Check if the replacement makes the word lexicographically smaller
            new_word = word.replace(ch, replacement)
            if new_word < word:
                word = new_word
                max_operations -= 1
    
    return word

# Test
word = "acbcecdba"
max_operations = 3
print("---" + stored_word(word,max_operations))