
def defang(address):
    address = list(address) 

    i = 0

    while(i < len(address)):
        print(i)
        if (address[i] == "."):
            address.insert(i, "[")
            address.insert(i+2, "]")
            i += 3
        elif (address[i] != "."):
            i += 1

    address = "".join(address)

    return address





if __name__ == "__main__":
    resp = defang("1.2.3.4")
    print(resp)