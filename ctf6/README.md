# Solution

The answer is located on packet #9968. The data contains the hashes of several users.

Leia's will look like this:

```
leia:1012
0250   3a 30 38 38 38 37 30 62 61 38 65 61 37 31 36 36   :088870ba8ea7166
0260   32 61 61 64 33 62 34 33 35 62 35 31 34 30 34 65   2aad3b435b51404e
0270   65 3a 34 36 31 39 63 35 39 32 66 64 61 35 31 36   e:4619c592fda516
0280   63 38 31 34 30 34 39 35 64 32 66 62 66 37 30 37   c8140495d2fbf707
0290   66 63 3a 3a 3a 0a 6c 75 6b 65 3a 31 30 31 31 3a   fc:::.luke:1011:
```

We get two pieces from this, the NT and LM hash:

- **NT:** `088870ba8ea71662aad3b435b51404ee`
- **LM:** `4619c592fda516c8140495d2fbf707fc`

From here we can use an online tool, use hashcat with a wordlist, or use a python script with a wordlist.
