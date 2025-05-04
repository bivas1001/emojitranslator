from tkinter import *

emoji_map = {
    "love": "❤️ ",
    "angry": "😤 ",
    "happy": "😊 ",
    "sad": "😢 ",
    "laugh": "😂 ",
    "cry": "😭 ",
    "cool": "😎 ",
    "surprise": "😮 ",
    "food": "🍕 ",
    "party": "🎉 ",
    "gift": "🎁 ",
    "fire": "🔥 ",
    "ok": "👌 ",
    "clap": "👏 ",
    "thumbs up": "👍 ",
    "good night": "🌙 ",
    "good morning": "🌅 ",
    "kiss": "😘 ",
    "thinking": "🤔 ",
    "sleep": "😴 ",
    "bored": "🥱 ",
    "sick": "🤒 ",
    "music": "🎵 ",
    "run": "🏃 ",
    "dog": "🐶 ",
    "cat": "🐱 ",
    "sun": "☀️ ",
    "rain": "🌧️ ",
    "star": "⭐ ",
    "heart": "💖 ",
    "broken": "💔 ",
    "money": "💵 ",
    "idea": "💡 ",
    "phone": "📱 ",
    "computer": "💻 ",
    "book": "📚 ",
    "school": "🏫 ",
    "work": "🏢 ",
}

def get_input():
    user_input = entry.get()  
    translated_text = ""  
    
    
    user_words = user_input.split()
    
    
    for word in user_words:
        if word in emoji_map:
            translated_text += emoji_map[word]  
        else:
            translated_text += word + " "  
    result_label.config(text=translated_text)


root = Tk()
root.title("Emoji Translator")
root.geometry("400x300")  


label = Label(root, text="Enter the text:", font=("Segoe UI Emoji", 14))  
label.pack(pady=10)


entry = Entry(root, font=("Segoe UI Emoji", 14))  
entry.pack(pady=10)


button = Button(root, text="Translate", command=get_input, font=("Segoe UI Emoji", 14))
button.pack()


result_label = Label(root, text="", wraplength=350, font=("Segoe UI Emoji", 14))  
result_label.pack(pady=20)


root.mainloop()
