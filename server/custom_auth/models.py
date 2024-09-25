from django.db import models

class Speciality(models.Model): #Специальность
    id = models.BigIntegerField()
    title = models.CharField()
    
class Group(models.Model): #Группа
    id = models.BigIntegerField()
    title = models.CharField()
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    speciality_id = models.ForeignKey('Speciality', on_delete=models.CASCADE)
    
class Audience(models.Model): #Аудитория
    id = models.BigIntegerField()
    number = models.CharField()

class Subject(models.Model): #Предмет
    id = models.BigIntegerField()
    title = models.CharField()

class Student(models.Model): #Студент
    id = models.BigIntegerField()
    iin = models.CharField()
    group_id = models.ForeignKey('Group', on_delete=models.CASCADE) 

class Teacher(models.Model): #Преподаватель
    id = models.BigIntegerField()
    iin = models.CharField()
    password = models.CharField(null=True)  
    
class TeacherAuidience(models.Model): #Преподаватель-аудитория
    id = models.BigIntegerField()
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    audience_id = models.ForeignKey('Audience', on_delete=models.CASCADE)
    
class TeacherSubject(models.Model): #Преподаватель-предмет
    id = models.BigIntegerField()
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE) 
    
class StudentInfo(models.Model): #Информация о студенте
    id = models.BigIntegerField()
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    first_name = models.CharField(null=True)
    last_name = models.CharField(null=True)
    patronymic = models.CharField(null=True)
    phone = models.CharField(null=True)
    birthday = models.DateField(null=True)
    
class TeacherInfo(models.Model): #Информация о преподавателе
    id = models.BigIntegerField()
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    first_name = models.CharField(null=True)
    last_name = models.CharField(null=True)
    patronymic = models.CharField(null=True)
    phone = models.CharField(null=True)
    birthday = models.DateField(null=True)
