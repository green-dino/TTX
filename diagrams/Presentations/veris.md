### Security Incident

- **Type**: string
- **Description**: Confirmed incident?

### Reference

- **Type**: string
- **Description**: Reference should be a URL, incident number, case ID, or other reference to the document the VERIS incident was based on.

### Summary

- **Type**: string
- **Description**: Give a good descriptive summary of the incident in several sentences. Use natural language instead of VERIS notation, but we should be able to 'VERISize' the incident pretty well from just this description.
- **REMINDER**: IF THIS IS FOR THE DBIR AND NOT VCDB - DON'T RECORD VICTIM-IDENTIFYING INFO.

### Source ID

- **Type**: string
- **Description**: Source of the data (e.g., vcdb, vzir, hr dept)

### Campaign ID

- **Type**: string
- **Description**: (Way to associate multiple incidents within one campaign).

### Confidence

- **Type**: string

### Timeline

- **Incident**

  - **Description**: When did this incident initially occur?
  - **Year**
    - **Type**: integer
    - **Maximum**: 2022
    - **Minimum**: 1950
    - **Required**: Yes
  - **Month**
    - **Type**: integer
    - **Maximum**: 12
    - **Minimum**: 1
  - **Day**
    - **Type**: integer
    - **Maximum**: 31
    - **Minimum**: 1
  - **Time**
    - **Description**: Use the format '05:45:00 PM'
    - **Type**: string
    - **Pattern**: ^0[1-9]|1[0-2]:[0-5][0-9]:[0-5][0-9] [AP]M$

- **Compromise**

  - **Description**: How long from the first action to the first compromise of an attribute?
  - **Unit**
    - **Type**: string
    - **Required**: Yes
  - **Value**
    - **Type**: number

- **Exfiltration**

  - **Description**: How long from initial compromise to first known data exfiltration?
  - **Unit**
    - **Type**: string
    - **Required**: Yes
  - **Value**
    - **Type**: number

- **Discovery**

  - **Description**: How long from compromise until the incident was discovered by the victim organization?
  - **Unit**
    - **Type**: string
    - **Required**: Yes
  - **Value**
    - **Type**: number

- **Containment**

  - **Description**: How long did it take the organization to contain the incident once it was discovered?
  - **Unit**
    - **Type**: string
    - **Required**: Yes
  - **Value**
    - **Type**: number
