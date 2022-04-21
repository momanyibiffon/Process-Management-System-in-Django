# This source code was written by :
#    Name: Momanyi Biffon Manyura   ID: 202114080103    Degree: PhD
#    University: 电子科技大学 School: Computer Science and Engineering
#    Course: Operating Systems Structure and applications
#    Lecturer: Prof. Chao Song
#    Date: 2022/04/19


from venv import create
from django.shortcuts import render, HttpResponse, redirect
import psutil as ps, datetime
from django.contrib import messages

# the home page view that retrieve all processes
def index_view(request):
    template = "processes/index.html"
    title = "Process Management"

    def all_ps():
        p = ps.process_iter(['pid', 'name', 'username', 'status', 'create_time'])
        return p

    context = {
        'title': title,
        'all_processes':  all_ps(),
    }
    return render(request, template, context,)

# managing a single process
def single_process_view(request):
    try:
        title = "Managing process"
        template = "processes/single_process.html"
        process_id = request.GET.get('p_id')

        ps_details = ps.Process(int(process_id))
        create_time = datetime.datetime.fromtimestamp(ps_details.create_time()).strftime("%Y-%m-%d %H:%M:%S")

        context = {
            'title': title,
            'process_id': process_id,
            'ps_details': ps_details,
            'create_time': create_time,
        }
        return render(request, template, context)
    
    except ps.AccessDenied:
        messages.error(request, "ERROR! You dont have permission to modify this process")


# suspending a process
def suspend_process_view(request):
    try:
        title = "Managing process"
        template = "processes/single_process.html"
        process_id = request.GET.get('p_id')

        ps_details = ps.Process(int(process_id))
        create_time = datetime.datetime.fromtimestamp(ps_details.create_time()).strftime("%Y-%m-%d %H:%M:%S")   

        try:
            try:
                if ps_details.status() != 'stopped':
                    ps_details.suspend()
                    messages.success(request, "Process {} has been suspended".format(process_id))
            except ps.AccessDenied:
                messages.warning(request, "You don't have permission to modify process {}".format(process_id))
        except ps.Error:
            messages.error(request, "An error occured!")

        ps_details = ps.Process(int(process_id))
    
    except ps.AccessDenied:
        messages.error(request, "ERROR! You dont have permission to modify this process")
        
    context = {
        # 'title': title,
        'process_id': process_id,
        'ps_details': ps_details,
        'title': title,
        'create_time': create_time,
    }
    return render(request, template, context)


# resuming a process
def resume_process_view(request):
    # suspending process
    title = "Managing process"
    template = "processes/single_process.html"
    process_id = request.GET.get('p_id')

    ps_details = ps.Process(int(process_id))
    create_time = datetime.datetime.fromtimestamp(ps_details.create_time()).strftime("%Y-%m-%d %H:%M:%S")
    old_status = ps_details.status()
    try:
        ps_details.resume()
        new_status = ps_details.status()
        if new_status != old_status:
            messages.success(request, "Process {} has been resumed".format(process_id))
        elif new_status == old_status:
            messages.error(request, "ERROR! This process cannot be modified at this moment")
        else:
            pass
    except ps.Error:
        messages.error(request, "ERROR! This process cannot be modified at this moment")

    ps_details = ps.Process(int(process_id))
    


    context = {
        # 'title': title,
        'process_id': process_id,
        'ps_details': ps_details,
        'title': title,
        'create_time': create_time,
    }
    return render(request, template, context)


# terminating a process
def terminate_process_view(request):
    title = "Managing process"
    template = "processes/single_process.html"
    process_id = request.GET.get('p_id')

    ps_details = ps.Process(int(process_id))

    try:
        if ps_details.status() == 'running' or ps_details.status() == 'stopped':
            ps_details.terminate()
            messages.success(request, "Process {} has been terminated!".format(process_id))
            return redirect('processes:index')
        else:
            pass
    except ps.Error:
        messages.error(request, "An error occured while terminating process {} ".format(process_id))

    context = {
        'title': title,
        'ps_details': ps_details,
        'ps': ps,
    }

    return render(request, template, context)

