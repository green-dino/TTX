# Integrating NIST


# NIST

## Identify
## Protect
## Detect
## Respond
## Recover




# Control Group

## control short number  
### group-number
### secondary control number
### group-number

## Description of the control
## Discussion Questions
## Files / Evidence
## Status
## Priority
## Selected
## last Updated 
## Requirements	
## Estimate	
## Design	
## Implementation
## Project Timeline 
### Start 
### End
## Responsible Team
## Team Members	
## Maintenance	
## Review Date
## Item ID	 
## Exception Required	 
## Exception For	 
## CSF Group	
## Exception Duration - Start	
## Exception Duration - End	
## Impact to the Process	

# RACI chart 
## Responsible	RCSF	
## Accountable	A-CSF	
## Consulted	C-CSF 
## Informed	    I-CSF

# Control 
	
## Visibility
## Alerting	
## Detection	
## Telemetry	 
## Signals	
## Components

#  Specialty Area
 ##  Specialty Area Description
### Work Role
### Work Role Description
#### Work Role ID
##### Knowledge
###### Computer networking concepts and protocols, and network security methodologies.
######  Cybersecurity and privacy principles.
###### Cyber threats and vulnerabilities.
######  Specific operational impacts of cybersecurity lapses.
######  Cyber defense and vulnerability assessment tools and their capabilities.
###### Cryptography and cryptographic key management concepts.
######  Organization's enterprise information security architecture.
###### Security Assessment and Authorization process.
######  Cybersecurity and privacy principles used to manage risks related to the use, processing, storage, and transmission of information or data.
###### Vulnerability information dissemination sources (e.g., alerts, advisories, errata, and bulletins).
######  Cybersecurity and privacy principles and organizational requirements (relevant to confidentiality, integrity, availability, authentication, non-repudiation).
###### Information technology (IT) security principles and methods (e.g., firewalls, demilitarized zones, encryption).
###### System and application security threats and vulnerabilities (e.g., buffer overflow, mobile code, cross-site scripting, Procedural Language/Structured Query Language [PL/SQL] and injections, race conditions, covert channel, replay, return-oriented attacks, malicious code).
###### Supply Chain Risk Management Practices (NIST SP 800-161)
###### Network security architecture concepts including topology, protocols, components, and principles (e.g., application of defense-in-depth).
###### Security architecture concepts and enterprise architecture reference models (e.g., Zachman, Federal Enterprise Architecture [FEA]).
######  Security models (e.g., Bell-LaPadula model, Biba integrity model, Clark-Wilson integrity model).
##### Skills
##### Abilities
###### Tasks
## OPERATE and MAINTAIN (OM)
### Data Administration (DTA)

### Knowledge Management (KMG)
### Customer Service and Technical Support (STS)
### Network Services (NET)
### Systems Administration (ADM)
### Systems Analysis (ANA)

## SECURELY PROVISION (SP)

### Risk Management (RSK)

### Software Development (DEV)

 ### Systems Architecture (ARC)

 ### Technology R&D (TRD)
 ### Systems Requirements Planning (SRP)
### Test and Evaluation (TST)
### Systems Development (SYS)

## OVERSEE and GOVERN (OV)
### Legal Advice and Advocacy (LGA)

### Training, Education, and Awareness (TEA)

### Cybersecurity Management (MGT)

### Strategic Planning and Policy (SPP)

### Executive Cyber Leadership (EXL)
### Program/Project Management (PMA) and Acquisition


## PROTECT and DEFEND (PR) 
### Cybersecurity Defense Analysis (CDA)
### Cybersecurity Defense Infrastructure Support (INF)
### Incident Response (CIR)
### Vulnerability Assessment and Management (VAM)

## ANALYZE (AN)

### Threat Analysis (TWA)
### Exploitation Analysis (EXP)
### All-Source Analysis (ASA)

### Targets (TGT)

### Language Analysis (LNG)


## COLLECT and OPERATE (CO) 
### Collection Operations (CLO)

### Cyber Operational Planning (OPL)


### Cyber Operations (OPS)

## INVESTIGATE (IN) 

### Cyber Investigation (INV)
### Digital Forensics (FOR)

# CCE
## Phase 1 
* events
* cyber Events
* scoring 

