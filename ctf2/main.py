import pefile as pf

file = pf.PE("ctf2.file")

for info in file.FileInfo[0]:
    if info.Key == b"StringFileInfo":
        for strings in info.StringTable:
            for key, val in strings.entries.items():
                print(key.decode(), "=", val.decode())