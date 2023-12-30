# We will create two programs,1.To crate address book and write some records into it and then we will save it as a file in our computer  2.Read this address book and print these address books.

book={}                                                                                                                  #crate a dictionary object.
book["tom"]={
    'name':"tom",
    "address":"1 red street, NY",
    "Phone":98989898
}

book['bob']={
    "name":"bob",
    "address":"1 green street, NY",
    "phone":2342424
}

import json
s=json.dumps(book)                                                                                                      #take a book dictionary and dump it as a string
#print(s)                                                                                                               #output is a big string , as a json format.
print(type(s))

with open ("C://Users//ruhul//OneDrive//Documents//Job preparation 2023//book.txt","w") as f:
    f.write(s)

f=open("C://Users//ruhul//OneDrive//Documents//Job preparation 2023//book.txt","r")
s1=f.read()
print(s1)                                                                                                               #this output is a string
import json
book=json.loads(s1)
print(book)                                                                                                              #this output is a dictionary
print(type(book))

#Record of bob
print(book['bob'])
#Record of bob's phone number
print(book['bob']['phone'])

#Once we convert it to a dictionary object it is very easy to access the information within that big object using the keys and that's the power fo JSON and dictionaries.

# now we will find all the address book records in our book for that we will use for loop.
for person in book:
    print(book[person])