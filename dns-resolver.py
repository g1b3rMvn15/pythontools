# -*- condig: utf-8 -*-
'''
DNS RESOLVER - BY GLAUBER MUNIZ - 

É NECESSARIO A INSTALAÇÃO DO DNS.RESOLVER VIA COMANDO: PIP INSTALL DNSPYTHON 

CODIGO FUNCIONAL PARA PYTHON 3

'''

import dns.resolver

#-------------------
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
#-------------------

alvo = input(BLUE + "DIGITE O DOMÍNIO ALVO:" + RESET)

#------------------------------------------
print(RED + "REGISTROS TIPO A  - IP's")

resultado = dns.resolver.resolve(alvo, 'A')
for ipvalor in resultado:
    print(GREEN + "IP: ", ipvalor.to_text())
    ip_alvo = ipvalor.to_text()
#-------------------------------------------
print("---------")
print(RED + "REGISTROS TIPO CNAME - ENTRADAS")
try:
    resultado = dns.resolver.resolve(alvo, 'CNAME')
    for cnamevalor in resultado:
        print(GREEN + 'CNAME: ', cnamevalor.target)
except:
    pass


print("---------")
print(RED + "REGISTROS TIPO AAAA - ENTRADAS")
try:
    resultado = dns.resolver.resolve(alvo, 'AAAA')
    for val in resultado:
        print(GREEN + 'AAAA: ', ipvalor.to_text())
except:
    pass

print("---------")
print( RED + "REGISTROS TIPO PTR - ENTRADAS")
try:

    resultado = dns.resolver.resolve(ip_alvo+'.in-addr.arpa', 'PTR')

    for val in resultado:
        print(GREEN + 'PTR: ', val.to_text())
except:
    pass
print("---------")

print(RED + "REGISTROS TIPO NS - ENTRADAS")
try:

    resultado = dns.resolver.resolve(alvo, 'NS')

    for val in resultado:
        print(GREEN + 'NS: ', val.to_text())
except:
    pass

print("---------")

print(RED + "REGISTROS TIPO MX - ENTRADAS")
try:

    resultado = dns.resolver.resolve(alvo, 'MX')

    for exdata in resultado:
        print(GREEN + 'MX: ', exdata.to_text())
except:
    pass
print("---------")

print(RED + "REGISTROS TIPO SOA - ENTRADAS")
try:

    resultado = dns.resolver.resolve(alvo, 'SOA')

    for val in resultado:
        print(GREEN + 'SOA: ', val.to_text())
except:
    pass

print("---------")

print(RED + "REGISTROS TIPO TXT - ENTRADAS")
try:

    resultado = dns.resolver.resolve(alvo, 'TXT')

    for val in resultado:
        print(GREEN + 'TXT: ', val.to_text())
except:
    pass

print("---------")
print(CYAN + BOLD + "DNS RESOLVER - BY g1b3rMvn15 - 2023 - https://github.com/g1b3rMvn15")



