from classes import *

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Grunter")
    print("2. Mofa")
    print("3. Geki")  
    print("4. Medic")  
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Grunter(name)
    elif class_choice == '2':
        return Mofa(name)
    elif class_choice == '3':
        return Geki(name)
    elif class_choice == '4':
        return Medic(name)
    else:
        print("Invalid choice. Defaulting to Grunter.")
        return Grunter(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            continue
        else:
            print("Invalid choice, try again.")
            continue

        if wizard.health > 0:
            enemy_action = random.choice(["attack", "special", "regen"])
            if enemy_action == "attack":
                wizard.attack(player)
            elif enemy_action == "special":
                wizard.special_ability(player)
            elif enemy_action == "regen":
                wizard.regenerate()

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    player = create_character()
    wizard = Feibang("The Feibang Lord")
    battle(player, wizard)

if __name__ == "__main__":
    main()