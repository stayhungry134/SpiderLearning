import pytesseract
from PIL import Image

# 打开图片
img = Image.open('路径')

# 识别图片中的内容
code = pytesseract.image_to_string(img)

# 输出验证码
print(code)