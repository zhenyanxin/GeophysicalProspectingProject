# coding=utf-8
from django.db import models


# Create your models here.


class Register(models.Model):  # 注册信息表
    user_id = models.IntegerField(primary_key=True)  # 用户ID
    nick_name = models.CharField(max_length=30)      # 昵称
    password = models.CharField(max_length=20)       # 密码
    phone = models.CharField(max_length=20)          # 手机号

    class Meta:
        db_table = 'register'


class Complete(models.Model):  # 完善信息表
    user_ida = models.ForeignKey(Register,primary_key=True)    # 用户ID
    user_name = models.CharField(max_length=20)       # 姓名
    identity = models.CharField(max_length=20)        # 身份证号
    bank = models.CharField(max_length=30)            # 开户行
    bank_number = models.CharField(max_length=50)     # 银行卡号
    gender = models.CharField(max_length=10)          # 性别
    address = models.CharField(max_length=300)        # 地址

    #   models.ForeignKey(user_ida)

    class Meta:
        db_table = 'complete'


class SelectTable(models.Model):    # 可选信息表
    user_ids = models.ForeignKey(Register,primary_key=True)    # 用户ID
    education = models.CharField(max_length=30)         # 学历
    qq = models.CharField(max_length=20)                # QQ号
    wechat = models.CharField(max_length=30)            # 微信号
    models.ForeignKey(user_ids)

    class Meta:
        db_table = 'selecttable'


class Equip_Type(models.Model):     # 设备分类表
    type_id1 = models.IntegerField(primary_key=True)    # 设备分类ID
    type_big1 = models.CharField(max_length=20)         # 设备大分类
    type_small1 = models.CharField(max_length=20)       # 设备小分类

    class Meta:
        db_table = 'equip_type'


class Collection(models.Model):     # 收藏表
    collect_id = models.IntegerField(primary_key=True)  # 用户ID
    user_idc = models.ForeignKey(Register)              # 收藏ID
    collect_type = models.IntegerField()                # 最初分类
    cproduct_id = models.IntegerField()                 # 收藏产品ID
    cproduct_image = models.CharField(max_length=200)   # 收藏产品图片
    cproduct_name = models.CharField(max_length=100)    # 收藏产品名称
    cproduct_price = models.DecimalField(max_digits=10, decimal_places=2)   # 出租费用

    class Meta:
        db_table = 'collection'


class Issue(models.Model):      # 发布表
    issue_id = models.IntegerField(primary_key=True)    # 用户ID
    user_idi = models.ForeignKey(Register)              # 发布ID
    issue_type = models.IntegerField()                  # 最初分类
    iproduct_id = models.IntegerField()                 # 发布产品ID
    iproduct_image = models.CharField(max_length=200)   # 发布产品图片
    iproduct_name = models.CharField(max_length=100)    # 发布产品名称
    iproduct_price = models.DecimalField(max_digits=10, decimal_places=2)   # 出租费用
    models.ForeignKey(user_idi)

    class Meta:
        db_table = 'issue'


class Equipment(models.Model):      # 设备信息表
    equip_id = models.IntegerField(primary_key=True, auto_created=True)     # 设备ID
    equip_type = models.IntegerField()                                      # 最初分类
    equip_name = models.CharField(max_length=100)                           # 设备名称
    produce_date = models.DateField()                                       # 生产日期
    equip_over = models.DateField()                                         # 到期年限
    equip_owner = models.ForeignKey(Register)                               # 设备所属
    equip_expense = models.DecimalField(max_digits=9, decimal_places=2)     # 设备价格
    equip_start = models.DateField()                                        # 出租开始时间
    equip_end = models.DateField()                                          # 出租结束时间
    equip_price = models.DecimalField(9, 2)                                 # 出租费用
    equip_picture = models.CharField(max_length=100)                        # 设备图片
    equip_typeb = models.CharField(max_length=100)                          # 设备大类别
    equip_types = models.CharField(max_length=100)                          # 设备小类别
    equip_parameter = models.CharField(max_length=100)                      # 性能参数
    equip_place = models.CharField(max_length=100)                          # 地点
    equip_comment = models.CharField(max_length=100)                        #备注
    models.ForeignKey(equip_owner)

    class Meta:
        db_table = 'equipment'


class Software(models.Model):   # 软件信息表
    software_id = models.IntegerField(primary_key=True)                     # 软件ID
    software_type = models.IntegerField()                                   # 最初分类
    software_name = models.CharField(max_length=100)                        # 软件名称
    software_owner = models.ForeignKey(Register)                            # 软件所属
    software_expense = models.DecimalField(max_digits=9, decimal_places=2)  # 软件价格
    software_start = models.DateField()                                     # 出租开始时间
    software_end = models.DateField()                                       # 出租结束时间
    software_price = models.DecimalField(max_digits=9, decimal_places=2)    # 出租费用
    software_picture = models.CharField(max_length=100)                     # 软件图片
    software_typed = models.CharField(max_length=100)                       # 软件大类别
    software_types = models.CharField(max_length=100)                       # 软件小类别
    software_describe = models.CharField(max_length=100)                    # 软件描述
    os = models.CharField(max_length=100)                                   # 运行平台
    software_comment = models.CharField(max_length=100)                     # 备注
    models.ForeignKey(software_type)

    class Meta:
        db_table = 'software'


class Technology(models.Model):     # 技术信息表
    tech_id = models.IntegerField(primary_key=True, auto_created=True)  # 软件ID
    tech_type = models.IntegerField()                                   # 最初分类
    tech_name = models.CharField(max_length=100)                        # 技术服务名称
    tech_info = models.CharField(max_length=100)                        # 技术服务信息
    tech_typeb = models.CharField(max_length=100)                       # 技术服务大类别
    tech_types = models.CharField(max_length=100)                       # 技术服务小类别
    tech_owner = models.ForeignKey(Register)                            # 技术服务所属
    tech_price = models.DecimalField(max_digits=9, decimal_places=2)    # 出租费用
    tech_image = models.CharField(max_length=100)                       # 技术服务图片
    tech_comment = models.CharField(max_length=100)                     # 备注
    models.ForeignKey(tech_owner)

    class Meta:
        db_table = 'technology'
