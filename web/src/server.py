from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response

import mysql.connector as mysql
import os

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def get_home(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/home.html', {'users': records}, request=req)

def get_product(req):
  return render_to_response('templates/product.html', {}, request=req)

def get_KVP(req):
  return render_to_response('templates/kvp.html', {}, request=req)

def get_mockup(req):
  return render_to_response('templates/mockup.html', {}, request=req)

def get_ui_laws(req):
  return render_to_response('templates/ui_laws.html', {}, request=req)

def get_costs(req):
  return render_to_response('templates/costs.html', {}, request=req)

def get_pivots(req):
  return render_to_response('templates/pivots.html', {}, request=req)

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')

  config.add_route('get_product', '/product')
  config.add_view(get_product, route_name='get_product')

  config.add_route('get_KVP', '/kvp')
  config.add_view(get_KVP, route_name='get_KVP')

  config.add_route('get_mockup', '/mockup')
  config.add_view(get_mockup, route_name='get_mockup')

  config.add_route('get_ui_laws', '/ui_laws')
  config.add_view(get_ui_laws, route_name='get_ui_laws')

  config.add_route('get_costs', '/costs')
  config.add_view(get_costs, route_name='get_costs')

  config.add_route('get_pivots', '/pivots')
  config.add_view(get_pivots, route_name='get_pivots')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()