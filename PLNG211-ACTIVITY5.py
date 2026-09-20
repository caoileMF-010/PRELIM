def find_alphaLast(word1, word2, word3):
    lastWord = max(word1, word2, word3)
    return lastWord
    
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the third word: ")

print(find_alphaLast(word1, word2 ,word3))
