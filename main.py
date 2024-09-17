from fastapi import FastAPI

app = FastAPI()

@app.post("/start-negotiation")
def start_negotiation():
    return {"message": "Let's start negotiating a price."}

@app.post("/offer-price")
def offer_price(user_offer: float):
    return {"message": "Offer received."}
base_price = 100.0

def offer_price(user_offer: float, user_message: str):
    sentiment = analyze_sentiment(user_message)
    if sentiment > 0.5:
        discount = base_price * 0.05
        return {"message": f"You're polite! Here's a discount. New price: {base_price - discount}"}
    else:
        return {"message": f"No discount. The price remains {base_price}"}

import openai

openai.api_key = "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"

def get_ai_response(prompt):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text
@app.post("/offer-price")
def offer_price(user_offer: float):
    ai_response = get_ai_response(f"The user offered ${user_offer}. How should the bot respond?")
    return {"message": ai_response}
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

def analyze_sentiment(user_input: str):
    sentiment = sid.polarity_scores(user_input)
    return sentiment['compound']  # Sentiment score from -1 to 1
@app.post("/offer-price")
def offer_price(user_offer: float, user_message: str):
    sentiment = analyze_sentiment(user_message)
    if sentiment > 0.5:
        discount = base_price * 0.05
        return {"message": f"You're polite! Here's a discount. New price: {base_price - discount}"}
    else:
        return {"message": f"No discount. The price remains {base_price}"}
