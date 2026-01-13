import os

#----------------------------------------------------------------------
#  ------------------------ WORD MANAGER CLASS ----------------------
#----------------------------------------------------------------------
# Functions: Adds words/ Deletes Words/ Options on what you want to do with words
# create a deck? proabably or just have explicit access to another function
# coupling is when two classes become intertwined because class wordmanager needs
# A functions from Deckmanager called MakeDeck

#TODO
# what is ANY in python
# current flashcard setup meaning: f"front: {投稿}| back: {submission; post}

class WordManager:
    
    #Insert a file for WordManager to deal with
    #word limit per deck
    def __init__(self, file_name, default=20):
        self.word = ""
        self.file_name = file_name
        self.set_word_limit = default

    def word_options(self):
        try:
            while True:
                print("1. Study Deck")
                print("2. add a word")
                print("3. delete a word")
                print("4. exits deck")

                choice = str(input("Select a number (1, 2, 3, 4): "))

                if choice == "2":
                    self.add_words()
                elif choice == "3":
                    self.delete_words()
                elif choice == "4":
                    #exits word_options()
                    break
                else:
                    print("Not a Valid Input!")
        except ValueError:
            print("User a Number Only, Please!")
    
    #Study Deck
    def study_deck(self):
        while True:
            print(f"Studying Deck: {self.file_name}")
            choice = input(f"front or back? (f or b): ")
            if choice == 'n':
                print("next card")
            elif choice == 'l':
                print("")
            if choice == 'f':
                print(f"front: ")
            elif choice == 'b':
                print(f"back: ")
            else:
                print("Not a valid choice must be 'b' or 'f'!")

    def show_front():
        pass

    def show_back():
        pass

    def back_a_word(self):
        pass
    
    def forward_a_word(self):
        pass
    # end of study deck section


    # search word within each of the list
    def add_words(self):
        while True:
        #will stop adding words if limit of words reached and creates another deck
            if self.limit_words(): 
                print("Creating a new DECK...(not implmented yet)")
                return
        
            first_word = str(input("Target Language Front('quit' or 'q'): ").strip())
            if first_word.lower() in ('q','quit'): break

            second_word = str(input("Native Tounge Back('quit' or 'q'): ").strip())
            if second_word.lower() in ('q', 'quit'): break

            join = f"{first_word.lower()}|{second_word.lower()}\n"

            with open(self.file_name, "a", encoding="utf-8") as f:
                f.write(join) # writes: привет|hello\n as a line

    #needs to detect either a or b in this format "a|b\n"
    def delete_words(self):
        while True:
            new_vocab_list = []

            print("Which word do you want to delete?")
            print('Format: "word1|word2" (you can delete one or more)')

            user_input = input("> ").strip().split("|")
            print(user_input)

            if any(item in ('') for item in user_input):
                print("Invalid Input!\n")
                continue

            confirm = input("Are you sure you want to delete?(y/n): ").lower()

            if confirm == 'y':
                with open(self.file_name, "r", encoding="utf-8") as file:
                    content = file.readlines()
                    print(f"old_vocab: {content}")
                    for line in content:
                        target, eng = line.strip().split("|")

                        # if ANY input matches, delete the line
                        if any(item in (target, eng) for item in user_input):
                            continue

                        # otherwise keep it
                        new_vocab_list.append(f"{target}|{eng}\n")
            elif confirm == 'n':
                continue
            else:
                print("Not a valid input!")

            print(f"new_vocab: {new_vocab_list}")

            #write over the old with a w
            #with open(self.file_name, "w", encoding="utf-8") as file:
                #file.write(new_vocab_list)


    # limits the amount of words and returns True or False
    def limit_words(self): #completed?
        line_count = 0
        
        #counts each line
        with open(self.file_name, "r", encoding="utf-8") as f:
            line_count = sum(1 for line in f) # What is this exactly
        
        
        print(f"Limit Set to: {line_count}/{self.set_word_limit}")

        if line_count >= self.set_word_limit:
            print(f"Too many words!")
            return True
        
    #how acess one function from another class
    def exit_words(self):
        pass