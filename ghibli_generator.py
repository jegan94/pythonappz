import torch
import tkinter as tk
from tkinter import filedialog
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image

# ✅ Set device to MPS (Apple Metal) for best performance
device = "mps" if torch.backends.mps.is_available() else "cpu"

# ✅ Load the Stable Diffusion model (Replace with Ghibli model path if needed)
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",  # Use a custom Ghibli model if available
    torch_dtype=torch.float32
).to(device)

# ✅ Open file dialog to select an image
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

if not file_path:
    print("❌ No file selected. Exiting...")
    exit()

# ✅ Load the user-selected image
init_image = Image.open(file_path).convert("RGB").resize((512, 512))

# ✅ Define the AI transformation prompt
prompt = "A beautiful Studio Ghibli-style landscape with vibrant colors and soft lighting"

# ✅ Generate AI-modified image
generator = torch.manual_seed(42)
output_image = pipe(
    prompt=prompt,
    image=init_image,
    strength=0.75,  # Higher means more AI influence
    guidance_scale=7.5  # Controls how closely AI follows the prompt
).images[0]

# ✅ Save and show the generated image
output_image.save("ghibli_output.png")
output_image.show()
print("✅ Image saved as ghibli_output.png")