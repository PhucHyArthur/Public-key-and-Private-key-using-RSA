import tkinter as tk
import rsa

def encrypt_and_decrypt_message():
    message = message_entry.get()
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
    encrypted_message_text.set(encrypted_message)
    decrypted_message_text.set(decrypted_message)

# Tạo cặp khóa
public_key, private_key = rsa.newkeys(1024)

# Tạo giao diện chính
root = tk.Tk()
root.title("RSA Encryption Demo")

# Tạo giao diện gởi tin nhắn
send_message_frame = tk.Frame(root)
send_message_frame.pack()

message_label = tk.Label(send_message_frame, text="Enter message to encrypt:")
message_label.pack()

message_entry = tk.Entry(send_message_frame)
message_entry.pack()

encrypt_and_decrypt_button = tk.Button(send_message_frame, text="Encrypted Message", command=encrypt_and_decrypt_message)
encrypt_and_decrypt_button.pack()

encrypted_message_text = tk.StringVar()
encrypted_message_label = tk.Label(send_message_frame, text="Encrypted Message:")
encrypted_message_label.pack()
encrypted_message_display = tk.Label(send_message_frame, textvariable=encrypted_message_text)
encrypted_message_display.pack()

# Tạo đoạn tin nhắn nhận được và đoạn tin nhắn đã mã hóa
receive_message_frame = tk.Frame(root)
receive_message_frame.pack()

decrypted_message_text = tk.StringVar()
decrypted_message_label = tk.Label(receive_message_frame, text="Decrypted Message:")
decrypted_message_label.pack()
decrypted_message_display = tk.Label(receive_message_frame, textvariable=decrypted_message_text)
decrypted_message_display.pack()

root.mainloop()
