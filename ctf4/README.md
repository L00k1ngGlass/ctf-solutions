# Solution

This one is straightforward! 
_grep_ each instance of a word to a line and pipe it to wordcount per line

```
grep -io "<wordchoice>" <logname>.log | wc -l
```

