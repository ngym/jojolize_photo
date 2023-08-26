import torchvision.models.segmentation as segmentation
import torch
from PIL import Image
from torchvision import transforms
import numpy as np

# モデルのロード
model = segmentation.deeplabv3_resnet101(pretrained=True)
model.eval()

# 画像のロード
image_path = '/Users/shota/Downloads/psvr.jpeg'
input_image = Image.open(image_path)

# 前処理の定義
preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# 前処理の適用
input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0)

# GPUが利用可能な場合、モデルとデータをGPUに転送
if torch.cuda.is_available():
    model.cuda()
    input_batch = input_batch.to('cuda')

# 推論の実行
with torch.no_grad():
    output = model(input_batch)['out'][0]
output_predictions = output.argmax(0).cpu().numpy()

# 人物クラスのラベル（通常は15）を抽出
person_class_label = 15
person_mask = (output_predictions == person_class_label)

# 元の画像をnumpy配列に変換
input_image_np = np.array(input_image)

# アルファチャンネル（透明度）の作成
alpha_channel = np.zeros_like(input_image_np[..., 0])
alpha_channel[person_mask] = 255

# 人物部分の切り抜きとアルファチャンネルの追加
person_image_with_alpha = np.concatenate([input_image_np, alpha_channel[..., None]], axis=-1)

# 切り抜いた部分をPILイメージに変換
person_image_pil = Image.fromarray(person_image_with_alpha, 'RGBA')

# 画像の保存
output_path = 'person_segmentation_result_with_transparency.png'
person_image_pil.save(output_path)

print(f"Person segmentation result with transparency saved to {output_path}")
