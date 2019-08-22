from django.db import models

# Create your models here.
# 어떤 데이터를 어떤 형태로 데이터베이스에 저장할 것이냐?
# 프론트에서 어떤 폼 태그와 어떤 제약 조건을 반영할 것이냐?
# models.Model : ORM 관련 기능을 가지고 있다.
# ORM : 실제 데이터를 코드로 추상화 해놓고 사용한다.
# 데이터를 저장, 확인, 수정, 삭제
class BMI(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    bmi_score = models.FloatField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # makemigrations bmi : 변경 사항을 추적해서 반영할 내용을 migration파일로 만들어 둔다.
    # migrate bmi 0001 : migration 파일을 실제 DB에 반영한다.

    def __str__(self):
        return "키 : "+str(self.height)+" 체중 : "+str(self.weight)+" BMI : "+str(self.bmi_score)


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.bmi_score = self.weight / ((self.height/100)**2)

        super(BMI, self).save(force_insert, force_update, using,update_fields)