## Phase 2 
* Information Gathering 
* System Diagrams 
* Interviews 
* Manuals 

## Phase 3 
### Boundary Condition 
* Technical Approach 
* Targeting Details
* System Targeting Profile 
* Critical needs
* Attack Scenarios 
* Payload 
* HCE 

# Cloud Security Review 

## Phase 1: Cloud Providers
### Stage 1: Identify the primary CSP
### Stage 2: Understand the high-level hierarchy
### Stage 3: Understand what is running in the Accounts
### Stage 4: Understand the network architecture
### Stage 5: Understand the current IAM setup
### Stage 6: Understand the current monitoring setup
### Stage 7: Understand the current secrets management setup
### Stage 8: Identify existing security controls
### Stage 9: Get the low-hanging fruits

## Phase 2: Workloads

### Stage 1: Understand the high-level business offerings
### Stage 2: Identify the primary tech stack
### Stage 3: Understand the network architecture
### Stage 4: Understand the current IAM setup
### Stage 5: Understand the current monitoring setup
### Stage 6: Understand the current secrets management setup
### Stage 7: Identify existing security controls
### Stage 8: Get the low-hanging fruits

## Phase 3: Code
### Stage 1: Understand the code's structure
### Stage 2: Understand the adoption of Infrastructure as Code
### Stage 3: Understand how CI/CD is setup
### Stage 4: Understand how the CI/CD platform is secured

# F3EAD: Find, Fix, Finish, Exploit, Analyze, Disseminate
## Find
- Shodan dorks/safaris
* Shodan Search Filter docs: https://beta.shodan.io/
search/filters
- https://help.shodan.io/the-basics/search-queryfundamentals
- https://www.shodan.io/explore
* https://github.com/sansatart/scrapts/blob/master/
shodan-favicon-hashes.csv
* Shodan dork repos:
- https://archive.ph/WtayW (Hunting C2 with Shodan
by Michael Koczwara on Medium)
- https://github.com/n0x08/ShodanTools
- https://pentestit.com/shodan-queries/
- https://cyberwarzone.com/shodan-queries-list-forthreat-
hunters-2022/
- https://github.com/jakejarvis/awesome-shodanqueries
* Shodan query examples:
- look up your own public IP addr: https://
me.shodan.io
- Cobalt Strike BEACON: `product:"Cobalt Strike
Beacon"` || https://www.shodan.io/search?
query=product%3A%22Cobalt%20Strike%20Beacon%22
- Cobalt Strike JARM:
`ssl.jarm:07d14d16d21d21d07c42d41d00041d24a458a375eef0c576d
23a7bab9a9fb1` (_note:_ this is based on the Java stack,
*not* Cobalt Strike _per se_)
~ @AseemShrey via Twitter:
- Search for secret API keys publicly exposed on
websites -->
* ex : Searching for slack API token on all the
scanned websites: `http.html:"xoxb-"`
- Search using 'favicon' hash (an accurate/
effective way of finding exposed services; see github repo
of favicon hashes above) -->
* ex: Find all jenkins server:
`http.favicon.hash:81586312`
- Search using website's title -->
* ex: Find all grafana dashboards:
`http.title:"Grafana"`
- Search services vulnerable to a particular CVE
(*note: this is behind an upgraded membership paywall) -->
* ex: Search all machines vulnerable to
'eternal blue': `vuln:ms17-010`
* ex: Services that are vulnerable to
Heartbleed - `vuln:CVE-2014-0160`
- Search for a particular port + service -->
* ex: SSH on port 22 or 3333: `ssh
port:22,3333` OR `proftpd port:21`
- can be used to find services on nonstandard
port, ex: `ssh -port:22` # ssh which is not on
port 22
- Search for a particular OS -->
* ex: Checking for vulnerable win 10 home
version: `os:"Windows 10 Home 19041"`
- Combine filters to generate more targeted results
(e.g., All windows 7 machines in India: `country:"IN"
os:"windows 7"`)
- Sandbox (Dynamic Analysis engines) results
* app.any.run
* tria.ge (note on accessing dropped files: https://
hatching.io/blog/dropped-files/)
* JoeSandbox
* HybridAnalysis
* Intezer
* MalwareBazaar
- http://tweettioc.com/
- https://tracker.viriback.com/
- http://benkow.cc/search.php
- https://github.com/stamparm/maltrail/
* https://github.com/stamparm/ipsum
- https://github.com/pan-unit42/tweets
- https://rstcloud.net/freefeed#download
- abuse.ch umbrella:
* https://threatfox.abuse.ch/ (`threat_type:botnet_cc`)
* https://urlhaus.abuse.ch/
* https://bazaar.abuse.ch/
- https://sslbl.abuse.ch/
- https://otx.alienvault.com
- https://malshare.com/
- https://virusdeck.com/dashboard
- maldatabase: `curl https://api.maldatabase.com/download
-H "Authorization:{authKeyHere}" --compressed -o
{outputFileNameHere}.csv`
- https://www.threat-intel.xyz/
- https://threatfeeds.io/
- https://threatview.io/
* https://threatview.io/Downloads/High-Confidence-
CobaltStrike-C2%20-Feeds.txt
- https://portal.malbeacon.com/
- https://www.malwareurl.com/index.php
- https://blokada.org/mirror/v5/energized/blu/hosts.txt
- https://malsilo.gitlab.io/feeds/dumps/domain_list.txt
- https://lookyloo.circl.lu/capture
- URLscan.io dorks:
* search reference: https://urlscan.io/docs/search/
* https://urlscan.io/search/#task.tags:%22c2%22
* https://urlscan.io/search/#task.tags:%22malware%22
* https://urlscan.io/search/#task.tags:
%22threatshare%22
* https://urlscan.io/search/#task.tags:%22lokibot%22
* https://urlscan.io/search/#task.tags:%22oski%22
* https://urlscan.io/search/#task.tags:%22amadey%22
* https://urlscan.io/search/#task.tags:%22cypress%22
* https://urlscan.io/search/#task.tags:
%22falconsandbox%22
* https://urlscan.io/search/#task.tags:
%22matanbuchus%22
- https://raw.githubusercontent.com/0xDanielLopez/
TweetFeed/master/today.csv

