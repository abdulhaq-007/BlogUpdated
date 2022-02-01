from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField("Tag nomi",max_length=100,)
    slug = models.SlugField("*",max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField("Kategoriya nomi",max_length=100)
    slug = models.SlugField("*",max_length=100, unique=True)
    image_of_category = models.ImageField(upload_to='category_images/')

    def get_absolute_url(self):
        return reverse("blog:category_detail",kwargs={"category_slug":self.slug})

    def __str__(self):
        return f"{self.name}"
  
class Post(models.Model):
	title = models.CharField(max_length=250)
	image = models.ImageField(verbose_name="Maqola rasmi", upload_to='post_Images/')
	body = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	up = models.PositiveIntegerField(default=0)
	down = models.PositiveIntegerField(default=0)
	active = models.BooleanField(default=True)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, related_name='categories')
	tag = models.ManyToManyField(Tag, related_name='tags')
	published = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-id"]                       

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='post_comments')
    name = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    alreadyLiked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} liked {self.post}"        