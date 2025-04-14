from owlready2 import *
from owlready2 import get_ontology, Thing, ObjectProperty, DataProperty, Imp, sync_reasoner_pellet

import pandas as pd

# Chargement des ontologies utilisées
onto_ssn = get_ontology("/Users/zitouni/Desktop/Ontology /used_ontologies/ssn.rdf").load()  # New SSN, cannot import the old one
onto_sosa = get_ontology("/Users/zitouni/Desktop/Ontology /used_ontologies/sosa.rdf").load()
onto_location = get_ontology("/Users/zitouni/Desktop/Ontology /used_ontologies/geo.owx").load()
onto_anomaly = get_ontology("http://example.org/anomaly.owl")

# Définition des classes et sous-classes pour l'ontologie des anomalies
with onto_anomaly:
    
    onto_anomaly.imported_ontologies.append(onto_sosa)
    onto_anomaly.imported_ontologies.append(onto_ssn)
    onto_anomaly.imported_ontologies.append(onto_location)

    # Classes liées aux batteries
    class Battery(Thing):
        """Classe représentant une batterie dans l'ontologie."""
        pass

    class BatteryCell(Battery):
        """Représente une cellule de batterie individuelle."""
        pass

    class BatteryPack(Battery):
        """Représente un pack de batteries contenant plusieurs cellules."""
        pass

    # Classes temporelles
    class TemporalEntity(Thing):
        """Représente une entité temporelle."""
        pass

    class Instant(TemporalEntity):
        """Représente un instant spécifique dans le temps."""
        pass

    class Interval(TemporalEntity):
        """Représente un intervalle de temps."""
        pass

    # Classes d'anomalies
    class Anomaly(Thing):
        """Classe de base pour représenter les anomalies."""
        pass

    # Sous-classes pour les anomalies liées aux capteurs
    class SensorFault(Anomaly):
        """Anomalie liée à un capteur."""
        pass

    class TemperatureSensorFault(SensorFault):
        """Défaut du capteur de température."""
        pass

    class CurrentSensorFault(SensorFault):
        """Défaut du capteur de courant."""
        pass

    class VoltageSensorFault(SensorFault):
        """Défaut du capteur de tension."""
        pass

    # Sous-classes pour les anomalies liées aux batteries
    class BatteryFault(Anomaly):
        """Anomalie liée à une batterie."""
        pass

    class ExternalShortCircuit(BatteryFault):
        """Court-circuit externe."""
        pass

    class Overdischarge(BatteryFault):
        """Décharge excessive."""
        pass

    class Overcharge(BatteryFault):
        """Surcharge."""
        pass

    class ThermalRunaway(BatteryFault):
        """Emballement thermique."""
        pass

    class BatteryAcceleratedDegradation(BatteryFault):
        """Dégradation accélérée de la batterie."""
        pass

    class BatterySwelling(BatteryFault):
        """Gonflement de la batterie."""
        pass

    class ElectrolyteLeakage(BatteryFault):
        """Fuite d'électrolyte."""
        pass

    class Smoke(BatteryFault):
        """Fumée détectée."""
        pass

    class Fire(BatteryFault):
        """Incendie."""
        pass

    class Explosion(BatteryFault):
        """Explosion."""
        pass

    # Surchauffe et sous-classes associées
    class Overheat(BatteryFault):
        """Surchauffe."""
        pass

    class PoorHeatDissipation(Overheat):
        """Mauvaise dissipation thermique."""
        pass

    class ExternalHeatTransfer(Overheat):
        """Transfert de chaleur externe."""
        pass

    class AbnormalHeatGeneration(Overheat):
        """Production anormale de chaleur."""
        pass

    # Court-circuit interne et sous-classes associées
    class InternalShortCircuit(BatteryFault):
        """Court-circuit interne."""
        pass

    class SeparatorTearing(InternalShortCircuit):
        """Déchirure du séparateur."""
        pass

    class SeparatorDefect(InternalShortCircuit):
        """Défaut du séparateur."""
        pass

    class SeparatorPenetration(InternalShortCircuit):
        """Pénétration du séparateur."""
        pass

    class Melting(InternalShortCircuit):
        """Fusion."""
        pass

    class SeparatorShrinkage(InternalShortCircuit):
        """Rétractation du séparateur."""
        pass

    # Anomalies liées aux actionneurs
    class ActuatorFault(Anomaly):
        """Défaut lié à un actionneur."""
        pass

    class BatteryConnectionFault(ActuatorFault):
        """Défaut de connexion de la batterie."""
        pass

    class CoolingSystemFault(ActuatorFault):
        """Défaut du système de refroidissement."""
        pass

    # Classe personnalisée pour les capteurs combinés
    class CombinedSensor(Thing):
        """Classe personnalisée combinant les fonctionnalités des capteurs SOSA et SSN."""
        pass

    # Classes pour la localisation spatiale
    class SpatialObject(Thing):
        """Représente un objet spatial, tel qu'une localisation géographique."""
        pass

    class GeographicRegion(SpatialObject):
        """Représente une région géographique."""
        pass

    class BatteryLocation(SpatialObject):
        """Représente la localisation d'une batterie."""
        pass

    # Intégration SOSA et SSN
    class Sensor(Thing):
        """Représente un capteur mesurant diverses propriétés."""
        pass

    class Observation(onto_sosa.Observation):
        """Représente une observation réalisée par un capteur."""
        pass

    class Property(onto_ssn.Property):
        """Représente une propriété mesurée ou contrôlée par un capteur."""
        pass

    class ObservableProperty(onto_sosa.ObservableProperty):
        """Représente une propriété observable par un capteur."""
        pass

    # Propriétés liant les anomalies et les batteries
    class hasBatteryInfo(ObjectProperty):
        """Lien entre une anomalie et ses informations associées sur la batterie."""
        domain = [Anomaly]
        range = [Battery]

    # Propriétés d'objets pour lier les ontologies
    
    class observes(ObjectProperty):
        """Relation entre un capteur et une propriété qu'il observe (SSN -> SOSA)."""
        domain = [Sensor]
        range = [onto_ssn.Property]

    class hosts(ObjectProperty):
       
        domain = [Battery]
        range = [Sensor]

    class madeObservation(ObjectProperty):
        """Lien entre un capteur et l'observation qu'il a effectuée (SSN -> Custom)."""
        domain = [Sensor]
        range = [Observation]

    class measures(ObjectProperty):
        """Lien entre un capteur et la propriété qu'il mesure (SOSA -> SSN)."""
        domain = [Sensor]
        range = [onto_ssn.Property]

    class hasObservation(ObjectProperty):
        """Lien entre un capteur et une observation qu'il effectue (SOSA -> Custom)."""
        domain = [Sensor]
        range = [Observation]

    class hasTime(ObjectProperty):
        """Lien entre une observation et le temps où elle a été réalisée (SOSA -> TIME)."""
        domain = [Observation, Anomaly]
        range = [TemporalEntity]

    class hasLocation(ObjectProperty):
        """Lien entre une observation et le lieu où elle a été réalisée (SOSA -> LOCATION)."""
        domain = [Observation, Anomaly]
        range = [SpatialObject]

    class hasSimpleResult(DataProperty):
        """Valeur d'une observation (par exemple, température, courant)."""
        domain = [Observation]
        range = [float]

    #class hasBeenDetected(DataProperty):
        #domain = [Anomaly]
        #range = [bool]

    class hasAnomalyTime(ObjectProperty):
        """Lien entre une anomalie et le moment où elle s'est produite (Custom -> TIME)."""
        domain = [Anomaly]
        range = [TemporalEntity]

    class hasAnomalyLocation(ObjectProperty):
        """Lien entre une anomalie et le lieu où elle s'est produite (Custom -> LOCATION)."""
        domain = [Anomaly]
        range = [SpatialObject]
    #class detect(ObjectProperty):
        #domaine=[Sensor]
        #range=[Anomaly]

    class hasTimeSlot(DataProperty):
        """Indique le moment où une observation a été effectuée."""
        domain = [Observation, Anomaly]
        range = [int]  # Use integers to represent time in minutes

 # Create instances of BatteryCell
with onto_anomaly:
    cell1 = BatteryCell("Cell1")

# Create instances of Temperature Sensors
with onto_anomaly:
    TempSensor1 = Sensor("TempSensor1")
    TempSensor2 = Sensor("TempSensor2")
    TempSensor3 = Sensor("TempSensor3")

# Create instance of Current Sensor
    CurrentSensor = Sensor("CurrentSensor")

# Link the same battery cell to all three sensors using the "hosts" property
with onto_anomaly:
    cell1.hosts = [TempSensor1, TempSensor2, TempSensor3, CurrentSensor]

# Step 4: Save the ontology after reasoning
onto_anomaly.save(file="onto_anomaly.owl", format="rdfxml")

