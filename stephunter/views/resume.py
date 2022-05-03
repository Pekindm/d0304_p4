from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from stephunter.models import Resume
from stephunter.forms import ResumeForm


class ResumeNewView(LoginRequiredMixin, View):
    def get(self, request):
        if Resume.objects.filter(owner_id=request.user.id):
            return redirect('resume_create')
        return render(request, 'stephunter/resume/resume-create.html')


class ResumeView(LoginRequiredMixin, View):
    def get(self, request):
        if Resume.objects.filter(owner_id=request.user.id):
            resume = Resume.objects.filter(owner_id=request.user.id).first()
            form = ResumeForm(instance=resume)
            return render(request, 'stephunter/resume/resume-edit.html', context={
                'form': form,
            })
        return redirect('resume_new')

    def post(self, request):
        resume = Resume.objects.filter(owner_id=request.user.id).first()
        if resume:
            form = ResumeForm(request.POST, instance=resume)
            if form.is_valid():
                resume = form.save(commit=False)
                resume.owner = get_object_or_404(User, id=request.user.id)
                resume.save()
                messages.add_message(request, messages.SUCCESS, 'Резюме обновлено!')
                return redirect('resume_new')
            messages.add_message(request, messages.ERROR, 'Что-то пошло не так!')
            return render(request, 'stephunter/resume/resume-edit.html', context={
                'form': form,
            })
        return redirect('resume_lets_start')


class ResumeCreateView(LoginRequiredMixin, View):
    def get(self, request):
        if Resume.objects.filter(owner_id=request.user.id):
            return redirect('resume')
        form = ResumeForm()
        return render(request, 'stephunter/resume/resume-edit.html', context={
            'form': form,
        })

    def post(self, request):
        if Resume.objects.filter(owner_id=request.user.id):
            return redirect('resume')
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.owner = get_object_or_404(User, id=request.user.id)
            resume.save()
            messages.add_message(request, messages.SUCCESS, 'Резюме обновлено!')
            return redirect('resume')
        messages.add_message(request, messages.ERROR, 'Ошибка!')
        return render(request, 'stephunter/resume/resume-edit.html', context={
            'form': form,
        })
