from PIL import Image, ImageDraw, ImageFont, ImageColor
import matplotlib.pyplot as plt
import numpy as np

# Bonus: Make a graph in the style of xkcd 2864
# The x-value of each point is represented by hue, typically scaleb between 0 and 360
# The y-value is represented by the label

# Add a layer of partially opaque text to an image
def add_layer(base, text, location, font, fill):
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    # get a drawing context
    d = ImageDraw.Draw(txt)
    # draw text, half opacity
    d.text(location, text, font=font, fill=fill)
    return Image.alpha_composite(base, txt)
    
# Add a point to the graph
# The range of x-values can be set using xrange, the opacity of each layer with a, and jitter can be enabled to prevent overlapping points _too_ much
def add_point(base, font, x, y, xrange=(0,360), a=127, jitter=0):
    h = 360*(x-xrange[0])/xrange[1]
    hsv = "hsv(" + str(h) + ",100%,100%)"
    fill = ImageColor.getrgb(hsv) + (a,)   # Get an RGBA string with the appropriate hue and opacity
    
    loc = (20 + np.random.uniform(-jitter, jitter),
           20 + np.random.uniform(-jitter, jitter))
  
    return(add_layer(base, str(y), loc, font, fill))
    
out = Image.new("RGBA", (100,100), "white")
fnt = ImageFont.truetype("calibrib.ttf", 50)

#     The red 62 corresponds to an x-value of approx. 17, a hue value corresponding to a shade of warm red.
#    The yellow 159 corresponds to an x-value of approx. 36, in the range that typically represents warm yellow.
#    The green 205 corresponds to an x-value of approx. 67, a hue value for yellowish green.
#    The turquoise 187: 187 is near the hue value for turquoise, between green and blue in the color wheel. (This data point's x-axis value of 85 would be yellowish green.)
#    The blue 230: 230 is the hue value for a clear, distinct blue. (This data point's x-axis value of 100 would be warm green.)

#data = [(17, 62), (36, 159),  (67,205),  (85,187),  (100,230)]
data = [(17, 62), (36, 159),  (67,205),  (187,85),  (230,100)]

for point in data:
    out = add_point(out, fnt, point[0], point[1], a=100, jitter=2)

plt.imshow(out)
plt.show() 
