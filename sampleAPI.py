import tweepy

def getAPI():

    consumer_key = 'Scxpg8VolNpPK3mebimr394C9'
    consumer_secret = 'MJsnSfvjy9Cld3tlif8T0Jk17mYrUPX5QsjK1QIgaL9dOjZdkW'
    access_token = '3044996513-OcmAyuqv0JK91WpoZmyeLcfncaHafWB3EpLIjA0'
    access_token_secret = 'T35YfZsBtAJqy6bVdto3ulTZ7rbW5qTUNLPT3IcwtXQbN'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

def getTweets(user, pages):
    api = getAPI()
    #print api.rate_limit_status()
    count = 1
    countPerPage = 200
    for page in range(1, pages+1):
        user_tweets = api.user_timeline(user, count = countPerPage, page = page)
        for tweet in user_tweets:
            #print count
            a = tweet.text.encode('utf-8')
                #if a[0] == "R" and a[1] == "T" and a[3] == " ":
                #continue
                #else:
            print a
            #print tweet.created_at
            count += 1

def main():
    
    pages = 10 # each page will contain 200 tweets
    '''user = 'WinObs'
    getTweets(user, pages)
    user = 'SARAH5C3NTS'
    getTweets(user, pages)
    user = 'MomsThoughts'
    getTweets(user, pages)
    user = 'SSourblondie'
    getTweets(user, pages)
    user = 'MicaelaNoL'
    getTweets(user, pages)
    user = 'MollyBarkerLead'
    getTweets(user, pages)
    user = 'evacide'
    getTweets(user, pages)
    user = 'LindaInDisguise'
    getTweets(user, pages)
    user = 'scotchism'
    getTweets(user, pages)
    user = 'ShaunKing'
    getTweets(user, pages)
    user = 'mwilsonsayres'
    getTweets(user, pages)
    user = 'RMVCARD'
    getTweets(user, pages)
    user = 'gandhiqts'
    getTweets(user, pages)
    user = 'bdindi'
    getTweets(user, pages)
    user = 'RyonHarms'
    getTweets(user, pages)
    user = 'sesentacinco'
    getTweets(user, pages)
    user = 'Twig235'
    getTweets(user, pages)
    user = 'fets19'
    getTweets(user, pages)
    user = 'MissYuriEster'
    getTweets(user, pages)
    user = 'HOMIEANDER'
    getTweets(user, pages)
    user = 'buttermilkmeeks'
    getTweets(user, pages)
    user = 'MattofJozi'
    getTweets(user, pages)
    user = 'KamronQuinn'
    getTweets(user, pages)
    user = 'y0urstrulyangie'
    getTweets(user, pages)
    user = 'BabieGbemi'
    getTweets(user, pages)
    user = 'MoCa369'
    getTweets(user, pages)
    user = '_Puh_POW_'
    getTweets(user, pages)
    user = 'MAM2K'
    getTweets(user, pages)
    user = 'brooksoakwood'
    getTweets(user, pages)
    user = 'kyuopta'
    getTweets(user, pages)
    user = 'cachly'
    getTweets(user, pages)
    user = 'elvaakins'
    getTweets(user, pages)
    user = 'SaladC'
    getTweets(user, pages)'''


    user = 'carvedharry'
    getTweets(user, pages)
    user = 'MandyTapfer'
    
    getTweets(user, pages)
    user = 'wordsandhate'
    getTweets(user, pages)
    user = 'AYGdavid'
    getTweets(user, pages)
    user = 'BriannaPar_'
    getTweets(user, pages)
    user = 'twerk4melissa'
    getTweets(user, pages)
    user = 'celestey_westey'
    getTweets(user, pages)
    user = 'Katlynnn__97'
    getTweets(user, pages)






if __name__ == "__main__":
    main()