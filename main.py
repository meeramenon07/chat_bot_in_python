#create a chat bot 
def chatbot_responder(user_msg):
  user_msg = user_msg.lower()
  if user_msg == "hello" or user_msg =="hi":
    return "Hello!. How may I help you?"
  elif user_msg =="information please":
    return "Sure, what information can I help you with today?"
  elif user_msg ==  "name please":
    return " I am a simple chatbot without any name! But I could answer your queries."
  elif user_msg == "later":
    return " Okay,Have a good day!"
  else:
    return " I am sorry,  I don't understand that."

print("Welcome to the chatbot. Type 'bye' to exit.")
while True:
  user_msg = input("User: ")
  if user_msg.lower() == "bye":
    print("chatbot: Goodbye, Have a great day ahead!")
    break
  response = chatbot_responder(user_msg)
  print(f"Chatbot: {response}")

  
