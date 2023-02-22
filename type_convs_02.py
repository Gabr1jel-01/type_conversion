




red = hex(234)
green = hex(67)
blue = hex(53)

print("Hex ispis: ", red, green, blue, sep="")


'Path=helloworld'.removeprefix('Path=')
# 'helloworld'


red = red.removeprefix("0x")
green = green.removeprefix("0x")
blue = blue.removeprefix("0x")

print("Hex ispis bez 0x : ", red, green, blue, sep="")


red = hex(234).removeprefix("0x")
green = hex(67).removeprefix("0x")
blue = hex(53).removeprefix("0x")

print("Hex ispis bez 0x : ", red, green, blue, sep="")