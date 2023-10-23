#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        if self.value and self.value[-1] == '.':
            return True
        return False

    def is_question(self):
        if self.value and self.value[-1] == '?':
            return True
        return False

    def is_exclamation(self):
        if self.value and self.value[-1] == '!':
            return True
        return False

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self.value)
        sentences = [sentence.strip() for sentence in sentences]
        sentences = list(filter(None, sentences))
        return len(sentences)
