# Contains functions to calculate calories and other health-related things
# I tried to avoid using MET (Metabolic Equivalent of Task) values in the calculations as it's kind of a pain for a person to have to calculate what their MET is for each exercise.

# Converts miles to kilometers
# Takes in distance in miles as a float and returns distance in kilometers as a float
def miles_to_km(distance_miles_flt):
    return (distance_miles_flt * 1.609344)


# Converts kilometers to miles
# Takes in distance in kilometers as a float and returns distance in miles as a float
def km_to_miles(distance_km_flt):
    return (distance_km_flt * 0.62137119)


# Pounds to Kilograms
# Takes in weight in pounds as a float and converts it to weight in kilograms as a float
def pounds_to_kg(weight_lb_flt):
    return (weight_lb_flt * .45359237)


# Kilograms to pounds
# Takes in weight in kilograms as a float and converts it to weight in pounds as a float
def kg_to_pounds(weight_kg_flt):
    return (weight_kg_flt * 2.20462)


# Calculates Body Mass Index
# Takes in weight in kilograms as a float and height in meters as a float and returns the BMI as a float
def calculate_BMI(weight_kg_flt, height_m_flt):
    return (weight_kg_flt / (height_m_flt * height_m_flt))


# Determines which category a BMI belongs to
# Takes in a BMI as a float and returns which category it belongs to as a string
def is_healthy_BMI(BMI_flt):
    if BMI_flt < 18.5:
        return "Underweight"
    elif 18.5 <= BMI_flt < 25:
        return "Normal Weight"
    elif 25 <= BMI_flt < 30:
        return "Overweight"
    else:
        return "Obese"


# Determines the healthy ammount of sleep per age group
# Takes in an age as a float and returns the min recommended sleep and max recommended sleep as a tuple of floats (min_sleep, max_sleep)
def recommended_sleep(age_flt):
    if 0 <= age_flt < 0.25:  # Newborns (0-3 months)
        return (14, 17)
    elif 0.25 <= age_flt < 1:  # Infants (4-11 months)
        return (12, 15)
    elif 1 <= age_flt < 2:  # Toddlers (1-2 years)
        return (11, 14)
    elif 2 <= age_flt < 6:  # Preschoolers (3-5 years)
        return (10, 13)
    elif 6 <= age_flt < 14:  # School-age children (6-13 years)
        return (9, 11)
    elif 14 <= age_flt < 18:  # Teenagers (14-17 years)
        return (8, 10)
    elif 18 <= age_flt < 65:  # Adults (18-64 years)
        return (7, 9)
    else:  # Senior Citizens (65+ years)
        return (7, 8)


# Distance ran(kilometers) to Calories(kcal)
# Takes in the distance ran in kilometers as a float and weight in kilograms as a float and converts it to Calories(kcal) burnt as a float
def distance_ran_to_calories(distance_km_flt, weight_kg_flt):
    return (distance_km_flt * weight_kg_flt * 1.036)


# Distance walked(kilometers) to Calories(kcal)
# Takes in the distance walked in kilometers as a float and weight in kilograms as a float and converts it to Calories(kcal) burnt as a float
def distance_walked_to_calories(distance_km_flt, weight_kg_flt):
    return (distance_km_flt * weight_kg_flt * 0.53)


# Distance biked(kilometers) to Calories(kcal)
# Takes in the distance biked in kilometers as a float and weight in kilograms as a float and converts it to Calories(kcal) burnt as a float
def distance_biked_to_calories(distance_km_flt, weight_kg_flt):
    return (distance_km_flt * weight_kg_flt * 0.55)  # Moderate Intensity (.35 - .7)


# Distance swam(kilometers) to Calories(kcal)
# Takes in the distance swam in kilometers as a float and weight in kilograms as a float and converts it to Calories(kcal) burnt as a float
def distance_swam_to_calories(distance_km_flt, weight_kg_flt):
    return (distance_km_flt * weight_kg_flt * 0.6)  # Moderate Intensity (.4 - .8)


