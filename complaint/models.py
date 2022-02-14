from django.db import models
from multiselectfield import MultiSelectField


class Complaint(models.Model):
    RECEIVING_CHOICES =(
        ('فنی','فنی'),
        ('فروش','فروش'),
        ('POS','POS'),
        ('سایر واحدها','سایر واحدها')
    )
    SERVICE_CHOICES =(
        ('POS','POS'),
        ('Internet','Internet')
    )
    USERTYPE_CHOICES=(
        ('کاربر حقیقی(خانگی)','حقیقی'),
        ('کاربر حقوقی(سازمانی)','کاربر حقوقی(سازمانی)')
    )
    OBTIN_CHOICES=(
        ('جلسه','جلسه'),
        ('حضوری','حضوری'),
        ('تلفنی','تلفنی'),
        ('آنلاین','آنلاین')
    )
    REASON_CHOICES=(
        ('اتمام سریع ترافیک','اتمام سریع ترافیک'),
        ('حسابداری','حسابداری'),
        ('نویز خط','نویز خط'),
        ('قطع و وصلی','قطع و وصلی'),
        ('کندی سرعت','کندی سرعت'),
        ('سیمبانی','سیمبانی'),
        ('نمایندگان','نمایندگان'),
        ('تجهیزات','تجهیزات'),
        ('پشتیبانی روزهای تعطیل','پشتیبانی روزهای تعطیل'),
        ('باز نشدن صفحات وب','باز نشدن صفحات وب'),
        ('عدم اطلاع رسانی','عدم اطلاع رسانی'),
        ('مشکلات دستگاه کارتخوان و خدماتش و دیر نصب شدن دستگاه','مشکلات دستگاه کارتخوان و خدماتش و دیر نصب شدن دستگاه'),
        ('طولانی شدن نصب اینترنت','طولانی شدن نصب اینترنت'),
        ('مشکلات وب سایت','مشکلات وب سایت'),
        ('عدم جمع اوری','عدم جمع اوری'),
        ('سایر','سایر')
    )

    Name = models.CharField(max_length=30)
    ID_name = models.CharField(max_length=20)
    Receivingـunit=models.CharField(max_length=30,choices=RECEIVING_CHOICES)
    Typeـservice=models.CharField(max_length=30,choices=SERVICE_CHOICES)
    Userـtype=models.CharField(max_length=30,choices=USERTYPE_CHOICES)
    obtain=models.CharField(max_length=30,choices=OBTIN_CHOICES)
    Phone_number = models.CharField(max_length=10)
    Mobile_number = models.CharField(max_length=15)
    Address = models.CharField(max_length=100,blank=True,null=True)
    ID_customer = models.CharField(max_length=10,blank=True,null=True)
    Reason_complaint=MultiSelectField(choices=REASON_CHOICES,max_choices=4,blank=True,null=True)
    Complaint_description=models.TextField(max_length=200,blank=True,null=True)
    suggestion=models.TextField(max_length=200,blank=True,null=True)
    created_at=models.DateTimeField(blank=True,null=True)

    class Meta :
        verbose_name='شکابت'
        verbose_name_plural='شکایات'


    def __str__(self):
        return self.Name
