from django.db import models
from django.utils import timezone


# Create your models here.
sex_choices=((0, 'Female'),(1, 'Male'))
#cp_typical_angina=((1, 'Typical Angina'),(2, 'Atypical Angina'),(3, 'Non-Angina'),(4, 'Asymptomatic'))
fasting_blood_sugar_choices=((1,'> 120 mg/dl'),((0,'< 120 mg/dl')))
resting_ecg_choices=((0, 'Normal'),(1, 'Having ST-T wave abnormality'),(2, 'hypertrophy'))
exercise_induced_angina_choices=((0, 'No'),(1, 'Yes'))
#st_slope_choices=((1, 'Upsloping'),(2, 'Flat'),(3, 'Down Sloping'))
number_of_vessels_choices=((0, 'None'),(1, 'One'),(2, 'Two'),(3, 'Three'))
#thallium_scan_results_choices=((3, 'Normal'),(6, 'Fixed Defect'),(7, 'Reversible Defect'))
#['age','sex','resting_blood_pressure','cholesterol','fasting_blood_sugar','rest_ecg','max_heart_rate','exercise_induced_angina','ST_depression','major_vessels_num','chest_pain_type_1','chest_pain_type_2','chest_pain_type_3','slope_exercise_0','slope_exercise_1','slope_exercise_2','thalassemia_0','thalassemia_1','thalassemia_2','thalassemia_3']

class Predictions(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField(choices=sex_choices, default=0)
    cp_Atypical_Angina = models.IntegerField(default=0)
    cp_Non_Angina = models.IntegerField(default=0)
    cp_Asymptomatic = models.IntegerField(default=0)
    resting_bp = models.IntegerField()
    serum_cholesterol = models.IntegerField()
    fasting_blood_sugar = models.IntegerField(choices=fasting_blood_sugar_choices,default=0)
    resting_ecg = models.IntegerField(choices=resting_ecg_choices,default=0)
    max_heart_rate = models.IntegerField()
    exercise_induced_angina = models.IntegerField(choices=exercise_induced_angina_choices,default=0)
    st_depression = models.DecimalField(max_digits=4, decimal_places=2)
    st_slope_Upsloping = models.IntegerField(default=0)
    st_slope_Flat = models.IntegerField(default=0)
    st_slope_DownSloping = models.IntegerField(default=0)
    number_of_vessels = models.IntegerField(choices=number_of_vessels_choices)
    thallium_None = models.IntegerField(default=0)
    thallium_Normal = models.IntegerField(default=0)
    thallium_Fixed_Defect = models.IntegerField(default=0)
    thallium_Reversible_Defect = models.IntegerField(default=0)
    predicted_on = models.DateTimeField(default=timezone.now)
    num=models.IntegerField(null=True)

    def get_absolute_url(self):
        return reverse('predict:predict')
