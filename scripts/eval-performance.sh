#!/bin/bash

jar=$1
fast=$3
tmp_consistent="/tmp/inconsistent.owl"
tmp_inconsistent="/tmp/inconsistent-made-inconsistent.owl"
results_break="results-inconsistent.csv"
results_repair="results-repair.csv"
results_raw="results-raw.txt"

function make_inconsistent {
    if timeout 5m bash -c "java -cp $jar -Xmx10g www.ontologyutils.apps.AppMakeInconsistent $fast $tmp_consistent 2>&1 | tee -a $results_raw"
    then
        tail -n 1 $results_raw \
            | sed -n 's/.*(\([0-9]*\)[^0-9()]*\([0-9]*\)[^0-9()]*).*/\1;\2/p' \
            | tee -a $results_break
        return 0
    else
        echo ";" >> $results_break
        return 1
    fi
}

function repair {
    if timeout 5m bash -c "java -cp $jar -Xmx10g www.ontologyutils.apps.AppAutomatedRepairWeakening $fast $tmp_inconsistent 2>&1 | tee -a $results_raw"
    then
        tail -n 1 $results_raw \
            | sed -n 's/.*(\([0-9]*\)[^0-9()]*\([0-9]*\)[^0-9()]*).*/\1;\2/p' \
            | tee -a $results_repair
        return 0
    else
        echo ";" >> $results_repair
        return 1
    fi
}

cp $2 $tmp_consistent

while true
do
    if  make_inconsistent
    then
        repair
    else
        echo ";" >> $results_repair
    fi
done

