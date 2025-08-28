from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home_view(request):
    item_list = Item_List.objects.all()
    item_objects = Item.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html', {'items': item_objects, 'item_list': item_list, 'review': review})

def about(request):
    obj_About = AboutUs.objects.all()
    return render(request, 'about.html', {'about': obj_About})

def menu_view(request):
    item_list = Item_List.objects.all()
    item_objects = Item.objects.all()
    return render(request, 'menu.html', {'items': item_objects, 'item_list': item_list})

def book_table_view(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        phone_number = request.POST['phone_number']
        user_email = request.POST['user_email']
        total_persons = request.POST['total_person']
        booking_date = request.POST['booking_data']
        if user_name != '' and phone_number != 0 and user_email != '':
            booking = BookTable(Name=user_name, PhoneNumber=phone_number, Total_Persons=total_persons, Email=user_email,Booking_date=booking_date)
            booking.save()
             # Send confirmation email
            subject = 'Booking Confirmation'
            message = f"Hello {user_name},\n\nYour booking has been successfully received.\n" \
                      f"Booking details:\nTotal persons: {total_persons}\n" \
                      f"Booking date: {booking_date}\n\nThank you for choosing us!"

            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user_email]  # The email of the user

            # Send the confirmation email
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Table booked successfully!')
        else:
            messages.error(request, 'Please fill in all fields.')
    return render(request, 'book_table.html')

def feedback_view(request):
    if request.method == 'POST':
        userName = request.POST['User_name']
        description = request.POST['Description']
        rating = request.POST['Rating']
        selfie = request.FILES['Selfie']

        feedback = Feedback(
            User_name=userName,
            Description=description,
            Ratings=rating,
            Image=selfie
        )
        feedback.save()

        messages.success(request, 'Feedback submitted successfully!')
        return redirect('/')

    return render(request, 'feedback.html')

def signup(request):
    if request.method == 'POST':
        # Handle signup logic here
        if request.method == 'POST':
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
        if User.objects.filter(username=username).exists():
            print('Username Already exists:')

        if password1 != password2:  
            messages.error(request, 'Passwords do not match.')
    
    user = User.objects.create_user(username, email, password1)
    user.password1 = password1
    user.password2 = password2
    user.save()

    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')

