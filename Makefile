SHELL := /bin/bash

dbdownload:

	@echo "Geographic IP Information Downloads"
	@echo "==================================="
	@echo 
	@echo "Downloading and extracting GeoLite2 Database from MaxMind"
	@echo "---------------------------------------------------------"
	wget -O ./config/dbs/geolite2/GeoLite2-City.mmdb.gz http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz
	gunzip ./config/dbs/geolite2/GeoLite2-City.mmdb.gz

pip:
	@echo "Setting Up Environment and Installing Dependencies"
	@echo "=================================================="
	pip install --upgrade pip
	pip install -r requirements.txt


init: pip dbdownload

test:
	nosetests tests
