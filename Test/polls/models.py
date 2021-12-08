import mysql
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import CharField, Model, Sum
from django_mysql.models import ListCharField

class user_info(models.Model):
    GENDER_MALE = "남"
    GENDER_FEMALE = "여"
    GENDER_CHOICES = ((GENDER_FEMALE, "남"), (GENDER_MALE, "여"))

    students = "초중고학생"
    freelancer = "프리랜서"
    univ_students = "대학생"
    office_worker = "회사원"
    JOB_CHOICES = ((students, "초중고학생"), (freelancer, "프리랜서"), (univ_students, "대학생"), (office_worker, "회사원"))

    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    year = models.IntegerField(db_column='년')
    month = models.IntegerField(db_column='월')
    day = models.IntegerField(db_column='일')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=5, db_column='성별')
    job = models.CharField(choices=JOB_CHOICES, max_length=20, db_column='직업')
    room_name = models.CharField(max_length=50, db_column='방이름', null=True)
    room_size = models.IntegerField(db_column='방크기', null=True)
    # rating = models.IntegerField(db_column='rating', max_length=10)


class Fixed_info(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    kitchen = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='주방')
    fridge = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='냉장고')
    toilet = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='화장실')
    bed = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='침대')
    closet = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='옷장')
    washer = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='세탁기')
    front = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='현관')


class Add_info(models.Model):
    MATTRESS_SINGLE = "싱글"
    MATTRESS_SUPER = "슈퍼싱글"
    MATTRESS_QUEEN = "퀸"
    MATTRESS_KING = "킹"
    MATTRESS_CHOICE = ((MATTRESS_SINGLE, "싱글"), (MATTRESS_SUPER, "슈퍼싱글"), (MATTRESS_QUEEN, "퀸"), (MATTRESS_KING, "킹"))
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    mattress = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='매트리스')
    fridge = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='냉장고')
    washer = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='세탁기')
    desk = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='책상')
    closet = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='옷장')
    cabinet = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='수납장')
    side_table = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='협탁')
    hanger = models.PositiveIntegerField(validators=[MaxValueValidator(25)], db_column='행거')


class File(models.Model):
    photo = models.ImageField(upload_to="")


class layout(models.Model):
    # user_id = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    tag = ListCharField(
        base_field=CharField(max_length=9),
        size=5,
        max_length=(5 * 10),
    )
    restLoca = models.IntegerField()
    kitchenLoca = models.IntegerField()


class Rating(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    layout = models.ForeignKey(layout, default='', on_delete=models.CASCADE)
    rating = models.IntegerField(db_column='rating')


#for i in len(layout.object.all()):
    #avg = float(Rating.objects.filter(layout=i).aggregate(Sum('rating'))['rating__sum'] / len(Rating.object.filter(layout=i)))

class Usertable:
    GENDER_MALE = "남"
    GENDER_FEMALE = "여"
    GENDER_CHOICES = ((GENDER_FEMALE, "남"), (GENDER_MALE, "여"))
    gender = models.CharField(choices=GENDER_CHOICES, max_length=5, db_column='gender')
    age = models.IntegerField(db_column='age')
    usernum = models.IntegerField(db_column='usernum')
    members = models.IntegerField(db_column='members')

class Grouptable:
    groupvalue = models.IntegerField(db_column='group')
    tagvalue = models.IntegerField(db_column='tag')
    picturenum = models.IntegerField(db_column='picturenum')
    usernum = models.IntegerField(db_column='usernum')

class Testrate:
    picturenum = models.IntegerField(db_column='picturenum')
    rating = models.IntegerField(db_column='rating')
    usernum = models.IntegerField(db_column='usernum')