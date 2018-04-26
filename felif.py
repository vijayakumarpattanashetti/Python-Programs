Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> file=open('v.txt','w')
>>> file.write('Vijayakumar Pattanashetti')
25
>>> file=open('v.txt','r')
>>> file.read() #reads full file content
'Vijayakumar Pattanashetti'
>>> file=open('v.txt','r') #opens file
>>> file.read(5) # reads first 5 characters of file content
'Vijay'
>>> file=open('v.txt','a')
>>> file.write('B.Tech - ECE') #adds these words to already existing content
12
>>> file=open('v.txt','r') #opens file
>>> file.read() #reads full file content
'Vijayakumar PattanashettiB.Tech - ECE'
>>> 
