# loyalty_balance.py
import json
import requests
from openai import OpenAI
from config import (
    OPENAI_API_KEY,
    LOYALTY_GATOR_USER_ID,
    LOYALTY_GATOR_USER_PASSWORD,
    LOYALTY_GATOR_ACCOUNT_ID,
    LOYALTY_GATOR_CAMPAIGN_ID,
)

# Initialize OpenAI client with your API key
client = OpenAI(api_key=OPENAI_API_KEY)


def fetch_customer_balance(email):
    """
    Fetches the customer balance from the Loyalty Gator API.

    :param email: The customer's email to query the balance.
    :return: The balance of the customer or an error message if failed.
    """
    url = "https://api.clienttoolbox.com"

    data = {
        "user_id": LOYALTY_GATOR_USER_ID,
        "user_password": LOYALTY_GATOR_USER_PASSWORD,
        "account_id": LOYALTY_GATOR_ACCOUNT_ID,
        "type": "customer_search",
        "campaign_id": LOYALTY_GATOR_CAMPAIGN_ID,
        "card_number": email,  # Assuming the email can be used as card_number
        "output": "JSON",
        "include_balances": "Y",
    }

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Will raise an exception for 4XX/5XX errors
        response_data = response.json()
        if response_data["customers"]:
            balance = response_data["customers"][0]["campaigns"][0]["balance"]
            return f"Your loyalty balance is {balance}."
        else:
            return "Customer not found."
    except requests.RequestException as e:
        return "Sorry, an error occurred while fetching your loyalty balance."
    except json.decoder.JSONDecodeError:
        return "Sorry, an error occurred while processing the response."
    except KeyError as e:
        return "Sorry, an error occurred while accessing your loyalty balance."
    except Exception as e:
        return "Sorry, an unexpected error occurred."


# The rest of your existing loyalty_balance.py code with modifications for tool specifications

# Tool specification for ChatGPT to use
tools = [
    {
        "type": "function",
        "function": {
            "name": "fetch_customer_balance",
            "description": "Get the loyalty balance for a given customer's email address.",
            "parameters": {
                "email": {
                    "type": "string",
                    "description": "The customer's email address to check balance",
                }
            },
            "returns": {
                "type": "string",
                "description": "The loyalty balance as a string message",
            },
        },
    }
]

# Initialize the conversation history with a system message
conversation_history = [
    {
        "role": "system",
        "content": "You are a helpful assistant who can help customers check their loyalty program balances. When a customer provides their email address, use the fetch_customer_balance function to retrieve their balance. Provide a conversational response to the customer based on the balance value.",
    }
]

while True:
    # Prompt the user for input
    user_input = input("User: ")
    conversation_history.append({"role": "user", "content": user_input})

    # Generate a response using the OpenAI chat completion API, including tool specifications
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=conversation_history,
        tools=tools,
    )
    assistant_message = completion.choices[0].message

    # Check if there is a function call in the tool_calls array
    if assistant_message.tool_calls:
        for tool_call in assistant_message.tool_calls:
            if tool_call.function.name == "fetch_customer_balance":
                arguments = json.loads(tool_call.function.arguments)
                email = arguments["email"]
                balance = fetch_customer_balance(email)
                conversation_history.append(
                    {
                        "role": "function",
                        "name": tool_call.function.name,
                        "content": balance,
                    }
                )
                break
        else:
            print("Function not recognized.")

    # Generate a response from the assistant based on the updated conversation history
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=conversation_history,
    )
    assistant_response = completion.choices[0].message.content
    print(f"Assistant: {assistant_response}")

    # Add the assistant's response to the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_response})
