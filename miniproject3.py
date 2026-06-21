# mini task of day15

import sys

try:
    import speech_recognition as sr
    import pyttsx3
    VOICE_MODE = True
except ImportError:
    sr = None
    pyttsx3 = None
    VOICE_MODE = False

menu = {
    "mocha": 150,
    "capchunio": 120,
    "latte": 100,
    "coldcoffe": 80,
    "blackcofee": 50,
}
icecream = {
    "mocha": 20,
    "capchunio": 15,
    "latte": 10,
    "coldcoffe": 5,
    "blackcofee": 0,
}
topping = {
    "mocha": 30,
    "capchunio": 25,
    "latte": 20,
    "coldcoffe": 10,
    "blackcofee": 0,
}
sugar = {
    "mocha": 10,
    "capchunio": 8,
    "latte": 5,
    "coldcoffe": 5,
    "blackcofee": 0,
}


def cafe_bill(order, quantity):
    total_price = menu[order] + icecream[order] + topping[order] + sugar[order]
    if total_price > 200:
        discount = total_price * 0.10
    else:
        discount = 0
    final_price = total_price - discount
    bill = final_price * quantity
    points = bill // 100

    print("\n--- Cafe Bill ---")
    print(f"Order: {order} x {quantity}")
    print(f"Total Price (before discount): {total_price}")
    print(f"Discount: {discount}")
    print(f"Final Price per item: {final_price}")
    print(f"Total Bill: {bill}")
    print(f"Loyalty Points Earned: {points}")
    print("-----------------")

    return bill, points


def print_menu():
    print("\n--- NISHA'S CAFE MENU ---")
    for item, price in menu.items():
        print(f"{item.title():<12} : ₹{price}")
    print("--------------------------")


def speak_text(text):
    if not VOICE_MODE:
        return
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception:
        pass


def listen_text():
    if not VOICE_MODE:
        return None
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("ChatBot: Listening... Please speak clearly.")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        print("ChatBot: Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("ChatBot: Voice service is unavailable. Please use text input.")
    return None


def chatbot():
    print("\nWelcome to NISHA'S CAFE ChatBot!")
    if VOICE_MODE:
        print("Voice mode is available. Type 'voice' to speak or 'text' for keyboard input.")
    else:
        print("Voice mode is not available. Install 'speech_recognition' and 'pyttsx3' to enable it.")
    print("Type 'menu' to see the menu, 'order <item> <qty>' to place an order, 'help' for commands, and 'exit' to leave.")

    last_order = None
    input_mode = "text"

    while True:
        if input_mode == "voice":
            spoken = listen_text()
            if spoken is None:
                continue
            user_input = spoken.strip().lower()
            print(f"You (voice): {user_input}")
        else:
            user_input = input("You: ").strip().lower()

        if not user_input:
            continue

        if user_input in {"voice", "speak"} and VOICE_MODE:
            input_mode = "voice"
            print("ChatBot: Voice mode enabled. Say 'text' to return to typing.")
            speak_text("Voice mode enabled. Say text to return to typing.")
            continue

        if user_input in {"text", "keyboard"}:
            input_mode = "text"
            print("ChatBot: Text mode enabled.")
            if VOICE_MODE:
                speak_text("Text mode enabled.")
            continue

        if user_input in {"exit", "quit", "bye"}:
            response = "Thank you for visiting NISHA'S CAFE. See you soon!"
            print(f"ChatBot: {response}")
            speak_text(response)
            break

        if user_input in {"help", "commands"}:
            response = "Available commands: menu, order <item> <qty>, price <item>, last order, exit. Say voice to enable voice mode."
            print(f"\n{response}")
            speak_text(response)
            continue

        if "menu" in user_input:
            print_menu()
            speak_text("Here is the menu.")
            continue

        if user_input.startswith("price"):
            parts = user_input.split()
            if len(parts) < 2:
                response = "Please tell me which item you want the price for, for example price mocha."
                print(f"ChatBot: {response}")
                speak_text(response)
                continue
            item = parts[1]
            if item in menu:
                item_total = menu[item] + icecream[item] + topping[item] + sugar[item]
                response = f"{item.title()} costs {menu[item]} rupees plus extras, total {item_total} before quantity and discount."
                print(f"ChatBot: {response}")
                speak_text(response)
            else:
                response = f"Sorry, we don't have {item}. Type menu to see available items."
                print(f"ChatBot: {response}")
                speak_text(response)
            continue

        if user_input.startswith("order"):
            parts = user_input.split()
            if len(parts) != 3:
                response = "Use the format order item quantity."
                print(f"ChatBot: {response}")
                speak_text(response)
                continue
            item = parts[1]
            if item not in menu:
                response = f"Sorry, {item} is not on the menu. Type menu to see the available drinks."
                print(f"ChatBot: {response}")
                speak_text(response)
                continue
            try:
                quantity = int(parts[2])
                if quantity <= 0:
                    raise ValueError
            except ValueError:
                response = "Quantity must be a positive whole number."
                print(f"ChatBot: {response}")
                speak_text(response)
                continue

            bill, points = cafe_bill(item, quantity)
            last_order = (item, quantity, bill, points)
            response = f"Your order for {item} x {quantity} has been placed. Total bill is {bill}."
            speak_text(response)
            continue

        if "last order" in user_input or ("last" in user_input and "order" in user_input):
            if last_order:
                item, quantity, bill, points = last_order
                response = f"Last order was {item} x {quantity}, total {bill}, points {points}."
                print(f"ChatBot: {response}")
                speak_text(response)
            else:
                response = "You have not placed an order yet."
                print(f"ChatBot: {response}")
                speak_text(response)
            continue

        if any(greet in user_input for greet in ["hi", "hello", "hey"]):
            response = "Hi there! I can help you order from the cafe. Type menu to get started."
            print(f"ChatBot: {response}")
            speak_text(response)
            continue

        response = "I'm sorry, I didn't understand that. Type help for commands."
        print(f"ChatBot: {response}")
        speak_text(response)


if __name__ == "__main__":
    chatbot()
