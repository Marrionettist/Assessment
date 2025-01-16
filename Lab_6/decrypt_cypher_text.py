def decrypt_cypher_text(text, key):
  
    decrypted_text = ""

    # Loop through each character in the text
    for char in text:
        # Convert the character to its ASCII code
        ascii_code = ord(char)

        # Subtract the key and apply modulo 256
        decrypted_ascii = (ascii_code - key) % 256

        # Convert the decrypted ASCII code back to a character
        decrypted_char = chr(decrypted_ascii)

        # Append the decrypted character to the result string
        decrypted_text += decrypted_char

    return decrypted_text


# Testing the function with the provided encrypted text and key = 3
encrypted_text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorsh"
key = 3
decrypted_text = decrypt_cypher_text(encrypted_text, key)
print(decrypted_text)
