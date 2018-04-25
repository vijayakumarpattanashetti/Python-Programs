#creating file
file=open.('v.txt','w') #creates file 
file.write('Vijayakumar Pattanashetti') #file content
file.close() 

#opening file
file=open.('v.txt','r') #opens file
x=file.read() #reads full file content
print(x) #prints the read content
y=file.read(5) # reads first 5 characters of file content
print(y) #prints the read content

#append/edit file
file=open.('v.txt','a') #opens file
file.write('B.Tech - ECE') #adds these words to already existing content t
file.close() #closes file

#read & write file
file=open.('v.txt','r') #opens file
x=file.read() #reads full file content
print(x)
y=file.write('Hello..!') # reads first 5 characters of file content
file.close() #closes file