# Push-Ups to Calories
# Takes in a number of push-ups as a float and a person's weight in kilograms as a float and converts it to Calories(kcal) burnt as a float
def pushup_to_calories(pushup_flt, weight_kg_flt):
    return ((weight_kg_flt / 100) * (.1) * (pushup_flt))


# Pull-Ups to Calories
# Takes in a number of pull-ups as a float and a person's weight in kilograms as a float and converts it to Calories(kcal) burnt as a float
def pullup_to_calories(pullup_flt, weight_kg_flt):
    if 0 <= weight_kg_flt < 56.8:  # Light Weight
        return (3 * pullup_flt)  # (2.5 - 3.5)
    elif 56.8 <= weight_kg_flt < 70.4:  # Moderate Weight
        return (3.5 * pullup_flt)  # (3 - 4)
    elif 70.4 <= weight_kg_flt < 84:  # Heavy Weight
        return (4 * pullup_flt)  # (3.5 - 4.5)
    else:  # Very Heavy Weight
        return (4.5 * pullup_flt)  # (4 - 5)


# Sit-Ups to Calories
# Takes in a number of sit-ups as a float and a person's weight in kilograms as a float and converts it to Calories(kcal) burnt as a float
def situp_to_calories(situp_flt, weight_kg_flt):
    if 0 <= weight_kg_flt < 56.8:  # Light Weight
        return (.375 * situp_flt)  # (.25 - .5)
    elif 56.8 <= weight_kg_flt < 70.4:  # Moderate Weight
        return (.75 * situp_flt)  # (.5 - 1)
    elif 70.4 <= weight_kg_flt < 84:  # Heavy Weight
        return (situp_flt)  # (1 * situp_flt)        #(.75 - 1.25)
    else:  # Very Heavy Weight
        return (1.25 * situp_flt)  # (1 - 1.5)


# Squats to Calories
# Takes in a number of squats as a float and a person's weight in kilograms as a float and converts it to Calories(kcal) burnt as a float
def squat_to_calories(squat_flt, weight_kg_flt):
    if 0 <= weight_kg_flt < 56.8:  # Light Weight
        return (.15 * squat_flt)  # (.1 - .2)
    elif 56.8 <= weight_kg_flt < 70.4:  # Moderate Weight
        return (.25 * squat_flt)  # (.2 - .3)
    elif 70.4 <= weight_kg_flt < 84:  # Heavy Weight
        return (.35 * squat_flt)  # (.3 - .4)
    else:  # Very Heavy Weight
        return (.45 * squat_flt)  # (.4 - .5)


# Jumping-Jacks to Calories
# Takes in a number of jumping-jacks as a float and a person's weight in kilograms as a float and converts it to Calories(kcal) burnt as a float
def jumpingjack_to_calories(jumpingjack_flt, weight_kg_flt):
    if 0 <= weight_kg_flt < 56.8:  # Light Weight
        return (.05 * jumpingjack_flt * weight_kg_flt)  # (.045 - .055)
    elif 56.8 <= weight_kg_flt < 70.4:  # Moderate Weight
        return (.055 * jumpingjack_flt * weight_kg_flt)  # (.05 - .06)
    elif 70.4 <= weight_kg_flt < 84:  # Heavy Weight
        return (.06 * jumpingjack_flt * weight_kg_flt)  # (.055 - .065)
    else:  # Very Heavy Weight
        return (.065 * jumpingjack_flt * weight_kg_flt)  # (.06 - .07)


# Shoulder-Shrugs to Calories
# Takes in a number of shoulder-shrugs as a float and a person's weight in kilograms as a float and converts it to Calories(kcal) burnt as a float
def shrug_to_calories(shrug_flt, weight_kg_flt):
    return ((.03) * (shrug_flt))  # Moderate Intensity (.02 - .04)