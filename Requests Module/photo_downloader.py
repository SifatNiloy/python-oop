import requests
img_url="https://images.pexels.com/photos/7017287/pexels-photo-7017287.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
response=requests.get(img_url)

with open("winter1.jpg", "wb",encoding=response.encoding) as f:
    f.write(response.content)