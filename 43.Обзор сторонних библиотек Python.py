import requests
from PIL import Image, ImageFilter

response = requests.get('https://api.github.com')
print(response.text)

payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('http://httpbin.org/post', data=payload)
print(response.json())

print(response.headers)


img = Image.open('image.jpg')
img.show()

img_resized = img.resize((300, 200))
img_resized.save('resized_image.jpg')

img_blur = img.filter(ImageFilter.BLUR)
img_blur.save('blurred_example.jpg')