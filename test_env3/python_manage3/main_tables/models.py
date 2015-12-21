# This is an auto-generated Django model module.
# You"ll have to do the following manually to clean this up:
#   * Rearrange models" order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don"t rename db_table values or field names.
#
# Also note: You"ll have to insert the output of "django-admin sqlcustom [app_label]"
# into your database.
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth import models as auth_models

from django.conf import settings


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class SchemaMigrations(models.Model):
    version = models.TextField()

    class Meta:
        managed = False
        db_table = "schema_migrations"


class SysOstObjectStatus(models.Model):
    ost_id = models.AutoField(primary_key=True)
    ost_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sys_ost_object_status"


class SysSymModule(models.Model):
    sym_id = models.AutoField(primary_key=True)
    sym_name = models.CharField(max_length=50, blank=True, null=True)
    sym_icon = models.CharField(max_length=100, blank=True, null=True)
    sym_folder = models.CharField(max_length=100, blank=True, null=True)
    sym_object = models.CharField(max_length=100, blank=True, null=True)
    sym_sym_id = models.IntegerField(blank=True, null=True)
    sym_url = models.CharField(max_length=255, blank=True, null=True)
    sym_priority = models.IntegerField(blank=True, null=True)
    sym_action_add = models.IntegerField(blank=True, null=True)
    sym_action_advanced = models.IntegerField(blank=True, null=True)
    sym_action_archive = models.IntegerField(blank=True, null=True)
    sym_action_delete = models.IntegerField(blank=True, null=True)
    sym_action_download = models.IntegerField(blank=True, null=True)
    sym_action_edit = models.IntegerField(blank=True, null=True)
    sym_action_run = models.IntegerField(blank=True, null=True)
    sym_action_test = models.IntegerField(blank=True, null=True)
    sym_action_view = models.IntegerField(blank=True, null=True)
    sym_beta_date = models.DateTimeField(blank=True, null=True)
    sym_ost_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "sys_sym_module"

    def __unicode__(self):
        return self.sym_name

    @models.permalink
    def get_absolute_url(self):
        return ('module_detail')

# an attempt to use django authentication below

# class CustomUserManager(auth_models.BaseUserManager):
#     def create_user(self, sya_email, password):

#         user = self.model(
#            email = CustomUserManager.normalize_email(sya_email), 
#         )

#         user.set_password(sya_password)
#         user.save(using = self._db)
#         return user


# class SysSyaAccount(auth_models.AbstractBaseUser):
#     sya_id = models.AutoField(primary_key=True)
#     sya_name = models.CharField(max_length=100, blank=True, null=True)
#     sya_email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
#     sya_password = models.CharField(max_length=50, blank=True, null=True)
#     sya_system = models.IntegerField(blank=True, null=True)
#     sya_ste_id = models.IntegerField(blank=True, null=True)
#     sya_ost_id = models.IntegerField(blank=True, null=True)
#     sys_sym_modules = models.ManyToManyField(SysSymModule, through="SysRlnSyaSym")
    
#     USERNAME_FIELD = "sya_email"
#     PASSWORD_FIELD = "sya_password"
#     objects = CustomUserManager()

#     class Meta:
#         managed = True
#         db_table = "sys_sya_account"

#     def __unicode__(self):
#         return str(self.sya_id)

#     def set_password(self, raw_password):
#         self.sya_password = make_password(raw_password)

#     def get_full_name(self):
#         return self.sya_email

class SysSyaAccount(models.Model):
    sya_id = models.AutoField(primary_key=True)
    sya_name = models.CharField(max_length=100, blank=True, null=True)
    sya_email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    sya_password = models.CharField(max_length=50, blank=True, null=True)
    sya_system = models.IntegerField(blank=True, null=True)
    sya_ste_id = models.IntegerField(blank=True, null=True)
    sya_ost_id = models.IntegerField(blank=True, null=True)
    sys_sym_modules = models.ManyToManyField(SysSymModule, through="SysRlnSyaSym")

    class Meta:
        managed = True
        db_table = "sys_sya_account"


class SysRlnSyaSym(models.Model):
    # rln_sya_id = models.IntegerField(blank=True, null=True)
    # rln_sym_id = models.IntegerField(blank=True, null=True)
    rln_sya = models.ForeignKey(SysSyaAccount, on_delete=models.CASCADE, blank=True, null=True)
    rln_sym = models.ForeignKey(SysSymModule, on_delete=models.CASCADE, blank=True, null=True)
    rln_sym_action_add = models.IntegerField(blank=True, null=True)
    rln_sym_action_advanced = models.IntegerField(blank=True, null=True)
    rln_sym_action_archive = models.IntegerField(blank=True, null=True)
    rln_sym_action_delete = models.IntegerField(blank=True, null=True)
    rln_sym_action_download = models.IntegerField(blank=True, null=True)
    rln_sym_action_edit = models.IntegerField(blank=True, null=True)
    rln_sym_action_run = models.IntegerField(blank=True, null=True)
    rln_sym_action_test = models.IntegerField(blank=True, null=True)
    rln_sym_action_view = models.IntegerField(blank=True, null=True)
    rln_id = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = "sys_rln_sya_sym"


