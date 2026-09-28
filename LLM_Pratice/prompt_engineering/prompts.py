from llm.llm_client import ask_llm


review = "The laptop is fast and the battery life is excellent."


prompts = [

    # 1. Zero-shot
    f"""
Classify this review as Positive or Negative:

{review}
""",

    # 2. Clear zero-shot
    f"""
Classify the following review as either Positive or Negative.

Review:
{review}

Return only the classification.
""",

    # 3. Role-based prompt
    f"""
You are a sentiment classification system.

Classify the following review as Positive or Negative:

{review}

Return only the label.
""",

    # 4. Structured prompt
    f"""
Task: Sentiment Classification

Review:
{review}

Possible labels:
- Positive
- Negative

Output only one label.
""",

    # 5. One-shot
    f"""
Example:

Review: The phone is amazing.
Sentiment: Positive

Now classify:

Review: {review}
Sentiment:
""",

    # 6. Few-shot
    f"""
Example 1:
Review: The phone is amazing.
Sentiment: Positive

Example 2:
Review: The headphones stopped working.
Sentiment: Negative

Now classify:

Review: {review}
Sentiment:
""",

    # 7. Few-shot structured
    f"""
Classify the sentiment.

Examples:

Review: The camera quality is excellent.
Sentiment: Positive

Review: The screen stopped working.
Sentiment: Negative

Review: {review}
Sentiment:
""",

    # 8. Reasoning-style
    f"""
Analyze the following review carefully.

Review:
{review}

Determine whether the overall sentiment is positive
or negative.

Final answer:
""",

    # 9. Step-by-step reasoning
    f"""
Analyze the review step by step.

1. Identify the important features.
2. Determine whether each feature is positive or negative.
3. Decide the overall sentiment.

Review:
{review}

Return the final sentiment.
""",

    # 10. Production-style prompt
    f"""
You are a sentiment classification model.

Task:
Classify the review as Positive or Negative.

Review:
{review}

Rules:
- Consider the overall sentiment.
- Do not provide unnecessary explanation.
- Return exactly one label.

Output:
Positive or Negative
"""
]


for i, prompt in enumerate(prompts, start=1):

    print("\n" + "=" * 60)
    print(f"PROMPT {i}")
    print("=" * 60)

    print("\nPrompt:")
    print(prompt)

    print("\nLLM Response:")

    try:
        response = ask_llm(prompt)
        print(response)

    except Exception as error:
        print("Error:", error)