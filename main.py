import tweepy

API_KEY = 'xxxx'
API_SECRET = 'xxxx'
ACCESS_TOKEN = 'xxxx-xxxx'
ACCESS_TOKEN_SECRET = 'xxxx'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def follow_back_calc(screen_name):
    try:
        follower = tweepy.Cursor(api.get_follower_ids, screen_name=screen_name, count=5000, cursor = -1).items(limit=10000)
        following = tweepy.Cursor(api.get_friend_ids, screen_name=screen_name, count=5000, cursor = -1).items(limit=10000)
    except:
        return False
    follower_list = []
    for followers in follower:
        follower_list.append(followers)
    lists_a = len(follower_list)
    if lists_a == 0:
        return False
    following_list = []
    for followings in following:
        following_list.append(followings)
    lists_b = len(following_list)
    if lists_b == 0:
        return 0
    and_list = set(following_list) & set(follower_list)
    and_count = len(list(and_list))
    follower_count = len(follower_list)
    result = round(and_count / follower_count * 100, 2)
    return result
