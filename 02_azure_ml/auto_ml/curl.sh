#!/usr/bin/env bash

ENDPOINT=<ENDPOINT>

curl -d '{
    "data": [
        {
            "AGE": 42,
            "SEX": 1,
            "BMI": 28.7,
            "BP": 102.3,
            "S1": 199,
            "S2": 89.0,
            "S3": 42.0,
            "S4": 5.0,
            "S5": 5.6789,
            "S6": 99
        }
    ]
}'\
    -H "Content-Type: application/json" \
    -X POST $ENDPOINT