class SysSlaLogAction(models.Model):
    sla_id = models.AutoField(primary_key=True)
    sla_name = models.CharField(max_length=255, blank=True, null=True)
    sla_sya_id = models.IntegerField(blank=True, null=True)
    sla_sym_id = models.IntegerField(blank=True, null=True)
    sla_ste_id = models.IntegerField(blank=True, null=True)
    sla_action = models.CharField(max_length=50, blank=True, null=True)
    sla_object = models.CharField(max_length=255, blank=True, null=True)
    sla_object_table = models.CharField(max_length=255, blank=True, null=True)
    sla_object_id = models.IntegerField(blank=True, null=True)
    sla_object_ref = models.CharField(max_length=255, blank=True, null=True)
    sla_ip = models.CharField(max_length=50, blank=True, null=True)
    sla_datestamp = models.DateTimeField(blank=True, null=True)
    sla_ost_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sys_sla_log_action"


class SysSleLogError(models.Model):
    sle_id = models.AutoField(primary_key=True)
    sle_name = models.CharField(max_length=255, blank=True, null=True)
    sle_sya_id = models.IntegerField(blank=True, null=True)
    sle_sym_id = models.IntegerField(blank=True, null=True)
    sle_ste_id = models.IntegerField(blank=True, null=True)
    sle_error_id = models.CharField(max_length=50, blank=True, null=True)
    sle_error_type = models.CharField(max_length=100, blank=True, null=True)
    sle_error_message = models.TextField(blank=True, null=True)
    sle_error_detail = models.TextField(blank=True, null=True)
    sle_error_query = models.TextField(blank=True, null=True)
    sle_url = models.CharField(max_length=255, blank=True, null=True)
    sle_ip = models.CharField(max_length=50, blank=True, null=True)
    sle_datestamp = models.DateTimeField(blank=True, null=True)
    sle_ost_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sys_sle_log_error"


class SysSlsLogSecurity(models.Model):
    sls_id = models.AutoField(primary_key=True)
    sls_name = models.CharField(max_length=255, blank=True, null=True)
    sls_sya_id = models.IntegerField(blank=True, null=True)
    sls_sym_id = models.IntegerField(blank=True, null=True)
    sls_ste_id = models.IntegerField(blank=True, null=True)
    sls_event = models.CharField(max_length=100, blank=True, null=True)
    sls_url = models.CharField(max_length=255, blank=True, null=True)
    sls_client = models.TextField(blank=True, null=True)
    sls_ip = models.CharField(max_length=50, blank=True, null=True)
    sls_datestamp = models.DateTimeField(blank=True, null=True)
    sls_ost_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sys_sls_log_security"


class SysSqcQueryControl(models.Model):
    sqc_id = models.AutoField(primary_key=True)
    sqc_sya_id = models.IntegerField(blank=True, null=True)
    sqc_name = models.CharField(max_length=100, blank=True, null=True)
    sqc_column = models.IntegerField(blank=True, null=True)
    sqc_direction = models.CharField(max_length=50, blank=True, null=True)
    sqc_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sys_sqc_query_control"


class SysSteSite(models.Model):
    ste_id = models.AutoField(primary_key=True)
    ste_name = models.CharField(max_length=255, blank=True, null=True)
    ste_value = models.CharField(max_length=255, blank=True, null=True)
    ste_priority = models.IntegerField(blank=True, null=True)
    ste_ost_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sys_ste_site"


class SysStxTextLabel(models.Model):
    stx_id = models.AutoField(primary_key=True)
    stx_name = models.CharField(max_length=100, blank=True, null=True)
    stx_value = models.CharField(max_length=255, blank=True, null=True)
    stx_ost_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sys_stx_text_label"


class SysSywWhitelist(models.Model):
    syw_id = models.AutoField(primary_key=True)
    syw_name = models.CharField(max_length=255, blank=True, null=True)
    syw_value = models.CharField(max_length=50, blank=True, null=True)
    syw_ste_id = models.IntegerField(blank=True, null=True)
    syw_ost_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sys_syw_whitelist"


class TstDmoDemo(models.Model):
    dmo_id = models.AutoField(primary_key=True)
    dmo_name = models.CharField(max_length=50, blank=True, null=True)
    dmo_value = models.TextField(blank=True, null=True)
    dmo_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    dmo_datestamp = models.DateTimeField(blank=True, null=True)
    dmo_ost_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tst_dmo_demo"


class TstExpExample(models.Model):
    exp_id = models.AutoField(primary_key=True)
    exp_name = models.CharField(max_length=50, blank=True, null=True)
    exp_value = models.TextField(blank=True, null=True)
    exp_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    exp_priority = models.IntegerField(blank=True, null=True)
    exp_ip = models.CharField(max_length=50, blank=True, null=True)
    exp_datestamp = models.DateTimeField(blank=True, null=True)
    exp_ost_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tst_exp_example"
