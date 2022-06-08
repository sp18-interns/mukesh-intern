
from PIL import Image


im = Image.open("dog1.png")
#im.show()

print ("Image information. size: {} format: {} mode: {}".format(im.size, im.format, im.mode))


### Experiment with functions that do not change
## the image but return a new image
im2 = im.convert("L")

#im2.show()

w,h = int(im.size[0]/3), int(im.size[1]/3)

im3 = im.resize( (w,h) )
#im3.show()

im4 = Image.new("RGB", (400,400))
#im4.show()

im5 = im.crop( (0,300,200,500) )

#im5.show()

## The only function that modified the
## image it is applied to but does not return
## anything, like sort for lists

im4.paste(im5, (0,0))
im4.paste(im5, (200,200))
im4.paste(im5, (0,200))
im4.paste(im5, (200,0))
im4.show()

im4.save("dog_pile.jpg")