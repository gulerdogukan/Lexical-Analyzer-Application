from enum import Enum

# Here I'm declaring two lists that store the reserved words and the operator that we will use them as tokens.
reserved_words = ["for", "while", "if", "else"]
operators = ["|", "||", "&", "&&"]


# Here we are creating a Tokenize class of type ENUM, by using the directory "ENUM"
class Tokenize(Enum):
    FOR = "for"
    WHILE = "while"
    IF = "if"
    ELSE = "else"
    INTEGER = "int"
    FLOAT = "float"
    BITWISE_OR = "|"
    LOGICAL_OR = "||"
    BITWISE_AND = "&"
    LOGICAL_AND = "&&"
    ID = "id"
    ERROR = "err"
