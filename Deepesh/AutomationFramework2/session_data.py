import os

#env = "TEST"
test_url = "https://google.com"
alpha_url = "https://facebook.com"
beta_url = "https://yahoo.com"
env_val = os.getenv('Test_Env')
print(f"env_value: {env_val}")
url = None
if env_val == 'TEST':
    url = test_url
elif env_val == 'ALPHA':
    url = alpha_url
elif env_val == 'BETA':
    url = beta_url


