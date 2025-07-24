
---

## 🐍 `crypto_bot.py`

```python
# crypto_bot.py

# CryptoBuddy – AI-Powered Financial Sidekick

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def welcome():
    print("👋 Hey there! I’m CryptoBuddy — your AI-powered crypto sidekick!")
    print("Ask me anything like 'Which crypto is sustainable?' or 'What should I invest in for growth?'\n")

def get_recommendation(query):
    query = query.lower()

    if "sustainable" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential!")

    elif "trending" in query or "rising" in query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print("📈 Trending cryptos:", ", ".join(trending))

    elif "long-term" in query or "growth" in query:
        candidates = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["sustainability_score"] > 0.7]
        if candidates:
            print(f"🚀 Consider {candidates[0]} — it’s rising and sustainable!")
        else:
            print("😕 Hmm... no clear long-term pick at the moment.")

    elif "most profitable" in query or "best investment" in query:
        candidates = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"]
        if candidates:
            print(f"💸 Go for {candidates[0]} — high cap and rising price!")
        else:
            print("🤔 No high-performing coin meets profitability criteria right now.")

    else:
        print("❓ I didn’t get that. Try asking about sustainability, trends, or profitability.")

def chatbot():
    welcome()
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit", "bye"]:
            print("👋 Bye! Remember: crypto is risky — always DYOR (Do Your Own Research)!")
            break
        get_recommendation(query)

if __name__ == "__main__":
    chatbot()
