choice={"dish1":"burger","dish2":"noodles"}
cooked={"dish1":"burger","dish2":"fries"}
for x in choice.values():
    for y in cooked.values():
        if x==y:
            print (x)
