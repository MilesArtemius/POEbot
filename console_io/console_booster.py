from system import main_handler

message_text = input("Enter the pseudo-message text!\n")
data = {'text': message_text}

main_handler.build(data)
