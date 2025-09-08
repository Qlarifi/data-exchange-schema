#!/usr/bin/env python3
import json
import csv
import os
from collections import defaultdict, OrderedDict

def flatten_event(event):
    """Flatten nested objects in an event"""
    flattened = {}
    
    for key, value in event.items():
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                flattened[f"{key}.{subkey}"] = subvalue
        else:
            flattened[key] = value
    
    return flattened

def get_ordered_columns():
    """Return the standard column ordering"""
    return [
        'effectiveTimestamp',
        'type', 
        'consumerId',
        'transactionId',
        'installmentId',
        'transactionType',
        'feeType',
        'postponedType',
        'refundId',
        'reason',
        'amount.number',
        'amount.currency',
        'newAmountDue.number',
        'newAmountDue.currency',
        'feeAmount.number',
        'feeAmount.currency',
        'dueTimestamp',
        'newDueTimestamp',
        'index',
        'metadata'
    ]

def process_scenario_file(scenario_path, output_dir):
    """Process a single scenario JSON file and create CSV files grouped by event type"""
    scenario_name = os.path.splitext(os.path.basename(scenario_path))[0]
    
    with open(scenario_path, 'r') as f:
        events = json.load(f)
    
    # Group events by type
    events_by_type = defaultdict(list)
    for event in events:
        flattened_event = flatten_event(event)
        events_by_type[event['type']].append(flattened_event)
    
    # Create CSV file for each event type
    for event_type, type_events in events_by_type.items():
        csv_filename = f"{scenario_name}_{event_type}.csv"
        csv_path = os.path.join(output_dir, csv_filename)
        
        # Get all unique columns from events of this type
        all_columns = set()
        for event in type_events:
            all_columns.update(event.keys())
        
        # Order columns according to standard order, then add any additional columns
        standard_columns = get_ordered_columns()
        ordered_columns = []
        
        # Add standard columns that exist in the data
        for col in standard_columns:
            if col in all_columns:
                ordered_columns.append(col)
                all_columns.remove(col)
        
        # Add any remaining columns (like metadata.DatasetId)
        remaining_columns = sorted(all_columns)
        for col in remaining_columns:
            if col.startswith('metadata.'):
                ordered_columns.append(col)
        
        # Add any other remaining columns
        for col in remaining_columns:
            if not col.startswith('metadata.') and col not in ordered_columns:
                ordered_columns.append(col)
        
        # Write CSV file
        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=ordered_columns)
            writer.writeheader()
            
            for event in type_events:
                # Create ordered dict with empty values for missing columns
                ordered_event = OrderedDict()
                for col in ordered_columns:
                    ordered_event[col] = event.get(col, '')
                writer.writerow(ordered_event)
        
        print(f"Created: {csv_path}")

def main():
    """Process all scenario files in both EUR and USD directories"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Process EUR scenarios
    eur_dir = os.path.join(base_dir, 'scenariosEUR')
    for i in range(1, 10):  # scenarios 1-9
        scenario_file = os.path.join(eur_dir, f'scenario{i}.json')
        if os.path.exists(scenario_file):
            process_scenario_file(scenario_file, eur_dir)
    
    # Process USD scenarios
    usd_dir = os.path.join(base_dir, 'scenariosUSD')
    for i in range(1, 10):  # scenarios 1-9
        scenario_file = os.path.join(usd_dir, f'scenario{i}.json')
        if os.path.exists(scenario_file):
            process_scenario_file(scenario_file, usd_dir)

if __name__ == "__main__":
    main()