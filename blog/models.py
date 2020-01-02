from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)#This assigns the current date and time to this field whenever an instance of this class is created.
    last_modified = models.DateTimeField(auto_now=True)#This assigns the current date and time to this field whenever an instance of this class is saved. That means whenever you edit an instance of this class, the date_modified is updated.
    categories = models.ManyToManyField('Category', related_name='posts')
    """The ManyToManyField takes two arguments.
     The first is the model with which the relationship is, in this case its Category.
     The second allows us to access the relationship from a Category object, even though we haven’t added a field there.
     By adding a related_name of posts, we can access category.posts to give us a list of posts with that category."""

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    """This is similar to the ManyToManyField but instead defines a many to one relationship.
    The reasoning behind this is that many comments can be assigned to one post.
    But you can’t have a comment that corresponds to many posts."""
