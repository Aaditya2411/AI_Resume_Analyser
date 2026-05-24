responses = {
    "hello": "Hi! Welcome to AI Career Bot.",
    "how are you": "I'm fine! How can I help you?",
    "jobs": "Upload your resume to get job recommendations.",
    "python": "Python is great for AI, Data Science, and Web Development.",
    "java": "Java is widely used for backend and Android development.",
    "html": "HTML is used to create webpages.",
    "css": "CSS is used for webpage styling.",
    "javascript": "JavaScript makes webpages interactive.",
    "ai": "Artificial Intelligence is the future technology.",
    "machine learning": "Machine Learning allows systems to learn from data.",
    "bye": "Goodbye!"
}

def get_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Sorry, I don't understand."