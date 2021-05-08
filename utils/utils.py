import requests as re

HN = "https://hacker-news.firebaseio.com/v0"


# Items functions
def get_item(item_id):
    return re.get(HN+"/item/"+str(item_id)+".json").json()


def get_max_item_id():
    return re.get(HN+"/maxitem.json").content


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
    return re.get(HN + "/user/" + user + ".json").json()


# Who's hiring
def get_all_who_is_hiring_posts():
    return get_user("whoishiring")


# To do

# parse comments from who is hiring
# search for location: London/Europe
# find the poster --> look at their other posts
