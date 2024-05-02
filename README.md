# loyalty_function_calling
A repository of my loyalty program function calling program

## The program consists of two main files:

1. `single_customer_search.py`: This file contains the `fetch_customer_balance` function, which interacts with the Loyalty Gator API to retrieve a customer's loyalty balance.
2. `main.py`: This file is the main script that integrates the OpenAI API with the `fetch_customer_balance` function, allowing users to have a conversation with the chatbot and retrieve their loyalty balance.

Let's dive into each file and explain how they work together.

`single_customer_search.py`:

1. The necessary modules, `requests` and `json`, are imported to handle HTTP requests and JSON parsing.
2. The API credentials and information (user_id, user_password, account_id, campaign_id) are defined as variables. These are used to authenticate and identify the specific loyalty program when making API requests.
3. The `fetch_customer_balance` function is defined, which takes a `card_number` parameter (the customer's email or card number) and returns the customer's loyalty balance or an error message if the request fails.
4. Inside the function, the API endpoint URL is defined as `url`.
5. A dictionary called `data` is created, containing the necessary parameters for the API request, such as the API credentials, customer information, and output format.
6. The function uses a `try-except` block to handle potential errors during the API request and response processing.
7. A POST request is sent to the API endpoint using `requests.post()`, passing the `url` and `data` parameters.
8. If the request is successful, the response data is parsed from JSON to a Python dictionary using `response.json()`.
9. The function checks if the `customers` key exists in the response data and if it's not empty. If a customer is found, it extracts the loyalty balance from the response data and returns a formatted string containing the balance.
10. If no customer is found, the function returns "Customer not found."
11. If any errors occur during the API request or response processing, appropriate error messages are returned.
12. At the end of the file, there's a test block that demonstrates how to use the `fetch_customer_balance` function by calling it with a test email and printing the result.

`main.py`:

1. The necessary modules, `json`, `OpenAI`, and the `fetch_customer_balance` function from `single_customer_search.py`, are imported.
2. An instance of the OpenAI client is created with the provided API key.
3. The `tools` variable is defined, which contains the specification for the `fetch_customer_balance` function that the chatbot can use. It includes the function name, description, and parameter details.
4. The conversation history is initialized with a system message that defines the chatbot's purpose and behavior.
5. The main loop starts, which continuously prompts the user for input and generates responses using the OpenAI chat completion API.
6. The user's input is appended to the conversation history as a message with the "user" role.
7. The `client.chat.completions.create()` method is called, passing the conversation history, tools, and the specified model ("gpt-4-turbo") to generate a response from the chatbot.
8. The assistant's message is extracted from the API response.
9. The script checks if there are any function calls in the `tool_calls` array of the assistant's message.
10. If a function call exists and its name matches "fetch_customer_balance", the email address is extracted from the function arguments by parsing the JSON string.
11. The `fetch_customer_balance` function is called with the extracted email, and the balance response is obtained.
12. The balance response is appended to the conversation history as a message with the "function" role, along with the function name.
13. The balance response is printed as the assistant's response.
14. If no function call is recognized, the assistant's response is printed as is.
15. The assistant's response is appended to the conversation history as a message with the "assistant" role.
16. The loop continues, allowing the user to have a continuous conversation with the chatbot.

In summary, the `single_customer_search.py` file handles the interaction with the Loyalty Gator API to retrieve customer balances, while the `main.py` file integrates the OpenAI API to create a conversational chatbot that can assist users and retrieve their loyalty balances when provided with an email address.

## The program flow goes like this:

1. The user starts the conversation by running the `main.py` script and entering a message.
2. The user's message is appended to the conversation history, and the OpenAI API is called to generate a response from the chatbot.
3. If the chatbot's response includes a function call to "fetch_customer_balance", the email address is extracted from the function arguments.
4. The `fetch_customer_balance` function from `single_customer_search.py` is called with the extracted email address to retrieve the customer's loyalty balance from the Loyalty Gator API.
5. The balance response is appended to the conversation history and printed as the assistant's response.
6. If no function call is recognized, the chatbot's response is printed as is.
7. The conversation continues until the user ends the program.
