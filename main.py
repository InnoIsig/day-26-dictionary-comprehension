#Exercice 1
import  random

names = ["Innocent", "Isaac", "David", "Gedeon", "Cynthia", "Herman"]
student_score = {student:random.randint(50, 100) for student in names}
passed_student = {student:score for (student, score) in student_score.items() if score >= 60}
print(student_score)
print(passed_student)


#Exercice 2
"""You are going to use Dictionary Comprehension to create a dictionary called result that 
takes each word in the given sentence and calculates the number of letters in each word.   
Try Googling to find out how to convert a sentence into a list of words.  *
*Do NOT** Create a dictionary directly."""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Splitting the sentence into a list of words
words = sentence.split()

# Using dictionary comprehension to create a dictionary with words and their corresponding lengths
result = {word: len(word) for word in words}

# Output the result
print(result)

#Exercice 3
"""You are going to use Dictionary Comprehension to 
create a dictionary called weather_f 
that takes each temperature in 
degrees Celsius and converts it into degrees Fahrenheit."""

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp_c * 9/5) + 32 for day, temp_c in weather_c.items()}

print(weather_f)