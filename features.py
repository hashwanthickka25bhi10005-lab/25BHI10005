import random

def analyze_oral_health(processed_img):
    issues = ["Cavity", "Gum Disease", "Plaque", "Healthy", "Ulcers"]
    predicted_issue = random.choice(issues)

    confidence = round(random.uniform(70, 95), 2)

    return {
        "issue": predicted_issue,
        "confidence": confidence,
        "clarity": processed_img["clarity_score"]
    }
