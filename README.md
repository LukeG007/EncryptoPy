## EncryptoPy
EncryptoPy is a simple, easy, and fun encryption library written in pure python

## Useage
```python
import EncryptoPy

Encryptor = EncryptoPy.TextEncryption()

Encrypted_text = Encryptor.BasicTextEncryption("Basic Encryption", 1234, 'en')

print(Encrypted_text)

Decrypted_text = Encryptor.BasicTextEncryption(Encrypted_text, 1234, 'de')

print(Decrypted_text)

Encrypted_emoji = Encryptor.EmojiEncryption('Emoji Encryption', 'en')

print(Encrypted_emoji)

Decrypted_emoji = Encryptor.EmojiEncryption(Encrypted_emoji, 'de')

print(Decrypted_emoji)

```
