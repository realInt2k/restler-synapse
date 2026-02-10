#!/usr/bin/env bash

set -e  # exit immediately if any command fails

case "$1" in
  compile)
    echo "Running compile..."
    docker run --rm \
        --network host \
        -v $(pwd)/mydata:/data \
        -v $(pwd)/restler-work:/work \
        -w /work \
        restler \
        /RESTler/restler/Restler compile --api_spec /data/full-synapse-api.json
    ;;
  
  test)
    echo "Running tests..."
    docker run --rm \
        --network host \
        -v $(pwd)/mydata:/data \
        -v $(pwd)/restler-work:/work \
        -w /work \
        restler \
        /RESTler/restler/Restler test \
        --grammar_file /work/Compile/grammar.py \
        --dictionary_file /work/Compile/dict.json \
        --settings /work/Compile/engine_settings.json --no_ssl
    ;;
  
  fuzz-lean)
     echo "Running fuzz-lean..."
     docker run --rm \
        --network host \
        -v $(pwd)/mydata:/data \
        -v $(pwd)/restler-work:/work \
        -w /work \
        restler \
        /RESTler/restler/Restler fuzz-lean --grammar_file /work/Compile/grammar.py --dictionary_file /work/Compile/dict.json --settings /work/Compile/engine_settings.json --no_ssl
    ;;

  fuzz)
     echo "Running fuzz..."
     docker run --rm \
        --network host \
        -v $(pwd)/mydata:/data \
        -v $(pwd)/restler-work:/work \
        -w /work \
        restler \
        /RESTler/restler/Restler fuzz --grammar_file /work/Compile/grammar.py --dictionary_file /work/Compile/dict.json --settings /work/Compile/engine_settings.json --no_ssl --time_budget 0.5
    ;;

  *)
    echo "Usage: $0 {compile|test}"
    exit 1
    ;;
esac

