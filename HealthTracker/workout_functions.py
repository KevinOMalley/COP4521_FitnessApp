# Contains functions to calculate calories and other health-related things

# Pounds to Kilograms
# Takes in pounds as a float and converts it to kilograms as a float
def pounds_to_kg(weight_lb_flt):
    return (weight_lb_flt * .45359237)


# Kilograms to pounds
# Takes in kilograms as a float and converts it to pounds as a float
def kg_to_pounds(weight_kg_flt):
    return (weight_kg_flt * 2.20462)


# Pushups to Calories
# Takes in a number of pushups as a float and a person's weight in kilograms as a float and converts it to Calories(kcal) as a float
def pushup_to_calories(pushup_flt, weight_kg_flt):
    return ((weight_kg_flt / 100) * (.1) * (pushup_flt))


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