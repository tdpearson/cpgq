from celery.task import task
from celery import signature, group

@task
def add(x,y):
    return x + y

@task
def double(x):
    return x * 2

@task
def triple(x):
    return x * 3

@task
def test_grouping(x,y):
    chain = (add.s(x,y) | group(double.s(), triple.s()))
    chain.delay()
    return "Kicked Off tasks"
