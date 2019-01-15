import requests

r = requests.post('https://vk-com-change.herokuapp.com/edit/',params={'name':'Коломиец ggg', 'photo':'https://pp.userapi.com/c849424/v849424371/4e998/j4wIK7nuN9Y.jpg?ava=1', 'is_user':True})
print(r.text)