# import requests
# import json

# response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# for data in response.json()['items']:
#     if data['is_answered'] == 0:
#         print(data['title'])
#         print(data['link']) 
#         print('\n') # to make it readable to screen
#     else:
#         print('skipped')
        
#     print()

