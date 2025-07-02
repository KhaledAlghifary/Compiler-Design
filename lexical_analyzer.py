#!/usr/bin/env python3
import re
from typing import List, Dict, Tuple


class Token:
    """Represents a token with type and value."""
    
    def __init__(self, token_type: str, value: str):
        self.type = token_type
        self.value = value
    
    def __str__(self) -> str:
        return f"Token({self.type}, '{self.value}')"


class LexicalAnalyzer:
    
    def __init__(self):
        # Define keywords
        self.keywords = {'begin', 'end', 'if', 'then'}
        
        # Define operators and symbols
        self.operators = {
            '+': 'PLUS',
            '-': 'MINUS', 
            '*': 'MULTIPLY',
            '/': 'DIVIDE',
            '=': 'EQUALS',
            ':=': 'ASSIGN',
            ';': 'SEMICOLON',
            '(': 'LPAREN',
            ')': 'RPAREN'
        }
        
        # Basic patterns for token recognition
        self.patterns = [
            (r'\b(begin|end|if|then)\b', 'KEYWORD'),
            (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'IDENTIFIER'),
            (r'\b\d+\b', 'INTEGER'),
            (r':=', 'ASSIGN'),
            (r'[+\-*/=;()]', 'OPERATOR'),
            (r'\s+', 'WHITESPACE'),
        ]
        
        # Compile patterns
        self.compiled_patterns = [(re.compile(pattern), token_type) 
                                 for pattern, token_type in self.patterns]
    
    def analyze(self, source_code: str) -> List[Token]:
        """Basic token analysis."""
        tokens = []
        lines = source_code.split('\n')
        
        for line in lines:
            position = 0
            while position < len(line):
                match = None
                token_type = None
                
                # Try to match patterns
                for pattern, t_type in self.compiled_patterns:
                    match = pattern.match(line, position)
                    if match:
                        token_type = t_type
                        break
                
                if match:
                    value = match.group()
                    position = match.end()
                    
                    # Skip whitespace
                    if token_type == 'WHITESPACE':
                        continue
                    
                    # Create token
                    if token_type == 'KEYWORD':
                        tokens.append(Token('KEYWORD', value))
                    elif token_type == 'IDENTIFIER':
                        tokens.append(Token('IDENTIFIER', value))
                    elif token_type == 'INTEGER':
                        tokens.append(Token('INTEGER', value))
                    elif token_type == 'ASSIGN':
                        tokens.append(Token('ASSIGN', value))
                    elif token_type == 'OPERATOR':
                        if value in self.operators:
                            tokens.append(Token(self.operators[value], value))
                else:
                    # Skip unknown characters for now
                    position += 1
        
        return tokens
    
    def display_tokens(self, tokens: List[Token]):
        """Display tokens in a simple format."""
        print("\nTOKEN LIST:")
        print("-" * 30)
        for token in tokens:
            print(f"{token.type:<12} '{token.value}'")
        print("-" * 30)


def main():
    
    test_program = """
begin
    x := 10;
    y := 20;
end
"""
    
    print("Basic Lexical Analyzer Test")
    print("=" * 30)
    print("Test Program:")
    print(test_program)
    
    # Create analyzer and analyze
    analyzer = LexicalAnalyzer()
    tokens = analyzer.analyze(test_program)
    
    # Display results
    analyzer.display_tokens(tokens)


if __name__ == "__main__":
    main() 