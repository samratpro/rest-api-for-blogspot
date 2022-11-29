

def blogger_poster(blog_id, token,post_title,post_content,label_list,meta_data = ""):
    """

    :param blog_id: input your blog id number
    :param token: input token which is generated from OAuth 2.0 Playground
    :param post_title: input post title/varibale
    :param post_content: input content variable
    :param label_list: input the list name of tag list/label list/category list
    :param meta_data:
    :return:
    """
    url= f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts"
    tokens = token
    header = {"Authorization": f'Bearer {tokens}'}


    data = {
      "kind": "blogger#post",

      "blog": {
        "id": f"{blog_id}"
      },
      "title": post_title.title(),
      "content": post_content,

      "customMetaData": meta_data,
      "labels": label_list

    }

    res = requests.post(url, json=data, headers=header)
    return (res.status_code, "=======", post_title)