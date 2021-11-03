from django.core.validators import MaxValueValidator
from django.db import models


class user_info(models.Model):
    AGE_TEN = 10
    AGE_TWENTY = 20
    AGE_THIRTY = 30
    AGE_FORTY = 40
    AGE_CHOICES = ((AGE_TEN, 10), (AGE_TWENTY, 20), (AGE_THIRTY, 30), (AGE_FORTY, 40))

    GENDER_MALE = "남"
    GENDER_FEMALE = "여"
    GENDER_CHOICES = ((GENDER_FEMALE, "남"), (GENDER_MALE, "여"))

    JOB_STUDENT = "학생"
    JOB_FREELANCE = "프리랜서"
    JOB_NONE = "무직"
    JOB_WORKER = "직장인"
    JOB_CHOICES = ((JOB_STUDENT, "학생"), (JOB_FREELANCE, "프리랜서"), (JOB_NONE, "무직"), (JOB_WORKER, "직장인"))

    #user_id = models.CharField(max_length=100, default='', db_column='아이디')
    age = models.IntegerField(choices=AGE_CHOICES, db_column='나이')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=5, db_column='성별')
    job = models.CharField(choices=JOB_CHOICES, max_length=20, db_column='직업')
    room_name = models.CharField(max_length=50, db_column='방이름')
    room_size = models.IntegerField(db_column='방크기')


class Fixed_info(models.Model):
    user_id = models.ForeignKey('user_info', default='', on_delete=models.CASCADE, db_column='아이디')
    kitchen = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='주방')
    frige = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='냉장고')
    toilet = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='화장실')
    bed = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='침대')
    closet = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='옷장')
    washer = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='세탁기')


class Add_info(models.Model):
    MATTRESS_SINGLE = "싱글"
    MATTRESS_SUPER = "슈퍼싱글"
    MATTRESS_QUEEN = "퀸"
    MATTRESS_KING = "킹"
    MATTRESS_CHOICE = ((MATTRESS_SINGLE, "싱글"), (MATTRESS_SUPER, "슈퍼싱글"), (MATTRESS_QUEEN, "퀸"), (MATTRESS_KING, "킹"))
    user_id = models.ForeignKey('user_info', on_delete=models.CASCADE, db_column='아이디')
    mattress = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='매트리스')
    frige = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='냉장고')
    washer = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='세탁기')
    desk = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='책상')
    closet = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='옷장')
    cabinet = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='수납장')
    side_table = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='협탁')
    hanger = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='행거')


class file(models.Model):
    photo = models.ImageField(upload_to="image")
