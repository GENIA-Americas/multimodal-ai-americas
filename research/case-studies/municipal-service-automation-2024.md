Title: Municipal Service Automation: Pilot in Urban Latin America
Sector: Public sector
Geography: Urban Latin America (composite)
Year: 2024
Authors: GENIA Americas Corporation

## Context

Municipal governments across Latin America process millions of citizen
service requests annually through manual intake: paper forms, in-person
counters, phone queues. Processing times range from days to months.
Citizens in lower-income areas face disproportionate barriers.

This case study describes a pilot deploying AI-assisted intake and
routing across three mid-sized Latin American cities. Details are
composited to protect partner confidentiality.

## Problem

Three failure modes motivated the pilot:

Intake bottlenecks: staff time consumed by data entry with no
analytical value, creating queues regardless of downstream capacity.

Routing errors: requests frequently routed to the wrong department
on first submission. Re-routing added an average of four days to
resolution time.

Language and literacy barriers: requests from citizens whose primary
language was not the official municipal language had higher error rates
and longer processing times.

## Approach

Three components deployed through Glapagos:

Automated intake classification: fine-tuned CivicIntent model classifies
incoming requests into service categories with 94% accuracy. Handles
Spanish and Portuguese with regional variant support.

Intelligent routing: rules engine combining classification output with
department load and priority queues. Human review required for
confidence below 0.82.

Multilingual interface: web and SMS supporting Spanish, Portuguese, and
two indigenous languages with audio input for low-literacy users.

A six-week parallel run preceded go-live: human staff and AI system
processed all requests independently before the AI took over primary
processing.

## Results

90 days of production operation, approximately 340,000 requests total.

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Average intake processing time | 4.2 days | 0.3 days | -93% |
| First-submission routing accuracy | 71% | 94% | +23pp |
| Staff time on intake | 38% FTE | 9% FTE | -29pp |
| Requests requiring human review | 100% | 18% | -82pp |
| Multilingual request error rate | 34% | 8% | -26pp |
| Citizen satisfaction (survey) | 61% positive | 79% positive | +18pp |

## Failure Modes

Low-confidence edge cases: 18% of requests required human review,
concentrated in ambiguous service categories. Targeted retraining
reduced this to 12% by end of measurement period.

Novel request types: model performed poorly on request types absent
from training data. New categories required manual handling until
sufficient labeled examples were collected.

SMS limitations: higher error rates than web interface due to
transcription errors on poor-quality audio.

## Lessons

Parallel running is non-negotiable. The six-week parallel run caught
three significant routing errors before go-live.

Confidence thresholds require per-deployment calibration. The 0.82
threshold needed adjustment for two of three cities due to local
request distribution differences.

Staff retraining is a deployment cost. Budget 10-15% of implementation
cost for change management.

Multilingual support is a fairness requirement. The population that
most needed better service was most underserved by the existing system.

## Replication

CivicIntent model and deployment configuration: models/public-sector/
Expected timeline: 8-12 weeks for data collection and model adaptation,
6 weeks parallel run minimum, quarterly retraining ongoing.

Contact admin@genia.ai for implementation support.
