import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError

# HTTP --> VERBS --> GET, POST, DELETE, PUT, PATCH, HEAD

# JSON --> JavaScript Object Notation --> {key: value pairs}

# 1- Basic request:

# The URL we want to request data from (using a public testing API)
url = "https://jsonplaceholder.typicode.com/posts/1"

# 1. Make the GET request
response = requests.get(url)

# 2. Check the Status Code (200 means OK, 404 means Not Found, etc.)
# print(f"Status Code: {response.status_code}")

# 3. Accessing the Response Data
# .text returns the response as a unicode string
# print("\nResponse Body (Text):")
# print(response.text)

# .json() converts the JSON response directly into a Python dictionary
# This is the preferred method for modern APIs
# data = response.json()
# print("\nParsed JSON Data:")
# print(data)
# print(f"Title: {data['title']}")

# 2- Passing Parameters (Query Strings):

search_url = "https://jsonplaceholder.typicode.com/posts"

# Define parameters as a dictionary
# This will automatically create: .../posts?userId=1
query_params = {
    "userId": 1,
    "id": 101
}

response = requests.get(search_url, params=query_params)
# Result will be: "https://jsonplaceholder.typicode.com/posts?userId=1"

# Verify the URL that was actually requested
print(f"Requested URL: {response.url}")

# Check how many items we got back
# data = response.json()
# print(f"Number of posts found: {len(data)}")
#
# print(f"data = {response.text}")

# 3- Making a POST Request (Sending Data):

post_url = "https://jsonplaceholder.typicode.com/posts"
#
# # The data we want to send to the server
# new_post = {
#     "title": "Learning Python Requests",
#     "body": "This is a comprehensive lesson.",
#     "userId": 1
# }
#
# # We use the 'json' parameter to automatically serialize the dict to a JSON string
# # and set the correct Content-Type header.
# response = requests.post(post_url, json=new_post)
#
# # 201 is the standard HTTP status code for "Created"
# print(f"Status Code: {response.status_code}")
# print("Server Response:", response.json())

# 4- Custom Headers:

# Define custom headers
# headers = {
#     "User-Agent": "MyPythonApp/1.0",
#     "Authorization": "Bearer YOUR_ACCESS_TOKEN_HERE" # Common for APIs
# }
#
# response = requests.get(post_url, headers=headers)
#
# print(f"response.headers = {response.headers}")
# print(f"response.text = {response.text}")


# # 5- Robust Error Handling:

error_url = "https://jsonplaceholder.typicode.com/nonexistent-page"

try:
    # 'timeout' is CRITICAL. Without it, your code can hang indefinitely if the server freezes.
    # It waits 5 seconds for a response before giving up.
    response = requests.get(error_url, timeout=5)

    # This will raise an HTTPError if the status code is 4xx or 5xx
    response.raise_for_status()

    print("Success!", response.json())

except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # e.g., 404 Not Found
except ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")  # e.g., DNS failure, refused connection
except Timeout as timeout_err:
    print(f"The request timed out: {timeout_err}")
except Exception as err:
    print(f"An unexpected error occurred: {err}")