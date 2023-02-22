
#192.168.0.1
IP_address = "192.168.0.1"


#Hardcoded
IP_address_part_1 = 192
IP_address_part_2 = 168
IP_address_part_3 = 0
IP_address_part_4 = 1

IP_address_part_1 = int(input("Upisite prvi dio IP adrese: "))
IP_address_part_2 = int(input("Upisite drugi dio IP adrese: "))
IP_address_part_3 = int(input("Upisite treci dio IP adrese: "))
IP_address_part_4 = int(input("Upisite cetvrti dio IP adrese: "))

print("int ispis",
      IP_address_part_1,
      IP_address_part_2,
      IP_address_part_3,
      IP_address_part_4, sep=".")

IP_address_part_1 = bin(IP_address_part_1) 
IP_address_part_2 = bin(IP_address_part_2)  
IP_address_part_3 = bin(IP_address_part_3)  
IP_address_part_4 = bin(IP_address_part_4)  


print("Bin ispis:",
      IP_address_part_1,
      IP_address_part_2,
      IP_address_part_3,
      IP_address_part_4, sep=".")


