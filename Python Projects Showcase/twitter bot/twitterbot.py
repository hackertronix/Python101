import tweepy

class TwitterAPI:
    def __init__(self):
        consumer_key = "UNgoWhTGVI2N9rEK8zhStZxIb"
        consumer_secret = "98PZlY5fzIviVenuV0sGd29I4ieRYqUPLxsomVz9zx4m4mtnFR"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "859698006-c7Pve6LIlL0y6ZTQfPpWGlHlRbWekx26IWkAs8bh"
        access_token_secret = "9M7BB563q9X26HPEgoGvmU1mfdu3PaRM6a9jvxA0No6zF"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet("I'm Posting My Awesome Tweet !!!")
    twitter.tweet("And Did I tell You This is a BOT? :D")
    