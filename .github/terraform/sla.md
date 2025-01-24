Priority	Definition	Response Goal	Restoration Goal	DR Solution	RTO	RPO	Key Features	SLO
P1	Major outages of entire business-critical applications	15 min	1 hr	DR Active Preferred (DR-102)	≤ 15 mnts	< 1 minute	- Active/Active multi-region with high availability enabled in each region. Instant failover mechanisms in place.	99.99%
P2	Outages and service degradations	15 min	4 hrs	DR Standby Preferred (DR-111)	≤ 2 hours	≤ 15 minutes	- Active/Passive multi-region with the secondary region in standby mode.	99.86%
P3	Single-user "hard down" or multi-user service degradation	4 business hrs	1 business day	DR Media Recovery (DR-104)	≤ 4 hours	≤ 1 hours	- Single-region with basic redundancy and regular backups.	99.89%
