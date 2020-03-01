from subprocess import check_output
import time

command = ["kubectl","get","service/auth","-o","jsonpath='{.status.loadBalancer.ingress[0].ip}'"]
whileLoop = True
while whileLoop:     
    try:           
        out = check_output(command)
        ipAddress = out.decode("utf-8")
        print(ipAddress.replace('\'',''))
    except:
        print("Not available")
        time.sleep(1)
# print(string)