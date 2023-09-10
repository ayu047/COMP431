__author__ = "730427647"

# TODO: Add your code here
import sys
import os

def httpparsing(a):
    print(a)
    a_list=a.split()
    ap=a_list[1]
    hv=a_list[2]
    isap=True
    ishv=True

    if ap[0:1]!="/":
        isap=False
    else:
        for i in range(len(ap)):
            if not(ap[i:i+1].isalnum() or ap[i:i+1]=="." or ap[i:i+1]=="/" or ap[i:i+1]=="_"):
                isap=False

    if len(hv)!=8:
        ishv=False
    else:
        if hv[0:5]!="HTTP/" or not(hv[5:6].isdigit()) or hv[6:7]!="." or not(hv[7:8].isdigit()):
            ishv=False

    if a[0:3]!="GET":
        print("ERROR -- Invalid Method token.")
    elif not(isap):
        print("ERROR -- Invalid Absolute-Path token.")
    elif not(ishv):
        print("ERROR -- Invalid HTTP-Version token.")
    elif len(a_list)>3:
        print("ERROR -- Spurious token before CRLF.")
    else:
        print("Method = GET")
        print("Request-URL = "+ap)
        print("HTTP-Version = "+hv)
        if (ap.lower()).endswith((".html",".txt",".htm")):
            ru=ap[1:]
            if os.path.exists(ru):
                try:
                    with open(ru) as f:
                        content = f.read()
                        print(content.strip("\n"))
                        f.close()
                except IOError as e:
                    print("ERROR: "+e)
                    raise
            else:
                print("404 Not Found: "+ap)
        else:
            print("501 Not Implemented: "+ap)

a=[] 
for line in sys.stdin: 
    a.append(line.replace("\n", ""))
for i in range(len(a)):
    httpparsing(a[i])

