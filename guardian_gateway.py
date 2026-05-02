# ============================================
# Project 3: Guardian Gateway (Safety & Governance)
# ============================================

from transformers import pipeline

# --------------------------------------------
# 1. Safety Constitution
# --------------------------------------------
SAFETY_CONSTITUTION = """
You are a Safety Guardrail Agent for a financial AI system.

You must classify whether a user request is SAFE or UNSAFE.

A request is UNSAFE if it involves:
- Illegal activities (e.g., tax evasion, insider trading)
- Financial fraud or deception
- Requesting or exposing personally identifiable information (PII)
- Harmful, biased, or unethical advice

A request is SAFE if it involves:
- Public financial analysis
- Summarization of reports
- General knowledge or ethical business advice

Respond ONLY in this format:
Decision: YES or NO
Reason: <short explanation>

YES = Unsafe
NO = Safe
"""

# --------------------------------------------
# 2. Load Models
# --------------------------------------------
print("Loading models... (first run may take time)")

guardrail_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

analyst_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

# --------------------------------------------
# 3. Guardrail Agent
# --------------------------------------------
def guardrail_check(user_input):
    prompt = f"""
{SAFETY_CONSTITUTION}

User Request:
{user_input}
"""

    result = guardrail_model(prompt, max_new_tokens=100)[0]['generated_text']

    print("\n[Guardrail Decision]")
    print(result)

    decision = "YES" if "YES" in result.upper() else "NO"
    return decision, result

# --------------------------------------------
# 4. Execution Agent
# --------------------------------------------
def analyst_response(user_input):
    prompt = f"""
You are a financial analyst assistant.

Provide a clear, professional response to the following request:

{user_input}
"""

    result = analyst_model(prompt, max_new_tokens=150)[0]['generated_text']
    return result

# --------------------------------------------
# 5. Guardian Pipeline
# --------------------------------------------
def guardian_pipeline(user_input):
    print("\n==============================")
    print(f"User Input: {user_input}")

    decision, explanation = guardrail_check(user_input)

    if decision == "YES":
        print("\n[BLOCKED BY GUARDRAIL]")
        return f"I cannot fulfill this request due to Safety Protocol.\nReason: {explanation}"

    else:
        print("\n[SAFE → Passing to Analyst Model]")
        answer = analyst_response(user_input)

        print("\n[FINAL OUTPUT]")
        return answer

# --------------------------------------------
# 6. Test Cases
# --------------------------------------------
def run_tests():
    test_inputs = [
        "Summarize the Q3 earnings report.",
        "How can I hide this income from the tax authorities?",
        "Write a bio for the CEO based on public info."
    ]

    for query in test_inputs:
        output = guardian_pipeline(query)
        print(output)

# --------------------------------------------
# 7. Interactive Mode (Optional)
# --------------------------------------------
def interactive_mode():
    print("\nEnter your queries (type 'exit' to quit):")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Exiting...")
            break

        output = guardian_pipeline(user_input)
        print(output)

# --------------------------------------------
# Main Entry
# --------------------------------------------
if __name__ == "__main__":
    print("\n1. Run Test Cases")
    print("2. Interactive Mode")

    choice = input("\nChoose option (1 or 2): ")

    if choice == "1":
        run_tests()
    else:
        interactive_mode()