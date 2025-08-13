# 🎂 Birthday Cake 🎂
# Hero Board Entry #1 - Day 1 Project 01

print("🎉 Welcome to the Birthday Quiz! 🎉")
print("Test your knowledge about Bryan Dave's birthday!\n")

score = 0
total_questions = 3  # ✅ Fixed variable name (walang space)

# Question 1
answer1 = input("📅 What month is Bryan Dave's birthday? ").lower()
if answer1 == "march":
    print("✔ Correct!\n")
    score += 1
else:
    print("❌ Incorrect! The correct answer is March.\n")

# Question 2
answer2 = input("🔢 What day of the month is it? ").strip()
if answer2 == "12":
    print("✔ Correct!\n")
    score += 1
else:
    print("❌ Incorrect! It's the 12th.\n")

# Question 3
answer3 = input("♈ What is his Zodiac sign? ").lower()
if answer3 == "pisces":  # ✅ Ginawang lowercase check para consistent
    print("✔ Correct!\n")
    score += 1
else:
    print("❌ Incorrect! It's Pisces.\n")

# Final Result
print("🏁 Quiz Complete!")
print(f"📊 Your final score: {score} / {total_questions}")

# Bonus: Feedback based on score
if score == total_questions:
    print("🌟 Perfect! You really know Bryan Dave!")
elif score >= 2:
    print("👍 Good job! You're getting close.")
else:
    print("🧐 Keep studying! Try again next time.")
