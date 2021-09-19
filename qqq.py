#Write a program to read lines from a text file and print the words which are less than 5 characters.


file=open('sample.txt','r')
readd = file.read() 
div= readd.split() 
for i in div: 
     if len(i)<4: 
         print(i) 
file.close()
