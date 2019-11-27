from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Department(models.Model):
    dept_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.dept_name


class MyAccountManager(BaseUserManager):
    def create_user(self, email, usn, password=None):
        if not email:
            raise ValueEror("Users Must Have An Email Address")
        if not usn:
            raise ValueEror("Users must have an usn")

        user = self.model(
            email=self.normalize_email(email),
            usn=usn,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, usn, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            usn=usn,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    usn = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    pass_out_batch = models.IntegerField(null=True)
    phone = models.CharField(max_length=12, null=True)
    designation = models.CharField(max_length=200, null=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    profile_img = models.ImageField(upload_to='profile_image/', default="profile_image/default_img.png")
    insta_link = models.URLField(max_length=250, null=True)
    facebook_link = models.URLField(max_length=250, null=True)
    pf_link = models.URLField(max_length=250, null=True)
    li_link = models.URLField(max_length=250, null=True)
    github_link = models.URLField(max_length=250, null=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usn']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def name(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class AlumniProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_image/', default="profile_image/default_img.png")

    def __str__(self):
        return self.user.email


class ImageSlider(models.Model):
    event_image = models.ImageField(upload_to="slider/")


class JobOpenings(models.Model):
    job_title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    salary = models.IntegerField(null=True)
    company = models.CharField(max_length=200)
    hr_email = models.CharField(max_length=50)
    posted_date = models.DateTimeField(auto_now_add=True)


class BestAlumnis(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name() + " From Dept " + self.user.dept.dept_name


class Events(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField()
    hosted_dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name + " by " + self.hosted_dept.dept_name


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Account.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=False)
