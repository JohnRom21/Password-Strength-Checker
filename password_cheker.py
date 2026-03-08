import re
from flask import Flask, render_template, request

app = Flask(__name__)


def check_password_strength(password):
    score = 0
    feedback = []
    # Define keyboard sequences
    letter_sequence = ["qwertyuiopasdfghjklzxcvbnm"]
    number_sequence = ["1234567890"]

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")
    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")
    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")
    # Check special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*).")
    # Check for three or more consecutive identical characters
    if not re.search(r"(.)\1{2,}", password):
        score += 1
    else:
        feedback.append(
            "Password should not contain three or more consecutive identical characters (e.g., 'aaa' or '111').")
    # Check for three or more raising/falling characters
    has_sequence = False
    lower_password = password.lower()

    def is_sequential(three_letters, sequences):
        for seq in sequences:
            if three_letters in seq or three_letters[::-1] in seq:
                return True
        return False

    for i in range(len(lower_password) - 2):
        three_letters = lower_password[i:i + 3]
        # Check letters
        if three_letters.isalpha() and is_sequential(three_letters, letter_sequence):
            has_sequence = True
            break

        # Check numbers
        if three_letters.isdigit() and is_sequential(three_letters, number_sequence):
            has_sequence = True
            break

    if not has_sequence:
        score += 1
    else:
        feedback.append(
            "Password should not contain three or more consecutive characters in keyboard order (e.g., 'qwe', '123', "
            "'edc').")

    # Determine strength
    if score >= 7:
        return "Strong password!", feedback
    elif score >= 4:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback


@app.route("/", methods=["GET", "POST"])
def home():
    strength = None
    feedback = []

    if request.method == "POST":
        password = request.form["password"]
        strength, feedback = check_password_strength(password)

    return render_template("index.html", strength=strength, feedback=feedback)


if __name__ == "__main__":
    app.run(debug=True)


