# BigQuery Setup for Keycloak Event Logs

This guide explains how to create a BigQuery dataset and table for importing Keycloak event logs using the provided schema.

## Prerequisites
- Google Cloud SDK (`gcloud` and `bq` command-line tools)
- Access to the project `c4hnrd-tools`
- The schema file: `keycloak_schema.json`

## 1. Create the BigQuery Dataset

Run the following command to create a new dataset named `keycloak_event_log` in the `northamerica-northeast1` location:

```sh
bq mk \
  --dataset \
  --location=northamerica-northeast1 \
  c4hnrd-tools:keycloak_event_log
```

## 2. Create the BigQuery Table

Run the following command to create a table named `events` in the dataset `keycloak_event_log` using the schema from `keycloak_schema.json`:

```sh
bq mk --table \
  --schema=keycloak_schema.json \
  c4hnrd-tools:keycloak_event_log.events
```

- Make sure `keycloak_schema.json` is in your current working directory.

## External Schema Changes

If log schema changes you can create a temp table to autodetect new schema:

```sh
bq load \
  --autodetect \
  --source_format=NEWLINE_DELIMITED_JSON \
  c4hnrd-tools:keycloak_event_log.temp_table \
  gs://keycloak-event-logs/events_2025-07-28.jsonl
```

You can load the autodetected schema via:

```sh
bq show --schema --format=prettyjson \
c4hnrd-tools:keycloak_event_log.temp_table > autodetected_schema.json
```

autodetected_schema.json can be used to create new table
