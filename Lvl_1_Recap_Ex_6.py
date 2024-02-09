hours_bicycling = float(input("Enter hours spent bicycling: "))
hours_jogging = float(input("Enter hours spent jogging: "))
hours_swimming = float(input("Enter hours spent swimming: "))

calories_bicycling = 200
calories_jogging = 475
calories_swimming = 275

total_calories = ((hours_bicycling * calories_bicycling) + (hours_jogging * calories_jogging) +
                  (hours_swimming * calories_swimming))

weight_loss_kgs = total_calories / 3500

print(f"You lost {weight_loss_kgs:.3f} kgs")
