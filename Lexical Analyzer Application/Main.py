from Buffer import File
from Lexical import print_symbol_table, lex
from Helper import *


def handle_lex_result(lex_result):
    print("\nLexical information: ")
    for x in lex_result.keys():
        print(x + ": " + str(lex_result[x]))


def main():
    introduction()
    file_name = File(input("Enter the file name you want to read from: "))
    input_token = file_name.read_from_file()
    input_token_index = -1
    number_chosen = 0

    while True:
        main_menu()
        number_chosen = int(input("\nEnter the number: "))
        if number_chosen == 1:
            print("\nCalling lex() function...")
            input_token_index += 1
            try:
                lex_result = lex(input_token[input_token_index])
                handle_lex_result(lex_result)
            except IndexError:
                print("\nAll the tokens have been analysed \n")
                print(print_symbol_table())
                print("\n")
        elif number_chosen == 2:
            print(print_symbol_table())
        elif number_chosen == 0:
            print("The system has been logged out.")
            end_the_program()
        else:
            print("Invalid Operation Number!!!.")


if __name__ == "__main__":
    main()
