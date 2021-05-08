import requests, re

HN = "https://hacker-news.firebaseio.com/v0"


# Items functions
def get_item(item_id):
    return requests.get(HN+"/item/"+str(item_id)+".json").json()


def get_max_item_id():
    return requests.get(HN+"/maxitem.json").content


def get_max_item():
    max_item_id = get_max_item_id()
    return get_item(max_item_id)


def get_top_n_items(n=1):
    max_item_id = int(get_max_item_id())

    stories = []
    for item_id in range(max_item_id, max_item_id-n, -1):
        stories.append(get_item(str(item_id)))
    return stories


# User
def get_user(user):
    return requests.get(HN + "/user/" + user + ".json").json()


# Comments
def get_comments(post, n=None):
    return [get_item(kid) for kid in post['kids'][:n]]


# Who's hiring
def get_all_who_is_hiring_posts():
    return get_user("whoishiring")


def is_who_is_hiring_post(post):
    return re.search('Who is hiring?', post['title']) is not None


def get_last_n_job_postings(n=1):
    all_who_is_hiring_posts = get_all_who_is_hiring_posts()

    idx = 0
    num_job_posts = 0
    job_posts = []

    while num_job_posts < n:
        post_id = all_who_is_hiring_posts['submitted'][idx]
        post = get_item(post_id)
        if is_who_is_hiring_post(post):
            job_posts.append(post)
            num_job_posts += 1
        idx += 1
    return job_posts


def search_comments(post, search_string, max_num_comments=None):
    comments = get_comments(post, max_num_comments)
    return [comment for comment in comments if re.search(search_string, comment['text'])]
