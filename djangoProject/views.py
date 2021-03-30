from django.http import HttpResponse
from django.shortcuts import render, redirect


def hello(request):
    return HttpResponse("Hello world ! ")







def runoob(request):
  views_name = "菜鸟教程"
  return  render(request,"index.html", {"name":views_name})

def runoob(request):
    name = request.GET.get("name")
    return HttpResponse('姓名：{}'.format(name))

def runoob(request):
    name = request.POST.get("name")
    return HttpResponse('姓名：{}'.format(name))
#数据类型是二进制字节流，是原生请求体里的参数内容，在 HTTP 中用于 POST，因为 GET 没有请求体。
#在 HTTP 中不常用，而在处理非 HTTP 形式的报文时非常有用，例如：二进制图片、XML、Json 等。
def runoob(request):
    name = request.body
    print(name)
    return HttpResponse("菜鸟教程")
#获取 URL 中的路径部分，数据类型是字符串。
def runoob(request):
    name = request.path
    print(name)
    return HttpResponse("菜鸟教程")
#获取当前请求的方式，数据类型是字符串，且结果为大写。
def runoob(request):
    name = request.method
    print(name)
    return HttpResponse("菜鸟教程")
#响应对象主要有三种形式：HttpResponse()、render()、redirect()。
#HttpResponse(): 返回文本，参数为字符串，字符串中写文本内容。如果参数为字符串里含有 html 标签，也可以渲染。
def runoob(request):
    # return HttpResponse("菜鸟教程")
    return HttpResponse("<a href='https://www.runoob.com/'>菜鸟教程</a>")

#render(): 返回文本，第一个参数为 request，第二个参数为字符串（页面名称），第三个参数为字典（可选参数，向页面传递的参数：键为页面参数名，值为views参数名）。
def runoob(request):
    name ="菜鸟教程"
    return render(request,"runoob.html",{"name":name})

#redirect()：重定向，跳转新页面。参数为字符串，字符串中填写页面路径。一般用于 form 表单提交后，跳转到新页面。
def runoob(request):
    return redirect("/index/")