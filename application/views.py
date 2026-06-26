from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Company
from django.contrib import auth
from django.contrib import messages

def index(request) :
    return render(request, 'index.html')

def candidate_register(request) :
    if request.method == "POST" :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2 : 
            if User.objects.filter(username = username).exists() :
                # print("Username already exists")
                messages.info(request, "Username already exists")
                # return redirect("/accounts/register")
                return redirect("candidate_register")


            elif User.objects.filter(email= email).exists() : 
                # print("Email already exists")
                messages.info(request, "Email already exists")
                return redirect("candidate_register")

            else : 
                user = User.objects.create_user(username=username, email=email, password=password1, first_name= first_name, last_name= last_name)
                user.save()
                print("User saved successfully")
                return redirect('candidate_login')


        else:
            # print("Password didn't match")
            messages.info(request, "Password didn't match")
            return redirect("candidate_register")

    else : 
         return render(request, "candidate_register.html")
    
def candidate_login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None :
            auth.login(request, user)
            print("User login success")
            return render(request, 'index.html')
        else :
            messages.info(request, "False Credentials")
            return redirect('candidate_login')
    else :
        return render(request, 'candidate_login.html')
    
def logout(request) :
     auth.logout(request)
     return redirect('/')

def candidate(request) :
    return render(request, 'authorize_candidate.html')
def recruiter(request) :
    return render(request, 'authorize_company.html')

def company_register(request) :
    if request.method == "POST" :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        company = request.POST['company']
        job = request.POST['job']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2 : 
            if User.objects.filter(username = username).exists() :
                messages.info(request, "Username already exists")
                return redirect("company_register")


            elif User.objects.filter(email= email).exists() : 
                messages.info(request, "Email already exists")
                return redirect("company_register")
            
            elif Company.objects.filter(company= company, job= job).exists() :
                 messages.info(request, "Company with same job profile already exists")
                 return redirect("company_register")

            else : 
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name
                )

                Company.objects.create(
                    user=user,
                    company=company,
                    job=job
                )
                messages.success(request, "Company registered successfully")
                return redirect("company_login")


        else:
            # print("Password didn't match")
            messages.info(request, "Password didn't match")
            return redirect("company_register")

    else : 
        return render(request, "company_register.html")
    

def company_login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        company = request.POST['company']
        recruiter = auth.authenticate(username = username, password = password)
        if recruiter is not None :
            auth.login(request, recruiter)
            print("User login success")
            return render(request, 'index.html')
        else :
            messages.info(request, "False Credentials")
            return redirect('company_login')
    else :
        return render(request, 'company_login.html')