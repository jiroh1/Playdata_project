from collections import Counter
import twitter
import json
twitter_consumer_key = "LMTY01TACDvRiYLINA1z4Fjpn"
twitter_consumer_secret = "EwsxbeGTYYrMTnH0ZYz6ex7WEP3u954fCxyCvO0i0bIE6IqvmQ"
twitter_access_token = "72482958-VL4hxkHwGhO3yOepwzLKXsJ0GuZBctCacS1Oo07hW"
twitter_access_secret = "dpUQZIVyfxymAIvH962eOjK1rquo2RErOFAzVEGzjcbUN"
twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret,
                          access_token_key=twitter_access_token,
                          access_token_secret=twitter_access_secret)
query = ["작위시"]
output_file_name = "작위시.txt"
with open(output_file_name, "w", encoding="utf-8") as output_file:
    stream = twitter_api.GetStreamFilter(track=query)
    while True:
        for tweets in stream:
            tweet = json.dumps(tweets, ensure_ascii=False)
            print(tweet, file=output_file, flush=True)