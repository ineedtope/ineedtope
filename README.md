# ineedto.pe

Domain-driven development at its finest.

[https://ineedto.pe](https://ineedto.pe)


# Dataset

We keep it simple and extract all public toilets from OpenStreetMap once.

    docker build -t ineedtope/ineedtope .

    wget http://download.geofabrik.de/europe/germany/berlin-latest.osm.pbf

    docker run --rm -v $(pwd):/data ineedtope/ineedtope osmium tags-filter /data/berlin-latest.osm.pbf n/amenity=toilets -o /data/toilets.osm.pbf
    docker run --rm -v $(pwd):/data ineedtope/ineedtope osmium export /data/toilets.osm.pbf -c export.json -o /data/toilets.geojson

We then transform the arbitrary OpenStreetMap tags to something standardized we can show.

    docker run --rm -v $(pwd):/data ineedtope/ineedtope python3 transform.py /data/toilets.geojson -o /data/toilets-transformed.geojson
