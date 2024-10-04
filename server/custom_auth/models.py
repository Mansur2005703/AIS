from django.db import models

class Speciality(models.Model): #Специальность
    title = models.CharField(max_length=70)
    short_title = models.CharField(max_length=30, null=True)
    code = models.CharField(max_length=30, null=True)
    
class Group(models.Model): #Группа
    title = models.CharField(max_length=50)
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    speciality_id = models.ForeignKey('Speciality', on_delete=models.CASCADE)

class Subject(models.Model): #Предмет
    title = models.CharField(max_length=70)

class Student(models.Model): #Студент
    iin = models.CharField(max_length=100)
    group_id = models.ForeignKey('Group', on_delete=models.CASCADE) 

class Teacher(models.Model): #Преподаватель
    iin = models.CharField(max_length=8)
    password = models.CharField(max_length=70,null=True)  
    
class TeacherAuthToken(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    
class Audience(models.Model): #Аудитория
    title = models.CharField(max_length=70)

class TeacherAuidience(models.Model): #Преподаватель-аудитория
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    audience_id = models.ForeignKey('Audience', on_delete=models.CASCADE)
    
class TeacherSubject(models.Model): #Преподаватель-предмет
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE) 
    
class StudentInfo(models.Model): #Информация о студенте
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    patronymic = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    birthday = models.DateField(null=True)
    
class TeacherInfo(models.Model): #Информация о преподавателе
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    birthday = models.DateField(null=True)
