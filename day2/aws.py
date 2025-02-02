'''Managing IAM users and playing around'''
import boto3
def pager():
    iam=boto3.client('iam')
    response=iam.create_user(UserName='murthy')
    print(response)

    users=iam.get_paginator('list_users')
    print(users)
    print(users.paginate())

    for resp in users.paginate():
        print(resp)

    iam.update_user(UserName='murthy',NewUserName="sriram") #how to fix this
    iam.delete_user(UserName='sriram')

if __name__=='__main__':
    pager()