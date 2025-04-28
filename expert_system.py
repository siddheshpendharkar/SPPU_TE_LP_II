def get_user_symptoms():
    print("Medical Diagnosis System")
    symptoms_input = input("Enter your symptoms (comma separated): ")
    return set(symptom.strip().lower() for symptom in symptoms_input.split(","))

def diagnose(symptoms):
    disease_database = {
        "Influenza (Flu)": {"cough", "fatigue", "fever", "muscle aches", "runny nose", "sore throat"},
        "Diabetes (Type 2)": {"blurred vision", "fatigue", "frequent urination", "increased thirst", "slow-healing wounds", "unexplained weight loss"},
        "Tuberculosis (TB)": {"chest pain", "coughing blood", "fatigue", "night sweats", "persistent cough", "weight loss"},
        "Dengue Fever": {"bleeding gums", "high fever", "joint pain", "nausea", "severe headache", "skin rash"},
        "Hypertension (High Blood Pressure)": {"blurred vision", "dizziness", "headaches", "nosebleeds", "shortness of breath"}
    }

    possible_diseases = {}

    for disease, disease_symptoms in disease_database.items():
        matching_symptoms = disease_symptoms.intersection(symptoms)
        if matching_symptoms:
            match_percentage = (len(matching_symptoms) / len(disease_symptoms)) * 100
            possible_diseases[disease] = (len(matching_symptoms), match_percentage)

    return possible_diseases

def display_diagnosis(possible_diseases):
    print("\nDiagnosing based on your symptoms...\n")

    if possible_diseases:
        print("Possible conditions (most likely first):\n")
        for disease, (match_count, percent) in sorted(possible_diseases.items(), key=lambda x: x[1][0], reverse=True):
            print(f"- {disease}: {match_count} symptom(s) matched ({percent:.1f}%)")
    else:
        print("No known diseases matched your symptoms. You may be healthy or experiencing unrelated symptoms.")

def main():
    user_symptoms = get_user_symptoms()
    possible_diseases = diagnose(user_symptoms)
    display_diagnosis(possible_diseases)

main()
