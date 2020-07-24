# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from blog.py")

def post():
    form = SQLFORM(db.blog)
    if form.process().accepted:
        response.flash='Form accepted'
    elif form.errors:
        response.flash='Form has errors'
    else:
        response.flash='Please fill out the form'
    return locals()

def view():
    rows = db(db.blog).select(orderby=db.blog.id)
    return locals()

def update():
    record = db.blog(request.args(0)) or redirect(URL('post'))
    form = SQLFORM(db.blog, record)
    if form.process().accepted:
        response.flash=T('Record updated')
    else:
        response.flash=T('Please complete the form')
    return locals()
