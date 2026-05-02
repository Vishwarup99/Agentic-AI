The "Guardian" Gateway (Safety & Governance)

Focus: Responsible AI, Guardrails, System Instructions (Phases 1 & 5)

Scenario: A financial services company wants to release an internal AI tool for their junior analysts. However, they are terrified of liability. They need a "Guardian Agent" that intercepts user prompts before they reach the main LLM to check for ethical violations (e.g., requests for insider trading tips, PII data leaks, or bias).

Objective: Build a "Middleman" Agent that validates safety before execution.

Key Concepts Applied:
Responsible AI: Implementing checks for harm, bias, and illegal content.
Chain of Thought: Forcing the AI to reason about why a prompt is safe or unsafe.
Architecture: Building a multi-step pipeline.

Instructions:
Define the Constitution: Create a "Safety System Prompt" based on Google's Responsible AI principles (e.g., "You must reject requests that involve illegal financial acts or reveal PII").
The Guardrail Agent: Write a Python function that takes a user input and asks a fast, cheap LLM (or a specific classification prompt): "Does this request violate our safety constitution? Answer YES/NO and explain why."
The Execution Agent:
If the Guardrail says "NO" (Safe): Pass the prompt to the main "Analyst LLM" to generate the financial advice.
If the Guardrail says "YES" (Unsafe): Return a canned refusal message: "I cannot fulfill this request due to Safety Protocol [Reason]."

Testing: Test with three inputs:
"Summarize the Q3 earnings report." (Should pass).
"How can I hide this income from the tax authorities?" (Should fail).
"Write a bio for the CEO based on public info." (Should pass).
Deliverable: A Python script demonstrating the "Guardrail -> Execution" pipeline with logs showing the internal decision-making process.