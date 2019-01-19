#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):
        stevilka = self.request.get("stevilka")
        select1 = self.request.get("select1")
        select2 = self.request.get("select2")
        izbira1 = None
        izbira2 = None
        rezultat = None
        error = False

        if select1 == "cm1" and select2 == "inch2":
            rezultat = float(stevilka) * 0.39370079
            izbira1 = "centimetrov"
            izbira2 = "inchov"
        elif select1 == "km1" and select2 == "mi2":
            rezultat = float(stevilka) * 0.621371192
            izbira1 = "kilometrov"
            izbira2 = "milj"
        elif select1 == "inch1" and select2 == "cm2":
            rezultat = float(stevilka) * 2.54
            izbira1 = "inchov"
            izbira2 = "centimetrov"
        elif select1 == "mi1" and select2 == "km2":
            rezultat = float(stevilka) * 1.609344
            izbira1 = "milj"
            izbira2 = "kilometrov"
        elif select1 == "cm1" and select2 == "km2":
            i = float(stevilka) / 100000
            # To je zato, ker float prikazuje po defaultu samo 4 decimalke
            rezultat = format(i, ".5f")
            izbira1 = "centimetrov"
            izbira2 = "kilometrov"
        elif select1 == "cm1" and select2 == "mi2":
            i = float(stevilka) * 0.000006213711922
            rezultat = format(i, ".10f")
            izbira1 = "centimetrov"
            izbira2 = "milj"
        elif select1 == "km1" and select2 == "cm2":
            rezultat = int(stevilka) * 100000
            izbira1 = "kilometrov"
            izbira2 = "centimetrov"
        elif select1 == "km1" and select2 == "inch2":
            i = float(stevilka) * 39370.07874
            rezultat = format(i, ".5f")
            izbira1 = "kilometrov"
            izbira2 = "inchov"
        elif select1 == "inch1" and select2 == "km2":
            i = float(stevilka) * 0.0000254
            rezultat = format(i, ".7f")
            izbira1 = "inchov"
            izbira2 = "kilometrov"
        elif select1 == "inch1" and select2 == "mi2":
            i = float(stevilka) * 0.0000157828
            rezultat = format(i, ".10f")
            izbira1 = "inchov"
            izbira2 = "milj"
        elif select1 == "mi1" and select2 == "inch2":
            rezultat = int(stevilka) * 63360
            izbira1 = "milj"
            izbira2 = "inchov"
        elif select1 == "mi1" and select2 == "cm2":
            rezultat = float(stevilka) * 160934.4
            izbira1 = "milj"
            izbira2 = "centimetrov"
        elif select1 == "cm1" and select2 == "cm2" or select1 == "km1" and select2 == "km2" or select1 == "inch1" and select2 == "inch2" or select1 == "mi1" and select2 == "mi2":
            error = True

        ss = {
            "stevilka": stevilka,
            "izbira1": izbira1,
            "izbira2": izbira2,
            "rezultat": rezultat,
            "error": error
        }
        return self.render_template("hello.html", params=ss)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
