#Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees >= 100 else "conference room"
print(venue)

#Task 2: Catering Choices

food = input("Would you like vegetarian food? Yes or No?: ")

recommendation = "Veggie Delight Caters" if food == 'Yes' else "Gourmet Meal Caterers"
print("We recoommend", recommendation)

