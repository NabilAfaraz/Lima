print 'Group Lima'
print 'Members : Nabil Bukhari, Nizam & Goggi'
print '\n'
import re
urladdress = "http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#InTheDocument"
print 'URL is :', urladdress

#getting index of protocol ending
protocolIndex = urladdress.index('://')
#print protocolIndex

#all values before protocol ending
protocol = urladdress[:protocolIndex]

#print protocol
#trimming url address and removing data related to protocol 
trimfunc = protocolIndex + 3;
trimmedval = urladdress[trimfunc:]

#print 'Trimmed Val' ,trimmedval
#getting : value to find the port
portIndex = trimmedval.index(':')
portIndex = portIndex + 1

#trimming earlier trimmed value and removing data related to domain
trimmedval1 = trimmedval[portIndex:]
#print 'Trimmed Val1' ,trimmedval1

pathIndex = trimmedval1.index('/')

#getting value of port
port = trimmedval1[:pathIndex]

#getting value of domain
domain = trimmedval[:portIndex]

#getting sub domain from domain
delimeterforSubdomain = ".";
PatternBreakerSD = '|'.join(map(re.escape, delimeterforSubdomain))
subdomain = re.split(PatternBreakerSD, domain)

#trimming earlier trimmed value and removing data related to port
trimmedval2 = trimmedval1[pathIndex:]

#print 'Trimmed Val2' ,trimmedval2

parameterIndex = trimmedval2.index('?')

#print (parameterIndex)
path = trimmedval2[:parameterIndex]

#to remove / and extra space
parameterIndex = parameterIndex + 3

#trimming earlier trimmed value and removing data related to path
trimmedval3 = trimmedval1[parameterIndex:]
#print 'Trimmed Val3' ,trimmedval3

fragmentIndex = trimmedval3.index('#')
#print fragmentIndex

parameters = trimmedval3[:fragmentIndex]

#increment by 1 to remove #
fragmentIndex = fragmentIndex + 1

#getting splitted parameters from parameters
delimeterforParameter = "&";
PatternBreakerP = '|'.join(map(re.escape, delimeterforParameter))
splittedParameters = re.split(PatternBreakerP, parameters)

#trimming earlier trimmed value and removing data related to path

fragment = trimmedval3[fragmentIndex:]

print '\n'
print '----------------Evaluated Values----------------' 
print 'Protocol :', protocol
print 'Domain :', domain
print 'Sub Domain :',subdomain
print 'Port:', port
print 'Path:', path
print 'Parameters:', parameters
print 'Splitted Parameters:', splittedParameters
#we can get value1 from it as well
print 'Fragment:', fragment
