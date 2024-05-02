# main.py
from .instagram_api import get_user_pages, get_page_access_token
from .message_handler import process_message


def main():
    # Main function to run the bot
    # Setup code will go here

    # Example of an infinite loop to keep the bot running
    while True:
        # Here you would have code to check for new messages

        # Placeholder for message processing
        message = "test"  # Replace this with actual message fetching logic
        process_message(message)


if __name__ == "__main__":
    main()
