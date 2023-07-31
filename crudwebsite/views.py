from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ValidationError
import pandas as pd
from .forms import UploadFileForm
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error Logging In, Please Try Again...")
            return redirect('home')
        
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully Logged Out!!...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticat and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have succesfully Registerd! Welcome!!...")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    # authentication check
    if request.user.is_authenticated:
        #look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    
    else:
        messages.success(request, "You Must Be Logged In To See The Page!!...")
        return redirect('home')


def delete_record(request, pk):
    # authentication check 
    if request.user.is_authenticated:
        # delete record
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record has been Deleted Sucessfully!!")
        return redirect('home')

    else:
        messages.success(request, "You Must Be Logged In To Do That!!...")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    #   authentication check 
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'This record has been added!')
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})

    else:
        messages.success(request, "You Must Be Logged In To Do That!!...")
        return redirect('home') 


def update_record(request, pk):
    #   authentication check 
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'This record has been updated!')
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    
    else:
        messages.success(request, "You Must Be Logged In To Do That!!...")
        return redirect('home')



def upload_record(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                handle_uploaded_file(request, request.FILES['file'])
                messages.success(request, 'This file has been added to the table!')
            except ValidationError as e:
                error_message = str(e).strip('[]').replace("'", "")
                messages.error(request, error_message)
            return redirect('upload_record')
    else:
        form = UploadFileForm()
    return render(request, 'upload_record.html', {'form': form})




def handle_uploaded_file(request, f):
    # Get the file extension
    file_extension = f.name.split('.')[-1]

    # Handle different file formats
    if file_extension == 'xlsx':
        # Read the Excel file into a DataFrame
        df = pd.read_excel(f, engine='openpyxl')
    elif file_extension == 'xls':
        # Read the Excel file into a DataFrame
        df = pd.read_excel(f, engine='xlrd')
    elif file_extension == 'csv':
        # Read the CSV file into a DataFrame
        df = pd.read_csv(f)
    else:
        raise ValidationError('This format is not supported. Please use xlxs, xls, or csv format!')

    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict('records')

    #print(data)

    # Update the data in the database
    update_data(request, data)




def update_data(request, data):
    # Define the required fields
    required_fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode']

    # Create a list to store the updated model instances
    updated_instances = []

    # Iterate over the data and update the model instances
    for row in data:
        # Check if all required fields are present
        if not all(field in row for field in required_fields):
            raise ValidationError('This record does not contain all required fields. Please fix this!')

        # Check if there are any extra fields
        if len(row) > len(required_fields):
            raise ValidationError('This record contains extra fields. Please fix this!')
        
        # Get the model instance using the primary key
        instance = Record(first_name=row.get('first_name'), last_name = row.get("last_name"), 
                        email = row.get("email"), phone = row.get("phone"), address = row.get("address"),
                        city = row.get("city"), state = row.get("state"), zipcode = row.get("zipcode"))

        # instance.save() # it would add a single record at a time
        # # Update the instance with the new data
        # instance.first_name = row.get("first_name")
        # instance.last_name = row.get("last_name")
        # instance.email = row.get("email")
        # instance.phone = row.get("phone")
        # instance.address = row.get("address")
        # instance.city = row.get("city")
        # instance.state = row.get("state")
        # instance.zipcode = row.get("zipcode")

        # Add the updated instance to the list
        updated_instances.append(instance)
        

    # Use the bulk_update method to update the data in the database
    Record.objects.bulk_create(updated_instances) # it would add multiple record as a bulk
    

def export_records(request):
    # Get data from the Record model
    records = Record.objects.all().values()
    # Create a DataFrame from the records data
    df = pd.DataFrame.from_records(records)
    # Convert the timezone-aware created_at values to timezone-naive values
    df['created_at'] = df['created_at'].apply(lambda x: x.replace(tzinfo=None))
    # Create a response object for the Excel file
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=records.xlsx'
    # Write the DataFrame to the response object as an Excel file
    writer = pd.ExcelWriter(response, engine='openpyxl')
    df.to_excel(writer, index=False)
    writer.close()
    return response