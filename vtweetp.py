#tweeting using python
import tweepy
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)
def main():
  # Fill in the values from ur tweeter a/c
  cfg = { 
    "consumer_key"        : "yznfje72iVFnCKdQRS7JlQT10",
    "consumer_secret"     : "KNsnNZmpIrzqJ8A90yu3U13UzA2jaxOwQ8ag5DBSexCgeS4ZxT",
    "access_token"        : "919291897146884097-5DGqfMHFuUbUplu3Ozoe5mE6TKoLwA9",
    "access_token_secret" : "xk1hNFF4mt9EoZIeNa3covFAlEeJ7wBNkD3aowyOJpBr3" 
    }
  api = get_api(cfg)
  tweet = "hi"
  status = api.update_status(status=tweet)  
  # Yes, tweet is called 'status' rather confusing 
if __name__ == "__main__":
  main()
  print('DONE')
  
