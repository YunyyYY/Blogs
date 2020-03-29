import twitter


api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

results = api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2019-02-26&count=10")
# print(type(results[0].created_at))
print(results[0])