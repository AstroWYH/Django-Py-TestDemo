from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)
    # extra = models.TextField(default=2) # 如果新增列，那么需要给默认值，或允许为空
    # extra2 = models.TextField(null=True, blank=True)
    
"""
create table app01_userinfo(
    id bigint auto_increment primary key,
    name varchar(32),
    password varchar(64),
    age int
)
"""

class Department(models.Model):
    title = models.CharField(max_length=16)
    
# 新建数据
# insert into app01_department(title)values("Market")
# Department.objects.create(title="Market")
# UserInfo.objects.create(name="zx", password="123", age=18)