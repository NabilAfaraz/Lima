import re
urladdress = "http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#InTheDocument"
delimiters = "://", ":","=", "#" , "?" , "&";
delimeterforSubdomain = ".";
PatternBreaker = '|'.join(map(re.escape, delimiters))
PatternBreakerSD = '|'.join(map(re.escape, delimeterforSubdomain))
t = re.split(PatternBreaker, urladdress)
print('URL:',urladdress)
print('Protocol :',t[0])
print('Domain :',t[1])
subdomain = re.split(PatternBreakerSD, t[1])
print('Sub Domain :',subdomain)
port = t[2][:2]
print('Port:', port)
path = t[2][2:]
print('Port:', path)
print('Parameters:', t[4] , t[6])
print('Fragment:', t[7])



