# Riders
The folder contains one python file &amp; 2 text files.
The python file *riders.py* converts the strings in the text files to respective JSON objects to python dictionaries. Presumably there will be an external function that keeps adding these text files as they come & keeps appending the *'directory'* variable in riders.py. All these objects of type *rider* (basically a dictionary) are then inserted in another object of class *riders* without repition. *riders* has functions to display all keys & print the value (of type *rider*) for a particular key.

**EXECUTION (on terminal) :**

(Have all the files in the same directory)

```sh
python3 riders.py
```

If you include many rider text files in the directory, the program auto populates riders so that there is no repetition & gives 2 options. *Option 1* prints all keys in riders. *Option 2* prints the values of the rider for a particular key.
