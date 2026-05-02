Project 1: The "Smart Triage" Customer Service Agent

Focus: Prompt Engineering, Python Logic, API Integration (Phases 2 & 4)

Scenario: You have been hired by an e-commerce company, "TechGear," that is drowning in customer support emails. They need an AI agent that can automatically read incoming messages, categorize them, extract key details (Order IDs), and draft a response only if the sentiment is not extremely negative. If the customer is furious, the agent must escalate the ticket to a human manager.

Objective: Build a Python script that uses the OpenAI API (or a similar high-quality LLM) to process a batch of raw customer emails.

Key Concepts Applied:
Prompt Engineering: Designing a system prompt that enforces specific output formatting (JSON).
NLP with Python: String manipulation to parse the AI's output.
Logic Flow: If/Else logic based on the AI's analysis (Agentic decision making).

Instructions:
Setup: Create a list of 5 dummy customer emails (mix of refund requests, technical questions, and one "angry" complaint).
The Brain (Prompting): Write a prompt that instructs the LLM to analyze text and output a JSON object containing:
Category (Refund, Tech Support, General).
Sentiment_Score (1 to 10, where 1 is furious and 10 is happy).
Order_ID (Extract if present, else "N/A").
The Action Loop: Write a Python function that iterates through the emails and sends them to the API.

Agent Logic:
If Sentiment_Score is < 3: Print "ALERT: Escalating to Human Manager."
Else: Have the LLM generate a polite, context-aware reply draft.
Output: Save the results to a CSV file.
Deliverable: A Python script (.py or Jupyter Notebook) and the resulting CSV file.