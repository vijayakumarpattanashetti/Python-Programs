#creating file
file=open('v.txt','w') #creates file 
file.write('Vijayakumar Pattanashetti') #file content
file.close() #closes file 

#opening file
file=open('v.txt','r') #opens file
file.read() #reads full file content
file.close() #closes file

file=open('v.txt','r') #opens file
file.read(5) # reads first 5 characters of file content
file.close() #closes file

#append/edit file
file=open('v.txt','a') #opens file
file.write('B.Tech - ECE') #adds these words to already existing content t
file.close() #closes file

#read & write file
file=open('v.txt','r') #opens file
file.read() #reads full file content
file.close() #closes file
