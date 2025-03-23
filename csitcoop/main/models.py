from django.db import models
    
class Partner(models.Model):
    partner_id = models.AutoField(primary_key=True)
    username_pn = models.CharField(max_length=150, unique=True)
    password_pn = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_th = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    agencies = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    description_pn = models.TextField(blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    subdistrict = models.CharField(max_length=255, blank=True, null=True)
    road = models.CharField(max_length=255, blank=True, null=True)
    soi = models.CharField(max_length=255, blank=True, null=True)
    moo = models.CharField(max_length=255, blank=True, null=True)
    building_no = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    related_fields = models.TextField(blank=True, null=True)
    email_pn = models.EmailField(unique=True, null=True)
    image_pn = models.ImageField(upload_to='partner_images/', blank=True, null=True)
    walfare_benefits = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name_en} ({self.username_pn})"

class HumanResource(models.Model):
    hr_id = models.AutoField(primary_key=True)
    username_hr = models.CharField(max_length=150, unique=True)
    password_hr = models.CharField(max_length=255)
    email_hr = models.EmailField(unique=True)
    name_hr = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    partner = models.ForeignKey("Partner", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.hr_id} ({self.name_hr})"

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    studentname_th = models.CharField(max_length=255)
    studentname_en = models.CharField(max_length=255)
    student_email = models.EmailField(unique=True)
    student_phone = models.CharField(max_length=20)
    degree = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=4)
    gpa = models.FloatField()
    address = models.TextField()
    program = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.student_id} - {self.studentname_en}"
    
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=255)
    job_posted = models.DateTimeField(auto_now_add=True)
    job_description = models.TextField()
    job_skill = models.TextField()
    job_major = models.CharField(max_length=255)
    job_welfare_benefits = models.CharField(max_length=2000)
    hr = models.ForeignKey("HumanResource", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job_id} - {self.job_name} ({self.job_posted})"

class Jobposition(models.Model):
    job_id =  models.ForeignKey("Job", on_delete=models.CASCADE, default=None)
    student_id = models.ForeignKey("Student", on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return f"{self.job_id} - {self.student_id}"

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    partner = models.ForeignKey("Partner", on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.review_id} - {self.student.studentname_en} ({self.review_date})"