# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class General(models.Model):
    loadfile = models.CharField(db_column='LoadFile', max_length=25, db_collation='Cyrillic_General_CI_AS')
    productionline = models.CharField(db_column='ProductionLine', max_length=15, db_collation='Cyrillic_General_CI_AS')
    ordernumber = models.CharField(db_column='OrderNumber', primary_key=True, max_length=15, db_collation='Cyrillic_General_CI_AS')
    loadfiletime = models.DateTimeField(db_column='LoadFileTime')
    datetimestart = models.DateTimeField(db_column='DateTimeStart')
    datetimestop = models.DateTimeField(db_column='DateTimeStop')
    r_mpurecipe = models.IntegerField(db_column='R_MpuRecipe')
    r_recipenumber = models.IntegerField(db_column='R_RecipeNumber')
    r_manufacturer = models.CharField(db_column='R_Manufacturer', max_length=15, db_collation='Cyrillic_General_CI_AS')
    r_type = models.CharField(db_column='R_Type', max_length=15, db_collation='Cyrillic_General_CI_AS')
    rawmatweightactual = models.FloatField(db_column='RawMatWeightActual', blank=True, null=True)
    operator = models.CharField(db_column='Operator', max_length=20, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    comment = models.CharField(db_column='Comment', max_length=10, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)

    def __str__(self):
        return f'{self.loadfile}, {self.productionline}, {self.r_manufacturer}, {self.r_type}, {self.rawmatweightactual}'

    class Meta:
        # managed = False
        db_table = 'General'
        # app_label = 'foaming_kl'
