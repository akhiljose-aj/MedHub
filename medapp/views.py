from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages


def home(request):
    return render(request,"index.html")

def appoint(request):
    return render(request,'appoinment.html')

def adminlog(request):
    return render(request,'admin.html')

def adminlog2(request):
    if request.method == 'POST':
        name=request.POST['name']
        pswd=request.POST['pasw']
        data=admin_log.objects.filter(admin_name=name)
        if data:
            data1 = admin_log.objects.get(admin_name=name)
            if data1.admin_pass == pswd:
                request.session['id'] = name
                return redirect(admin2)
            else:
                messages.info(request, 'invalid username or password')
                return redirect(adminlog)
        else:
            messages.info(request, 'invalid username or password')
            return redirect(adminlog)

def login(request):
    return render(request,'login1.html')

def signup(request):
    return render(request,'signup.html')

def signup2(request):
    if request.method=='POST':
        name = request.POST['name']
        phn=request.POST['mob']
        mail=request.POST['email']
        user=request.POST['uname']
        psw=request.POST['pasw']
        radio=request.POST['gender']
        data=user_log.objects.create(full_name=name,phone=phn,gmail=mail,username=user,password=psw,gender=radio)
        data.save()
    messages.success(request, "SignUp Successfull!")
    return redirect(login)

def admin2(request):
    d=user_log.objects.all()
    return render(request,'admin2.html',{'data':d})

def homepage(request):
    if request.method == 'POST':
        mail = request.POST['logemail']
        pswd = request.POST['logpas']
        data = user_log.objects.filter(gmail=mail)
        if data:
            data1 = user_log.objects.get(gmail=mail)
            if data1.password == pswd:
                request.session['id'] = mail
                return render(request, 'homepage.html')
            else:
                messages.info(request, 'invalid E-mail or password')
                return redirect(login)
        else:
            messages.info(request, 'invalid E-mail or password')
            return redirect(login)

def home2(request):
    return render(request,'homepage.html')

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(home)

def book_appoint(request):
    if request.method == 'POST':
        fname=request.POST['name']
        mail=request.POST['email']
        radio = request.POST['gender']
        bkdate=request.POST['setTodaysDate']
        depart=request.POST['dep']
        phn=request.POST['phone']
        msg=request.POST['message']
        payment=request.POST['pay']
        data=appoint_booking.objects.create(name=fname,email=mail,gender=radio,date=bkdate,phone=phn,department=depart,message=msg,payment_id=payment)
        data.save()
        messages.info(request, 'Booking successfull !')
        return render(request,'appoinment.html')
def doctors1(request):
    return render(request,'doctors.html')

def doctorform(request):
    if request.method=='POST':
        doc_name=request.POST['dname']
        doc_id=request.POST['did']
        doc_img=request.FILES['dpic']
        dep=request.POST['dep']
        data=doctor_form.objects.create(doctor_name=doc_name,doctor_id=doc_id,doctor_img=doc_img,doctor_dept=dep)
        data.save()
        messages.info(request, 'Doctor Added Successfully!')
        return render(request,'doctors.html')
    else:
        messages.info(request, 'Something Went Wrong Please Try Again')
        return render(request, 'doctors.html')

def reg_docs(request):
    d=doctor_form.objects.all()
    return render(request,'registered_doc.html',{'data':d})

def del_doc(id):
    doctor_form.objects.filter(pk=id).delete()
    return redirect(reg_docs)

def admin_app(request):
    d=appoint_booking.objects.filter(status='pending')
    return render(request,'admin_app.html',{'data':d})

def del_app(request,id):
    appoint_booking.objects.filter(pk=id).delete()
    return redirect(admin_app)

def accept_app(request,id):
    appoint_booking.objects.filter(pk=id).update(status='approve')
    return redirect(admin_app)

def booking_details(request):
    pending_bookings=[]
    history=[]
    d = appoint_booking.objects.filter(status='pending')
    for i in d:
        if i.email == request.session['id']:
            pending_bookings.append(i)
    d1= appoint_booking.objects.filter(status='approve')
    for j in d1:
        if j.email == request.session['id']:
            history.append(j)
    return render(request, 'user_bk_details.html',{'data':pending_bookings,'data1':history})

