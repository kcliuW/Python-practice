# Recycle garbage according to their nature

print("Your garbage type is plastic or metal or paper or others?")
g_type = input("Please enter your garbage type : ")
 
if g_type == "plastic":
    print("Please put it into the BROWN recycling bin!")

elif g_type == "metal":
    print("Please put it into the YELLOW recycling bin!")

elif g_type == "paper":
    print("Please put into the BLUE recycling bin!")

else:
    print("Garbage bin please.")