# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import JSONField


class Account(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'account'


class AccountHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'account_history'
        unique_together = (('id', 'txid'),)


class Activitydefinition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'activitydefinition'


class ActivitydefinitionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'activitydefinition_history'
        unique_together = (('id', 'txid'),)


class Adverseevent(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'adverseevent'


class AdverseeventHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'adverseevent_history'
        unique_together = (('id', 'txid'),)


class Allergyintolerance(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'allergyintolerance'


class AllergyintoleranceHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'allergyintolerance_history'
        unique_together = (('id', 'txid'),)


class Appointment(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'appointment'


class AppointmentHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'appointment_history'
        unique_together = (('id', 'txid'),)


class Appointmentresponse(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'appointmentresponse'


class AppointmentresponseHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'appointmentresponse_history'
        unique_together = (('id', 'txid'),)


class Auditevent(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auditevent'


class AuditeventHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auditevent_history'
        unique_together = (('id', 'txid'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Basic(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'basic'


class BasicHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'basic_history'
        unique_together = (('id', 'txid'),)


class Binary(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'binary'


class BinaryHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'binary_history'
        unique_together = (('id', 'txid'),)


class Biologicallyderivedproduct(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'biologicallyderivedproduct'


class BiologicallyderivedproductHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'biologicallyderivedproduct_history'
        unique_together = (('id', 'txid'),)


class Bodystructure(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bodystructure'


class BodystructureHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bodystructure_history'
        unique_together = (('id', 'txid'),)


class Capabilitystatement(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'capabilitystatement'


class CapabilitystatementHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'capabilitystatement_history'
        unique_together = (('id', 'txid'),)


class Careplan(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'careplan'


class CareplanHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'careplan_history'
        unique_together = (('id', 'txid'),)


class Careteam(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'careteam'


class CareteamHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'careteam_history'
        unique_together = (('id', 'txid'),)


class Chargeitem(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'chargeitem'


class ChargeitemHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'chargeitem_history'
        unique_together = (('id', 'txid'),)


class Claim(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'claim'


class ClaimHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'claim_history'
        unique_together = (('id', 'txid'),)


class Claimresponse(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'claimresponse'


class ClaimresponseHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'claimresponse_history'
        unique_together = (('id', 'txid'),)


class Clinicalimpression(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'clinicalimpression'


class ClinicalimpressionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'clinicalimpression_history'
        unique_together = (('id', 'txid'),)


class Codesystem(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'codesystem'


class CodesystemHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'codesystem_history'
        unique_together = (('id', 'txid'),)


class Communication(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'communication'


class CommunicationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'communication_history'
        unique_together = (('id', 'txid'),)


class Communicationrequest(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'communicationrequest'


class CommunicationrequestHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'communicationrequest_history'
        unique_together = (('id', 'txid'),)


class Compartmentdefinition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'compartmentdefinition'


class CompartmentdefinitionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'compartmentdefinition_history'
        unique_together = (('id', 'txid'),)


class Composition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'composition'


class CompositionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'composition_history'
        unique_together = (('id', 'txid'),)


class Concept(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'concept'


class ConceptHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'concept_history'
        unique_together = (('id', 'txid'),)


class Conceptmap(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'conceptmap'


class ConceptmapHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'conceptmap_history'
        unique_together = (('id', 'txid'),)


class Condition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = JSONField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'condition'


class ConditionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'condition_history'
        unique_together = (('id', 'txid'),)


class Consent(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'consent'


class ConsentHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'consent_history'
        unique_together = (('id', 'txid'),)


class Contract(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'contract'


class ContractHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'contract_history'
        unique_together = (('id', 'txid'),)


class Coverage(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'coverage'


class CoverageHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'coverage_history'
        unique_together = (('id', 'txid'),)


class Detectedissue(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'detectedissue'


class DetectedissueHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'detectedissue_history'
        unique_together = (('id', 'txid'),)


class Device(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'device'


class DeviceHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'device_history'
        unique_together = (('id', 'txid'),)


class Devicecomponent(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'devicecomponent'


class DevicecomponentHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'devicecomponent_history'
        unique_together = (('id', 'txid'),)


class Devicemetric(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'devicemetric'


class DevicemetricHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'devicemetric_history'
        unique_together = (('id', 'txid'),)


class Devicerequest(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'devicerequest'


class DevicerequestHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'devicerequest_history'
        unique_together = (('id', 'txid'),)


class Deviceusestatement(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'deviceusestatement'


class DeviceusestatementHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'deviceusestatement_history'
        unique_together = (('id', 'txid'),)


class Diagnosticreport(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'diagnosticreport'


class DiagnosticreportHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'diagnosticreport_history'
        unique_together = (('id', 'txid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documentmanifest(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'documentmanifest'


class DocumentmanifestHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'documentmanifest_history'
        unique_together = (('id', 'txid'),)


class Documentreference(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'documentreference'


class DocumentreferenceHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'documentreference_history'
        unique_together = (('id', 'txid'),)


class Eligibilityrequest(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'eligibilityrequest'


class EligibilityrequestHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'eligibilityrequest_history'
        unique_together = (('id', 'txid'),)


class Eligibilityresponse(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'eligibilityresponse'


class EligibilityresponseHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'eligibilityresponse_history'
        unique_together = (('id', 'txid'),)


class Encounter(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'encounter'


class EncounterHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'encounter_history'
        unique_together = (('id', 'txid'),)


class Endpoint(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'endpoint'


class EndpointHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'endpoint_history'
        unique_together = (('id', 'txid'),)


class Enrollmentrequest(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'enrollmentrequest'


class EnrollmentrequestHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'enrollmentrequest_history'
        unique_together = (('id', 'txid'),)


class Enrollmentresponse(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'enrollmentresponse'


class EnrollmentresponseHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'enrollmentresponse_history'
        unique_together = (('id', 'txid'),)


class Entrydefinition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'entrydefinition'


class EntrydefinitionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'entrydefinition_history'
        unique_together = (('id', 'txid'),)


class Episodeofcare(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'episodeofcare'


class EpisodeofcareHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'episodeofcare_history'
        unique_together = (('id', 'txid'),)


class Eventdefinition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'eventdefinition'


class EventdefinitionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'eventdefinition_history'
        unique_together = (('id', 'txid'),)


class Examplescenario(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'examplescenario'


class ExamplescenarioHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'examplescenario_history'
        unique_together = (('id', 'txid'),)


class Expansionprofile(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'expansionprofile'


class ExpansionprofileHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'expansionprofile_history'
        unique_together = (('id', 'txid'),)


class Explanationofbenefit(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'explanationofbenefit'


class ExplanationofbenefitHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'explanationofbenefit_history'
        unique_together = (('id', 'txid'),)


class Familymemberhistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'familymemberhistory'


class FamilymemberhistoryHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'familymemberhistory_history'
        unique_together = (('id', 'txid'),)


class Flag(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'flag'


class FlagHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'flag_history'
        unique_together = (('id', 'txid'),)


class Goal(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'goal'


class GoalHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'goal_history'
        unique_together = (('id', 'txid'),)


class Graphdefinition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'graphdefinition'


class GraphdefinitionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'graphdefinition_history'
        unique_together = (('id', 'txid'),)


class Group(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'group'


class GroupHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'group_history'
        unique_together = (('id', 'txid'),)


class Guidanceresponse(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'guidanceresponse'


class GuidanceresponseHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'guidanceresponse_history'
        unique_together = (('id', 'txid'),)


class Healthcareservice(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'healthcareservice'


class HealthcareserviceHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'healthcareservice_history'
        unique_together = (('id', 'txid'),)


class Imagingstudy(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'imagingstudy'


class ImagingstudyHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'imagingstudy_history'
        unique_together = (('id', 'txid'),)


class Immunization(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'immunization'


class ImmunizationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'immunization_history'
        unique_together = (('id', 'txid'),)


class Immunizationevaluation(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'immunizationevaluation'


class ImmunizationevaluationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'immunizationevaluation_history'
        unique_together = (('id', 'txid'),)


class Immunizationrecommendation(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'immunizationrecommendation'


class ImmunizationrecommendationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'immunizationrecommendation_history'
        unique_together = (('id', 'txid'),)


class Implementationguide(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'implementationguide'


class ImplementationguideHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'implementationguide_history'
        unique_together = (('id', 'txid'),)


class Invoice(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'invoice'


class InvoiceHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'invoice_history'
        unique_together = (('id', 'txid'),)


class Iteminstance(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'iteminstance'


class IteminstanceHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'iteminstance_history'
        unique_together = (('id', 'txid'),)


class Library(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'library'


class LibraryHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'library_history'
        unique_together = (('id', 'txid'),)


class Linkage(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'linkage'


class LinkageHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'linkage_history'
        unique_together = (('id', 'txid'),)


class List(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'list'


class ListHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'list_history'
        unique_together = (('id', 'txid'),)


class Location(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'location'


class LocationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'location_history'
        unique_together = (('id', 'txid'),)


class Measure(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'measure'


class MeasureHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'measure_history'
        unique_together = (('id', 'txid'),)


class Measurereport(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'measurereport'


class MeasurereportHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'measurereport_history'
        unique_together = (('id', 'txid'),)


class Media(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'media'


class MediaHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'media_history'
        unique_together = (('id', 'txid'),)


class Medication(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medication'


class MedicationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medication_history'
        unique_together = (('id', 'txid'),)


class Medicationadministration(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicationadministration'


class MedicationadministrationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicationadministration_history'
        unique_together = (('id', 'txid'),)


class Medicationdispense(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicationdispense'


class MedicationdispenseHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicationdispense_history'
        unique_together = (('id', 'txid'),)


class Medicationrequest(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicationrequest'


class MedicationrequestHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicationrequest_history'
        unique_together = (('id', 'txid'),)


class Medicationstatement(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicationstatement'


class MedicationstatementHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicationstatement_history'
        unique_together = (('id', 'txid'),)


class Medicinalproduct(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproduct'


class MedicinalproductHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproduct_history'
        unique_together = (('id', 'txid'),)


class Medicinalproductauthorization(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductauthorization'


class MedicinalproductauthorizationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductauthorization_history'
        unique_together = (('id', 'txid'),)


class Medicinalproductclinicals(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductclinicals'


class MedicinalproductclinicalsHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductclinicals_history'
        unique_together = (('id', 'txid'),)


class Medicinalproductdevicespec(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductdevicespec'


class MedicinalproductdevicespecHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductdevicespec_history'
        unique_together = (('id', 'txid'),)


class Medicinalproductingredient(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductingredient'


class MedicinalproductingredientHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductingredient_history'
        unique_together = (('id', 'txid'),)


class Medicinalproductpackaged(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductpackaged'


class MedicinalproductpackagedHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductpackaged_history'
        unique_together = (('id', 'txid'),)


class Medicinalproductpharmaceutical(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductpharmaceutical'


class MedicinalproductpharmaceuticalHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicinalproductpharmaceutical_history'
        unique_together = (('id', 'txid'),)


class Messagedefinition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'messagedefinition'


class MessagedefinitionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'messagedefinition_history'
        unique_together = (('id', 'txid'),)


class Messageheader(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'messageheader'


class MessageheaderHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'messageheader_history'
        unique_together = (('id', 'txid'),)


class Metadataresource(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'metadataresource'


class MetadataresourceHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'metadataresource_history'
        unique_together = (('id', 'txid'),)


class Namingsystem(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'namingsystem'


class NamingsystemHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'namingsystem_history'
        unique_together = (('id', 'txid'),)


class Nutritionorder(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'nutritionorder'


class NutritionorderHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'nutritionorder_history'
        unique_together = (('id', 'txid'),)


class Observation(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'observation'


class ObservationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'observation_history'
        unique_together = (('id', 'txid'),)


class Observationdefinition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'observationdefinition'


class ObservationdefinitionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'observationdefinition_history'
        unique_together = (('id', 'txid'),)


class Occupationaldata(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'occupationaldata'


class OccupationaldataHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'occupationaldata_history'
        unique_together = (('id', 'txid'),)


class Operationdefinition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'operationdefinition'


class OperationdefinitionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'operationdefinition_history'
        unique_together = (('id', 'txid'),)


class Operationoutcome(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'operationoutcome'


class OperationoutcomeHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'operationoutcome_history'
        unique_together = (('id', 'txid'),)


class Organization(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'organization'


class OrganizationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'organization_history'
        unique_together = (('id', 'txid'),)


class Organizationrole(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'organizationrole'


class OrganizationroleHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'organizationrole_history'
        unique_together = (('id', 'txid'),)


class Parameters(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'parameters'


class ParametersHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'parameters_history'
        unique_together = (('id', 'txid'),)


class Patient(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = JSONField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'patient'


class PatientHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'patient_history'
        unique_together = (('id', 'txid'),)


class Paymentnotice(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'paymentnotice'


class PaymentnoticeHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'paymentnotice_history'
        unique_together = (('id', 'txid'),)


class Paymentreconciliation(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'paymentreconciliation'


class PaymentreconciliationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'paymentreconciliation_history'
        unique_together = (('id', 'txid'),)


class Person(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'person'


class PersonHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'person_history'
        unique_together = (('id', 'txid'),)


class Plandefinition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'plandefinition'


class PlandefinitionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'plandefinition_history'
        unique_together = (('id', 'txid'),)


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Practitioner(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'practitioner'


class PractitionerHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'practitioner_history'
        unique_together = (('id', 'txid'),)


class Practitionerrole(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'practitionerrole'


class PractitionerroleHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'practitionerrole_history'
        unique_together = (('id', 'txid'),)


class Procedure(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'procedure'


class ProcedureHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'procedure_history'
        unique_together = (('id', 'txid'),)


class Processrequest(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'processrequest'


class ProcessrequestHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'processrequest_history'
        unique_together = (('id', 'txid'),)


class Processresponse(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'processresponse'


class ProcessresponseHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'processresponse_history'
        unique_together = (('id', 'txid'),)


class Productplan(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'productplan'


class ProductplanHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'productplan_history'
        unique_together = (('id', 'txid'),)


class Provenance(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'provenance'


class ProvenanceHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'provenance_history'
        unique_together = (('id', 'txid'),)


class Questionnaire(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'questionnaire'


class QuestionnaireHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'questionnaire_history'
        unique_together = (('id', 'txid'),)


class Questionnaireresponse(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'questionnaireresponse'


class QuestionnaireresponseHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'questionnaireresponse_history'
        unique_together = (('id', 'txid'),)


class Relatedperson(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'relatedperson'


class RelatedpersonHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'relatedperson_history'
        unique_together = (('id', 'txid'),)


class Requestgroup(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'requestgroup'


class RequestgroupHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'requestgroup_history'
        unique_together = (('id', 'txid'),)


class Researchstudy(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'researchstudy'


class ResearchstudyHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'researchstudy_history'
        unique_together = (('id', 'txid'),)


class Researchsubject(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'researchsubject'


class ResearchsubjectHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'researchsubject_history'
        unique_together = (('id', 'txid'),)


class Riskassessment(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'riskassessment'


class RiskassessmentHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'riskassessment_history'
        unique_together = (('id', 'txid'),)


class Schedule(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'schedule'


class ScheduleHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'schedule_history'
        unique_together = (('id', 'txid'),)


class Sequence(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sequence'


class SequenceHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sequence_history'
        unique_together = (('id', 'txid'),)


class Servicerequest(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'servicerequest'


class ServicerequestHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'servicerequest_history'
        unique_together = (('id', 'txid'),)


class Slot(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'slot'


class SlotHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'slot_history'
        unique_together = (('id', 'txid'),)


class Specimen(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'specimen'


class SpecimenHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'specimen_history'
        unique_together = (('id', 'txid'),)


class Specimendefinition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'specimendefinition'


class SpecimendefinitionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'specimendefinition_history'
        unique_together = (('id', 'txid'),)


class Structuredefinition(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'structuredefinition'


class StructuredefinitionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'structuredefinition_history'
        unique_together = (('id', 'txid'),)


class Structuremap(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'structuremap'


class StructuremapHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'structuremap_history'
        unique_together = (('id', 'txid'),)


class Subscription(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'subscription'


class SubscriptionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'subscription_history'
        unique_together = (('id', 'txid'),)


class Substance(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'substance'


class SubstanceHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'substance_history'
        unique_together = (('id', 'txid'),)


class Substancepolymer(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'substancepolymer'


class SubstancepolymerHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'substancepolymer_history'
        unique_together = (('id', 'txid'),)


class Substancereferenceinformation(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'substancereferenceinformation'


class SubstancereferenceinformationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'substancereferenceinformation_history'
        unique_together = (('id', 'txid'),)


class Substancespecification(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'substancespecification'


class SubstancespecificationHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'substancespecification_history'
        unique_together = (('id', 'txid'),)


class Supplydelivery(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'supplydelivery'


class SupplydeliveryHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'supplydelivery_history'
        unique_together = (('id', 'txid'),)


class Supplyrequest(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'supplyrequest'


class SupplyrequestHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'supplyrequest_history'
        unique_together = (('id', 'txid'),)


class Task(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'task'


class TaskHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'task_history'
        unique_together = (('id', 'txid'),)


class Terminologycapabilities(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'terminologycapabilities'


class TerminologycapabilitiesHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'terminologycapabilities_history'
        unique_together = (('id', 'txid'),)


class Testreport(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'testreport'


class TestreportHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'testreport_history'
        unique_together = (('id', 'txid'),)


class Testscript(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'testscript'


class TestscriptHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'testscript_history'
        unique_together = (('id', 'txid'),)


class Transaction(models.Model):
    ts = models.DateTimeField(blank=True, null=True)
    resource = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'transaction'


class Usersession(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'usersession'


class UsersessionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'usersession_history'
        unique_together = (('id', 'txid'),)


class Valueset(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'valueset'


class ValuesetHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'valueset_history'
        unique_together = (('id', 'txid'),)


class Verificationresult(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'verificationresult'


class VerificationresultHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'verificationresult_history'
        unique_together = (('id', 'txid'),)


class Visionprescription(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'visionprescription'


class VisionprescriptionHistory(models.Model):
    id = models.TextField(primary_key=True)
    txid = models.BigIntegerField()
    ts = models.DateTimeField(blank=True, null=True)
    resource_type = models.TextField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    resource = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'visionprescription_history'
        unique_together = (('id', 'txid'),)
