import re
import streamlit as st

class SimpleLexer:
    rules = [
        ("CTE", r"[0-9]+"),                 # Integer constants
        ("OP_ADD", r"\+"),                  # Addition operator
        ("OP_SUB", r"-"),                   # Subtraction operator
        ("OP_MUL", r"\*"),                  # Multiplication operator
        ("OP_DEV", r"\/"),                  # Devision operator
        ("LPAREN", r"\("),                  # Left parenthesis
        ("RPAREN", r"\)"),                  # Right parenthesis
        ("WHITESPACE", r"[ \t]+"),          # Spaces (to ignore)
    ]

    def __init__(self):
        self.tokens = []

    def tokenize(self, text):
        self.tokens = []  # Reset tokens for each new input
        position = 0
        while position < len(text):
            match = None
            for token_name, token_regex in self.rules:
                regex = re.compile(token_regex)
                match = regex.match(text, position)
                if match:
                    value = match.group(0)
                    if token_name != "WHITESPACE":  # Ignore spaces
                        self.tokens.append((token_name, value))
                    position += len(value)
                    break
            if not match:
                raise ValueError(f"Erreur lexicale : caractère inattendu '{text[position]}'")
        return self.tokens

# Streamlit UI
st.title("Lexical Analyzer")
st.write("Enter a mathematical expression to tokenize:")

# Input box for the expression
expression = st.text_input("Expression", value="5 + (2 * (8 - 3))")

if expression:
    lexer = SimpleLexer()
    try:
        tokens = lexer.tokenize(expression)
        st.success("Tokens extracted successfully!")
        st.json(tokens)  # Display tokens as JSON
    except ValueError as e:
        st.error(f"Error: {e}")
