import re
import string

def assess_password_strength(password):
    """Assess password strength based on multiple criteria."""
    score = 0
    feedback = []
    recommendations = []

    # Criterion 1: Length
    if len(password) > 12:
        score += 3
        feedback.append("✅ Excellent length (12+ characters)")
    elif len(password) >= 8:
        score += 2
        feedback.append("✅ Good length (8–11 characters)")
    elif len(password) >= 6:
        score += 1
        feedback.append("⚠️ Weak length (6–7 characters)")
    else:
        feedback.append("❌ Very short password (<6 characters)")
        recommendations.append("Use at least 8 characters (preferably 12 or more).")

    # Criterion 2: Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")
        recommendations.append("Include uppercase letters (e.g., A, B, C).")

    # Criterion 3: Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")
        recommendations.append("Include lowercase letters (e.g., a, b, c).")

    # Criterion 4: Numbers
    if re.search(r"[0-9]", password):
        score += 2
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Missing numbers")
        recommendations.append("Add numbers (e.g., 1, 2, 3).")

    # Criterion 5: Special characters
    special_chars = set(string.punctuation)
    if any(char in special_chars for char in password):
        score += 2
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Missing special characters")
        recommendations.append("Add special characters (e.g., !, @, #).")

    # Criterion 6: Repeated characters
    if len(password) == len(set(password)):
        score += 2
        feedback.append("✅ No repeated characters")
    else:
        feedback.append("⚠️ Contains repeated characters")
        recommendations.append("Avoid repeating characters for better uniqueness.")

    # Final strength assessment
    if score >= 12:
        strength = "🔒 Very Strong"
    elif score >= 9:
        strength = "💪 Strong"
    elif score >= 6:
        strength = "🟡 Moderate"
    elif score >= 3:
        strength = "🔓 Weak"
    else:
        strength = "❗ Very Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback,
        "recommendations": recommendations
    }

def main():
    print("🔍 Password Strength Checker")
    print("Type a password to check its strength (or 'quit' to exit)")

    while True:
        password = input("\nEnter password: ")
        if password.lower() == 'quit':
            print("👋 Exiting program...")
            break

        if not password:
            print("⚠️ Password cannot be empty.")
            continue

        result = assess_password_strength(password)
        print(f"\n🧠 Strength: {result['strength']}  (Score: {result['score']}/13)")

        print("\n📝 Feedback:")
        for item in result['feedback']:
            print(f" - {item}")

        if result['recommendations']:
            print("\n📌 Suggestions to Improve:")
            for item in result['recommendations']:
                print(f" - {item}")
        else:
            print("\n✅ No improvements needed — your password is strong!")

if __name__ == "__main__":
    main()

