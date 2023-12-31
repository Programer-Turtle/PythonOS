bots_name = "Python OS Chat Bot" #Put bots name

Bots_unknown_responses = [
    "I'm sorry, I don't understand.",
    "I am still learning and didn't quite get that.",
    "Sorry, I didn't catch that."
] #List of what bot might say if it dosn't understand the prompt

ChatData = [
    [["hello", "hi", "hey"], f"Hello! I'm {bots_name}, an AI chatbot. How can I assist you today?", f"Hi, I'm {bots_name}. How can I help you?"],
    [["what", "are", "you", "who", "are", "you"], f"I am {bots_name}, an AI chatbot. What would you like to talk about?"],
    [["how", "are", "you", "what's", "up", "how", "is", "your", "day"], "I'm doing well, thank you! How about you? Is there anything specific you'd like to chat about?"],
    [["tell", "me", "a", "joke", "do", "you", "know", "any", "jokes"], "Sure, here's one for you: Why don't scientists trust atoms? Because they make up everything!"],
    [["favorite", "movie", "what's", "your", "favorite", "movie"], "I don't have a favorite movie, but I can recommend some popular ones. What genre are you interested in?"],
    [["favorite", "hobby", "what", "do", "you", "like", "to", "do"], "As an AI, I don't have hobbies in the same way humans do. However, I enjoy learning new things and assisting users like you!"],
    [["sports", "do", "you", "like", "sports"], "I don't have personal preferences, but I can provide information about various sports. Is there a particular sport you want to know more about?"],
    [["how", "are", "you", "how", "is", "your", "day"], "My day was good.", "It was great!", "I had a good day."],
    [["goodbye", "bye", "take", "care"], "Goodbye! It was nice chatting with you. If you have more questions in the future, feel free to ask. Take care!"],
    [["weather", "what's", "the", "weather", "like", "how's", "the", "weather"], "The weather is always changing. Where are you located? I can check the weather for you."],
    [["music", "what's", "your", "favorite", "music", "genre"], "As an AI, I don't have personal preferences for music. However, I can recommend popular genres like pop, rock, hip-hop, or classical. What type of music do you enjoy?"],
    [["technology", "what's", "the", "latest", "technology", "news"], "There have been exciting developments in the field of technology recently. From artificial intelligence to blockchain, there's a lot to explore. Is there a specific topic you're interested in?"],
    [["travel", "tell", "me", "about", "your", "favorite", "travel", "destination"], "While I don't have personal travel experiences, I can provide information about various travel destinations. Where would you like to learn more about?"],
    [["food", "what's", "your", "favorite", "food", "cuisine"], "As an AI, I don't have a favorite food. However, I can suggest popular cuisines like Italian, Chinese, Indian, or Mexican. What type of cuisine do you enjoy?"],
    [["science", "do", "you", "like", "science"], "Science is fascinating! From physics to biology and everything in between, there's so much to explore. Is there a specific scientific topic you're curious about?"],
    [["books", "recommend", "me", "a", "book"], "Certainly! What genre of books do you enjoy? Mystery, romance, fantasy, or something else?"],
] #Chat data. With everylist the list inside of it is every word the person would say than the text after will randomly select one string than return it