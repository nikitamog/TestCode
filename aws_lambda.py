#!/usr/bin/python3
#-*- coding:utf-8 -*-

"""
@author: Nikita Mogilevsky
@email: nikitamog@gmail.com

@description:
"""

#===================================================
# IMPORTS
#===================================================
import json
import os
#===================================================
# CONSTANTS
#===================================================
#===================================================
# METHODS
#===================================================

def lambda_greeter(event, context):
    print('os environment: ', os.environ)

    name = event['name']
    title = event['title']
    age = event['age']

    print('name:', name)
    print('title:', title)

    memory_allocated_to_function = context.memory_limit_in_mb
    request_id = context.aws_request_id

    # Assume some logic here
    print('total sales calculated')
    print('employee does not qualify for yearly bonus')

    return {
        'statusCode' : 200,
        'name' : name,
        'title' : title,
        'age' : age,
        'memory allocated to function (Megabytes)' : memory_allocated_to_function,
        'request ID' : request_id
    }

