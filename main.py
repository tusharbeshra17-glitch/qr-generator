import qrcode

URL = input("enter the URL: ") # https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/250px-Flag_of_India.svg.png?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail
file_name = input("enter name of the file you want to save it as: ")

if not file_name.endswith('.png'):
    file_name += '.png'

img = qrcode.make(URL)
img.save(file_name)