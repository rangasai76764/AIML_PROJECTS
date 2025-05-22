# chatbot.py

# Predefined analyzed financial data (dummy values for illustration)
financial_data = {
    "total_revenue": "$2.5 million",
    "net_income_change": "increased by $200,000",
    "operating_expenses": "$1.2 million",
    "profit_margin": "15%",
    "earnings_per_share": "$1.35"
}

# Chatbot function
def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return f"The total revenue is {financial_data['total_revenue']}."
    elif user_query == "How has net income changed over the last year?":
        return f"The net income has {financial_data['net_income_change']}."
    elif user_query == "What are the operating expenses?":
        return f"The operating expenses are {financial_data['operating_expenses']}."
    elif user_query == "What is the profit margin?":
        return f"The profit margin is {financial_data['profit_margin']}."
    elif user_query == "What is the earnings per share?":
        return f"The earnings per share is {financial_data['earnings_per_share']}."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Command-line interaction
if __name__ == "__main__":
    print("Welcome to the Finance Chatbot!")
    print("Ask a question like:\n- What is the total revenue?\n- How has net income changed over the last year?\n(Type 'exit' to quit)\n")

    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = simple_chatbot(query)
        print("Chatbot:", response)
