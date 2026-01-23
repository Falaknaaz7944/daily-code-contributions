mood = input("How are you feeling today? ")

if "happy" in mood.lower():
    print("😊 Keep smiling!")
elif "sad" in mood.lower():
    print("💙 It’s okay, better days are coming.")
elif "angry" in mood.lower():
    print("😤 Take a deep breath.")
else:
    print("🤔 Interesting mood!")
