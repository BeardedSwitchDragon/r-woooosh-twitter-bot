import praw
import pickle
def authenticateReddit():
    reddit = praw.Reddit(
        client_id="client id here",
        client_secret="client secret here",
        password="password_here",
        user_agent="upload content to twitter",
        username="username_here"
        )
    return reddit





def fetchSubmission():
    redditApi = authenticateReddit()

    subreddit = redditApi.subreddit("woooosh")

    #'Cleans' urls from invisible text and loads them from file
    post_urls = []

    try:
        post_files = open("previousPost.txt", "rb")
        temp_urls = pickle.load(post_files)
        for url in temp_urls:
            print(url)
            post_urls.append(url)
    except:
        print("is empty")

    clean_post_urls = []
    for url in post_urls:
        print(url)
        if len(url) == 35:
            clean_post_urls.append(url[url.index("h"):35])
    post_urls = clean_post_urls
    #35: the character length of reddit image urls
    print(post_urls)
    count = 0
    MAX_iterable = 20
    #Goes through top 10 subreddit posts and returns the best one that hasn't been saved earlier.
    for submission in subreddit.top("day"):

        count += 1
        current_url = submission.__dict__["url"]
        current_url = current_url[current_url.index("h"):35]
        #print(submission.__dict__["url"])
        if count >= MAX_iterable:
            break
        if (current_url in post_urls):
            print(current_url in post_urls)
            print(repr(post_urls[0]))
            continue

        elif (current_url in post_urls) == False:
            print(current_url in post_urls)
            post_urls.append(current_url)
            print(current_url)
            post_files = open("previousPost.txt", "wb")
            pickle.dump(post_urls, post_files)
            post_files.close()

            print("NAME: " + submission.author.name)
            print()
            return  submission



