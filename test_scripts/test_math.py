from educhain.core.config import LLMConfig
from educhain.engines.qna_engine import QnAEngine

llm_config = LLMConfig(
    api_key="",
    model_name="gpt-4o-mini",
    temperature=0.7,
    max_tokens=500
)

engine = QnAEngine(llm_config=llm_config)

topic = "Linear Algebra"

num_questions = 5
response = engine.generate_mcq_math(
    topic=topic,
    num=num_questions,
    output_format="pdf"
)

print(response)

print("Generated MCQ Math Questions:")
for question in response.questions:
    print(f"Question: {question.question}")
    print("Options:")
    for option in question.options:
        print(f" - {option.text} {'(Correct)' if option.correct == 'true' else ''}")
    print(f"Explanation: {question.explanation}\n")
