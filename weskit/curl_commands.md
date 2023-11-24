# Workflow submission to a WESkit instance via cURL

1. Check service information about WESkit

```terminal
curl --ipv4 https://129.70.51.29:443/ga4gh/wes/v1/service-info -k
```

2. Submit a workflow 

```terminal
run_id=$(curl -vv \
    --ipv4 \
    -k \
    -X POST  https://129.70.51.29:443/ga4gh/wes/v1/runs \
    -F workflow_params='{}'\
    -F workflow_type="SMK" \
    -F workflow_type_version="6.10.0" \
    -F workflow_url="Snakefile" \
    -F workflow_engine_parameters='{
                    "jobs": "1",
                    "cores": "1"
               }' | jq -r .run_id)
```

```terminal 
echo $run_id
```

3. Check all submitted workflows 

```terminal
curl \
    --ipv4 \
    -k \
    -X GET  https://129.70.51.29:443/ga4gh/wes/v1/runs \
    --header 'Content-Type: multipart/form-data' \
    --header 'Accept: application/json'
```

4. Check the state of your submitted workflow 

```terminal
curl \
    --ipv4 \
    -k \
    -X GET  https://129.70.51.29:443/ga4gh/wes/v1/runs/$run_id/status \
    --header 'Content-Type: multipart/form-data' \
    --header 'Accept: application/json'
```

```terminal
curl \
    --ipv4 \
    -k \
    -X GET  https://129.70.51.29:443/ga4gh/wes/v1/runs/$run_id \
    --header 'Content-Type: multipart/form-data' \
    --header 'Accept: application/json'
```


