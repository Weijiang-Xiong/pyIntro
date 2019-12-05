from urllib.request import urlopen

with urlopen('http://www.baidu.com') as response:
    for line in response:
        line = line.decode('utf-8') # decoding the binary data to text.
        if 'baidu' in line or '百度' in line:
            print(line)
