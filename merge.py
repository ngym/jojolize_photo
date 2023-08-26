from PIL import Image

# 腕組み画像のパス
user_image_path = 'person.JPG'

# PSVRの人（スタンド）画像のパス
stand_image_path = 'person_segmentation_result_with_transparency.png'

# 腕組み画像のロード
user_image = Image.open(user_image_path)

# スタンド画像のロード
stand_image = Image.open(stand_image_path)

# スタンド画像のサイズ調整（必要に応じて）
stand_image_resized = stand_image.resize((int(stand_image.width * 6), int(stand_image.height * 6)))

# 位置の指定（左上の座標）
position = (0, 200)

# スタンド画像を腕組み画像に合成
#composite_image = user_image.copy()
#composite_image.paste(stand_image_resized, position, stand_image_resized)

# 透明度を指定して画像を合成
alpha = 0.5  # 透明度（0.0から1.0までの値）
composite_image = Image.new("RGBA", user_image.size)
composite_image.paste(user_image, (0, 0))
composite_image.paste(stand_image_resized, position, stand_image_resized)

# 透明度を適用
composite_image = Image.blend(user_image.convert("RGBA"), composite_image, alpha)
#composite_image = Image.blend(user_image, composite_image, alpha)


composite_image = composite_image.crop((300, 0, composite_image.width - 1100, composite_image.height))

# 画像の保存
output_path = 'composite_result.png'
composite_image.save(output_path)

print(f"Composite result saved to {output_path}")
