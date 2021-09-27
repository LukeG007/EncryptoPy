"""
An advanced encryption engine
with multiple encryption types
"""

__version__ = '1.0.0'
__name__ = 'EncryptoPy'
__author__ = 'UltraProGamerYT'
__email__ = 'ultraprogameryt@gmail.com'


import sys
from . import emojies

class TextEncryption:
    def __init__(self) -> None:
        pass
    
    def BasicTextEncryption(self, Message, Password, Mode):
        if Mode.lower() == 'en':
            Characters = list(Message)
            EncryptedMessage = ''
            for c in Characters:
                EncryptedMessage += chr(ord(c)+Password)
            return EncryptedMessage
        elif Mode.lower() == 'de':
            Characters = list(Message)
            DecryptedMessage=''
            for c in Characters:
                DecryptedMessage +=chr(ord(c)-Password)
            return DecryptedMessage
        else:
            sys.exit("'Mode' argument only takes 'en' or 'de'")
        
    def EmojiEncryption(self, Message, Mode):
        if Mode.lower() == 'de':
            Decrypted_text = emojies.EmojiDecryption(Message)
            return Decrypted_text
        elif Mode.lower() == 'en':
            Encrypted_text = emojies.EmojiEncryption(Message)
            return Encrypted_text
        else:
            sys.exit("'Mode' argument only takes 'en' or 'de'")
        
    