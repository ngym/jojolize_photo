from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Load the image
image_path = "composite_result.png"
image = Image.open(image_path)



# Define the text and font style
text = "f*[y"
font_path = "/Users/shota/Library/Fonts/BIZARG__.TTF" # 例として、ヒラギノ角ゴシックを使用
font_size = 600
font = ImageFont.truetype(font_path, font_size)

# Define drawing context
draw = ImageDraw.Draw(image)

# Manually set the text position (you can adjust these values)
text_x = image.width / 8
text_y = image.height / 15

# Draw the text on the image
draw.text((text_x, text_y), text, font=font, fill="black")


# Save the image
output_path = "ban.png"
image.save(output_path)

# Display the image (optional)
plt.imshow(image)
plt.axis("off")
plt.show()

print(f"Image saved to {output_path}")

