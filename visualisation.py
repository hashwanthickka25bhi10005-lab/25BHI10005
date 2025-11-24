def get_recommendation(issue):
    suggestions = {
        "Healthy": "Maintain brushing twice a day & floss regularly.",
        "Cavity": "Visit dentist & avoid sugary snacks. Start fluoride paste.",
        "Gum Disease": "Use antibacterial mouthwash & get gum cleaning.",
        "Plaque": "Do professional dental cleaning.",
        "Ulcers": "Take vitamin B12 supplements & avoid spicy foods."
    }
    return suggestions.get(issue, "Consult a dentist for detailed examination.")
