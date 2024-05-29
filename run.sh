#!/bin/bash
python pull_events.py
for filename in $(ls "./"); do
  echo $filename
  if [[ $filename == *".txt" ]]; then
    gsutil cp "./$filename" "gs://${DB_BUCKET}/"
    rm "./$filename"
  fi
done
