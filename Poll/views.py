from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PollForm
from .models import Poll

# Create your views here.

def home(request):
    polls = Poll.objects.all()
    context = {'polls':polls}
    return render(request,'Poll/home.html',context)

def create(request):
    if request.method=='POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = PollForm()
        context={'form':form}
    return render(request,'Poll/create.html',context)

def vote(request,id):
    poll = Poll.objects.get(pk=id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count +=1
        elif selected_option == 'option2':
            poll.option_two_count +=1
        elif selected_option == 'option3':
            poll.option_three_count +=1
        else:
            return HttpResponse(400,'invalid form')
        poll.save()
        return redirect('result_page', poll.id)
    context = {'poll':poll}
    return render(request,'Poll/vote.html',context)

def result(request,id):
    poll = Poll.objects.get(pk=id)
    context = {'poll':poll}
    return render(request,'Poll/result.html',context)