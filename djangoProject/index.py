from django.http import HttpResponse
from djangoProject.interface import send_message2FG as send #将处理后的csv文件内容发送给FG
from django.shortcuts import render, redirect
from djangoProject.interface import instuctions_toFG as ins
import threading

fg_path = "E:\\softwareBoot\\flightgear\\FlightGear 2020.3.5\\bin"
csv_path ="C:\\Users\\flyeat_22\\AppData\\Roaming\\flightgear.org\\Export\\7.csv"
def index(request):
    context={}
    return render(request, 'index.html', context)
def open_fg(request):
    context={}
    terrasync =request.POST.get("terrasync")
    if terrasync == "on":
        terrasync="--enable-terrasync"
    else:
        terrasync=" "
    fdm = request.POST.get("fdm")
    if fdm == "on":
        fdm = " "
    else:
        fdm = " --fdm=null"
    airport = request.POST.get("airport")
    if airport :
        airport_con = " --airport="+airport
    else:
        airport_con = " "

    aircraft = request.POST.get("aircraft")
    flight_config = ""
    if aircraft:
        aircraft_con = "--aircraft="+aircraft
        if aircraft=="c172p":
            flight_config = "C172P"
        elif aircraft=="c172r":
            flight_config = "C172R"
        elif aircraft=="da42":
            flight_config = "DA_42"
        elif aircraft=="sr22":
            flight_config = "SR_22"
        elif aircraft=="erj145":
            flight_config="ERJ_145"
        else:
            flight_config = "playback_edit2"

    else:
        aircraft_con = " "
    outport = request.POST.get("outport")
    inport = request.POST.get("inport")
    send_frequency = request.POST.get("send_frequency")
    receive_frequency = request.POST.get("receive_frequency")
    other_config = request.POST.get("other_config")
    config_instructions = "fgfs.exe --httpd=7080 "+terrasync+" "+fdm+airport_con+" "+aircraft_con+\
                          " --generic=socket,out,"+send_frequency+",127.0.0.1,"+outport+\
                          ",udp,"+flight_config+" --generic=socket,in,"+receive_frequency+\
                          ",127.0.0.1,"+inport+",udp,"+flight_config+" "+other_config
    print(config_instructions)
    switch = request.POST.get("switch")
    if switch == "on":
        ins.open_FG_Root(fg_path)
        ins.start_FG(config_instructions,fg_path)
    fg_pathtest = request.POST.get("path_text")
    print(config_instructions)
    return render(request, 'index.html', context)
def upload(request):
    context = {}
    file = request.POST.get("file")
    print(file)
    return render(request, 'index.html', context)
def send_message(request):
    context = {}
    ip = request.POST.get("ip")
    des_port = request.POST.get("des_port")
    des_port_int = int(des_port)
    send_frequency = request.POST.get("send_frequency")
    send_frequency_int = int(send_frequency)
    #file = request.POST.get("file")
    csv_path = request.POST.get("csv_path")
    send.send_csv_message(csv_path,send_frequency_int,ip,des_port_int)
    return render(request, 'index.html', context)



# def start_send_message(request):
#     send_message_th = threading.Thread(target=send_message, args=(request,))
#     context = {}
#     send_message_th.join(0)
#     send_message_th.start()
#     send_message_th.join(0)
#     return render(request, 'index.html', context)
