
# game.py

# Define the Game class to manage the game.
class Game:
    def __init__(self, player):
        # Initializes the game.
        self.player = player

    def start_adventure(self):
        # Begin the game.
        print(f"Welcome, Commander {self.player.name}, to your space mission!")
        self.choose_spaceship()

    def choose_spaceship(self):
        spaceship = self.get_decision("Choose your spaceship: 'Falcon' (speed) or 'Titan' (strength)? (falcon/titan): ", ["falcon", "titan"])
        print(f"The {spaceship.capitalize()} is ready for your command.")
        self.choose_first_destination()

    def choose_first_destination(self):
        destination = self.get_decision("First destination: 'Red Planet' or 'Comet Arc'? (planet/comet): ", ["planet", "comet"])
        self.explore_destination(destination)

    def explore_destination(self, destination):
        if destination == "planet":
            self.explore_red_planet()
        elif destination == "comet":
            print("At Comet Arc. There's something in the ice.")
            self.comet_decision()

    def explore_red_planet(self):
        print("Exploring Red Planet. The surface is vast and filled with red rocks and dust.")
        decision = self.get_decision("Investigate the mysterious canyon or explore the ancient ruins? (canyon/ruins): ", ["canyon", "ruins"])
        if decision == "canyon":
            self.explore_canyon()
        elif decision == "ruins":
            self.explore_ruins()

    def explore_canyon(self):
        print("Venturing into the canyon. The walls are steep and there are signs of past water flow.")
        decision = self.get_decision("Climb down to the canyon floor or send a drone to scout ahead? (climb/drone): ", ["climb", "drone"])
        if decision == "climb":
            print("Climbing down. Discovered fossilized alien life forms.")
            self.choose_next_action()
        elif decision == "drone":
            print("Drone scouting reveals a hidden cave with alien technology.")
            print("However, as the drone explores the cave, it suddenly becomes self-aware and turns against you!")
            print("The drone attacks and steals the discovered technology.")
            self.game_over("Mission failed. Smart drone attack and theft.")

    def explore_ruins(self):
        print("Exploring ancient ruins. There are hieroglyphs and structures unlike any on Earth.")
        decision = self.get_decision("Decipher the hieroglyphs or search for artifacts? (decipher/search): ", ["decipher", "search"])
        if decision == "decipher":
            print("Deciphered hieroglyphs reveal the history of an ancient Martian civilization.")
            self.choose_next_action()
        elif decision == "search":
            print("Found a mysterious artifact emitting a low hum.")
            self.analyze_artifact()

    def investigate_cave(self):
        print("Entered the cave. It's filled with advanced technology.")
        decision = self.get_decision("Attempt to activate the technology or take samples back for analysis? (activate/samples): ", ["activate", "samples"])
        if decision == "activate":
            print("Activated an ancient machine, creating a portal to another dimension.")
            self.enter_portal()
        elif decision == "samples":
            print("Collected samples of the technology for further analysis.")
            self.choose_next_action()

    def analyze_artifact(self):
        print("Analyzing the artifact. It seems to be a power source of unknown origin.")
        decision = self.get_decision("Use the artifact to power the ship or keep it safe for research? (power/research): ", ["power", "research"])
        if decision == "power":
            print("As the artifact's energy surges through the ship, the systems overload!")
            print("In a blaze of glory, the ship explodes, ending the mission in a spectacular fashion.")
            self.game_over("Mission Failed.")
        elif decision == "research":
            print("Keeping the artifact for research. It could hold untold secrets.")
            print("While studying the artifact, you make a groundbreaking discovery!")
            self.game_over("You found an eternal food source and saved humanity!.")

    # def unexpected_outcome(self):
    #     print("As the artifact's energy surges through the ship, the systems overload!")
    #     print("In a blaze of glory, the ship explodes, ending the mission in a spectacular fashion.")
    #     self.game_over("Ended in a dramatic space explosion.")

    def enter_portal(self):
        print("Stepping through the portal, you find yourself in a strange new world.")
        print("However, as you take your first steps, something goes terribly wrong.")
        print("Your body begins to disintegrate, atom by atom, as you're absorbed by the alien environment.")
        self.game_over("Ended in a mysterious disintegration in an alien world.")

    def comet_decision(self):
        decision = self.get_decision("Collect ice samples or analyze energy source? (collect/analyze): ", ["collect", "analyze"])
        if decision == "collect":
            print("Collected rare ice crystals. They could be valuable.")
            self.choose_next_action()
        elif decision == "analyze":
            print("Analyzed energy source. Discovered an unknown form of energy.")
            self.choose_next_action()

    def choose_next_action(self):
        action = self.get_decision("Continue exploring or head back to report? (explore/report): ", ["explore", "report"])
        if action == "explore":
            print("Exploring further. Found something intriguing.")
            self.investigate_intrigue()
        elif action == "report":
            print("Heading back to report discoveries.")
            print("As you navigate to the space station you run into an asteroid feild.")
            print("You run into a large asteroid and disintegrate into space dust.")
            self.game_over("Mission failed.")

    def investigate_intrigue(self):
        print("You've stumbled upon an ancient alien artifact.")
        decision = self.get_decision("Do you attempt to activate the artifact or take it back for research? (activate/research): ", ["activate", "research"])
        if decision == "activate":
            print("The artifact comes to life, revealing a map to a hidden sector in space.")
            self.explore_hidden_sector()
        elif decision == "research":
            print("You decide to bring the artifact back for thorough research.")
            print("While studying the artifact, you make a groundbreaking discovery!")
            self.game_over("Found the secret to life and completed the mission successfully.")

    def explore_hidden_sector(self):
        print("Following the map, you discover a hidden sector with unexplored planets.")
        decision = self.get_decision("Explore the nearest planet or scan the sector first? (explore/scan): ", ["explore", "scan"])
        if decision == "explore":
            print("You land on the nearest planet, discovering a hostile alien civilization.")
            print("As you explore further, you realize that you've been hunted for food by the hostile aliens!")
            self.game_over("Ended up as dinner for the alien civilization.")
        elif decision == "scan":
            print("You decide to scan the hidden sector before landing on any planets.")
            print("However, as you initiate the scanning process, the ship's systems suddenly malfunction.")
            print("The control panel sparks and the ship begins to shake violently.")
            print("In a matter of seconds, the ship explodes into pieces, ending the mission in a catastrophic fashion.")
            self.game_over("Mission ended due to a catastrophic ship explosion during scanning.")

    # Display a game over message with the option to play again.
    def game_over(self, reason=""):
        complete_message = f"Thank you for your bravery, Commander {self.player.name}."
        if reason:
            complete_message += " " + reason
        print(complete_message)
        self.ask_to_play_again()

    def ask_to_play_again(self):
        decision = input("Do you want to play again? (yes/no): ").lower()
        if decision == "yes":
            self.restart_game()
        elif decision == "no":
            print("Thank you for playing! Goodbye, Commander.")
        else:
            print("Invalid command. Please answer with 'yes' or 'no'.")
            self.ask_to_play_again()

    def restart_game(self):
        print("Restarting the game...\n")
        self.start_adventure()

    def get_decision(self, prompt, valid_choices):
        # Get a player's decision from a list of valid choices.
        while True:
            decision = input(prompt).lower()
            if decision in valid_choices:
                return decision
            else:
                print(f"Invalid command. Please choose one of the following: {', '.join(valid_choices)}.")