from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView
# Create your views here.
from .forms import UserAnswerForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
def question(request):
    context = {
        'questions': questions.objects.all()
    }
    return render(request, 'BITS_Assist/question.html', context)

class QuestionListView(ListView):
    model = questions
    template_name = 'BITS_Assist/question.html'
    context_object_name = 'questions'
    ordering = ['-date_posted']


class QuestionDetailView(DetailView):
    model = questions
    
class QuestionCreateView(CreateView):
    model = questions
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = questions
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


def answer(request,**kwargs):
    pk = kwargs['pk']
    q = questions.objects.filter(id=pk)[0]
    context = {
        'form':UserAnswerForm
    }
    if request.method == 'POST':
        form = UserAnswerForm(request.POST)
        if form.is_valid():
            form.instance.of_question = q
            form.instance.author = request.user
            form.save()
            return redirect('BITS_Assist-question')
    else:
        return render(request, 'BITS_Assist/answer.html', context)

class get_answer(LoginRequiredMixin,CreateView):
    model = answers
    fields = ['content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False

class AnswerListView(ListView):
    model = answers
    context_object_name = 'answers'
    template_name = 'BITS_Assist/answer_list.html'
    ordering = ['-date_posted']

   

@login_required
def upvote(request,**kwargs):
    answer = get_object_or_404(answers,id=request.POST.get('answer_id'))
    is_liked = False
    if answer.upvote.filter(id=request.user.id).exists():
      answer.upvote.remove(request.user)
      is_liked = False
    else:
      answer.upvote.add(request.user) 
      is_liked = True
    return HttpResponseRedirect(answer.get_absolute_url())

@login_required
def downvote(request,**kwargs):
    answer = get_object_or_404(answers,id=request.POST.get('answer_id'))
    answer.downvote.add(request.user) 
    return HttpResponseRedirect(answer.get_absolute_url())


# def downvote(request,**kwargs):
#     pk = kwargs['pk']
#     q = answers.objects.filter(id=pk)[0]
#     q.downvotes.count = q.downvotes.count + 1
#     return render(request, 'BITS_Assist/question.html')


