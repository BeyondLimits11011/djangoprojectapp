from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripción de tarea", widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Título del proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))

