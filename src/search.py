#!/usr/bin/python -tt
#coding:utf-8

import requests
import re

class Search(object):

    def __init__(get, payload={}):
        self.requests = requests
        self.payload = payload
        self.payload['format'] = 'json'

    def find():
        r = self.get

    def query(query):
        self.payload['q'] = query
        return self

    def street(street):
        self.payload['street'] = street
        return self

    def city(city):
        self.payload['city'] = city
        return self

    def county(county):
        self.payload['county'] = county
        return self

    def state(state):
        self.payload['state'] = state
        return self

    def country(country):
        self.payload['country'] = country
        return self

    def postal_code(postal_code):
        self.payload['postalcode'] = postal_code;
        return self

    def language(language):
        self.payload['accept-language'] = language
        return self

    def country_code(country_code):
        if not re.search(r'^[a-z]{2}$', country_code, re.IGNORECASE):
            raise ValueError('Invalid country code')
        if 'country_code' in payload:
            payload['country_code'] += ',' + country_code
        else:
            payload['country_code'] = country_code
        return self

    def address_details(details = True):
        self.payload['addressdetails'] = 1 if details else 0
        return self

    def get_payload():
        return self.payload

    def get_client():
        return self.get
