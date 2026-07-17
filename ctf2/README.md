# Solution

You can solve this using your terminal and a few commands. This applies for Linux and should work for MacOS not sure if the same commands carry over to Windows

## MacOS/Linux

If you use the _file_ command on .file, you should get something along the lines of:
```
    PE32 executable (GUI) Intel 80386, for MS Windows
```

From here, we can identify that .file is a Windows executable and we can dig further for its contents to find the file name.

A majority of the data is unreadable so using the _tr_, _strings_ and piping _grep_ command will filter for useful information. 

The original filename of a PE32 executable is located in the OriginaFilename key 

To find the file name we can enter the following command:
```
tr -d '\0' < <filename> | strings | grep -i originalfilename
```