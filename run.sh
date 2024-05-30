#!/bin/bash
python3 pull_events.py
for filename in $(ls "./"); do
  if [[ $filename == *".jsonl" ]]; then
    echo $filename
    gsutil cp "./$filename" "gs://${DB_BUCKET}/"
    rm "./$filename"
  fi
done
