from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth


class user_info(models.Model):

    #AGE_TEN = 10
    #AGE_TWENTY = 20
    #AGE_THIRTY = 30
    #AGE_FORTY = 40
    #AGE_CHOICES = ((AGE_TEN, 10), (AGE_TWENTY, 20), (AGE_THIRTY, 30), (AGE_FORTY, 40))

    GENDER_MALE = "남"
    GENDER_FEMALE = "여"
    GENDER_CHOICES = ((GENDER_FEMALE, "남"), (GENDER_MALE, "여"))

    JOB_STUDENT = "학생"
    JOB_FREELANCE = "프리랜서"
    JOB_NONE = "무직"
    JOB_WORKER = "직장인"
    JOB_CHOICES = ((JOB_STUDENT, "학생"), (JOB_FREELANCE, "프리랜서"), (JOB_NONE, "무직"), (JOB_WORKER, "직장인"))

    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    year = models.IntegerField(db_column='년')
    month = models.IntegerField(db_column='월')
    day = models.IntegerField(db_column='일')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=5, db_column='성별')
    job = models.CharField(choices=JOB_CHOICES, max_length=20, db_column='직업')
    room_name = models.CharField(max_length=50, db_column='방이름', null=True)
    room_size = models.IntegerField(db_column='방크기', null=True)
    #rating = models.IntegerField(db_column='rating', max_length=10)

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

class UserLatestTags(models.Model):
    user_id = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    furniture = models.IntegerField(db_column='furniture')
    tag = models.IntegerField(db_column='tag')

class Rating(models.Model):
    user_id = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    furniture = models.IntegerField( db_column='furniture')
    rating = models.IntegerField( db_column='rating')
    rtype = models.CharField(max_length=10, db_column='type')
    tag = models.IntegerField(db_column='tag')

    
class Test(models.Model):
    furniture = models.ForeignKey("rating", related_name='furniture', on_delete=models.CASCADE, db_column='furniture')
    gname = models.CharField(max_length=50, db_column='name')
    rtype= models.CharField(max_length=50, db_column='type')
    tag = models.IntegerField( db_column='tag')
    rating = models.IntegerField( db_column='rating')
    members = models.IntegerField( db_column='memebers')

