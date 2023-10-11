import random
import tkinter as tk

game_idea_adjective = ["Robotic", "Monochrome", "Funny", "Sad", "Fast", "Adorable", "Beautiful", "Clean", "Drab", "Elegant", "Fancy", "Glamorous", "Handsome", "Long", "Magnificent", "Old-fashioned", "Plain", "Quaint", "Sparkling", "Ugliest", "Unsightly", "Wide-eyed", "Mysterious", "Enchanted", "Gigantic", "Tiny", "Colorful", "Bizarre", "Silly", "Stealthy", "Ancient", "Futuristic", "Charming", "Whimsical", "Dazzling", "Glowing", "Rustic", "Turbulent", "Whispering", "Energetic", "Bewitched", "Curious", "Incredible", "Mystical", "Radiant", "Serene", "Thundering", "Vibrant", "Zigzagging", "Radiant", "Magical", "Heroic", "Legendary"]
game_idea_noun = ["Man", "Giraffe", "Robot", "Car", "Apple", "Dog", "Snake", "Box", "Horse", "Jam", "Kitten", "Light", "Loaf", "Lock", "Lunch", "Trip", "Uncle", "Vase", "Winter", "Water", "Week", "Wheel", "Dragon", "Pirate", "Astronaut", "Wizard", "Ninja", "Alien", "Superhero", "Vampire", "Penguin", "Unicorn", "Pirate", "Tiger", "Moon", "Star", "Ship", "Castle", "Forest", "Planet", "Robot", "King", "Queen", "Princess", "Villain", "Monster", "Fairy", "Mermaid", "Sorcerer", "Warrior", "Artist", "Detective", "Explorer"]
game_idea_action = ["Commits genocide", "Runs forever", "Survives forever", "Jumps on blocks", "Creates a monopoly", "Races other people", "Beats up people", "Builds stuff", "Pets dogs", "Solves puzzles", "Fights monsters", "Sings songs", "Tames wild animals", "Collects treasure", "Solves mysteries", "Defeats the boss", "Embarks on an adventure", "Conquers the world", "Saves the day", "Travels through time", "Explores the unknown", "Defends the kingdom", "Battles evil forces", "Completes quests", "Sails the high seas", "Solves riddles", "Casts magical spells", "Flies to the moon", "Invents new gadgets", "Creates art", "Wins the championship", "Solves a murder mystery", "Discovers hidden treasure", "Builds a time machine", "Dances like no one's watching", "Bakes delicious treats", "Rides a dragon", "Battles space invaders", "Fights for justice", "Falls in love", "Saves the environment", "Solves a grand puzzle", "Sails across the universe", "Trains a dragon", "Plants a magical garden", "Becomes a superhero", "Becomes a rock star", "Becomes a chef", "Becomes a detective", "Becomes a scientist", "Becomes a spy"]

def generate_game_idea():
    idea = f"{random.choice(game_idea_adjective)} {random.choice(game_idea_noun)} {random.choice(game_idea_action)}"
    idea_label.config(text=idea)

def change_background_color():
    selected_color = color_var.get()
    root.configure(bg=selected_color)

root = tk.Tk()
root.title("Game Idea Generator")
root.configure(bg='lightblue')

idea_label = tk.Label(root, text="", wraplength=400, font=("Arial", 16), foreground="white", background='lightblue')
idea_label.pack(pady=20)

generate_button = tk.Button(root, text="Generate Idea", command=generate_game_idea, font=("Arial", 14), width=20, height=2, background="lightseagreen", foreground="white")
generate_button.pack()

color_var = tk.StringVar()
color_var.set("lightblue")
color_dropdown = tk.OptionMenu(root, color_var, "lightblue", "darkblue", "lightgreen", "darkgreen", "white", "red", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "black", "lightgray", "darkgray", "cyan", "magenta", "violet", "lime")
color_dropdown.pack(pady=10)
color_button = tk.Button(root, text="Change Background", command=change_background_color)
color_button.pack()

root.mainloop()
