from netaddr import *
import pprint

Octet = [128, 64, 32, 16, 8, 4, 2, 1]
OctetAll = [1, 1, 1, 1, 1, 1, 1, 1]
OctetNone = [0, 0, 0, 0, 0, 0, 0, 0]


def findipclass(IP):
    ip = IPAddress(IP)
    FirstOctet = int(ip.format().split('.')[0])
    #IP Ranges
    ARange = range(1, 127)
    BRange = range(128, 192)
    CRange = range(192, 224)
    if FirstOctet in ARange:
        return 'a'

    elif FirstOctet in BRange:
        return 'b'

    elif FirstOctet in CRange:
        return 'c'


IpInput = input("what is your ip address?")
SubnetMaskInput = input("what is the Subnet Mask?")

if findipclass(IpInput) == 'a':
    #sets Mask octet values for 2nd, 3rd, and 4th octet
    Subnet2ndOctet = [int(x) for x in str((IPAddress(SubnetMaskInput).bits().split('.')[1]))]
    Subnet3rdOctet = [int(x) for x in str((IPAddress(SubnetMaskInput).bits().split('.')[2]))]
    SubnetLastOctet = [int(x) for x in str((IPAddress(SubnetMaskInput).bits().split('.')[3]))]
    #sets IP Octet values for 2nd, 3rd, and 4th octet
    IP2ndOctet = [int(x) for x in str(IPAddress(IpInput).bits().split('.')[1])]
    IP3rdOctet = [int(x) for x in str(IPAddress(IpInput).bits().split('.')[2])]
    IPLastOctet = [int(x) for x in str(IPAddress(IpInput).bits().split('.')[3])]

    #find 2nd Octet Subnet number
    if Subnet2ndOctet == OctetAll:
        SecondOctetSubID = str(IPAddress(IpInput).format().split('.')[1])
    else:
        x = 0
        SubnetID = 0
        for items in Subnet2ndOctet:
            if Subnet2ndOctet[x] + IP2ndOctet[x] == 2:
                SubnetID = SubnetID + Octet[x]
            x = x + 1
        SecondOctetSubID = SubnetID

    #find 3rd Octet Subnet number
    if Subnet3rdOctet == OctetAll:
        ThirdOctetSubID = str(IPAddress(IpInput).format().split('.')[2])
    elif Subnet3rdOctet != OctetNone:
        x = 0
        SubnetID = 0
        for items in Subnet3rdOctet:
            if Subnet3rdOctet[x] + IP3rdOctet[x] == 2:
                SubnetID = SubnetID + Octet[x]
            x = x + 1
        ThirdOctetSubID = SubnetID
    else:
        ThirdOctetSubID = 0

    #find 4th Octet Subnet number
    if SubnetLastOctet == OctetAll:
        LastOctetSubID = str(IPAddress(IpInput).format().split('.')[3])
    elif SubnetLastOctet != OctetNone:
        x = 0
        SubnetID = 0
        for items in SubnetLastOctet:
            if SubnetLastOctet[x] + IPLastOctet[x] == 2:
                SubnetID = SubnetID + Octet[x]
            x = x + 1
        LastOctetSubID = SubnetID
    else:
        LastOctetSubID = 0

    print("Subnet Address is: " + str(IPAddress(IpInput).format().split('.')[0]) + '.' + str(SecondOctetSubID) + '.'
          + str(ThirdOctetSubID) + '.' + str(LastOctetSubID))
    print("The Subnet Id is: " + "0." + str(SecondOctetSubID) + '.' + str(ThirdOctetSubID) + '.' +
          str(LastOctetSubID))
    print("The Host Id is: " + "0." + str(int(IPAddress(IpInput).format().split('.')[1]) - int(SecondOctetSubID)) + '.' +
          str(int(IPAddress(IpInput).format().split('.')[2]) - int(ThirdOctetSubID)) + '.'
          + str(int(IPAddress(IpInput).format().split('.')[3]) - int(LastOctetSubID)))

if findipclass(IpInput) == 'b':
    # sets Mask octet values for 2nd, 3rd, and 4th octet
    Subnet3rdOctet = [int(x) for x in str((IPAddress(SubnetMaskInput).bits().split('.')[2]))]
    SubnetLastOctet = [int(x) for x in str((IPAddress(SubnetMaskInput).bits().split('.')[3]))]
    # sets IP Octet values for 2nd, 3rd, and 4th octet
    IP3rdOctet = [int(x) for x in str(IPAddress(IpInput).bits().split('.')[2])]
    IPLastOctet = [int(x) for x in str(IPAddress(IpInput).bits().split('.')[3])]

    # find 3rd Octet Subnet number
    if Subnet3rdOctet == OctetAll:
        ThirdOctetSubID = str(IPAddress(IpInput).format().split('.')[2])
    elif Subnet3rdOctet != OctetNone:
        x = 0
        SubnetID = 0
        for items in Subnet3rdOctet:
            if Subnet3rdOctet[x] + IP3rdOctet[x] == 2:
                SubnetID = SubnetID + Octet[x]
            x = x + 1
        ThirdOctetSubID = SubnetID
    else:
        ThirdOctetSubID = 0

    # find 4th Octet Subnet number
    if SubnetLastOctet == OctetAll:
        LastOctetSubID = str(IPAddress(IpInput).format().split('.')[3])
    elif SubnetLastOctet == OctetNone:
        LastOctetSubID = 0

    elif SubnetLastOctet != OctetNone:
        x = 0
        SubnetID = 0
        for items in SubnetLastOctet:
            if SubnetLastOctet[x] + IPLastOctet[x] == 2:
                SubnetID = SubnetID + Octet[x]
            x = x + 1
        LastOctetSubID = SubnetID


    print("Subnet Address is: " + str(IPAddress(IpInput).format().split('.')[0]) + '.' + str(IPAddress(IpInput).format().split('.')[1]) + '.'
        + str(ThirdOctetSubID) + '.' + str(LastOctetSubID))
    print("The Subnet Id is: " + "0.0" + '.' + str(ThirdOctetSubID) + '.' +
        str(LastOctetSubID))
    print("The Host Id is: " + "0.0" + '.' +
        str(int(IPAddress(IpInput).format().split('.')[2]) - int(ThirdOctetSubID)) + '.'
        + str(int(IPAddress(IpInput).format().split('.')[3]) - int(LastOctetSubID)))

if findipclass(IpInput) == 'c':
    SubnetLastOctet = [int(x) for x in str((IPAddress(SubnetMaskInput).bits().split('.')[3]))]
    IPLastOctet = [int(x) for x in str(IPAddress(IpInput).bits().split('.')[3])]
    x = 0
    SubnetID = 0

    for items in SubnetLastOctet:
        if SubnetLastOctet[x] + IPLastOctet[x] == 2:
            SubnetID = SubnetID + Octet[x]
        x = x + 1

    print("Subnet Address is: " + str(IPAddress(IpInput).format().split('.')[0]) +
    '.' + str(IPAddress(IpInput).format().split('.')[1]) + '.' + str(IPAddress(IpInput).format().split('.')[2]) +
    '.' + str(SubnetID))

    print("Subnet ID is: " + "0.0.0." + str(SubnetID))

    print("Host Id is: " + "0.0.0." + str(int(IPAddress(IpInput).format().split('.')[3]) - SubnetID))