from django import forms
from django.utils import timezone
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Optional details...'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_title(self):
        title = (self.cleaned_data.get('title') or '').strip()
        if not title:
            raise forms.ValidationError('Title is required')
        return title

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if not due_date:
            return due_date

        today = timezone.localdate()

        # if editing an existing todo:
        if self.instance and self.instance.pk:
            old_due_date = self.instance.due_date

            # if user Did Not change due_date, allow it even if it is now in the past
            if old_due_date == due_date:
                return due_date

            # if user changed it, enforce the rule
            if due_date < today:
                raise forms.ValidationError('Due date cannot be in the past.')
            return due_date

        # if createing a new todo, enforce the rule
        if due_date < today:
            raise forms.ValidationError('Due date cannot be in the past.')

        return due_date
