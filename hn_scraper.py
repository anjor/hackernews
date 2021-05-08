from utils import get_item, get_all_who_is_hiring_posts

if __name__ == '__main__':
    post_ids = get_all_who_is_hiring_posts()['submitted']
    post_ids.sort(reverse=True)
    latest_post = get_item(post_ids[0])
    comment_ids = latest_post['kids']

    for comment_id in comment_ids:
        print(get_item(comment_id))

