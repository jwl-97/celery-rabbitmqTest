from django.db import models


class CommonModelFieldMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Test(CommonModelFieldMixin):
    username = models.CharField(max_length=255, blank=True, default="")
    email = models.CharField(max_length=255, blank=True, default="")

    def save(self, *args, **kwargs):
        super(Test, self).save(*args, **kwargs)
        from .tasks import create_random_user_accounts
        create_random_user_accounts.delay(self.username)
