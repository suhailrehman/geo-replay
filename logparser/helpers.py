# -*- coding: utf-8 -*-
import maxminddb
import dns.resolver
import ipaddress

# TODO: Move to config files
GEODB_PATH = 'config/dbs/geolite2/GeoLite2-City.mmdb'
AWS_COUNTRY_INDEX_PATH = 'config/dbs/awsmap/countries.index'
AWS_USA_INDEX_PATH = 'config/dbs/awsmap/usa.index'
DEFAULT_ZONE = 'us-east-1'


class DataCenterLookup(object):

    def load_index(self, index_file):
        dc_index = {}
        with open(index_file) as f:
            for line in f:
                tokens = line.strip().split(';')
                dc_index[tokens[0]] = tokens[2]
        return dc_index

    def __init__(self):
        self.reader = maxminddb.open_database(GEODB_PATH)
        self.aws_country_dict = self.load_index(AWS_COUNTRY_INDEX_PATH)
        self.aws_state_dict = self.load_index(AWS_USA_INDEX_PATH)

    def get_ip(self, address):
        try:
            ipaddress.ip_address(address)
            return address
        except ValueError:
            try:
                resolved = dns.resolver.query(address)[0].address
                return resolved
            except:
                return None

    def geolocate_ip(self, ipaddress_string):
        record = self.reader.get(ipaddress_string)
        location_dict = {}
        location_dict['country'] = record['country']['iso_code']
        if location_dict['country'] == 'US':
            try:
                location_dict['state'] = record['subdivisions'][0]['iso_code']
            except:
                pass
        return location_dict

    def find_aws_datacenter(self, ipaddress_string):
        try:
            ipaddress_string = self.get_ip(ipaddress_string)
            location_dict = self.geolocate_ip(ipaddress_string)
            if location_dict['country'] == 'US':
                return self.aws_state_dict[location_dict['state']]
            else:
                return self.aws_country_dict[location_dict['country']]
        except:
            return DEFAULT_ZONE
