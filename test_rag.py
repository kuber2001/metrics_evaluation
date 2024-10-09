from deepeval import evaluate
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase
import requests
import json
from custom import CustomB
import os
from deepeval.metrics.ragas import RagasMetric

# # Define your input and expected output
# input_text = "What is the capital of France?"
# expected_output = "The capital of France is Paris."
# actual_output= "The capital of France is Belgium."


#  FOR RAGAS
# Replace this with the actual output from your LLM application
actual_output = "We offer a 30-day full refund at no extra cost."

# Replace this with the expected output from your RAG generator
expected_output = "You are eligible for a 30 day full refund at no extra cost."

# Replace this with the actual retrieved context from your RAG pipeline
retrieval_context = ["All customers are eligible for a 30 day full refund at no extra cost."]



# Replace this with the actual output from your LLM application
actual_output = "We offer a 30-day full refund at no extra cost."

# Replace this with the actual retrieved context from your RAG pipeline
retrieval_context = ["All customers are eligible for a 30 day full refund at no extra cost."]





# Make a request to your local LM Studio instance
custom=CustomB()
metric = FaithfulnessMetric(
    threshold=0.7,
    model=custom,
    include_reason=True
)


test_case = LLMTestCase(
    input="What if these shoes don't fit?",
    actual_output=actual_output,
    retrieval_context=retrieval_context
)


# try:
#     metric = RagasMetric(threshold=0.5, model=custom)
#     # # Create a test case
#     # test_case = LLMTestCase(
#     #     input=input_text,
#     #     actual_output=actual_output,
#     #     expected_output=expected_output
#     # )
#     # Create a Test for Ragas 
#     test_case = LLMTestCase(
#     input="What if these shoes don't fit?",
#     actual_output=actual_output,
#     expected_output=expected_output,
#     retrieval_context=retrieval_context
#     )  

#     # Define metrics
#     metric.measure(test_case)
#     print(metric.score)
#     # ans_metric= AnswerRelevancyMetric(threshold=0.5,model=custom)

#     # Evaluate the test case
#     # results = evaluate([test_case], [ans_metric])
#     results = evaluate([test_case], [metric])
#     # # Print the results
#     # print("Input:", input_text)
#     # print("Expected Output:", expected_output)
#     # print("Actual Output:", actual_output)
#     # print("\nEvaluation Results:")
#     # for metric_name, metric_result in results.items():
#     #     print(f"{metric_name}:")
#     #     print(f"  Score: {metric_result.score}")
#     #     print(f"  Passed: {metric_result.passed}")
#     #     if hasattr(metric_result, 'reason'):
#     #         print(f"  Reason: {metric_result.reason}")
#     #     print()

# except Exception as e:
#     print(f"An error occurred: {str(e)}")
   
   
metric.measure(test_case)
print(metric.score)
print(metric.reason)    

# or evaluate test cases in bulk
results = evaluate([test_case], [metric])
print(results)
    
    
