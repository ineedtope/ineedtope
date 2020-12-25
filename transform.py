#!/usr/bin/env python3

import json
import pathlib
import argparse


def transform(feature):
    tags = {"@id": "*",
            "@timestamp": "*",
            "name": "*",
            "fee": ["yes", "no"],
            "access": ["yes", "customers"],
            "wheelchair": ["yes", "no", "limited"]}

    props = {k: v for k, v in feature["properties"].items()
                if k in tags and (tags[k] == "*" or v in tags[k])}

    feature["properties"] = props


def main(args):
    with args.infile.open() as infile:
        collection = json.load(infile)

    for feature in collection["features"]:
        transform(feature)

    with args.outfile.open("w") as outfile:
        json.dump(collection, outfile, ensure_ascii=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="postcodes")

    parser.add_argument("infile", type=pathlib.Path)
    parser.add_argument("--outfile", "-o", required=True, type=pathlib.Path)

    main(parser.parse_args())
