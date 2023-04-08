import sys,dns.resolver

dominio = sys.argv[1]

registros = ["A", "AAAA", "MX", "NS", "TXT"] 

for registro in registros:
    response = dns.resolver.query(dominio, registro, raise_on_no_answer=False);
    if response.rrset is not None:
        print (response.rrset)  