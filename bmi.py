def calculate_bmi(height, weight):
    bmi = round((weight/(height**2)),2)
    print("\nHeight is " + str(height) +"m")
    print("Weight is " + str(weight) + "kg")
    print("Bmi is " +str(bmi)
    if(bmi<18.5):
             print("This person is underweight")
    elif(bmi>25.0):
        print("This person is overweight")
 
    else:
        print("This person's weight is normal")

calculate_bmi(weight=57, height=1.73)
