import os
import sys

#Deck manager finally functions. *almost
class DeckManager:
    def __init__(self, file_name = ""):
        self.file_name = file_name
        self.deck_list = []

    #should not return or take any input except for look for files

    #should print deck_name and word
    def search_word():
        print("scanning all decks...")

    def display_decks(self):
        print("Displaying Decks:")
        try:
            #get current working directory
            current_dir = os.getcwd()
            print(f"Scanning directory: {current_dir}\n")

            with os.scandir(current_dir) as entries:
                for entry in entries:
                    if entry.is_file() and entry.name.lower().endswith(".txt"):
                        print(f"- {entry.name}")
                        self.deck_list.append(entry.name)
                        
        except FileNotFoundError:
                print("File not found!")
        except PermissionError:
            print("Error: Permission denied.")


    # You can leave make_deck as is no need to change.
    #TODO
    #prevent empty names and the adding of .txt or any other file type
    def make_deck(self, deck_name, base_path="."):
        name = f"{deck_name}.txt" #stores filename.txt
        full_path = os.path.join(base_path, name) #combines filename with bast path being .\\filename
        if os.path.exists(full_path): #if a file exists in full path
            print("Deck already exists!")
            #prevents the function from creating a file
            return
        with open(full_path, "x", encoding="utf-8") as f:
            f.write("")
            #to be used to name folder
            return deck_name

        print(f"Deck created: {full_path}")

#----------------TODO----------------------------
    def create_new_deck(self, is_full):
        try:
            if isinstance(is_full, bool):
                print("making a new deck.")
        except ValueError:
            print("Must be a Boolean data type.")

    
    def delete_deck(self, filename, base_path="."):
        file_path = os.path.join(base_path, filename)
        try:
            if os.path.exists(file_path):
                os.remove(file_path) #deletes file
                print(f"File '{file_path}' deleted.")
            else:
                print(f"File '{file_path} does not exist")
        except PermissionError:
            print(f"Permision denied: cannot delete file.")     

    #returns which file you selected
    def which_deck(self):
        try:
            print("\n--- Which deck do you want to study ---")
            for deck in self.deck_list:
                print(deck)

            print()
            self.file_name = input("Select a Deck: ")
            print()

            if self.file_name in self.deck_list:
                #reads the deck raw
                with open(self.file_name, "r", encoding="utf-8") as f:
                    content = f.read()
                    print(content)
                    print()
                    print(f"Selected: {self.file_name}")
                    print()
                    return self.file_name
            else:
                print("No such deck exists!\n")
                return

        except ValueError:
            print("Error: Please enter a valid number.")
