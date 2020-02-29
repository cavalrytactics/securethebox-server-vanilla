string = '''NAME                             TYPE  TTL    DATA
external-dns-test.gcp.zalan.do.  NS    21600  ns-cloud-e1.googledomains.com.,ns-cloud-e2.googledomains.com.,ns-cloud-e3.googledomains.com.,ns-cloud-e4.googledomains.com.
'''

possible = ["ns-cloud-a1","ns-cloud-b1","ns-cloud-c1","ns-cloud-d1","ns-cloud-e1"]

thisstring = string.splitlines()[1]

for x in possible:
    if x in thisstring:
        print(x[:-1])

# print(string)