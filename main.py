from vocabulary.deckmanager import DeckManager
from vocabulary.wordmanager import WordManager
from vocabulary.filemanager import FileManager

#TODO
# create a SRS features
# how do I make a flashcard retain users
# Limiting the amount of words per deck
# Drawing pad for japanese and chinese
# modular flashcard app?
# make tabs for flashcard
## Difficult Cards Tab
## Practice Test Tab


# add a settings button

def menu():
    deck = DeckManager()
    deck.display_decks()
    print()
    print("1. Make a deck.")
    print("2. delete a deck.")
    print("3. choose a deck.")
    print("4. Exit application.")
    print()
    choice = int(input("Select What To Do(1, 2, 3): "))
    
    # try and except block?
    match choice:
        case 1: # case one seems to be clean
            name = str(input("Name of file?"))
            deck.make_deck(name)
        case 2:
            file_name = str(input("Delete what file?"))
            deck.delete_deck(file_name)
        case 3:
            file_name = deck.which_deck()
            file = WordManager(file_name) #instantiated the wordmanager
            file.word_options()
        case 4:
            print("exiting application.")
        case _:
            print("Invalid choice. Please select, 1, 2, or 3.")
            
def main():
    menu()

if __name__ == "__main__":
    main()