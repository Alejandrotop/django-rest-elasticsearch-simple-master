from django.db import models

class Store(models.Model):
  title = models.CharField(max_length=10)

  def __str__(self):
    return self.title

class Product(models.Model):
  title = models.CharField(max_length=50)
  store = models.ForeignKey(Store, on_delete=models.CASCADE)

  @property
  def store_indexing(self):
    if self.store is not None:
      return self.store.id

  def __str__(self):
    return self.title