## Fix
_Track evil; fix it in time & space._
- https://zeltser.com/malicious-ip-blocklists/
- https://zeltser.com/automated-malware-analysis/
- https://zeltser.com/lookup-malicious-websites/
- [ip context repo](https://gist.github.com/ashbyca/
2d1e58232938bcbcdf1d8c7b89fa9372)
- https://id-ransomware.blogspot.com/
* https://id-ransomware.malwarehunterteam.com/

## Intel Platforms/Aggregators/Dashboards
- https://exchange.xforce.ibmcloud.com/
- virustotal
- https://www.threatminer.org/index.php
- [Kaspersky Threat Intel Portal](https://
opentip.kaspersky.com/howto)
- https://community.riskiq.com/home
* RiskIQ Cobalt Strike Team Server query: `https://
community.riskiq.com/search/components/
Command%20and%20Control%20Server/Cobalt%20Strike/`
- https://app.binaryedge.io/services/query
- https://www.domainiq.com/ (limited free queries)
- https://domainbigdata.com/) (hit or miss)
- https://spyse.com/ (paywall)
- https://pulsedive.com/dashboard/
- alienvault otx (https://otx.alienvault.com)
- https://cybergordon.com/
- https://github.com/pirxthepilot/wtfis
### Palo Alto  
* playbook ( https://pan-unit42.github.io/playbook_viewer/?pb=evasive-serpens)
* atoms (https://unit42.paloaltonetworks.com/atoms/)

### IBM X-Force	
* Threat Actors (Hive) (https://exchange.xforce.ibmcloud.com/search/hive)
* Threat Actors (ITG) (https://exchange.xforce.ibmcloud.com/search/ITG)
### Malpedia	
* Threat Actors ( https://malpedia.caad.fkie.fraunhofer.de/actors)
### Kaspersky	
* Threat Actors (https://apt.securelist.com/)
### MITRE	
* Threat Actors (https://attack.mitre.org/groups/)
### Crowdstrike	
* Threat Actors profiles ( https://adversary.crowdstrike.com/en-US/)
### Mandiant	
* Well-known Threat Actors (https://www.mandiant.com/resources/insights/apt-groups)
* Threat Actors (APT) ( https://www.mandiant.fr/search?search=APT)
* Threat Actors (UNC) ( https://www.mandiant.fr/search?search=UNC)
### Secureworks	
* Threat Actors profiles (https://www.secureworks.com/research/threat-profiles)
### Dragos	
* Threat Actors profiles (https://www.dragos.com/threat-activity-groups/)
### Thales	
* Threat Actors profiles (https://cyberthreat.thalesgroup.com/attackers)
### APTMAP	
* Threat Actors profiles ( https://andreacristaldi.github.io/APTmap/ )
### Thai CERT	
* Threat Actors profiles(https://apt.etda.or.th/cgi-bin/listgroups.cgi)
### CERT-UA	
* Threat Actors (UAC) (https://cert.gov.ua/search/UAC-)
### Microsoft	
* Threat Actors + naming taxonomy (https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide)




### Sandboxes/Attribution/Reputation
- Dynamic Analyis platforms (see above in *FIND*)
* app.any.run
* tria.ge
* JoeSandbox
* HybridAnalysis
* Intezer
- https://www.filescan.io/scan
- https://app.docguard.io/
- https://labs.inquest.net/
- https://manalyzer.org/
- https://capesandbox.com/
- https://cuckoo.cert.ee/analysis/search/
- [Polish Cert MWDB](https://mwdb.cert.pl/)
- https://totalhash.cymru.com/
- https://valkyrie.comodo.com/
- [Known Goods - hashdd](https://hashdd.com/)
- https://talosintelligence.com/
- abuse.ch properties
* urlhaus
* bazaar
* threatfox
- https://domain-reputation.whoisxmlapi.com/lookup
- https://www.barracudacentral.org/lookups/lookupreputation
- https://check.spamhaus.org/
- http://cinsscore.com/list/ci-badguys.txt
- https://www.blocklist.de/en/search.html
- https://www.brightcloud.com/tools/url-ip-lookup.php
- https://www.abuseipdb.com/
- https://www.ipvoid.com/
- http://iplists.firehol.org/
- https://sitecheck.sucuri.net/

### Reconnaissance
#### Active Scanning Repos
- https://builtwith.com/
- https://sitereport.netcraft.com/
- https://publicwww.com/ (web source code search engine)
- https://www.nerdydata.com/ (web source code search
engine)
- https://well-known.dev/ (Search `/.well-known/` resources
served by sites across the web.)
- [Stanford Internet Research Data Repo (scans.io)]
(https://scans.io/)
- [Rapid7's Project Sonar](https://opendata.rapid7.com/)
- https://urlscan.io/
- https://search.censys.io/
- https://beta.shodan.io/
- circl.lu (pDNS, pSSL, lookyloo)
- https://check-host.net/
#### Passive Data Collectors/Aggregators
- https://securitytrails.com/
- https://dnsdumpster.com/
- https://searchdns.netcraft.com/
- https://www.robtex.com/
- https://www.greynoise.io/viz/
- https://spur.us/app/context
- https://www.dan.me.uk/
- ip2whois
- whoisXML
- research.domaintools.com
- Zetalytics/Zonecruncher
- https://crt.sh/
- https://bgp.he.net/
- https://bgpview.io/
- https://stat.ripe.net/widget/routing-history (BGP
Announcement/ASN history)
- ipinfo.io & host.io
* e.g., `https://ipinfo.io/45.9.148.35`
* e.g., `https://host.io/edonerose.net`
- https://www.ipaddressguide.com/
* https://www.ipaddressguide.com/cidr
- https://dnslytics.com/
#### Misc
- https://osintframework.com/
- https://mxtoolbox.com/SuperTool.aspx
- https://centralops.net/co/
- https://network-tools.com/
- https://dnschecker.org/all-tools.php
- https://toolbox.googleapps.com/apps/main/
- Google dorks reference: https://pentestit.com/googledorks/
## Finish
### _Execute AOO; generate the desired effects for mission
accomplishment._

## Exploit
### _Gather information from the target that was previously
unavailable._
- exploiting URL shorteners: https://isc.sans.edu/diary/
Taking+Apart+URL+Shorteners/28980
* `curl -k -v -I [shortened_url] 2>&1 | grep -i "<
location"`
## Analyze

_Take stock of your newly acquired information and how it
fits into your old intel picture. Normalize the data;
identify trends & patterns; draw conclusions & gain new
insights. Generate new intelligence for follow-on ops._
- https://gchq.github.io/CyberChef/
* recipes: https://github.com/mattnotmax/cyberchefrecipes
- https://htmledit.squarefree.com/
- https://replit.com/languages/nodejs
- REGEX notes:
* testing/debugging:
1. https://regexr.com/
2. https://regex101.com/
* ID subdomains: `grep -e '\..*\.' -v`
* match IPv4 address: `([0-9]{1,3}[\.]){3}[0-9]{1,3}`
* match IPv4 address w/ explicitly-defined port:
`([0-9]{1,3}[\.]){3}[0-9]{1,3}:[0-9]{1,5}`
- `sed` usage examples:
* to delete blank lines and redirect output to a new
file (preserving the old one): `sed -r '/^\s*$/d'
input.file > output.file` (_example use-case_: there's a
blank line between entries because copy/paste from a
website includes an extra `\n`...)
* to convert URLs > domains: `sed -e 's|^[^/]*//||' -e
's|/.*$||'`
* to convert `curl` HTTP `\n` chars to _actual_
newlines: `sed 's/\\n/\n/g' [inputFile] > [outputFile]`
* to convert a list of domains separated by **SPACE**
to a list separated by **NEWLINE**: `cat [fileName] | sed
-E "s/[[:space:]]/\n/g" > [outputFile]`
### Splunk notes:
_(also see Kovar's github and "Hunting with Splunk: the
basics" links in #DISSEMINATE)_
- declaring relative time:
```
second s, sec, secs, second, seconds
minute m, min, mins, minute, minutes
hour h, hr, hrs, hour, hours
day d, day, days
week w, week, weeks
monthmon, month, months
quarter q, qtr, qtrs, quarter, quarters
year y, yr, yrs, year, years
```
- https://www.splunk.com/en_us/blog/tips-and-tricks/rexgroks-
gibberish.html?301=/blog/2017/08/30/rex-groksgibberish.
html
## Disseminate

### _Get the finished Intelligence product to the decision
-  makers: it must be timely, accurate, actionable, in a
format that enables efficient ingestion.

### Non-infosec
- Geopolitical context:
* https://www.internetexchangemap.com/
* https://www.cloudinfrastructuremap.com/
* https://www.submarinecablemap.com/
* https://www.submarinenetworks.com/en/systems
* https://www2.telegeography.com/submarine-cable-faqsfrequently-
asked-questions#Cable-101
- https://www.time.gov/
- https://publicsuffix.org/list/
- https://user-agents.net/
- https://developers.whatismybrowser.com/useragents/parse
- https://www.whatismyip.net/tools/user-agent-lookup.php
- https://github.com/mxm0z/awesome-intelligence-writing
- https://majestic.com/reports/majestic-million
- https://umbrella.cisco.com/blog/cisco-umbrella-1-million
- https://trends.netcraft.com/topsites
- https://bgpstream.crosswork.cisco.com/

#### CompSci & Networking 101
- https://en.wikipedia.org/wiki/
Category:Protocols_by_OSI_layer
- BGP:
- https://www.kentik.com/blog/the-mystery-of-as8003/
- https://www.juniper.net/documentation/us/en/software/
junos/bgp/topics/topic-map/bgp-overview.html#id-bgpmessages-
overview__d128e74
- https://tls.ulfheim.net/
- https://wiki.osdev.org/Expanded_Main_Page
- https://utcc.utoronto.ca/usg/technotes/smtp-intro.html
- [informative writeup on MOTW & Zone.Identifier Alternate
Data Stream](https://techcommunity.microsoft.com/t5/
microsoft-defender-for-endpoint/hunting-tip-of-the-monthbrowser-
downloads/ba-p/220454)
- https://www.speedguide.net/conversion.php

### Infosec
#### Context
- Threat Assessment considerations:
INTENT, CAPABILITY, AND OPPORTUNITY (+ Motivation*)
*note: Motivation != Intent; Intent can be constant
(e.g., constitutionally mandated foreign-focused SIGINT and
espionage would be "intent"); whereas Motivation can wax
and wane with the geopolitical climate (e.g., recent
sanctions activity may _increase_ Motivation vis-a-vis a
malicious actor w/ pre-existing intent).

- https://isc.sans.edu/
- https://dashboard.shadowserver.org/
- Team Cymru DNB
- RiskIQ Threat Intel Digest
- The Cyberwire
- https://threatconnect.com/blog/ingest-technical-blogsreports/
- [list of national CERT RSSs](https://github.com/
pulsedive/certrss)
- JARM & JA3/S:
* https://ja3er.com/
* https://github.com/salesforce/ja3/tree/master/
* https://github.com/cedowens/C2-JARM/

#### Defensive Tradecraft
##### Defensive Tooling Documentation:
- https://docs.zeek.org/en/master/logs/index.html
- VirusTotal:
* [Advanced Threat Hunting with VT](https://www.ccncert.
cni.es/pdf/documentos-publicos/xiv-jornadas-stic-ccncert/
ponencias-1/5500-s18-d30-03-adavanced-threat-huntingblack-
belt/file.html)
* VTI tags: https://support.virustotal.com/hc/en-us/
articles/360002160378-Full-list-of-VirusTotal-Intelligencetag-
modifier
* VT search modifiers: https://support.virustotal.com/
hc/en-us/articles/360001385897-File-search-modifiers
* VTI intro, performing file searches: https://
support.virustotal.com/hc/en-us/articles/360001387057
* Florian Roth's VTI-dorks repo: https://github.com/
Neo23x0/vti-dorks
* https://alparslanakyildiz.medium.com/virus-totalintelligence-
dorks-24d9a098bfb0
* examples from VT's blog series:
1. https://blog.virustotal.com/2022/11/threathunting-
with-virustotal.html
2. https://blog.virustotal.com/2022/08/deceptionat-
scale.html
3. https://blog.virustotal.com/2022/11/deceptionat-
scale-how-attackers-abuse.html
4. https://blog.virustotal.com/2020/02/uncoveringthreat-
infrastructure-via.html
* additional info re VTI tags & file metadata for Yara/
VTI: https://support.virustotal.com/hc/en-us/articles/
360007088057-Writing-YARA-rules-for-Livehunt
##### Security References & Tactical Guides
- https://s0cm0nkey.gitbook.io/s0cm0nkeys-security-reference-guide/
- https://www.sans.org/media/score/504-incident-response-cycle.pdf
- https://www.iblue.team/
- https://wiki.sans.blue/#!index.md
- https://github.com/Defenders-Guide/TheDefendersGuide
- https://kb.eventtracker.com/
- https://github.com/jsecurity101/Windows-API-To-Sysmon-Events
- https://www.sandflysecurity.com/linux-compromise-detection-command-cheatsheet.pdf
- https://orkl.eu/search
- https://www.vx-underground.org/
- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx
- https://learn.microsoft.com/en-us/windows-server/identity/securing-privileged-access/reference-tools-logon-types
- "30 cybersecurity search engines for researchers" -- https://archive.vn/cIDCV
##### Malicious Actors, TTPs, Tools
- https://aptmap.netlify.app/
- https://attack.mitre.org/
* ATT&CK `GROUPS` --> https://attack.mitre.org/groups/
* ATT&CK `TOOLS` --> https://attack.mitre.org/software/
- https://apt.etda.or.th/cgi-bin/aptgroups.cgi
- https://github.com/StrangerealIntel/EternalLiberty ("This
repository contains all Threat Actor aliases used by
different Threat Intelligence companies in their reports.")
- `Russian State-Sponsored and Criminal Cyber Threats to
Critical Infrastructure` --> https://www.cisa.gov/uscert/
ncas/alerts/aa22-110a
- Google Doc `APT Groups and Operations` --> https://
docs.google.com/spreadsheets/d/
1H9_xaxQHpWaa4O_Son4Gx0YOIzlcBWMsdvePFX68EKU/
edit#gid=1864660085
- https://www.gov.uk/government/publications/russias-fsbmalign-
cyber-activity-factsheet/russias-fsb-malignactivity-
factsheet
- https://valisluureamet.ee/doc/raport/2018-en.pdf
- https://www.secureworks.com/research/threat-profiles
- https://malpedia.caad.fkie.fraunhofer.de/
- https://www.vx-underground.org/
- https://github.com/ForensicArtifacts/artifacts
- https://jpcertcc.github.io/ToolAnalysisResultSheet/
- https://papers.vx-underground.org/papers/VXUG/Mirrors/
BassterlordNetworkingManual.pdf
- https://book.hacktricks.xyz/
- https://lots-project.com/
- https://lolbas-project.github.io/
- https://gtfobins.github.io/
- https://github.com/wietze/hijacklibs
- https://persistence-info.github.io/
- Microsoft updated TA naming crosswalk --> https://learn.microsoft.com/en-gb/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide
- https://aptmap.netlify.app/
- https://attack.mitre.org/
- ATT&CK GROUPS --> https://attack.mitre.org/groups/
- ATT&CK TOOLS --> https://attack.mitre.org/software/
- https://apt.etda.or.th/cgi-bin/aptgroups.cgi
- https://github.com/StrangerealIntel/EternalLiberty ("This repository contains all Threat Actor aliases used by different Threat Intelligence companies in their reports.")
https://app.tidalcyber.com/
- Russian State-Sponsored and Criminal Cyber Threats to Critical Infrastructure --> https://www.cisa.gov/uscert/ncas/alerts/aa22-110a
- Google Doc APT Groups and Operations --> https://docs.google.com/spreadsheets/d/1H9_xaxQHpWaa4O_Son4Gx0YOIzlcBWMsdvePFX68EKU/edit#gid=1864660085
- https://www.gov.uk/government/publications/russias-fsb-malign-cyber-activity-factsheet/russias-fsb-malign-activity-factsheet
- https://valisluureamet.ee/doc/raport/2018-en.pdf (mapping of Russian APTs to the state security apparatus)
- https://www.secureworks.com/research/threat-profiles
- https://malpedia.caad.fkie.fraunhofer.de/
- https://www.vx-underground.org/
- https://github.com/ForensicArtifacts/artifacts
- https://jpcertcc.github.io/ToolAnalysisResultSheet/
- https://papers.vx-underground.org/papers/VXUG/Mirrors/BassterlordNetworkingManual.pdf
- https://book.hacktricks.xyz/
- https://lots-project.com/
- https://lolbas-project.github.io/
- https://gtfobins.github.io/
- https://www.loldrivers.io/
- https://hijacklibs.net/ (curated list of DLL Hijacking candidates; see repo at https://github.com/wietze/hijacklibs)
- Https://persistence-info.github.io/
- https://github.com/bluscreenofjeff/Red-Team-Infrastructure-Wiki/blob/master/README.md#domain-fronting
- https://github.com/trickest/cve (POCs by CVE, year)
##### Doctrine, Policy, Strategy
- TrustedSec "Back To Basics" series
1. https://www.trustedsec.com/blog/back-to-basics-thetrustedsec-
guide-to-strong-cyber-hygiene/
2. https://www.trustedsec.com/blog/back-to-basics-thetrustedsec-
guide-to-strong-cyber-hygiene-part-2/
- https://www.cert.govt.nz/it-specialists/guides/
- https://www.cyber.gov.au/acsc/view-all-content/essentialeight
- https://www.iacdautomate.org/
- https://www.ncsc.gov.uk/information/logging-made-easy
- https://www.appliedincidentresponse.com/resources/
- https://docs.microsoft.com/en-us/security/compass/
incident-response-playbooks
- https://github.com/ThreatHuntingProject/ThreatHunting
- [Mandiant Linux Hardening Guide](https://
www.mandiant.com/sites/default/files/2022-03/wp-linuxendpoint-
hardening.pdf)
- https://media.defense.gov/2022/Mar/01/2002947139/-1/-1/0/
CTR_NSA_NETWORK_INFRASTRUCTURE_SECURITY_GUIDANCE_20220301.P
DF
- https://www.cisa.gov/free-cybersecurity-services-andtools
- https://github.com/infosecB/awesome-detection-engineering

#### Journals
- https://dl.acm.org/journal/dtrap
- https://offensivecyber.org/
- https://cyberdefensereview.army.mil/
- https://www.airuniversity.af.edu/AetherJournal/
#### Learning & Training
- https://github.com/RoseSecurity/Obfusc8ted
- https://portswigger.net/web-security
- https://github.com/stuxnet999/MemLabs
- openanalysis.net
#### Malicious Corpus
- online SaaS sandboxes/dynamic analysis engines (see
_Sandboxes/dynamic analysis engines_ from #FIND & #FIX)
- https://malshare.com/
- https://bazaar.abuse.ch/
- vxug
- https://digitalcorpora.org/
- https://mordordatasets.com/introduction.html
- https://www.netresec.com/?page=PcapFiles (PCAPs)
- Splunk Security Dataset Project @ https://live.splunk.com
/splunk-security-dataset-project
#### Misc GitHub repos
- https://github.com/GossiTheDog?tab=repositories
- malware sinkhole repos/lists:
- https://github.com/grettir/malware-sinkholes/blob/
master/malware_sinkholes.txt
- https://github.com/brakmic/Sinkholes
* based on Lesley Carhartt's list here --> https://
tisiphone.net/2017/05/16/consolidated-malware-sinkholelist/
- dDNS providers:
1. https://gist.github.com/jkeychan/
cd6172ec00f76d55476cf2e21a094c74
2. https://github.com/neu5ron/dynamic_dns_lists
- "Awesome Hacker Search Engines" --> https://github.com/
edoardottt/awesome-hacker-search-engines
- "Scanner User Agents" --> https://github.com/digininja/
scanner_user_agents/blob/main/list.json
- Cobalt Strike queries --> https://github.com/
MichaelKoczwara/Awesome-CobaltStrike-Defence
- "awesome-threat-intelligence" --> https://github.com/
hslatman/awesome-threat-intelligence#readme
- https://github.com/C3n7ral051nt4g3ncy/OSINT_Inceptionlinks
- https://github.com/cipher387/osint_stuff_tool_collection
- https://github.com/rkovar
* https://github.com/rkovar/dns_detection
- https://github.com/VetSec/awesome-infosec
- https://github.com/AndrewRathbun/DFIRArtifactMuseum
### Hall of Fame writeups:
- Lambert, John. "The Githubification of InfoSec" - 2019
DEC 08. https://medium.com/@johnlatwc/the-githubificationof-
infosec-afbdbfaad1d1
- Nickels, Katie `CTI 101 series on Medium -->`
1. Part I: https://medium.com/katies-five-cents/acyber-
threat-intelligence-self-study-planpart-
1-968b5a8daf9a
2. Part II: https://medium.com/katies-five-cents/acyber-
threat-intelligence-self-study-plan-part-2-
d04b7a529d36
- Sanders, Chris. "Information Security Mental Models" -
2019 MAY 29. https://chrissanders.org/2019/05/infosecmental-
models/
- Slowik, Joe. "Indicators and Network Defense" - 2018 MAY
16. https://pylos.co/2018/05/16/indicators-and-networkdefense/
- Slowik, Joe. "Analyzing Network Infrastructure as
Composite Objects" - 2020 NOV 18. https://
www.domaintools.com/resources/blog/analyzing-networkinfrastructure-
as-composite-objects/
- Slowik, Joe. "Formulating a Robust Pivoting Methodology"
- 2021. https://www.domaintools.com/wp-content/uploads/
formulating-a-robust-pivoting-methodology.pdf
- Slowik, Joe. "Developing an Intelligence-Driven Threat
Hunting Methodology" - 2022 SEP 02. https://
www.gigamon.com/content/dam/resource-library/english/whitepaper/
wp-intelligence-driven-threat-hunting-methodology.pdf
- Splunk (h/t Kovar); https://www.splunk.com/en_us/blog/
security/hunting-with-splunk-the-basics.html?301=/blog/
2017/07/06/hunting-with-splunk-the-basics.html
- https://github.com/BishopFox/sliver/wiki/DNS-C2


<!-- Markdeep: --><style class="fallback">body{visibility:hidden;white-space:pre;font-family:monospace}</style><script src="markdeep.min.js" charset="utf-8"></script><script src="https://morgan3d.github.io/markdeep/latest/markdeep.min.js" charset="utf-8"></script><script>window.alreadyProcessedMarkdeep||(document.body.style.visibility="visible")</script>