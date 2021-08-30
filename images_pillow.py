from PIL import Image

mac = Image.open('./Images/pencils.jpg')
type(mac)
# mac.show()

# cropping 
x = 0
y = 0

w = mac.size[0] / 3
h = mac.size[1] / 10
m = mac.crop((x, y, w, h))
m.show()

# funcs
# mac.paste
# mac.save()