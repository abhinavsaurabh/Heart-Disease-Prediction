from django import forms
from django.core import validators

from first_component.models import Predictions

class Predict_Form(forms.ModelForm):
    class Meta:
        model = Predictions
        fields = ('age','sex','cp_Atypical_Angina','cp_Non_Angina','cp_Asymptomatic','resting_bp','serum_cholesterol','fasting_blood_sugar','resting_ecg','max_heart_rate',
        'exercise_induced_angina','st_depression','st_slope_Upsloping','st_slope_Flat','st_slope_DownSloping','number_of_vessels','thallium_None','thallium_Normal','thallium_Fixed_Defect','thallium_Reversible_Defect')
        widgets = {'age': forms.TextInput(attrs={'class': 'form-control'}),
                   'sex': forms.Select(attrs={'class': 'form-control'}),
                   'cp_Atypical_Angina': forms.TextInput(attrs={'class': 'form-control'}),
                   'cp_Non_Angina': forms.TextInput(attrs={'class': 'form-control'}),
                   'cp_Asymptomatic': forms.TextInput(attrs={'class': 'form-control'}),
                   'resting_bp':forms.TextInput(attrs={'class': 'form-control'}),
                   'serum_cholesterol':forms.TextInput(attrs={'class': 'form-control'}),
                   'fasting_blood_sugar':forms.Select(attrs={'class': 'form-control'}),
                   'resting_ecg':forms.Select(attrs={'class': 'form-control'}),
                   'max_heart_rate':forms.TextInput(attrs={'class': 'form-control'}),
                   'exercise_induced_angina':forms.Select(attrs={'class': 'form-control'}),
                   'st_depression':forms.TextInput(attrs={'class': 'form-control'}),
                   'st_slope_Upsloping': forms.TextInput(attrs={'class': 'form-control'}),
                   'st_slope_Flat': forms.TextInput(attrs={'class': 'form-control'}),
                   'st_slope_DownSloping': forms.TextInput(attrs={'class': 'form-control'}),
                   'number_of_vessels':forms.Select(attrs={'class': 'form-control'}),
                   'thallium_None':forms.TextInput(attrs={'class': 'form-control'}),
                   'thallium_Normal':forms.TextInput(attrs={'class': 'form-control'}),
                   'thallium_Fixed_Defect':forms.TextInput(attrs={'class': 'form-control'}),
                   'thallium_Reversible_Defect':forms.TextInput(attrs={'class': 'form-control'}),
                   }