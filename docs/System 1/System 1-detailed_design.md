---
Template_Version: 1.0
Document_Version: 
Author: 
Classification:
---


Template version: {{ Template_Version }}<br>
Document version: [Manually Insert]<br>
Author: [Manually Insert]<br>
Classification: [Manually Insert]<br>

![Company Logo](/common_images/companylogo.png)

# System Detailed Design: [System Item Name]

- **Date**: [Insert Date]
- **Author**: [Insert Author]
- **Version**: [Insert Document Version]

## Revision History

| Version | Date | Description | Author |
| --- | --- | --- | --- |

{% for commit in git.log %}
| {{ commit.id[:7] }} | {{ commit.date }} | {{ commit.message }} | {{ commit.author }} |
{% endfor %}

# System Detailed Design: System 1

- **Date**: Insert Date
- **Author**: Insert Author

## System Overview
System overview description goes here.

## Design Goals
- Design goal 1
- Design goal 2
- Design goal 3

## Architecture
Brief description of the system architecture.

## Adherence to Requirements
Description of how the system adheres to the initial requirements.

### TEST MEGA-MERGE

### Second TEST

## High-Level Subsystem Overview
- **Security**: Brief description
- **Subsystem 1B**: Brief description
- **Subsystem 1C**: Brief description

## System-Specific Functional Requirements

| ID | Description | Detail | Source | 
| --- | --- | --- | --- |
| FR001 | Description of functional requirement FR001. | Extended detail about functional requirement FR001. | Document or person source for FR001. |
