import requests
from config import FACEBOOK_ACCESS_TOKEN


def get_user_pages() -> str:
    """
    Fetches the user's pages using the access token from the environment and returns the first page's ID.

    :return: The page ID if successful, empty string otherwise.
    """
    url = f"https://graph.facebook.com/v9.0/me/accounts?access_token={FACEBOOK_ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()

    print(f"Response Status Code: {response.status_code}")
    print(f"Response Data: {data}")

    if "data" in data and len(data["data"]) > 0:
        first_page = data["data"][0]
        page_id = first_page["id"]
        print(f"Page ID: {page_id}, Page Name: {first_page['name']}")
        return page_id
    else:
        print("No pages found or failed to retrieve page information.")
        return ""


def get_page_access_token(page_id: str) -> str:
    """
    Fetches the page access token for the given page ID using the environment's access token.

    :param page_id: The ID of the Facebook Page.
    :return: The page access token if successful, empty string otherwise.
    """
    url = f"https://graph.facebook.com/{page_id}?fields=access_token&access_token={FACEBOOK_ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()

    if "access_token" in data:
        page_access_token = data["access_token"]
        print(f"Page Access Token: {page_access_token}")
        return page_access_token
    else:
        print("Failed to retrieve Page Access Token.")
        return ""


# Example usage
if __name__ == "__main__":
    # Get user pages and extract the page ID
    page_id = get_user_pages()
    # Get page access token using the page ID
    if page_id:
        get_page_access_token(page_id)
