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
