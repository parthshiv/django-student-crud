from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import Student
from django.http import HttpResponse

# Get the Home page
def Home(request):
    args = {}    
    args['title'] = "Home"
    return render(request, 'enroll/home.html', args)

# Get the Dashboard with all data from Students table
def Dashboard(request):
    args = {}    
    args['title'] = "Dashboard"
    args['students'] = Student.objects.all() # fetch all data from student table of database
    return render(request, 'enroll/dashboard.html', args)

# Save the data of Add Student form into database
def SaveStudent(request):
    args = {}
    
    if request.method == 'POST':
        if request.POST.get('student_id'):  # this is for Edit student          
            studentId = request.POST.get('student_id')
            args['student_id'] = studentId
            student = Student.objects.get(pk=studentId)
            form = StudentRegistration(request.POST, instance=student) # will get form with edited filled data
            if form.is_valid(): #checks validated data of form 
                #if you want to save all fields from Form into Database
                form.save()
                return redirect('dashboard')  # redirect after saving
            else:
                args['form'] = form
                return render(request, 'enroll/edit_student.html', args)
        else: # this is for Add Student
            form = StudentRegistration(request.POST) # will get form with newly filled data
            if form.is_valid():
                form.save() 
                return redirect('dashboard')  
                """
                below will only save particular fields and not all fields, i.e in this line we didn't added email field, so it wont be saved
                """
                # name = form.cleaned_data['name'] #cleaned_data is a form function to get clean data from form to save
                # email = form.cleaned_data['email']
                # password = form.cleaned_data['password']
                # #below will only save particular fields and not all fields, i.e in below line we didn't added email field, so it wont be saved in db
                # registration = Student(name=name, password=password) 
                # registration.save()
                
            else:
                args['form'] = form
                return render(request, 'enroll/add_student.html', args)  
    
# Get form of Add Student
def AddStudent(request):
    args = {}    
    args['title'] = "Student Registartion Form"
    form = StudentRegistration() #represents blank form
    args['form'] = form    
    return render(request, 'enroll/add_student.html', args)

# Get form of Edit Student
def EditStudent(request, id):
    args = {}    
    args['title'] = "Edit Student Registartion Form Data"
    args['student_id'] = id
    studentId = Student.objects.get(pk=id)
    form = StudentRegistration(instance=studentId) #represents a form with filled data
    args['form'] = form    
    return render(request, 'enroll/edit_student.html', args)

def DeleteStudent(request):
    
    if request.method == 'POST':
        studentId = request.POST.get('student_id')
        student = Student.objects.get(pk=studentId)
        
        try:
            student = Student.objects.get(pk=studentId)  # Fetch the student by primary key
            student.delete()  # Delete the student record
            return redirect('dashboard')  # Redirect to the dashboard after deletion
        except Student.DoesNotExist:
            return HttpResponse("Student not found.", status=404)
    

