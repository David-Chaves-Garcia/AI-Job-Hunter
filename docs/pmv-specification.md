# AI Job Hunter — PMV Specification v1.0

## Objective
Build a job-search assistant focused initially on InfoJobs.

## Included in the PMV
- Professional profile without identification photo.
- Configurable job-search preferences.
- InfoJobs as the first portal.
- Offer collection and normalization.
- Persistent database and search history.
- Duplicate detection and new/updated offer detection.
- Configurable matching score from 0 to 100.
- Configurable minimum score.
- Short offer summary.
- Direct link to the original offer.
- Configurable recurring scan interval, 60 minutes by default.

## Excluded from the PMV
- LinkedIn, Indeed, Adecco and Eurofirms.
- Automatic application submission.
- Automatic CV/cover-letter generation.
- Automatic application-form answers.
- Candidate photo processing.

## Main workflow
InfoJobs search → normalize → database → detect new/updated offers → score → filter → display → open original offer → repeat on schedule.

## Offer states
NEW, ANALYZED, RELEVANT, DISCARDED, VIEWED, APPLIED, CLOSED, EXPIRED.

## Security
Never commit secrets or credentials. Do not bypass CAPTCHAs, authentication controls, rate limits, robots restrictions or other anti-automation mechanisms.
