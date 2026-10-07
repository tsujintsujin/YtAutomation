"""Cut the Geek out of JinTheGeek/ProfileImage.jpg: the orange background (incl. its light icons) is every
warm, non-dark pixel connected to the image border; the black outline around the Geek stops the fill."""
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

im = Image.open("../JinTheGeek/ProfileImage.jpg").convert("RGB")
hsv = np.asarray(im.convert("HSV")).astype(int)
h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
warm = (h >= 14) & (h <= 40) & (s >= 50) & (v >= 150)          # orange/yellow bg + pale icons (PIL hue 0-255)
lab, _ = ndimage.label(warm)
edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
bg = np.isin(lab, edge[edge > 0])
bg = np.pad(bg, 4, constant_values=True); bg = ndimage.binary_closing(bg, iterations=2)[4:-4, 4:-4]  # pad: closing must not erode at the border
fg = ndimage.binary_fill_holes(~bg)                              # holes inside the Geek stay solid
fg = ndimage.binary_opening(fg, iterations=3)
keep, n = ndimage.label(fg)
sizes = ndimage.sum(fg, keep, range(1, n + 1))
fg = keep == (1 + int(np.argmax(sizes)))                        # largest blob = the Geek
alpha = Image.fromarray((fg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
out = im.convert("RGBA"); out.putalpha(alpha)
out = out.crop(out.getbbox())
out.save("intro/assets/geek.png"); out.save("outro/assets/geek.png")
print(out.size)
