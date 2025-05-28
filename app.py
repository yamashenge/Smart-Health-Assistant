import streamlit as st

def add_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
            min-height: 100vh;
            background-attachment: fixed;
        }
        .main .block-container {
            background: rgba(255, 255, 255, 0.85);
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "Consider a nutritious meal plan to gain weight."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "Maintain your healthy lifestyle."
    elif 25 <= bmi < 29.9:
        return "Overweight", "Try balanced meals and regular exercise."
    else:
        return "Obese", "Consult a healthcare provider for personalized advice."

def meal_plan_and_workout(category):
    plans = {
        "Underweight": ("High-calorie nutritious meals", "Strength training 3x/week"),
        "Normal weight": ("Balanced diet", "Mix of cardio and strength exercises"),
        "Overweight": ("Low-calorie diet", "Daily moderate cardio"),
        "Obese": ("Medical diet plan", "Supervised physical activity"),
    }
    return plans.get(category, ("General healthy diet", "Regular physical activity"))

def main():
    add_background()
    st.title("BMI Calculator - Smart Health Assistant")

    # Welcoming message here
    st.markdown(
        """
        <h3 style='color:#0077b6;'>
            Welcome! Please enter your height and weight below to calculate your BMI and get personalized health recommendations.
        </h3>
        """,
        unsafe_allow_html=True
    )

    height_input = st.text_input("Height (cm):", value="")
    weight_input = st.text_input("Weight (kg):", value="")

    if st.button("Calculate BMI"):
        error = None
        try:
            height = float(height_input)
            weight = float(weight_input)

            if height <= 0 or weight <= 0:
                error = "Please enter positive numbers for height and weight."
        except ValueError:
            error = "Please enter valid numeric values for height and weight."

        if error:
            st.error(f"❗ {error}")
        else:
            bmi = calculate_bmi(weight, height)
            category, health_recommendation = bmi_category(bmi)
            meal_plan, workout_plan = meal_plan_and_workout(category)

            st.markdown(f"### Your BMI Result")
            st.write(f"**BMI:** {bmi}")
            st.write(f"**Category:** {category}")
            st.write(f"**Health Recommendation:** {health_recommendation}")
            st.write(f"**Suggested Meal Plan:** {meal_plan}")
            st.write(f"**Workout Plan:** {workout_plan}")

if __name__ == "__main__":
    main()
