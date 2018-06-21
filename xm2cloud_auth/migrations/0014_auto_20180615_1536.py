# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-15 15:36
from __future__ import unicode_literals

from django.db import migrations
import functools
import xm2cloud_auth.common.db.models
import xm2cloud_auth.common.storage


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_auth', '0013_auto_20180615_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=xm2cloud_auth.common.db.models.StrictedImageFileField(blank=True, upload_to=functools.partial(xm2cloud_auth.common.storage.upload_to, *('avatars',), **{}), validators=[functools.partial(xm2cloud_auth.common.db.models.valid_content_type, *(None, {'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', b'invalid_content_type': 'ContentType %(content_type)s is not allowed.', b'invalid_image_size': 'Out of the allowed image size 200x200.', b'invalid_upload_size': 'Out of the allowd upload size %(max_upload_size)s.', 'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.', 'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.'}), **{}), functools.partial(xm2cloud_auth.common.db.models.valid_image_size, *(200, 200, {'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', b'invalid_content_type': 'ContentType %(content_type)s is not allowed.', b'invalid_image_size': 'Out of the allowed image size 200x200.', b'invalid_upload_size': 'Out of the allowd upload size %(max_upload_size)s.', 'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.', 'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.'}), **{}), functools.partial(xm2cloud_auth.common.db.models.valid_upload_size, *(None, {'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', b'invalid_content_type': 'ContentType %(content_type)s is not allowed.', b'invalid_image_size': 'Out of the allowed image size 200x200.', b'invalid_upload_size': 'Out of the allowd upload size %(max_upload_size)s.', 'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.', 'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.'}), **{}), functools.partial(xm2cloud_auth.common.db.models.valid_content_type, *(None, {'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', b'invalid_content_type': 'ContentType %(content_type)s is not allowed.', b'invalid_image_size': 'Out of the allowed image size 200x200.', b'invalid_upload_size': 'Out of the allowd upload size %(max_upload_size)s.', 'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.', 'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.'}), **{}), functools.partial(xm2cloud_auth.common.db.models.valid_image_size, *(200, 200, {'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', b'invalid_content_type': 'ContentType %(content_type)s is not allowed.', b'invalid_image_size': 'Out of the allowed image size 200x200.', b'invalid_upload_size': 'Out of the allowd upload size %(max_upload_size)s.', 'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.', 'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.'}), **{}), functools.partial(xm2cloud_auth.common.db.models.valid_upload_size, *(None, {'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', b'invalid_content_type': 'ContentType %(content_type)s is not allowed.', b'invalid_image_size': 'Out of the allowed image size 200x200.', b'invalid_upload_size': 'Out of the allowd upload size %(max_upload_size)s.', 'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.', 'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.'}), **{}), functools.partial(xm2cloud_auth.common.db.models.valid_content_type, *(None, {'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', b'invalid_content_type': 'ContentType %(content_type)s is not allowed.', b'invalid_image_size': 'Out of the allowed image size 200x200.', b'invalid_upload_size': 'Out of the allowd upload size %(max_upload_size)s.', 'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.', 'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.'}), **{}), functools.partial(xm2cloud_auth.common.db.models.valid_image_size, *(200, 200, {'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', b'invalid_content_type': 'ContentType %(content_type)s is not allowed.', b'invalid_image_size': 'Out of the allowed image size 200x200.', b'invalid_upload_size': 'Out of the allowd upload size %(max_upload_size)s.', 'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.', 'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.'}), **{}), functools.partial(xm2cloud_auth.common.db.models.valid_upload_size, *(None, {'blank': 'This field cannot be blank.', 'invalid_choice': 'Value %(value)r is not a valid choice.', b'invalid_content_type': 'ContentType %(content_type)s is not allowed.', b'invalid_image_size': 'Out of the allowed image size 200x200.', b'invalid_upload_size': 'Out of the allowd upload size %(max_upload_size)s.', 'null': 'This field cannot be null.', 'unique': '%(model_name)s with this %(field_label)s already exists.', 'unique_for_date': '%(field_label)s must be unique for %(date_field_label)s %(lookup_type)s.'}), **{})]),
        ),
    ]
