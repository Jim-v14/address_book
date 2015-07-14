#coding:utf-8
from django.shortcuts import render,render_to_response,get_object_or_404,HttpResponseRedirect
from django import forms
from address_book.models import  Member,Manager
from django.http import HttpResponse




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
    	managername = forms.CharField(label='用户名：',max_length=100)
 	password = forms.CharField(label='密码：',widget=forms.PasswordInput())

def addMsg(req):
	if req.method=='POST':
		msg=MemberMsg(req.POST)
		if msg.is_valid():
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
	return render_to_response('manage.html',{'msg':msg})

def main(req):
	if req.method=='GET':			
		msgs=Member.objects.all()
		return render_to_response('main.html',{'msgs':msgs})
	else:
		search=req.POST['search']
		if  search=='':
			msgs=Member.objects.all()
			return render_to_response('main.html',{'msgs':msgs})
		else:
			msgs=Member.objects.filter(name=search)
			return render_to_response('main.html',{'msgs':msgs})

def msgUpdate(req,id):
	if req.method=='GET':
		member= get_object_or_404(Member, id=id,)
		return render_to_response('update.html',{'member':member})
	else:
		member_id=id
		member=Member.objects.filter(id=member_id)
		update_msg=MemberMsg(req.POST)
		if update_msg.is_valid():
			member.name=update_msg.cleaned_data['name']
			member.grade=update_msg.cleaned_data['grade']
			member.sex=update_msg.cleaned_data['sex']
			member.department=update_msg.cleaned_data['department']
			member.stuID=update_msg.cleaned_data['stuID']
			member.dormitory=update_msg.cleaned_data['dormitory']
			member.phone_num_long=update_msg.cleaned_data['phone_num_long']
			member.phone_num_short=update_msg.cleaned_data['phone_num_short']
			member.birthday_type=update_msg.cleaned_data['birthday_type']
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
				msgs=Member.objects.all()
				return render_to_response('main.html',{'msgs':msgs,'manager':manager})
			else:
				return HttpResponseRedirect('/login/')
	else:
		mf=ManagerForm()
	return render_to_response('login.html',{'mf':mf})

	
		

