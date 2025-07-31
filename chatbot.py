import re

def simple_ai_chatbot(user_input, category):
    user_input = user_input.lower().strip()

    # Support switching categories mid-chat
    if "switch to healthcare" in user_input:
        return "Switching to healthcare category.", 1
    elif "switch to general" in user_input:
        return "Switching to general chatbot category.", 2

    if category == 1:  # Healthcare
        if re.search(r"\b(hello|hi|hey|good morning|good evening)\b", user_input):
            return "Hi there! What health topic would you like to discuss today?"
        if  any(keyword in user_input for keyword in ["cold", "common cold"]):
            return "The common cold typically comes with a scratchy throat, mild fever, watery eyes, and frequent sneezing. Always remember to rest and drink plenty of fluids."
        if any(keyword in user_input for keyword in ["diabetes", "type 1 diabetes", "type 2 diabetes"]):
            return "Warning signs of diabetes often include excessive thirst, constant hunger, frequent urination, and feeling tired all the time. Please consult your doctor for medical advice."
        if any(keyword in user_input for keyword in ["flu", "influenza"]):
            return "Flu usually starts suddenly, causing high fever, chills, sore muscles, and a persistent cough. If symptoms worsen, reach out to a medical provider."
        if any(keyword in user_input for keyword in ["high blood pressure", "hypertension"]):
            return "High blood pressure is called the 'silent killer' because it usually has no symptoms, but can lead to severe headaches or vision problems. Regular check-ups are important."
        if any(keyword in user_input for keyword in ["depression", "sadness", "mental health"]):
            return "Depression involves prolonged sadness, lack of interest, or hopelessness. Support from mental health professionals, therapy, and sometimes medication can help manage it."
        if any(keyword in user_input for keyword in ["chickenpox", "varicella"]):
            return "Chickenpox causes itchy blisters, fever, and tiredness. It usually resolves on its own, but rest, hydration, and calamine lotion help. Avoid scratching and stay isolated."
        if any(keyword in user_input for keyword in ["migraine", "severe headache"]):
            return "Migraine is a recurring headache, often with nausea or light sensitivity. Identify triggers like stress or certain foods and use doctor-prescribed medication for relief."


            
        elif "return" in user_input or "back" in user_input:
            return "Returning you to the main menu."
        else:
            return "I'm sorry, I don't have information on that. Could you rephrase or ask about another health topic?"

    elif category == 2:  # General Chatbot
        if any(keyword in user_input for keyword in ["who are you", "what are you"]):
            return "I'm your helpful assistant chatbot, created to guide you with health facts and simple support."
        elif any(keyword in user_input for keyword in ["help", "features", "commands", "what can you do"]):
            return "You can ask me basic health questions or general queries about how I work! My main goal is to provide straightforward information."
        elif any(keyword in user_input for keyword in ["thank you", "thanks"]):
            return "No problem! If you need to know anything else, just let me know."
        elif any(keyword in user_input for keyword in ["joke", "tell me a joke"]):
            return "Here's a quick joke: Why did the math book look sad? Because it had too many problems!"
        elif "return" in user_input or "back" in user_input:
            return "Returning you to the main menu."
        else:
            return "Hmm, I'm not sure how to help with that. Try asking something else or use keywords like 'symptoms' or 'help'."

print("-----WELCOME-----")
print("Choose a category:")
print("1. Healthcare-related queries")
print("2. General queries regarding Chatbot")
category_choice = input("Enter '1' for healthcare or '2' for general: ").strip()

if category_choice not in ['1', '2']:
    print("Invalid choice. Exiting.")
else:
    category_choice = int(category_choice)
    while True:
        user_input = input("Enter query or input (type 'exit' to end): ").strip()

        if user_input.lower() == "exit":
            print("🤖: Goodbye!")
            break

        response = simple_ai_chatbot(user_input, category_choice)

        # If response is a tuple, update category
        if isinstance(response, tuple):
            print("🤖:", response[0])
            category_choice = response[1]
        else:
            print("🤖:", response)

        # Return to main menu if user requested it
        if isinstance(response, str) and "returning you to the main menu" in response.lower():
            print("-----WELCOME-----")
            print("Choose a category:")
            print("1. Healthcare-related queries")
            print("2. General queries regarding Chatbot")
            category_choice = input("Enter '1' for healthcare or '2' for general: ").strip()
            if category_choice not in ['1', '2']:
                print("Invalid choice. Exiting.")
                break
            else:
                category_choice = int(category_choice)