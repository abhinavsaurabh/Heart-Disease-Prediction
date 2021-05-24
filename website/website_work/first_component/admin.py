from django.contrib import admin
from first_component.models import Predictions
from django import forms

# Register your models here.

class Prediction(admin.ModelAdmin):
    list_display=('age','sex','cp_Atypical_Angina','cp_Non_Angina','cp_Asymptomatic','resting_bp','serum_cholesterol','fasting_blood_sugar','resting_ecg','max_heart_rate',
        'exercise_induced_angina','st_depression','st_slope_Upsloping','st_slope_Flat','st_slope_DownSloping','number_of_vessels','thallium_None','thallium_Normal','thallium_Fixed_Defect','thallium_Reversible_Defect', 'num')

admin.site.register(Predictions,Prediction)