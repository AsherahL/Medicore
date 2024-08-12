import streamlit as st
import random


responses = {
    "heyzz": [
        "Hi, how can I assist you today?",
        "Hey there! What's on your mind?"
    ],

    "thank you": [
        "You're welcome!",
        "Of course, feel free to ask anything else."
    ],

    "i need relationship advice": [
        "Sure, how can I help you?"
    ],

    "what if your bf of five years cheats on you what should you do?": [
        "If your boyfriend of five years cheats on you, it's important to prioritize your own well-being. Consider your feelings and whether trust can be rebuilt. It may be time to reevaluate the relationship.",
        "Dealing with infidelity is tough. Take time to process your emotions and consider what's best for you moving forward."
    ],

    "should i go to marriage counselling with my husband or continue with the divorce": [
        "Choosing between marriage counseling and divorce depends on many factors, such as your willingness to work on the relationship and whether both parties are committed to change. Understanding the root issues can guide your decision.",
        "Marriage counseling can offer a chance to work through challenges together. Consider what you hope to achieve and whether counseling aligns with your goals."
    ],

    "he cheated": [
        "Discovering infidelity can be devastating. It's important to prioritize your well-being and consider your options for moving forward, whether that involves counseling, separation, or divorce.",
        "Betrayal can shake the foundation of trust. Take time to process your emotions and consider seeking support from trusted friends or professionals.", "LEAVE HIM"
    ],

    "how can i fix my relationship?": [
        "Understanding the reasons behind the issues is crucial. Effective communication and mutual respect are key to rebuilding trust and intimacy. Consider counseling to explore these issues in a safe environment.",
        "Improving relationships often starts with open and honest communication. Reflect on what needs improvement and consider seeking professional guidance if needed."
    ],

    "i don't think i should leave him.": [
        "Consider what's keeping you in the relationship and whether it aligns with your values and well-being. It's important to prioritize your happiness and emotional health.",
        "Reflect on your reasons for staying in the relationship. Trust your instincts and seek support from loved ones or counselors if you're uncertain about your decision."
    ],

    "what are signs that it's time to end a relationship?": [
        "Signs such as consistent unhappiness, lack of trust, or incompatible values may indicate it's time to reevaluate the relationship.",
        "Feeling emotionally drained, constant conflicts, or differing life goals can be indicators that it's time to consider moving on."
    ],

}


# Streamlit app title
st.title("Ckaive Chatbot")

# Input for user message
user_input = st.text_input("Asherah:")

# Process user input
if user_input:
    if user_input.lower() in responses:
        ckaive_reply = random.choice(responses[user_input.lower()])
        st.write("Ckaive:", ckaive_reply)
    else:
        st.write("Ckaive:", "I'm sorry, I don't comprehend.")



