from django import forms
from .models import Topic, Problem

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['name', 'difficulty', 'leetcode_link', 'logic_notes', 'solved', 'need_revision']
