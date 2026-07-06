bob = [{"Name":"Jeremy","Marks":92,"Attendance":99},
       {"Name":"Carl","Marks":43,"Attendance":100},
       {"Name":"Jimmy","Marks":95,"Attendance":41},
       {"Name":"Billy","Marks":82,"Attendance":83},
       {"Name":"Bob","Marks":93,"Attendance":96}]
def good_student(y):
    return y["Marks"] > 75 and y["Attendance"] > 84
result = list(filter(good_student, bob))
print(result)