from django.db import models

class Speciality(models.Model): #Специальность
    title = models.CharField()
    
class Group(models.Model): #Группа
    title = models.CharField()
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    speciality_id = models.ForeignKey('Speciality', on_delete=models.CASCADE)
    
class Audience(models.Model): #Аудитория
    number = models.CharField()

class Subject(models.Model): #Предмет
    title = models.CharField()

class Student(models.Model): #Студент
    iin = models.CharField()
    group_id = models.ForeignKey('Group', on_delete=models.CASCADE) 

class Teacher(models.Model): #Преподаватель
    iin = models.CharField(max_length=100,)
    password = models.CharField(max_length=100,null=True)  
    
class AuthToken(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"Token for {self.teacher.iin}"
        
class Group(models.Model): #Группа
    title = models.CharField(max_length=100,)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    speciality_id = models.ForeignKey('Speciality', on_delete=models.CASCADE)

class TeacherAuidience(models.Model): #Преподаватель-аудитория
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    audience_id = models.ForeignKey('Audience', on_delete=models.CASCADE)
    
class TeacherSubject(models.Model): #Преподаватель-предмет
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE) 
    
class StudentInfo(models.Model): #Информация о студенте
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    first_name = models.CharField(null=True)
    last_name = models.CharField(null=True)
    patronymic = models.CharField(null=True)
    phone = models.CharField(null=True)
    birthday = models.DateField(null=True)
    
class TeacherInfo(models.Model): #Информация о преподавателе
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    first_name = models.CharField(null=True)
    last_name = models.CharField(null=True)
    patronymic = models.CharField(null=True)
    phone = models.CharField(null=True)
    birthday = models.DateField(null=True)
