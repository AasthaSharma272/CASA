from functools import wraps
from flask import flash, redirect, render_template, session

def apology(message, page):
  flash(message, 'error')
  return render_template(page)

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if session.get("user_id") is None:
        return redirect("/login")
    return f(*args, **kwargs)
  return decorated_function