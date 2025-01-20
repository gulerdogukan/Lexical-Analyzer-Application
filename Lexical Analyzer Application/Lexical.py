from Helper import *
from Tokens import reserved_words, Tokenize

symbol_table = []
symbol_table.extend(reserved_words)


def lexical_results(input_token, value=None):
    token_type = Tokenize(input_token).name
    if not value:
        return {
            "token": token_type
        }
    elif input_token == "int":
        return {
            "token": token_type,
            "integer_value": value
        }
    elif input_token == "float":
        return {
            "token": token_type,
            "float_value": value
        }
    if input_token == "err":
        return {
            "token": token_type,
            "unrecognized_string": value
        }
    elif input_token == "id":
        return {
            "token": token_type,
            "index": value
        }


def add_to_symbol_table(identifier):
    if symbol_table.count(identifier):
        return symbol_table.index(identifier)
    else:
        symbol_table.append(identifier)
        return symbol_table.index(identifier)


def print_symbol_table():
    return "Symbol Table: " + str(symbol_table)


def lex(input_token):
    if is_operator(input_token):
        return lexical_results(input_token)
    elif is_identifier(input_token):
        index = add_to_symbol_table(input_token)
        return lexical_results(input_token="id", value=index)
    elif is_reserved_word(input_token):
        return lexical_results(input_token)
    elif is_integer(input_token):
        x = int(input_token)
        return lexical_results(input_token="int", value=x)
    elif is_float(input_token):
        x = float(input_token)
        return lexical_results(input_token="float", value=x)
    else:
        return lexical_results(input_token="err", value=input_token)
