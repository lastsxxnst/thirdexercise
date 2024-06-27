import rsa

# Генерация ключей
(public_key, private_key) = rsa.newkeys(2048)

# Ваше сообщение
plaintext = input("Enter a plaintext: ")

# Шифрование
ciphertext = rsa.encrypt(plaintext.encode(), public_key)

# Дешифрование
decrypted_text = rsa.decrypt(ciphertext, private_key).decode()

print("Encrypted text:", ciphertext)
print("Decrypted text:", decrypted_text)
