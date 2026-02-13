from PIL import Image

# === CONFIGURATION ===
image_paths = [
    "D:/Affan/Rushda_and_Yusra_holiday_homework_photos_and_collages/Rushda/Photos/B2/image1.jpg",
    "D:/Affan/Rushda_and_Yusra_holiday_homework_photos_and_collages/Rushda/Photos/B2/image2.jpg",
    "D:/Affan/Rushda_and_Yusra_holiday_homework_photos_and_collages/Rushda/Photos/B2/image3.jpg",
    "D:/Affan/Rushda_and_Yusra_holiday_homework_photos_and_collages/Rushda/Photos/image4.jpg",
    "D:/Affan/Rushda_and_Yusra_holiday_homework_photos_and_collages/Rushda/Photos/image5.jpg",
    "D:/Affan/Rushda_and_Yusra_holiday_homework_photos_and_collages/Rushda/Photos/image6.jpg",
]

# A4 dimensions at 300 DPI
a4_width = 2480
a4_height = 3508
columns = 2
rows = 3
border_size = 5

# Final size for each bordered image slot
slot_width = a4_width // columns  # 1240
slot_height = a4_height // rows   # 1169

# Inner image size after accounting for border
image_width = slot_width - 2 * border_size  # 1230
image_height = slot_height - 2 * border_size  # 1159

# === PROCESSING ===
images = [Image.open(path).resize((image_width, image_height)) for path in image_paths]

# Add black border
images_with_borders = []
for img in images:
    bordered = Image.new("RGB", (slot_width, slot_height), "black")
    bordered.paste(img, (border_size, border_size))
    images_with_borders.append(bordered)

# === CREATE COLLAGE ===
collage = Image.new("RGB", (a4_width, a4_height), "white")

for idx, img in enumerate(images_with_borders):
    x = (idx % columns) * slot_width
    y = (idx // columns) * slot_height
    collage.paste(img, (x, y))

# === SAVE ===
output_path = "Opposites_Collage_A4_FullHighRes.jpg"
collage.save(output_path, dpi=(300, 300))
print(f"Perfectly-packed A4 collage saved at {output_path}")
