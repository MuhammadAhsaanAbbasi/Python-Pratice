person: int = int(input("Enter your Age!"))

if person<2:
    print("person is a toddler")
elif person==2 or person<4:
    print("\nperson is a kid")
elif person==4 or person<13:
    print("\nperson is a kid")
elif person==13 or person<20:
    print("\nperson is a teenager")
elif person==20 or person<65:
    print("\nperson is a adult")
else:
    print("\nperson is elder")

# Exercise 5.7
fruits: list[str] = ["Banana","Apple","Mango","Grapes","Orange","Pears","Peach"]
favourite_fruits: list[str] = input("Enter ',' Seperated Favourite Fruits").split(',')

for favourite_fruit in favourite_fruits:
    if favourite_fruit in fruits:
        print(f"\nYou Really like {favourite_fruit}")