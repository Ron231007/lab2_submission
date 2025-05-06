def calculate_bmi(height, weight):
    bmi = round((weight/(height**2)),2)
    print("\nHeight is " + str(height) +"m")
    print("Weight is " + str(weight) + "kg")
    print("Bmi is " +str(bmi))
    if(bmi<18.5):
             print("This person is underweight")
             return -1
    elif(bmi>25.0):
        print("This person is overweight")
        return 1
 
    else:
        print("This person's weight is normal")
        return 0

def main():

      height = float(input("\nWhat is ur height in m: "))
      weight = float(input("What is ur weight in kg: "))
 
      calculate_bmi(height,weight)
 

if __name__ =="__main__":
    main()
