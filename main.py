from graph import graph

user_input = input("Ask something: ")

result = graph.invoke({
    "input": user_input,
    "decision": "",
    "output": "",
    "history": [],
    "sentiment": "",
    "fact_check": "",
    "error": ""
})

print(result["output"])  
print("Sentiment:", result["sentiment"])
print("Fact Check:", result["fact_check"])
