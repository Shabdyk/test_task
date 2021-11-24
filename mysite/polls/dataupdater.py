from polls.views import loc_json, web_json, data_fixture

target_url = 'http://jsonplaceholder.typicode.com/posts'
target_model = 'polls.user_posts'

json_data = web_json(target_url)

act = data_fixture(json_data, target_model)
