def calculate_macros(height_cm, weight_kg, age, gender, activity_level, goal):
    # Step 1: Calculate BMR
    if gender.lower() == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    # Step 2: Adjust for activity level
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very_active': 1.9
    }

    multiplier = activity_multipliers.get(activity_level.lower())
    if not multiplier:
        raise ValueError("Invalid activity level.")

    maintenance_calories = bmr * multiplier

    # Step 3: Adjust for goal
    if goal.lower() == 'lose':
        total_calories = maintenance_calories - 500
    elif goal.lower() == 'gain':
        total_calories = maintenance_calories + 500
    else:
        total_calories = maintenance_calories

    # Step 4: Macronutrient calculations
    protein_grams = weight_kg * 2          # 2g per kg of weight
    fat_grams = weight_kg * 0.8            # 0.8g per kg of weight

    protein_calories = protein_grams * 4   # 4 kcal per gram of protein
    fat_calories = fat_grams * 9           # 9 kcal per gram of fat

    remaining_calories = total_calories - (protein_calories + fat_calories)
    if remaining_calories < 0:
        remaining_calories = 0  # prevent negative carb calories

    carb_grams = remaining_calories / 4    # 4 kcal per gram of carbs

    return {
        'total_calories': round(total_calories, 2),
        'protein_g': round(protein_grams, 2),
        'fat_g': round(fat_grams, 2),
        'carbs_g': round(carb_grams, 2)
    }
