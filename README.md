# debugger
You learned that the proper way to debug a program is by printing lines, but found that is a bit tedious process?<br>
No worry anon, get ready to turn your spaghetti debugging code to a readable and easy to use format!

Go from this:
```
print("0")
// something
print("1")
// something else
print("aaaa")
```
to a more glorious/professional looking:
```
from debugger import breakpoint as b
 
# Normal breakpoint:  
b()    
# Verbose breakpoint:
b(None, True)                         
# Passing object to print value:
x = 42
b(x)      
# Verbose breakpoint with object value: 
b(x, True)
```

and end up with this output:
```
------Breakpoint------
Line:  4
----------------------
------Breakpoint------
File:  /home/x/dev/python/tester.py
Function:  <module>
Line:  7
----------------------
------Breakpoint------
Line:  11
Value:  42
----------------------
------Breakpoint------
File:  /home/x/dev/python/tester.py
Function:  <module>
Line:  14
Value:  42
----------------------
```
As you can see, the debugger is meticulously designed to support all the common line printing tactics.<br>
Have fun debuggin gloriously!
