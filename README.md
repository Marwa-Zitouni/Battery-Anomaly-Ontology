
## Abstract
Lithium-ion batteries are critical components in modern applications like Electric Vehicles (EVs), making the early detection of potential anomalies essential for safety and performance. This project introduces a comprehensive ontology for battery anomaly detection, integrating concepts from SOSA, SSN, and geographic ontologies. The ontology models:
- Various battery components (cells, packs)
- Sensor systems (temperature, voltage, current)
- Comprehensive anomaly classification (thermal runaway, overcharge, sensor faults)
- Temporal and spatial dimensions of anomalies

The ontology provides a formal framework for knowledge representation in Battery Management Systems (BMS), enabling standardized anomaly detection and classification across different systems and manufacturers.

## Introduction
This repository contains the implementation of a battery anomaly ontology using owlready2 in Python, integrating with:
- Semantic Sensor Network (SSN) ontology
- Sensor Observation Sample Actuator (SOSA) ontology
- Geographic location ontologies

The ontology enables:
- Standardized representation of battery anomalies
- Integration with sensor observation data
- Temporal and spatial tracking of anomalies
- Reasoning about anomaly relationships

## Requirements
- Python 3.8+
- owlready2 >= 0.23 (`pip install owlready2`)
- pandas >= 1.0 (for potential data integration)


## How to Use

### 1. Prepare Ontology Files
Place the following ontology files in `src/ontology/used_ontologies/`:
- `ssn.rdf` (Semantic Sensor Network)
- `sosa.rdf` (Sensor Observation Sample Actuator) 
- `geo.owx` (Geographic ontology)

### 2. Generate the Anomaly Ontology
Run the ontology creation script:

python src/python/create_ontology.py


## Contact
We welcome contributions and feedback! For any inquiries, suggestions, or issues related to this ontology, please contact:




