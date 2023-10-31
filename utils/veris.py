import re

class SecurityIncident:
    def __init__(self, incident_type, reference, summary, source_id, campaign_id, confidence, timeline):
        self.incident_type = incident_type
        self.reference = reference
        self.summary = summary
        self.source_id = source_id
        self.campaign_id = campaign_id
        self.confidence = confidence
        self.timeline = Timeline(**timeline)

class Timeline:
    def __init__(self, incident, compromise, exfiltration, discovery, containment):
        self.incident = Incident(**incident)
        self.compromise = TimePeriod(**compromise)
        self.exfiltration = TimePeriod(**exfiltration)
        self.discovery = TimePeriod(**discovery)
        self.containment = TimePeriod(**containment)

class Incident:
    def __init__(self, year, month, day, time):
        self.year = year
        self.month = month
        self.day = day
        self.time = time

class TimePeriod:
    def __init__(self, unit, value):
        self.unit = unit
        self.value = value

    def validate(self):
        # Validate the time period unit and value here if needed
        pass

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __repr__(self):
        return self.__str__()

# Example usage:
timeline_data = {
    "incident": {
        "year": 2022,
        "month": 10,
        "day": 31,
        "time": "05:45:00 PM"
    },
    "compromise": {
        "unit": "days",
        "value": 7
    },
    # Add other timeline data here
}

incident_data = {
    "type": "Security Incident",
    "reference": "https://example.com/incident123",
    "summary": "A security breach occurred in our network, exposing sensitive data.",
    "source_id": "vcdb",
    "campaign_id": "campaign123",
    "confidence": "High",
    "timeline": timeline_data
}

incident = SecurityIncident(**incident_data)

# Validate and print the containment period
incident.timeline.containment.validate()
print(f"Containment Time: {incident.timeline.containment}")
