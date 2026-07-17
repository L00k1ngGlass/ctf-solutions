# Solution 

We can catch this flag by using our terminal and a seperate tool known as hivex to read the registry files in a readable format.  

We can launch the interactive shell by running the _hivexsh_ command along side the _SYSTEM_ registry.

From here simply navigate down the following direstories 
```

cd ControlSet001\Services\Tcpip\Parameters\Interfaces
```

When you _ls_ the contents in this directory, you should see the following GUID keys:

```
{313A5211-5EB4-41A2-A9E4-74BEC3D717FD}
{36ED44A2-F897-4727-9872-AA628CA31484}
{3C21CB11-D9E9-4121-824C-42455DB4AC3F}
{e5576e42-c683-11dc-aff1-806e6f6e6963}
```

The flag is located in the _{313A5211-5EB4-41A2-A9E4-74BEC3D717FD}_ key under _NameServer_ and is 192.168.1.100