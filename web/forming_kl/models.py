# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Blockstorage(models.Model):
    numer = models.IntegerField(db_column='Numer', blank=True, null=True)  # Field name made lowercase.
    masa = models.FloatField(db_column='Masa')  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=10, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dataczasprodukcji = models.DateTimeField(db_column='DataCzasProdukcji', primary_key=True)  # Field name made lowercase.
    kodkreskowy = models.CharField(db_column='KodKreskowy', max_length=27, db_collation='Polish_CI_AS')  # Field name made lowercase.
    typbloku = models.CharField(db_column='TypBloku', max_length=7, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    regranulat = models.SmallIntegerField(db_column='Regranulat', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=11, db_collation='Polish_CI_AS')  # Field name made lowercase.
    czassezonowania = models.SmallIntegerField(db_column='CzasSezonowania')  # Field name made lowercase.
    dataczasciecia = models.DateTimeField(db_column='DataCzasCiecia', blank=True, null=True)  # Field name made lowercase.
    czasodciecia = models.SmallIntegerField(db_column='CzasOdCiecia', blank=True, null=True)  # Field name made lowercase.
    przerwa = models.CharField(db_column='Przerwa', max_length=8, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sposoby = models.CharField(db_column='Sposoby', max_length=11, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pvac1 = models.SmallIntegerField(db_column='Pvac1', blank=True, null=True)  # Field name made lowercase.
    pvac2 = models.SmallIntegerField(db_column='Pvac2', blank=True, null=True)  # Field name made lowercase.
    pp1 = models.SmallIntegerField(db_column='Pp1', blank=True, null=True)  # Field name made lowercase.
    pp2 = models.SmallIntegerField(db_column='Pp2', blank=True, null=True)  # Field name made lowercase.
    pp3 = models.SmallIntegerField(db_column='Pp3', blank=True, null=True)  # Field name made lowercase.
    pp4 = models.SmallIntegerField(db_column='Pp4', blank=True, null=True)  # Field name made lowercase.
    czvac1 = models.SmallIntegerField(db_column='CzVac1', blank=True, null=True)  # Field name made lowercase.
    czvac2 = models.SmallIntegerField(db_column='CzVac2', blank=True, null=True)  # Field name made lowercase.
    czp1 = models.SmallIntegerField(db_column='CzP1', blank=True, null=True)  # Field name made lowercase.
    czp2 = models.SmallIntegerField(db_column='CzP2', blank=True, null=True)  # Field name made lowercase.
    czp3 = models.SmallIntegerField(db_column='CzP3', blank=True, null=True)  # Field name made lowercase.
    czp4 = models.SmallIntegerField(db_column='CzP4', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.dataczasprodukcji} {self.kodkreskowy} {self.typbloku} {self.masa} {self.operator}'

    class Meta:
        # managed = False
        db_table = 'BlockStorage'
        app_label = 'forming_kl'


# class Magazynpaczek(models.Model):
#     numer = models.IntegerField(db_column='Numer', blank=True, null=True)  # Field name made lowercase.
#     nazwaproduktu = models.CharField(db_column='NazwaProduktu', max_length=15, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     gruboscplyt = models.CharField(db_column='GruboscPlyt', max_length=15, db_collation='Polish_CI_AS')  # Field name made lowercase.
#     dlugoscpaczek = models.IntegerField(db_column='DlugoscPaczek')  # Field name made lowercase.
#     liczbaplyt = models.CharField(db_column='LiczbaPlyt', max_length=11, db_collation='Polish_CI_AS')  # Field name made lowercase.
#     liczbapaczek = models.SmallIntegerField(db_column='LiczbaPaczek')  # Field name made lowercase.
#     kodkreskowybloku = models.CharField(db_column='KodKreskowyBloku', max_length=16, db_collation='Polish_CI_AS')  # Field name made lowercase.
#     dataczasciecia = models.DateTimeField(db_column='DataCzasCiecia', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'MagazynPaczek'


# class Produkty(models.Model):
#     numer = models.IntegerField(db_column='Numer')  # Field name made lowercase.
#     produkt = models.CharField(db_column='Produkt', max_length=20, db_collation='Polish_CI_AS')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Produkty'


# class Surowce(models.Model):
#     kodsurowca = models.CharField(db_column='KodSurowca', max_length=10, db_collation='Polish_CI_AS')  # Field name made lowercase.
#     nazwa = models.CharField(db_column='Nazwa', max_length=20, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     dataczasspieniania = models.DateTimeField(db_column='DataCzasSpieniania', blank=True, null=True)  # Field name made lowercase.
#     operator = models.CharField(db_column='Operator', max_length=6, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     gestosc = models.DecimalField(db_column='Gestosc', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
#     silos = models.SmallIntegerField(db_column='Silos', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Surowce'


# class Typyblokow(models.Model):
#     typ = models.CharField(db_column='Typ', max_length=10, db_collation='Polish_CI_AS')  # Field name made lowercase.
#     ilość = models.IntegerField(db_column='Ilość', blank=True, null=True)  # Field name made lowercase.
#     masa_od = models.FloatField(db_column='Masa_od', blank=True, null=True)  # Field name made lowercase.
#     masa_do = models.FloatField(db_column='Masa_do', blank=True, null=True)  # Field name made lowercase.
#     kolor = models.CharField(db_column='Kolor', max_length=1, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     regranulat = models.IntegerField(db_column='Regranulat', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'TypyBlokow'


# class Sysdiagrams(models.Model):
#     name = models.CharField(max_length=128, db_collation='Polish_CI_AS')
#     principal_id = models.IntegerField()
#     diagram_id = models.AutoField(primary_key=True)
#     version = models.IntegerField(blank=True, null=True)
#     definition = models.BinaryField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sysdiagrams'
#         unique_together = (('principal_id', 'name'),)
