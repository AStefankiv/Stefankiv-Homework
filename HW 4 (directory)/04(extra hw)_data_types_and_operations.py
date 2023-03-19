ice_cream = input("Which ice cream flavour would you like? ")

match ice_cream:
    case "Vanilla":
        print("It's our best-seller.")

    case "Peanut butter":
        print("Rich in flavour")

    case "Walnut & maple syrup":
        print("Canadian best rated")

    case "Chocolate":
        print("Just like your grandma used to have back in 60th")

    case "Plain":
        print("Simple is the option")

    case _:
        print("All of it is cold.")