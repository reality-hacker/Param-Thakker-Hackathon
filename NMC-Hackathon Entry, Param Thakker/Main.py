import numpy as np
import matplotlib.pyplot as plt
def linear_regression(x,y):
    w = np.linalg.inv(x.T.dot(x)).dot(x.T).dot(y)

    return w

user_entry_1 = float(input("First value for x Out of 7 values: "))

user_entry_2 = float(input("Second value for x Out of 7 values: "))

user_entry_3 = float(input("Third value  for x  Out of 7 values: "))

user_entry_4 = float(input("Fourth value for x Out of 7 values: "))

user_entry_5 = float(input("Fifth value for x Out of 7 values: "))

user_entry_6 = float(input("Sixth value for x Out of 7 values: "))

user_entry_7 = float(input("Seventh value for x Out of 7 values: "))

user_entry_8 = float(input("First value for y Out of 7 values: "))

user_entry_9 = float(input("Second value for y Out of 7 values: "))

user_entry_10 = float(input("Third value  for y Out of 7 values: "))

user_entry_11 = float(input("Fourth value for y Out of 7 values: "))

user_entry_12 = float(input("Fifth value for y Out of 7 values: "))

user_entry_13 = float(input("Sixth value for y Out of 7 values: "))

user_entry_14 = float(input("Seventh value for y Out of 7 values: "))

x = np.array([[user_entry_1,1],[user_entry_2,1],[user_entry_3,1],[user_entry_4,1],[user_entry_5,1],[user_entry_6,1],[user_entry_7,1]])
y = np.array([user_entry_8,user_entry_9,user_entry_10,user_entry_11,user_entry_12,user_entry_13,user_entry_14])



weights=linear_regression(x,y)
print("Weights:", weights)

plt.scatter(x[:,0],y, color='blue', label='Data points')

x_values=np.linspace(np.min(x[:,0]), np.max(x[:,0]), 100)
y_values=weights[0]*x_values+weights[1]
plt.plot(x_values, y_values, color='red', label='Prediction for patient Adherence/Endurance')

patient_name=input("What is patient's name: ")
print("The next screen will show you the endurance level and best possible treatment for the patient ", patient_name)
plt.xlabel('Treatment Intensity')
plt.ylabel('Patient Adherence')
plt.title('Best Procedure for the Patient')
plt.legend()
plt.grid(True)
plt.show()