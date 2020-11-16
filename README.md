# ugen

**Advisory**

All the binaries/scripts/code of ugen should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own networks and/or with the network owner's permission.
* * *

**What is ugen?**

Ugen is a python script that will take a username list and output multiple variations, allowing you to then attempt to enumerate and discover the username formatting that is in force.

**Where would you use ugen?**

How many times have you found a website that lists its employees? Lets say we find a webpage on a CTF exercise that has a list of employees, how do we then take that a step further and try and work out the possibilities of the username format.

For example, the user Joe Bloggs may be one of the following:
- joebloggs
- joe.bloggs
- bloggs.joe
- jbloggs
- bloggsj
- j.bloggs
- And so many other possibilities

That is just for one user!

So adding these users to a text file and passing it to ugen will output a number of possibilities that you can then take a step further and enumerate with, using tools such as kerbrute.

**Notes**

There are similar and more extensive scripts/tools out there to do a similar job. However, this is a cheap and cheerful script that works for me and does a lot of the common formats, so thought I would share. In addition, it is very simple to modify and add your own custom formats should you need to.

**Example**

```
python ugen.py -i userList.txt -o outputFile.txt -n
```
-i = input files

-o = output files

-n = adds numbers 1-5 to the end of each username type - for example jbloggs1, jbloggs2 etc







