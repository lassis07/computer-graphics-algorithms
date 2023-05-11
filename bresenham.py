def bresenham(img, xi, yi, xf, yf, color):
  dx = abs(xf - xi)
  dy = abs(yf - yi)
  
  dx2 = 2 * dx
  dy2 = 2 * dy
  
  p = dy2 - dx
  x = abs(xi)
  y = abs(yi)
  
  for i in range(dx):
    img = setPixel(img, x, y, color)

    x = x + 1
    if p >= 0:
      y = y + 1

      p = p - dx2 + dy2

    else:
      p = p + dy2
