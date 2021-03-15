import nmap

scanner = nmap.PortScanner()
host = input("Please enter the IP address : ")
scanner.scan(host,'1-1024','-sV')

print("The host name is : "+ scanner[host].hostname())
print("The host status is : "+ scanner[host].state())

keys = scanner[host]['tcp'].keys()

for i in keys:
    print('---------------------')
    print(f'+ the port : {str(i)}')
    result = scanner[host]['tcp'][i]
    for re in result:
        print("   ",re, ':', result[re])