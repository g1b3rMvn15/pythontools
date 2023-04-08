import sys, socket
#entrada do dominio a ser analisado via argumento
domain =sys.argv[1]

#abrindo wordlist para o brute force de consulta de subdominios

with open (sys.argv[2]) as wordlist:
    subdomains = wordlist.readlines()

#condição para concatenação dos subdominios com o IP encontrado, ocultando os subdominios não encontrados
for subdomains in subdomains:
    DNS = subdomains.strip ("\n") + "." + domain
    try:
        print (DNS, ":", socket.gethostbyname(DNS));
    except socket.gaierror:
        pass