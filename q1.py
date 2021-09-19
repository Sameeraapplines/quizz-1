


word1 = input("enter string\n")
word2 =input("enter 2nd word\n")
length = len(word1)
new  = round(length//2)
length1 = len(word2)
new1 = round(length1//2)
final = word1[0]+word2[0]+word1[new]+word2[new1]+word1[-1]+word2[-1]
print(final)

