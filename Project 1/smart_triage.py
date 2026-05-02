"""
Smart Triage Customer Service Agent
-----------------------------------
Processes customer emails using an LLM to:
- Categorize (Refund / Tech Support / General)
- Score sentiment (1–10)
- Extract Order ID
- Escalate angry customers
- Generate replies for others
- Save results to CSV

"""

import json
import pandas as pd
from openai import OpenAI

client = OpenAI(api_key="")

#  Dummy Emails
emails = [
    "Hi, I want to return my headphones. Order ID: TG12345. They stopped working after a week.",
    
    "Hello, can you help me set up my new keyboard? I can't get the RGB lights to work.",
    
    "Where is my order TG54321? It was supposed to arrive yesterday.",
    
    "This is ridiculous! My laptop (Order TG99999) arrived damaged and no one is responding. I am extremely angry and want a refund NOW!",
    
    "Do you offer discounts for bulk purchases of gaming mice?"
]

#  System Prompt
SYSTEM_PROMPT = """
You are an AI customer support analyst.

Analyze the given customer email and respond ONLY in valid JSON format with the following fields:
- Category: (Refund, Tech Support, General)
- Sentiment_Score: integer from 1 (furious) to 10 (happy)
- Order_ID: Extract if present, else "N/A"

Rules:
- Angry or aggressive language → Sentiment_Score between 1-3
- Neutral questions → 4-7
- Positive tone → 8-10
- Return ONLY JSON. No explanation.
"""

#  Analyze Email
def analyze_email(email):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": email}
            ],
            temperature=0
        )

        content = response.choices[0].message.content
        return json.loads(content)

    except Exception as e:
        print(f"Error analyzing email: {e}")
        return None


#  Generate Reply
def generate_reply(email):
    try:
        prompt = f"""
Write a polite and helpful customer service reply to the following email:

{email}

Keep it professional and concise.
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating reply: {e}"


#  Main Processing Function
def process_emails(email_list):
    results = []

    for email in email_list:
        print(f"Processing: {email[:50]}...")

        analysis = analyze_email(email)

        if not analysis:
            continue

        category = analysis.get("Category", "Unknown")
        sentiment = analysis.get("Sentiment_Score", 5)
        order_id = analysis.get("Order_ID", "N/A")

        #  Agent Logic
        if sentiment < 3:
            action = "Escalate"
            reply = "ALERT: Escalating to Human Manager."
            print(" Escalation triggered")
        else:
            action = "Respond"
            reply = generate_reply(email)

        results.append({
            "Email": email,
            "Category": category,
            "Sentiment_Score": sentiment,
            "Order_ID": order_id,
            "Action": action,
            "Reply": reply
        })

    return results


#  Save Results
def save_to_csv(results, filename="smart_triage_results.csv"):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"\n Results saved to {filename}")


# Entry Point
if __name__ == "__main__":
    print("Starting Smart Triage Agent...\n")

    processed_results = process_emails(emails)

    save_to_csv(processed_results)

    print("\n Processing Complete!")