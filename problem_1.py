# Problem 1

def url_parser(url):
    x = url.split("/")
    proto = x[0][:-1]
    domain = x[2]
    path = ""
    for i in range(3,len(x)):
        path += x[i]
        if(len(x) > 4):
            path += "/"
    print("Protocol: " + proto)
    print("Domain: " + domain)
    print("Path: " + path)
