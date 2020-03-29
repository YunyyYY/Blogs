import twitter


api = twitter.Api(consumer_key='NT8UUHKltyqrTFSDKHnvbSQyo',
                  consumer_secret='aQSSesLMfgndME5VgAsyp2P3ToJQ6226KN5iSRbTBKlHpv3ZVY',
                  access_token_key='1118624367527768065-tRLtQu1lIXN4hoLVcHhsKqjasf4dzz',
                  access_token_secret='Sf77mq3MHgQWq8JuztPU9dsY6v1FU0d69CJGiNIFGg2eF')

results = api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2019-02-26&count=10")
# print(type(results[0].created_at))
print(results[0])