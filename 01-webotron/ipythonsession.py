# coding: utf-8

"""I don't know why it needs this from me."""

import boto3
session = boto3.Session(profile_name='TerraformUser')
s3 = session.resource('s3')
