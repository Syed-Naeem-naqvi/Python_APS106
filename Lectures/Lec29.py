# x and y are instance attributes

class PatientData:

    def __init__(self, height=0, weight=0):
        self.height_cm = 0
        self.weight_kg = 0
        self.date_of_measurement = 0

# Keys are ID numbers
# dict = {first_name: str, last_name: str, Measurements: PatientData}
patient_data = {'1':{'First_name':'Jane','Last_name':'Doe', 'measurement': PatientData(155,52)}}
print(patient_data)


# Print() shits itself and doesn't work if you try to use it by calling __str__() on an instance that's nested within another data structure










