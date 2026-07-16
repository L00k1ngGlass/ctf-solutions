#Solution
The easiest way to catch this flag is to open the .pcap file in Wireshark and filter by '''smtp'''. You'll see a couple of login attempts but the flag is located on packet 171.

You should something along the lines of:
'''Pass <Base64>'''

From here all we need to do is convert the encoded password back to readable text. You can use online tools or a quick python script located in ctf1.py
