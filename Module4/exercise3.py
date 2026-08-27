biological_gender = input("Enter biological gender (male/female): ")
Hemoglobin_factor = float(input( "Enter hemoglobin value (g/l): "))

biological_gender = biological_gender.lower()

if biological_gender == "male" and (134 <= Hemoglobin_factor <= 167):
    print("Your hemoglobin is normal.")
elif biological_gender == "male" and (Hemoglobin_factor > 167):
    print("Your hemoglobin is high.")
elif biological_gender == "male" and (Hemoglobin_factor < 134):
    print("Your hemoglobin is low.")
elif biological_gender == "female" and (117 <= Hemoglobin_factor <= 155):
    print("Your hemoglobin is normal.")
elif biological_gender == "female" and (Hemoglobin_factor > 155):
    print("Your hemoglobin is high.")
elif biological_gender == "female" and (Hemoglobin_factor < 117):
    print("Your hemoglobin is low.")
else:
    print("Invalid gender.")