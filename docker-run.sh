#!/bin/bash

# Sharing for FTSConfig.yaml
echo "Starting FreeTAKServer"

cat /opt/fts/FTSConfig.yaml || echo "FTSConfig.yaml not found."

if [[ ! -f "/opt/fts/FTSConfig.yaml" ]]
  then
    echo "Generating FTSConfig.yaml"
    python -c "from FreeTAKServer.core.configuration.configuration_wizard import autogenerate_config; autogenerate_config()"
fi

echo "Starting FreeTAKServer"
python -m FreeTAKServer.controllers.services.FTS