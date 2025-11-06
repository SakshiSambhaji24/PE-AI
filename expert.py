
def traffic_light_controller():
    print("=== Traffic Light Expert System ===")
    print("Traffic Conditions: heavy / moderate / light")
    
    
    condition = input("Enter the current traffic condition: ").lower()
    
    
    if condition == "heavy":
        print("Keep Green Light ON for 60 seconds.")
        print("Red Light for 30 seconds.")
    elif condition == "moderate":
        print("Keep Green Light ON for 40 seconds.")
        print("Red Light for 20 seconds.")
    elif condition == "light":
        print("Keep Green Light ON for 20 seconds.")
        print("Red Light for 10 seconds.")
    else:
        print("Invalid input. Please enter 'heavy', 'moderate', or 'light'.")


traffic_light_controller()
