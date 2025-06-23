#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
      if isinstance(val, str):
        self._value = val
      else:
        print("The value must be a string.")


    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        
        parts = re.split(r'[.!?]+', self._value)
        
        sentences = [p.strip() for p in parts if p.strip()]
        return len(sentences)

