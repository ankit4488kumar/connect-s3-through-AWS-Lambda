# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 18:11:00 2021

@author: ankit
"""

import re
from urllib.parse import urlsplit
from base64 import b32decode
import os
import boto3


def lambda_handler(event, context):
    print('Hello World')
    bucketname='mfiltterit-developer'
    itemname='test_ankit.json'
    
    s3 = boto3.resource('s3')
    obj = s3.Object(bucketname, itemname)
    body = obj.get()['Body'].read()
    print(body)
    return 'ok'