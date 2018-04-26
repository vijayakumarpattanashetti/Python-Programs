#creating file
file=open('v.txt','w') #creates file 
file.write('Vijayakumar Pattanashetti') #file content

#opening file
file=open('v.txt','r') #opens file
file.read() #reads full file content

file=open('v.txt','r') #opens file
file.read(5) # reads first 5 characters of file content

#append/edit file
file=open('v.txt','a') #opens file
file.write('B.Tech - ECE') #adds these words to already existing content

#read & write file
file=open('v.txt','r') #opens file
file.read() #reads full file content
