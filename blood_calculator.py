print("This is the blood_calculator.py file")
print("Python thinks this is called {}".format(__name__))


def interface():
    print("blood calculator")
    keep_running = True
    while keep_running:
        print("Options:")
        print("9 - Quit")
        print("1 - HDL Analysis")
        print("2 - LDL Analysis")       
        choice = input("Select an options:")
        if choice == "9":
             keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
    print("Program ending")
    
def HDL_driver():
    HDL_in = HDL_input()
    HDL_analy = HDL_analysis(HDL_in)
    HDL_output(HDL_in, HDL_analy)
    
    
def HDL_input():
    HDL_value = input("Enter the HDL result:")
    HDL_value = int(HDL_value)
    return HDL_value

def HDL_analysis(HDL_int):
    if HDL_int>= 60:
        answer = "Normal"
    elif 40 <= HDL_int <60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer


def HDL_output(HDL_value, HDL_analy):
    print("The HDL result of {} is considered {}".format(HDL_value,HDL_analy))
    return

def LDL_driver():
    LDL_in = LDL_input()
    LDL_analy = LDL_analysis(LDL_in)
    LDL_output(LDL_in, LDL_analy)
    
    
def LDL_input():
    LDL_value = input("Enter the LDL result:")
    LDL_value = int(LDL_value)
    return LDL_value

def LDL_analysis(LDL_int):
    if LDL_int< 130:
        answer = "Normal"
    elif 130 <= LDL_int <159:
        answer = "Borderline High"
    elif 160 <= LDL_int <189:
        answer = "High"
    else:
        answer = "Very Low"
    return answer


def LDL_output(LDL_value, LDL_analy):
    print("The LDL result of {} is considered {}".format(LDL_value,LDL_analy))
    return
    
    
    
def Total_Cholesterol_driver():
    Total_Cholesterol_in = Total_Cholesterol_input()
    Total_Cholesterol_analy = Total_Cholesterol_analysis(Total_Cholesterol_in)
    Total_Cholesterol_output(Total_Cholesterol_in, Total_Cholesterol_analy)
    
    
def Total_Cholesterol_input():
    Total_Cholesterol_value = input("Enter the Total Cholesterol result:")
    Total_Cholesterol_value = int(Total_Cholesterol_value)
    return HDL_value

def Total_Cholesterol_analysis(Total_Cholesterol_int):
    if Total_Cholesterol_int < 200:
        answer = "Normal"
    elif 200 <= Total_Cholesterol_int <239:
        answer = "Borderline High"
    else:
        answer = "Low"
    return answer


def Total_Cholesterol_output(Total_Cholesterol_value, Total_Cholesterol_analy):
    print("The Total Cholesterol result of {} is considered {}".format(Total_Cholesterol_value,Total_Cholesterol_analy))
    return

if __name__ == "__main__":
    interface()