import hashlib
from authority.models import user as u
def addUser(un,pw,ip=""):
	
	
	obj=u(username=un,password=pw,regIP=ip)
	obj.save()
	
def delUser(un):
	
	try:
		obj=u.objects.get(username=un)
		obj.delete()
	except:
		return False
	return True

def getUserList():
	return u.objects.all()

def changePassword(user,newpwd):
	obj=u.objects.get(username=user)
	newpwd=sha512(newpwd)
	obj.password=newpwd
	obj.save()

def getPasswd(un):
	from Blog.models import user as u
	try:
		
		obj=u.objects.get(username=un)
	except:
		return ""
	return obj.password

def isLogin(request):#如果已登录，则返回登录用户的用户名；如果没登录，返回""
	
	try:
		un=request.COOKIES['user']
	except:
		un=""
	try:
		user=u.objects.get(username=un)
	except:
		return ""
	try:
		value=request.COOKIES['password']
	except:
		return ""	

	if value==getKey(un):
		return un
	else:
		return ""

def isAdmin(request):#如果目前登录的用户是管理员，则返回True；如果目前登陆的用户不是管理员或没登录，则返回False
	
	user=isLogin(request)
	try:
		user=u.objects.get(username=user)
	except:
		return False
	return user.isAdmin

def auth(username,passwd):
	pw=getPasswd(username)
	if pw==passwd and passwd!="":
		return True
	else:
		return False

def setCookie(request,username,jumpTo):
	r=render(request,jumpTo)
	r.set_cookie("user",username)
	r.set_cookie("password",getKey(username))
	return r

def logout(request,jumpTo):
	r=render(request,jumpTo)
	r.set_cookie("user","")
	r.set_cookie("password","")
	return r

def getKey(username):
	s=username+getPasswd(username);
	return sha512(s)

def sha512(str):
	m=hashlib.sha512()
	m.update(str.encode("utf-8"))
	return m.hexdigest()