# Workflow submission to a WESkit instance via cURL

## Check service information about WESkit
curl --ipv4 https://129.70.51.29:443/ga4gh/wes/v1/service-info -k

## Submit a workflow 
run_id=$(curl -vv \
    --ipv4 \
    -k \
    -X POST  https://129.70.51.29:443/ga4gh/wes/v1/runs \
    -F workflow_params='{}'\
    -F workflow_type="SMK" \
    -F workflow_type_version="6.10.0" \
    -F workflow_attachment='@/home/ubuntu/deNBI_workshop/weskit/Snakefile'\
    -F workflow_url="Snakefile" \
    -F workflow_engine_parameters='{
                    "engine-environment": "/weskit/workflows/environment.sh",
                    "jobs": "1",
                    "cores": "1"
               }' | jq -r .run_id)

## Check the state of the submitted workflow 
curl \
    --ipv4 \
    -k \
    -X GET  https://129.70.51.29:443/ga4gh/wes/v1/runs/$run_id \
    --header 'Content-Type: multipart/form-data' \
    --header 'Accept: application/json'

