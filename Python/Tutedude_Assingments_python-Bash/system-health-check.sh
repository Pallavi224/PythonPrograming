#!/bin/bash

# Log file
LOG_FILE="system_health.log"

# Get CPU usage
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

# Get available memory percentage
MEMORY_AVAILABLE=$(free | grep Mem | awk '{print $7/$2 * 100.0}')

# Check CPU usage
if (( $(echo "$CPU_USAGE > 80.0" | bc -l) )); then
    echo "$(date): High CPU usage detected: ${CPU_USAGE}%" >> $LOG_FILE
else
    echo "$(date): CPU usage is normal: ${CPU_USAGE}%" >> $LOG_FILE
fi

# Check memory availability
if (( $(echo "$MEMORY_AVAILABLE < 20.0" | bc -l) )); then
    echo "$(date): Low available memory detected: ${MEMORY_AVAILABLE}%" >> $LOG_FILE
else
    echo "$(date): Memory availability is normal: ${MEMORY_AVAILABLE}%" >> $LOG_FILE
fi