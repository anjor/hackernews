from utils import *

if __name__ == '__main__':
    latest_job_post = get_last_n_job_postings()[0]
    comments = search_comments(latest_job_post, '(?i)London', 100)
    print(comments)