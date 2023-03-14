from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View
from django.contrib import messages
from .forms import Regform
from .forms import DepForm
from .models import RegModel
from .forms import Department,ManageForm,Manager,DepForm

# from .forms import Regform


# Create your views here.

class Regview(View):
    def get(self,req):
        form=Regform()
        return render(req,"reg.html",{"form":form})

    def post(self,req):
        form_data=Regform(req.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data.get('name')
            age=form_data.cleaned_data.get('age')
            em=form_data.cleaned_data.get('email')
            ex=form_data.cleaned_data.get('experience')
            RegModel.objects.create(name=name,age=age,email=em,experience=ex)
            messages.success(req,"Registration completed successfully")
            return redirect('reg')
        else:
            messages.error(req,"registration failed")
            return render(req,"reg.html",{'form':form_data})    



class Home(View):
    def get(self,req):
        return render(req,'HOME.HTML')


class ViewEmp(View):
    def get(self,req):
        emp=RegModel.objects.all()
        return render(req,"viewsemp.html",{'data':emp})

class DeleteEmp(View):
    def get(self,req,*args,**kwargs):
        id=kwargs.get('id')
        eob=RegModel.objects.get(eid=id)
        eob.delete()
        return redirect('vemp')

class EditEmp(View):
    def get(self,req,*args,**kwargs):
        id=kwargs.get('id')
        emp=RegModel.objects.get(eid=id)
        # email=emp['email']
        # print(email)
        form=Regform(initial={'name':emp.name,'age':emp.age,'email':emp.email,'experience':emp.experience})
        return render(req,"editempp.html",{'form':form})
    def post(self,req,*args,**kwargs):
        form=Regform.get('id')
        if form.is_valid():
            name=form.cleaned_data.get('name') 
            age=form.cleaned_data.get('age') 
            em=form.cleaned_data.get('email') 
            ex=form.cleaned_data.get('experience')
            RegModel.objects.filter(eid=id).update(
                name=name,age=age,email=em,experience=ex
                )   
            return redirect('vemp')
        else:
            return redirect('editemp') 
        

class Deptview(View):
    def get(self,req,*args,**kwargs):
        form=DepForm()
        return render(req,"deptreg.html",{'form':form})
    def post(self,req,*args,**kwargs):    
        form_data=DepForm(req.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(req,"Department Added")
            return redirect('dept')       

class DepRet(View):
    def get(self,req):
        data=Department.objects.all()
        return render(req,"viewdept.html",{"data":data})   

class DepDelete(View):
    def get(self,req,*args,**kwargs):
        did=kwargs.get('id')
        dept=Department.objects.get(id=did)
        dept.delete()
        return redirect('depret')    

# class Depedit(View):
#     def get(self,req,*args,**kwargs):
#         i_id=kwargs.get('did')
#         dept=Department.objects.get('did')
#         form=DepForm(req.POST,instance=dept)
        
#         return render(req,"editdept.html",{'form':form})

class DeptEdit(View):
    def get(self,req,*args,**kwargs):
        d_id=kwargs.get('id')
        dept=Department.objects.get(id=d_id)
        form=DepForm(instance=dept)
        return render(req,"editdept.html",{'form':form})       

def post(self,req,*args,**kwargs):
    d_id=kwargs.get('did')
    dept=Department.objects.get(id=d_id)
    form_data=DepForm(req.POST,instance=dept)
    if form_data.is_valid():
        form_data.save()
        return redirect('depret')
    else:
        return redirect('deptedit')       

class ManagerReg(View):
    def get(self,req):
        form=ManageForm()
        return render(req,'addman.html',{'form':form})        

    def post(self,req):
        form_data=ManageForm(req.POST,files=req.FILES)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('this file is uploaded succsessfully')
        else:
            return redirect('addman')        

class ManagerList(View):
    def get(self,req):
        data=Manager.objects.all()
        return render(req,"viewman.html",{"data":data}) 
            

class DelMen(View):
    def get(self,req,*args,**kwargs):
        id=kwargs.get('id')  
        delm=ManagerList         



class Index(View):
    def get(self,req):
        return render(req,'index.html')