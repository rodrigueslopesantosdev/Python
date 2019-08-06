# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:42:18 2019

@author: tiago.santos
"""

import boto3;

s3=boto3.resource ('s3');

for bkt in s3.buckets.all():
    print(bkt.name)