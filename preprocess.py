import random

def preprocess_image(image_path):
    # Fake image cleaning simulation
    print(f"Processing image: {image_path}")
    clarity_score = random.randint(70, 98)
    return {"path": image_path, "clarity_score": clarity_score}
