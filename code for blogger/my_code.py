import requests
API_KEY = ""    # https://developers.google.com/oauthplayground/
BLOG_ID = ""    # blogger id from backend dashboard url

# Define the URL for the Blogger API
BASE_URL = f'https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/'

# Define the post content
post_data = {
    'kind': 'blogger#post',
    'blog': {
        'id': BLOG_ID
    },
    'title': 'title',
    'content': 'post_body',
    'labels': ['category_name']
}

# Define the headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

# Send POST request to create a new post
response = requests.post(BASE_URL, headers=headers, json=post_data)


print(response)
print(response.content)
