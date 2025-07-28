import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def generate_captcha(text_length=6, width=200, height=70):
    # Generate random text
    letters = string.ascii_uppercase + string.digits
    captcha_text = ''.join(random.choice(letters) for _ in range(text_length))

    # Create image with white background
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype("arial.ttf", 40)  # Make sure this font exists or use a path to a .ttf file
    draw = ImageDraw.Draw(image)

    # Draw random lines for noise
    for _ in range(8):
        start = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([start, end], fill=(random.randint(0,150), random.randint(0,150), random.randint(0,150)), width=2)

    # Draw captcha text with random position jitter
    for i, char in enumerate(captcha_text):
        x = 30 * i + random.randint(0, 5)
        y = random.randint(5, 20)
        draw.text((x, y), char, font=font, fill=(random.randint(0, 100), 0, 0))

    # Apply some filters for distortion
    image = image.filter(ImageFilter.GaussianBlur(1))

    return image, captcha_text

# Generate and save captcha image
if __name__ == "__main__":
    captcha_img, captcha_text = generate_captcha()
    print("CAPTCHA Text:", captcha_text)
    captcha_img.show()  # Opens the default image viewer
    captcha_img.save("captcha.png")
