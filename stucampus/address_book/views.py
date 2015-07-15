#coding:utf-8
from django.shortcuts import render,render_to_response,get_object_or_404,HttpResponseRedirect
from django import forms
from address_book.models import  Member,Manager
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q




# Create your views here.
#定义表单模型
class MemberMsg(forms.Form):
	name=forms.CharField()
	grade=forms.CharField()
	sex=forms.CharField()
	department=forms.CharField()
	position=forms.CharField()
	stuID=forms.CharField()
	dormitory=forms.CharField()
	birthday_type=forms.CharField()
	#birthday=forms.DateField()
	phone_num_long=forms.CharField()
	phone_num_short=forms.CharField()
	is_work=forms.CharField()
	wechat=forms.CharField()
	qq=forms.CharField()

class ManagerForm(forms.Form):
    	managername = forms.CharField(max_length=100)
 	password = forms.CharField(widget=forms.PasswordInput())

def addMsg(req):
	managername=req.session.get('managername','')
	if req.method=='POST':
		msg=MemberMsg(req.POST)
		if msg.is_valid() and managername:
			member=Member()
			member.name=msg.cleaned_data['name']
			member.grade=msg.cleaned_data['grade']
			member.sex=msg.cleaned_data['sex']
			member.department=msg.cleaned_data['department']
			member.stuID=msg.cleaned_data['stuID']
			member.dormitory=msg.cleaned_data['dormitory']
			member.birthday_type=msg.cleaned_data['birthday_type']
			member.position=msg.cleaned_data['position']
			#member.birthday=msg.cleaned_data['birthday']
			member.phone_num_long=msg.cleaned_data['phone_num_long']
			member.phone_num_short=msg.cleaned_data['phone_num_short']
			member.wechat=msg.cleaned_data['wechat']
			member.is_work=msg.cleaned_data['is_work']
			member.qq=msg.cleaned_data['qq']
			member.save()
			return HttpResponse('OK')
		else:
			return HttpResponse('NO')
	else:
		msg=MemberMsg()
	return render_to_response('manage.html',{'msg':msg,'managername':managername})

def main(req):
	managername=req.session.get('managername','')
	if req.method=='GET':			
		all_objects=Member.objects.all()
		msgs, page_range = my_pagination(req, all_objects)
		return render_to_response('main.html',{'msgs':msgs,'page_range':page_range,'managername':managername})
	else:
		search=req.POST['search']
		if  search=='':
			return HttpResponseRedirect('/main/')
		else:
			all_objects=Member.objects.filter(Q(name=search)|Q(stuID=search))
			msgs, page_range = my_pagination(req, all_objects)
			return render_to_response('main.html',{'msgs':msgs,'page_range':page_range,'managername':managername})

def showGradeMsg(req,grade):
	managername=req.session.get('managername','')
	all_objects=Member.objects.filter(grade=grade)
	msgs, page_range = my_pagination(req, all_objects)
	return render_to_response('main.html',{'msgs':msgs,'page_range':page_range,'managername':managername})


def msgUpdate(req,id):
	managername=req.session.get('managername','')
	
	if req.method=='GET':
		member= get_object_or_404(Member, id=id,)
		return render_to_response('manage.html',{'member':member,'managername':managername})
	else:
		member_id=id
		member=Member.objects.get(id=member_id)
		update_msg=MemberMsg(req.POST)
		if update_msg.is_valid() and managername:
			member.name=update_msg.cleaned_data['name']
			member.grade=update_msg.cleaned_data['grade']
			member.sex=update_msg.cleaned_data['sex']
			member.department=update_msg.cleaned_data['department']
			member.stuID=update_msg.cleaned_data['stuID']
			member.dormitory=update_msg.cleaned_data['dormitory']
			member.phone_num_long=update_msg.cleaned_data['phone_num_long']
			member.phone_num_short=update_msg.cleaned_data['phone_num_short']
			member.birthday_type=update_msg.cleaned_data['birthday_type']
			#member.birthday=update_msg.cleaned_data['birthday']
			member.position=update_msg.cleaned_data['position']
			member.wechat=update_msg.cleaned_data['wechat']
			member.qq=update_msg.cleaned_data['qq']
			member.save()
			return HttpResponse('update OK')
		else:
			return HttpResponse('update NO')

def login(req):
	if req.method=='POST':
		mf=ManagerForm(req.POST)
		if mf.is_valid():
			managername=mf.cleaned_data['managername']
			password=mf.cleaned_data['password']
			manager=Manager.objects.filter(managername__exact=managername,password__exact=password)
			if manager:
				req.session['managername']=managername
				req.session.set_expiry(3600*2)
				return HttpResponseRedirect('/main/')
			else:
				return HttpResponseRedirect('/login/')
	else:
		mf=ManagerForm()
	return render_to_response('login.html',{'mf':mf})

def logout(req):
	try:
		del req.session['managername']
	except KeyError:
		pass
	return HttpResponseRedirect('/main/')


#与main函数配合，实现分页功能
def my_pagination(req,queryset,display_amount=15,after_range_num=5,bevor_range_num=4):
	paginator=Paginator(queryset,display_amount)
	try:
		page=int(req.GET.get('page'))
	except :
		page=1
	try:
		objects=paginator.page(page)
	except EmptyPage:
		objects=paginator.page(paginator.num_pages)
	except:
		objects=paginator.page(1)
	if page>=after_range_num:
		page_range=paginator.page_range[page-after_range_num:page+bevor_range_num]
	else:
		page_range=paginator.page_range[0:page+bevor_range_num]
	return objects,page_range


