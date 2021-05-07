import tweepy
from os import system, name
import os

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

#################################

# setting up some variables

usersInformation = api.get_user("USERID")

currentName = usersInformation.name
currentBio = usersInformation.description
currentLocation = usersInformation.location
currentURL = usersInformation.url


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def startUp():
    # prints title
    print("___________       .__  __    __                   _____              _________     _____  ________   ")
    print("\__    ___/_  _  _|__|/  |__/  |_  ___________  _/ ____\___________  \_   ___ \   /     \ \______ \  ")
    print("  |    |  \ \/ \/ /  \   __\   __\/ __ \_  __ \ \   __\/  _ \_  __ \ /    \  \/  /  \ /  \ |    |  \ ")
    print("  |    |   \     /|  ||  |  |  | \  ___/|  | \/  |  | (  <_> )  | \/ \     \____/    Y    \|    `   |")
    print("  |____|    \/\_/ |__||__|  |__|  \___  >__|     |__|  \____/|__|     \______  /\____|__  /_______  /")
    print("                                      \/                                     \/         \/        \/ ")
    print("                                                                                                     ")
    print("                                                                                                     ")
    # show commands for new users
    print("Commands: ")
    print("                                                                                                     ")
    print("setup     | setups up the tweepy api")
    print("bio       | changes your profile bio")
    print("location  | changes your profile location")
    print("url       | changes your profile url")
    print("name      | changes your profile name")
    print("tweet     | sends a tweet")
    print("user info | prints the info of a user")
    print("dm        | dms a specific user")
    print("follow    | follows specified user")
    print("view user | shows tweets from specific user")
    print("timeline  | shows your timeline")
    print("mentions  | shows your mentions")
    print("                               ")
    print("made by @jeremymann07 on twitter")
    print("                                                                                                     ")
    print("                                                                                                     ")


def newCmd():
    # allows input of commands
    cmdToPerform = input("CMD: ")

    if cmdToPerform == "setup":
        clear()
        os.system("python -m pip install tweepy")
        clear()
        newCmd()

        #
    elif cmdToPerform == "reset":
        clear()
        startUp()
        newCmd()

        #
    elif cmdToPerform == "name":
        clear()
        nameUser = input("what is your new name? | ")
        api.update_profile(nameUser)
        newCmd()

        #
    elif cmdToPerform == "tweet":
        clear()
        tweet = input("what would you like to tweet? | ")
        api.update_status(tweet)
        newCmd()

        #
    elif cmdToPerform == "follow":
        clear()
        ptf = input("who would you like to follow? | ")
        api.create_friendship(ptf)
        newCmd()

        #
    elif cmdToPerform == "user info":
        clear()
        user = input("what is the id of the user? | ")
        print("             ")
        print("             ")
        userInfo = api.get_user(user)
        print("Username: ")
        print(userInfo.name)
        print("           ")
        print("User's Location: ")
        print(userInfo.location)
        print("           ")
        print("User's Bio: ")
        print(userInfo.description)
        print("            ")
        print("User's URL: ")
        print(userInfo.url)
        newCmd()

        #
    elif cmdToPerform == "dm":
        clear()
        dmid = input("who would you like to dm? | ")
        text = input("what would you like to say? | ")
        api.send_direct_message(dmid, text)

        #
    elif cmdToPerform == "follow":
        clear()
        followUser = input("what is the name of the user you want to follow? | ")
        api.create_friendship(followUser.id)

        #
    elif cmdToPerform == "view user":
        clear()
        tweetUser = input("what is the user's name? | ")
        tweetCount = input("how many tweets do you want to see? | ")
        timeline = api.user_timeline(user_id="1268218110374563841", count=tweetCount, tweet_mode="extended")
        textonly_tweets = [tweet.full_text for tweet in timeline]
        print(*textonly_tweets, sep="\n")
        print("                           ")
        print("                           ")
        newCmd()

        #
    elif cmdToPerform == "timeline":
        clear()
        # figure out timeline display
        newCmd()

        #
    elif cmdToPerform == "mentions":
        clear()
        mentions = api.mentions_timeline(user_id="1268218110374563841", count=6, tweet_mode="extended")
        textonly_mentions = [tweet.full_text for tweet in mentions]
        print(*textonly_mentions, sep="\n")
        # mentionCount = 0
        # muchMentions = input("how many mentions do you want to display? | ")
        # muchMentionInt = int(muchMentions)
        # mentionsDisplay = 0
        # mentionsDisplayCount = 1
        # mentionsDisplayCountInt = str(mentionsDisplayCount)

        # while mentionCount < muchMentionInt:
        #    mentions = api.mentions_timeline(user_id="1268218110374563841",count=mentionsDisplayCountInt,tweet_mode="extended")
        #    textonly_mentions = [tweet.full_text for tweet in mentions]
        #    print(*textonly_mentions, sep = "\n")
        #    print("                            ")
        #   mentionCount = mentionCount + 1
        #   mentionsDisplay = mentionsDisplay + 1
        newCmd()

        #
    elif cmdToPerform == "bio":
        clear()
        bioChange = input("what would you like to change your bio to? | ")
        api.update_profile(description=bioChange)
        newCmd()

        #
    elif cmdToPerform == "location":
        clear()
        locationChange = input("what would you like to change your location to? | ")
        api.update_profile(location=locationChange)
        newCmd()

        #
    elif cmdToPerform == "url":
        clear()
        urlChange = input("what would you like to change your url to? | ")
        api.update_profile(url=urlChange)
        newCmd()

        #


clear()
startUp()
newCmd()
