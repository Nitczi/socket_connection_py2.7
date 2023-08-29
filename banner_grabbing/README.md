This script made in python2.7, will do a connection in an host by the address and port passed by the user, then it will return the banner of that service.

I put all my work on the response if an error is returned. At first, I manually crafted the get_name function with this line of code:
```
file=open("C:\Users\David\Desktop\services.txt", 'r')

def get_name(p):
    found = False
    for line in file:
        if "\t" + str(p) + "/" in line:
            conv = line.split()
            print "Unavailable service -->", p, "[", conv[0],"]"
            found = True
            break    
    if not found:
        print "Unavailable service -->", p, "[no service name]"
```

However, during my exploration of the Python socket documentation, I came across the `getservbyport` method. This method proved to be more efficient than opening and filtering files, especially when considering the possibility that the file may not exist in the specified location. But as I spend a time making this filter, I believe it's valid to share it here.
