import tkinter as tk
from tkinter import scrolledtext

def get_current_time():
    return datetime.now().strftime("%I:%M:%S %p")

def handle_query(query):
    if query == "what is time now":
        return "The current time is " + get_current_time()
    elif any(operator in query for operator in ['+', '-', '*', '/']):
        try:
            result = eval(query)  
            return f"The result is: {result}"
        except Exception:
            return "Sorry, I couldn't calculate that. Please enter a valid arithmetic expression."
    elif "define" in query:
        term = query.split("define ")[-1].strip()
        return get_definition(term)
    else:
        return "I'm sorry, I didn't understand your query."

def get_definition(term):
    dictionary = {
        "ambivalent": "Having mixed feelings or contradictory ideas about something or someone.",
        "ecosystem": "A biological community of interacting organisms and their physical environment.",
        "democracy": "A system of government by the whole population or all the eligible members of a state, typically through elected representatives.",
        "computer": "A machine that can be programmed to automatically carry out sequences of arithmetic or logical operations. Modern digital electronic computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks.",
        "marketing": "The process of creating, communicating, delivering, and exchanging offerings that have value for customers, clients, partners, and society at large.",
        "advertising": "A marketing tactic that involves paying for space to promote a product, service, or cause to the public. The goal of advertising is to reach people who are likely to buy a company's products or services and entice them to do so."
    }
    return f"The definition of '{term}' is: {dictionary.get(term, f'Sorry, I couldn\'t find a definition for \'{term}\'.')}"

def simple_chatbot(user_input):
    rules = {
        "hi": "Hello! How can I help you?",
        "hello": "Hello! How can I help you?",
        "how are you": "I'm just a chatbot, but I'm doing well! How about you?",
        "how r u": "I'm just a chatbot, but I'm doing well! How about you?",
        "bye": "Goodbye! Have a great day!",
        "goodbye": "Goodbye! Have a great day!",
        "time": "what is time now",  
        "who is the prime minister of india": "Mr. Narendra Modi",
        "who is the prime minister of india?": "Mr. Narendra Modi",
        "what is the capital of india?": "New Delhi"
    }
    user_input = user_input.lower()
    for rule, response in rules.items():
        if rule in user_input:
            if response == "what is time now":
                return handle_query(response)  
            return response
    return handle_query(user_input)

def send_message(event=None):
    user_input = input_box.get("1.0", "end-1c")
    input_box.delete("1.0", tk.END)
    if user_input.lower() == 'bye':
        chat_area.insert(tk.END, "You: " + user_input + "\n")
        chat_area.insert(tk.END, "ChatBot: Goodbye! Have a great day!\n")
        chat_area.see(tk.END)
    else:
        bot_response = simple_chatbot(user_input)
        chat_area.insert(tk.END, "You: " + user_input + "\n")
        chat_area.insert(tk.END, "ChatBot: " + bot_response + "\n")
        chat_area.see(tk.END)

# GUI setup
root = tk.Tk()
root.title("ChatBot by Parshwa")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_area.pack(expand=True, fill="both")

input_box = tk.Text(root, wrap=tk.WORD, width=50, height=1)
input_box.pack(side=tk.LEFT, expand=True, fill="x")

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

input_box.bind("<Return>", send_message)
input_box.focus_set()

root.mainloop()
