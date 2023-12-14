from bottle import route, post, run, template, redirect, request
import database
@route("/")
def get_index():
    redirect("/list")
@route("/list")
def get_list():
    items = database.get_customers()
    return template("list.tpl", customers=items)
@route("/add")
def get_add():
    return template("add_item.tpl")
run(host='localhost', port=8080)