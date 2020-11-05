from flask import Flask, render_template, request
import tweepy
import json

application = Flask(__name__)

secrets = json.loads(open('twitter.json').read())
api_key = secrets['api_key']
api_secret_key = secrets['api_secret_key']
access_token = secrets['access_token']
access_token_secret = secrets['access_token_secret']


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/tweet/')
def tweet():
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweet = request.args.get('t')


@application.route('/search/')
def search():
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    search = request.args.get('search')

    public_tweets = api.search_users(search)

    return render_template('home.html', tweets=public_tweets)


if __name__ == '__main__':
    application.run(debug=True)
