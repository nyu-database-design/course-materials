---
layout: presentation
title: MongoDB Aggregation
permalink: /slides/mongodb-aggregation/
---

class: center, middle

# MongoDB Aggregation

Database Design

---

# Agenda

1. [Overview](#overview)
1. [Example Data Set](#data-set)
1. [Basics](#sanity-check)
1. [Aggregation](#aggregation)
1. [Conclusions](#conclusions)

---

name: overview

# Overview

--

## Concept

Lorem ipsum.

---

name: data-set

# Example Data Set

--

## Save the data file

This set of slides use data about [NYC city government jobs](https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t), sourced from the [official government jobs site](http://www.nyc.gov/html/careers/html/search/search.shtml). To follow along, export the data into a CSV file named [NYC_Jobs.csv](../files/mongodb/NYC_Jobs.csv).

```javascript
Job ID,Agency,Posting Type,# Of Positions,Business Title,Civil Service Title,Title Classification,Title Code No,Level,Job Category,Full-Time/Part-Time indicator,Career Level,Salary Range From,Salary Range To,Salary Frequency,Work Location,Division/Work Unit,Job Description,Minimum Qual Requirements,Preferred Skills,Additional Information,To Apply,Hours/Shift,Work Location 1,Recruitment Contact,Residency Requirement,Posting Date,Post Until,Posting Updated,Process Date
415211,DEPARTMENT OF CORRECTION,External,1,Data Analyst,CITY RESEARCH SCIENTIST,Non-Competitive-5,21744,02,"Technology, Data & Innovation Policy, Research & Analysis",F,Experienced (non-manager),73305,84301,Annual,75-20 Astoria Blvd,Information Systems-Admin,"The New York City Department of Correction (DOC) is an integral part of the Cityâs evolving criminal justice system, participating in reform initiatives and strategies aimed to move the City towards the smallest jail system possible without compromising public safety. The DOC is solely responsible for maintaining a safe and secure environment for staff, visitors, volunteers and people in custody inside our jails. Importantly, safe jails enable DOC to providing people in custody with the tools and opportunities they need to successfully re-enter their communities. The DOC operates facilities and court commands across the five boroughs with over 12,000 diverse professionals and knowledge experts.  The DOC seeks to recruit a Data Analyst, to assist with all of the aspects of the Data Analytics and Research Unit. Under the direct supervision of the Director of Data Analytics and Research Unit; the selected candidate will be responsible for supporting the analytic and research efforts of the department to further policy, planning and strategic initiatives, including but not limited to:  â¢	Supporting quantitative analytic and research projects related to program and policy evaluation;  â¢	Providing technical assistance to units throughout the Department in analysis and reporting;  â¢	Analyzing databases to assess accessibility and accuracy and identifying    opportunities for new data sources;  â¢	Performing and automating ad hoc requests and recurring reports;  â¢	Identifying areas of concern and developing strategies to correct deficiencies or problems;  â¢	Developing tools and methods to support reproducible and automated reports and analyses.","1.  For Assignment Level I (only physical, biological and environmental sciences and public health) A master's degree from an accredited college or university with a specialization in an appropriate field of physical, biological or environmental science or in public health.  To be appointed to Assignment Level II and above, candidates must have:  1. A doctorate degree from an accredited college or university with specialization in an appropriate field of physical, biological, environmental or social science and one year of full-time experience in a responsible supervisory, administrative or research capacity in the appropriate field of specialization; or  2. A master's degree from an accredited college or university with specialization in an appropriate field of physical, biological, environmental or social science and three years of responsible full-time research experience in the appropriate field of specialization; or  3. Education and/or experience which is equivalent to 1 or 2 above. However, all candidates must have at least a master's degree in an appropriate field of specialization and at least two years of experience described in 2 above. Two years as a City Research Scientist Level I can be substituted for the experience required in 1 and 2 above.    NOTE:  Probationary Period  Appointments to this position are subject to a minimum probationary period of one year.","â¢	Applied knowledge of R, Python, and related applications/languages; familiarity with SPSS, Stata  â¢	Practical experience with Tableau and SQL (applications and scripting)  â¢	Proficiency Microsoft Office Suite (PowerPoint, Word, Excel, Outlook, Access etc.)  â¢	Knowledge of research concepts, processes, and applied statistics  â¢	Research, reporting, and analytic experience within NYC government setting  â¢	Excellent writing, communication, interpersonal, research, problem-solving, and organizational skills  â¢	Demonstrated ability to initiate and manage complex and interdisciplinary projects; think creatively,    embrace new approaches; prepare and deliver informative and well-organized presentations  â¢	Experience in a high paced environment, with the ability to manage information and distribute    appropriately.",,For City employees: Go to Employee Self-Service (ESS) - www.nyc.gov/ess and search for Job ID# 415211  For all other applicants: Go to https://a127-jobs.nyc.gov and search for Job ID# 415211  Submission of a resume is not a guarantee that you will receive an interview.,,,,"New York City residency is generally required within 90 days of appointment. However, City Employees in certain titles who have worked for the City for 2 continuous years may also be eligible to reside in Nassau, Suffolk, Putnam, Westchester, Rockland, or Orange County. To determine if the residency requirement applies to you, please discuss with the agency representative at the time of interview.",10/02/2019,,02/07/2020,03/23/2021
435648,TAXI & LIMOUSINE COMMISSION,Internal,1,Programs Data Manager,COMMUNITY COORDINATOR,Non-Competitive-5,56058,00,"Policy, Research & Analysis",F,Experienced (non-manager),54100,83981,Annual,"33 Beaver St, New York Ny",Programs & Operations,"The New York City Taxi and Limousine Commission (TLC) establishes and enforces professional and uniform standards of for-hire transportation service and ensures public safety. TLC licenses and regulates all aspects of New York Cityâs medallion (yellow) taxicabs, for-hire vehicles (Boro Taxis, community-based liveries, black cars, including app-based services, and luxury limousines), commuter vans, and paratransit vehicles. With over 115,000 licensed vehicles and approximately 170,000 drivers, TLC is the most active taxi and limousine licensing regulatory agency in the United States. To learn more about the TLC, please visit: www.nyc.gov/taxi.  Under the leadership of the Director of Programs, this position will manage quantitative, data projects for the agencyâs programs. This position will interface across all internal divisions, including Management Information Systems (MIS), Legal, Fiscal/Accounting, Licensing and Policy, as well as with partner agencies, TLC licensees, and vendors. A successful candidate has a strategic lens and an ability to anticipate oncoming program and data challenges. The candidate must have a background in using large data sets to manage public funds. Responsibilities may include but are not limited to:   â¢	Project planning and implementation: develop work plans and timelines for data projects, identify milestones, complete tasks, and manage projects to completion, working closely with program managers and project analysts. â¢	New project development: work with the Director of Programs to develop a programs data agenda, identify new research topics, and explore opportunities for collaboration on data and reporting. â¢	Programs policy research: design and perform quantitative and qualitative research projects using program data, which may include financial modeling, industry trend analysis, literature review, and conducting outreach and focus groups with driver and owner communities. â¢	Programs policy development: participate in planning and problem-solving sessions, work with key staff and stakeholders to seek feedback on policy ideas, and develop requirements. â¢	Overall support: writing reports and policy memos, researching initiatives, preparing PowerPoint presentations, giving presentations to the Commission, licensees, and members of the general public, meeting planning and management, managing day-to-day relationships and communications with industry stakeholders, and taking an active role in supporting the activities of the agency. Respond to telephone and correspondence requests for information.","1. A baccalaureate degree from an accredited college and two years of experience in community work or community centered activities in an area related to the duties described above; or  2. High school graduation or equivalent and six years of experience in community work or community centered activities in an area related to the duties as described above; or  3. Education and/or experience which is equivalent to 1 or 2 above. However, all candidates must have at least one year of experience as described in 1 above.","Candidates should be highly motivated and able to work well independently and as part of a team. Interested candidates should have excellent written and verbal communication skills, effective problem-solving and analytic skills, and the ability to prioritize, manage time, and engage in multiple tasks in a fast-paced environment.   Ability to analyze and manipulate data is a must. Demonstrated experience analyzing and manipulating data using Access/SQL queries and R/Python models is strongly desired.  Although not required, the successful applicant will likely have one or more of the following academic or professional experiences: urban planning, transportation policy, public administration, public policy, business, economics, statistics, political science, environmental studies, or in a related degree program. B.A. or B.S. required. Project management experience (especially management of research projects) strongly desired.",,"Click, APPLY NOW Current city employees must apply via Employee Self-Service (ESS)",,"33 Beaver St, New York Ny",,"New York City residency is generally required within 90 days of appointment. However, City Employees in certain titles who have worked for the City for 2 continuous years may also be eligible to reside in Nassau, Suffolk, Putnam, Westchester, Rockland, or Orange County. To determine if the residency requirement applies to you, please discuss with the agency representative at the time of interview.",02/27/2020,,02/27/2020,03/23/2021
458782,CONSUMER AFFAIRS,Internal,1,Community Affairs Associate,COMMUNITY COORDINATOR,Non-Competitive-5,56058,00,Communications & Intergovernmental Affairs Legal Affairs,F,Experienced (non-manager),54100,62215,Annual,"42 Broadway, N.Y.",External  Affairs,"Job Description The NYC Department of Consumer Affairs (DCA) protects and enhances the daily economic lives of New Yorkers to create thriving communities. DCA licenses more than 81,000 businesses in more than 50 industries and enforces key consumer protection, licensing, and workplace laws that apply to countless more. By supporting businesses through equitable enforcement and access to resources and, by helping to resolve complaints, DCA protects the marketplace from predatory practices and strives to create a culture of compliance. Through its community outreach and the work of its offices of Financial Empowerment and Labor Policy & Standards, DCA empowers consumers and working families by providing the tools and resources they need to be educated consumers and to achieve financial health and work-life balance. DCA also conducts research and advocates for public policy that furthers its work to support New York Cityâs communities. For more information about DCA and its work, call 311 or visit DCA at nyc.gov/dca or on its social media sites, Twitter, Facebook, Instagram and YouTube. External Affairs (âEAâ) is the intergovernmental division of the agency and custodian of DCAâs relationship with City Hall, elected officials, government entities, community and faith-based organizations, and stakeholders with broad policy and public affairs jurisdiction. EA is responsible for these relationships to ensure that the agency speaks with a singular and consistent voice to officials and entities that have touchpoints across DCAâs wide jurisdiction. EA is seeking an individual pursuing a career in public relations, government relations, community relations, or related fields to serve as a Community Affairs Associate. Under the supervision of the Director of Community Affairs the Community Affairs Associate will work with colleagues to advance the agencyâs work in consumer and worker protection and education. All candidates should have a strong academic record, be highly organized with a keen attention to detail, possess the ability to manage multiple tasks and most importantly have a commitment to excellence. Responsibilities will include, but are not be limited to: â¢ Develop and maintain external relationships with elected officials, government agencies, industry and community stakeholders, and members of the public; â¢ Accurately and concisely represent the work and policies of the agency in an engaging manner; â¢ Coordinate event logistics, locations, materials, staffing, and trainings; â¢ Effectively link with other departmental divisions to ensure project success; â¢ Work closely with colleagues to help inform the Director of Community Affairs and Executive Director for External Affairs in their formulation and implementation of outreach strategies; and â¢ Provide administrative support and assist in special or ad-hoc projects as needed.","1. A baccalaureate degree from an accredited college and two years of experience in community work or community centered activities in an area related to the duties described above; or  2. High school graduation or equivalent and six years of experience in community work or community centered activities in an area related to the duties as described above; or  3. Education and/or experience which is equivalent to 1 or 2 above. However, all candidates must have at least one year of experience as described in 1 above.","Preferred Skills â¢ Experience cultivating partnerships with local community stakeholders; â¢ Ability to successfully manage multiple tasks simultaneously; â¢ Attention to detail and ability to work quickly under pressure; â¢ Excellent written and oral communication skills; â¢ Proficiency in Microsoft Office, major internet search engines and databases; â¢ Aptitude to quickly learn new computer programs and technology; â¢ Ability to capture and analyze data; â¢ Ability to understand laws and rules; â¢ Multilingual capacity (Spanish or Mandarin) a plus; â¢ Driverâs license a plus; â¢ Flexibility in hours.",,"To Apply For Non-City/External Candidates: Visit the External Applicant NYC Careers site and type âConsumer Affairsâ on the search line. Then locate the Job ID number. For Current City Employees: Visit Employee Self Service (ESS) to view and click on Recruiting Activities, Careers, and search by Job ID number. A RESUME AND COVER LETTER ARE REQUIRED. PLEASE INDICATE IN YOUR COVER LETTER HOW YOU HEARD ABOUT THIS POSITION. INCOMPLETE APPLICATIONS WILL NOT BE CONSIDERED.  NO PHONE CALLS, FAXES, E-MAILS OR PERSONAL INQUIRIES PERMITTED. NOTE: ONLY THOSE CANDIDATES UNDER CONSIDERATION WILL BE CONTACTED.  *Appointments are subject to Office of Management and Budget (OMB) approval.  *55-a Candidates: NYC Department of Consumer Affairs is committed to recruiting and retaining a diverse and culturally responsive workforce. We strongly encourage 55-A candidates to apply to our positions in order to be given the opportunity.  **LOAN FORGIVENESS: The federal government provides student loan forgiveness through its Public Service Loan Forgiveness Program (PSLF) to all qualifying public service employees. Working with DCA qualifies you as a public service employee and you may be able to take advantage of this program while working full-time and meeting the programâs other requirements. Please visit the Public Service Loan Forgiveness Program site to view the eligibility requirements: https://studentaid.ed.gov/sa/repay-loans/forgiveness-cancellation/public-service",,,,"New York City residency is generally required within 90 days of appointment. However, City Employees in certain titles who have worked for the City for 2 continuous years may also be eligible to reside in Nassau, Suffolk, Putnam, Westchester, Rockland, or Orange County. To determine if the residency requirement applies to you, please discuss with the agency representative at the time of interview.",02/25/2021,26-APR-2021,02/25/2021,03/23/2021
458064,NYC HOUSING AUTHORITY,Internal,1,Deputy Director Records Management,ADMINISTRATIVE PUBLIC RECORDS,Competitive-1,10041,M3,"Legal Affairs Policy, Research & Analysis",F,Manager,72038,192152,Annual,Records Management,VP of Compliance,"The New York City Housing Authority (NYCHA) is the nationâs largest public housing authority, with an operating budget of $3.3 billion and over 11,000 employees who manage and maintain 302 developments that house about 400,000 residents.  NYCHA also operates the countryâs largest Section 8 program, which provides rental assistance to about 200,000 additional people.  Reporting to the Vice President in the Compliance Department, the Deputy Director for the Records Management Office is responsible for work relating to the overall management, planning and operation of an archival or records management program or in an information science and library management program; or other assignments equivalent to that described herein.  Responsibilities include, but are not limited to the following:  â¢	Direct a unit responsible for significant policy implementation.  Supervise a staff of nine (9) and assist with day-to-day records storage, retention, and retrieval management responsibilities and notify the Vice President and/or Chief Compliance Officer when/if issues arise that require senior management intervention. â¢	Draft policies and procedures related to record retention. â¢	Categorize and disseminate descriptive guides to records, collections, and other significant historical documents. â¢	Permanently preserve records and related materials having historical, research, cultural or other important value; or develop and/or review and evaluate general and specialized professional library programs of considerable scope and complexity; or other assignments equivalent to that described herein. â¢	Evaluate current internal controls built around records storage, records retention, and records retrieval to ensure that processes are efficient, sufficient, and have the appropriate levels of approval from departments throughout the authority. â¢	Advise and make recommendations to the agencyâs Chief Compliance Officer and other executive staff on questions of law, fact and administrative policy. â¢	Perform complex computerized research, enter data and generate reports using custom databases. â¢	Collaborate with business liaisons from designated departments to develop and implement a records retention schedule.  Ensure that affected parties follow governing agency rules, regulations and guidelines as it relates to records storage and retention.  â¢	Assist in responding to audits and other external compliance reviews of NYCHA.  NOTE:  IF THIS APPOINTMENT IS MADE ON A PROVISIONAL BASIS PURSUANT TO Â§65 OF THE NYS CIVIL SERVICE LAW, NO TENURE OR PERMANENCE ACCRUES TO AN INCUMBENT IN THIS POSITION BY VIRTUE OF SUCH APPOINTMENT.   NOTE:  This position is open to qualified persons with a disability who are eligible for the 55-a Program.  Please indicate in your cover letter that you would like to be considered for the position under the 55-a Program.  For detailed information regarding the 55-a Program, please visit the following link:  http://www.nyc.gov/html/dcas/downloads/pdf/psb/100_1.pdf   Please read this posting carefully to make certain you meet the qualification requirements before applying to this position.","Qualification Requirements  1. A master's degree from an accredited college in Library Science, Archival Science, American History or Political Science or a related area, plus four years of full-time professional experience in a governmental archives, records management center or library complex, 18 months of which must have been in a supervisory, administrative, consultative, managerial or executive capacity; or    2. Education and/or experience equivalent to 1 above. However, all candidates must have a master's degree and the 18 months supervisory, administrative, consultative, managerial or executive experience as described in 1 above.","1.	7 â 10 years effectively managing a records management program. 2.	Extensive research and writing skills with ability to communicate in different styles and to varied audiences (e.g., memoranda, policies, abstracts, manuscripts, grants, proposals, protocols, presentations, outreach materials, and social media). 3.	Excellent interpersonal and conflict resolution skills. 4.	Ability to manage relationships, balance competing priorities, and manage up and down. 5.	Experience managing high-priority projects and tracking project life-cycles. 6.	Experience working collaboratively to develop and execute project plans. 7.	Ability to make timely and effective decisions and produce results through strategic planning. 8.	Excellent communication skills with ability to engage and facilitate cooperation among multiple stakeholders. 9.	Experience managing vendors. 10.	Firm working knowledge of Microsoft Word, Excel, Outlook, PowerPoint, and Publisher. 11.	Project management skills with experience in managing and supervising administrative projects.  Familiarity with Smartsheet, Basecamp, Lucidchart, Visio, and Projects.","1.	NYCHA employees applying for promotional, title or level change opportunities must have served a period of one year in their current title and level (if applicable). 2.	NYCHA residents are encouraged to apply.",Click the Apply Now button.,,,,NYCHA has no residency requirements.,02/09/2021,,02/09/2021,03/23/2021
458663,PRESIDENT BOROUGH OF MANHATTAN,External,1,Information Technology Manager,COMPUTER SYSTEMS MANAGER,Competitive-1,1005D,00,"Technology, Data & Innovation",F,Experienced (non-manager),80000,100000,Annual,"1 Centre St., N.Y.",Administration,"Please Note: Only candidates serving permanently in the title of Computer Systems Manager or have passed the latest Computer Systems Manager exam (# 9011) and be reachable for appointment from the resulting list will be considered for the position.   Manhattan Borough President Gale A. Brewer seeks an Information Technology Manager to be part of her energetic and collaborative Operations team.  The position reports to the Director of Human Resources and Operations.  The person in this position is responsible for the management of the computers, printers and telephone system within the two locations of the Manhattan Borough Presidentâs Office.   This is a hands-on position that requires the candidate to have demonstrated successful skills in working in a LAN/WAN environment. This is a one-person shop. The IT Manager will provide help desk support to staff, as well as monitor network performance, including software, hardware, power, and communications; work with consultants, vendors and with the Cityâs Department of Information Technology and Telecommunications (DoITT), the Citywide IT agency -- to which our network is connected and through which we receive our Internet connection -- to ensure that the network is secure; troubleshoot problems with the network and with desktop software, including maintaining security updates for operating system desktop software and security-specific software, such as McAfee and CrowdStrike; coordinate with DoITT for the implementation and use of all Internet, Intranet and Extranet activities; monitor, troubleshoot and upgrade our office Internet connection and WiFi from third parties such as Spectrum on a separate internal network that is retained to provide City Charter-mandated live streaming of meetings that are hosted by and held in the office; work with DoITT to connect to City-provided WiFi for access to online video meetings (for example, Zoom, WebEx).  The IT Manager will also be responsible for: the performance of desktop computers and peripherals; maintain inventory of IT desktop and network equipment; liaison with outside vendors regarding the maintenance and security of our Cisco switches; research problems or errors within the networking system and subsystems; documenting all facets of the IT network operations; recommending and making necessary improvements to network configurations to achieve operating efficiencies; and performing all other duties as assigned. Required familiarity with the Microsoft Office Suite and Microsoft 365; PC hardware/software, desktop and laptop network configuration connectivity troubleshooting, including DHCP, and DNS configurations; some familiarity with Windows Server.  This position will also be responsible for monitoring and troubleshooting the VoIP telephone connections.  In addition, the office has a number of MacBooks and iMacs for which this position will need to provide support in conjunction with DoITTâs Apple Support Team.","1. A master's degree in computer science from an accredited college or university and three (3) years of progressively more responsible, full-time, satisfactory experience in Information Technology (IT) including applications development, systems development, data communications and networking, database administration, data processing, or user services. At least eighteen (18) months of this experience must have been in an administrative, managerial or executive capacity in the areas of applications development, systems development, data communications and networking, database administration, data processing or in the supervision of staff performing these duties; or  2. A baccalaureate degree from an accredited college or university and four (4) years of progressively more responsible, full-time, satisfactory experience as described in 1 above; or  3. A four-year high school diploma or its educational equivalent, and six (6) years of progressively more responsible, full-time, satisfactory experience as described in 1 above; or  4. A satisfactory combination of education and experience equivalent to 1, 2 or 3 above. However, all candidates must have at least a four-year high school diploma or its educational equivalent and must possess at least three (3) years of experience as described in 1 above, including the eighteen (18) months of administrative, managerial, executive or supervisory experience as described in 1 above.   In the absence of a baccalaureate degree, undergraduate credits may be substituted for a maximum of two (2) years of the required experience in IT on the basis of 30 semester credits for six (6) months of the required experience. Graduate credits in computer science may be substituted for a maximum of one (1) year of the required experience in IT on the basis of 30 graduate semester credits in computer science for one (1) year of the required IT experience. However, undergraduate and/or graduate credits may not be substituted for the eighteen (18) months of experience in an administrative, managerial, executive, or supervisory capacity as described in 1 above.","â¢	Experience with Microsoft Windows Server and Microsoft Office Suite. MCSE certification a plus. Four to six yearsâ experience in the installation and support of LAN and WAN technologies required. Experience in training end-users is required.  â¢	Experience with CISCO routers and firewalls, 3COM switches, and related protocols.  Experience with installing, troubleshooting, and maintaining Server and Desktop computer configurations. Administering a BES server and related devices. Strong organizational skills required.  â¢	Experience required in network design, deployment and troubleshooting. Capable of delivering summary reports of network analysis, including security audits, hardware/software patch updates, and network monitoring; good research and consulting skills necessary; capable of leading meetings and giving presentations to customers; responsible for performing network architecture reviews, developing detailed implementation plans and detailed engineering packages for site implementations. Good documentation skills are a must. 5-7 yrs of network engineering/administration/management, 3-5 yrs LAN/WAN design, 3-5 yrs Cisco LAN/WAN router/switch/hub configuration and troubleshooting skills; excellent written/verbal communication skills; and capable of extensive interaction with team members, program managers and clients.   â¢	Skilled in project planning, performance analysis and fault management; self-motivated; close interaction with users - must be a team player; results oriented and able to respond quickly; timeliness of response to service requests and thoroughness in problem solving required; professional, courteous handling of employee requests, âCustomer Serviceâ attitude; excellent analytical, problem-solving and communication skills.",,Please Note: Only candidates serving permanently in the title of Computer Systems Manager or have passed the latest Computer Systems Manager exam (# 9011) and be reachable for appointment from the resulting list will be considered for the position.   1.	Email a cover letter and resume to resumes@manhattanbp.nyc.gov with  Information Technology Manager  in the subject line AND 						  2.     Apply to this posting,,,,New York City Residency is not required for this position,02/23/2021,,02/23/2021,03/23/2021
```

---

template: data-set

## Saving the data file to a web server

If you typically connect to the MongoDB database server from a web server, such as **i6** , it's easy to upload the data file to the web server using a Secure File Transfer (SFTP) application like [Cyberduck](https://cyberduck.io/).

![Cyberduck login](../files/mongodb/cyberduck.png)

---

template: data-set

## Setting up the environment on the i6 web server

On **i6**, to import the data file into a MongoDB databae collection, first go to the UNIX/Linux command line from where you typically connect to a MongoDB database, navigate to whichever folder you saved the data file into, and issue the following commands to set up the environment:

```bash
export LC_ALL=en_US.UTF-8
module load mongodb-3.2.0
```

- If you have already entered these commands into your account's `.bashrc` settings file, then you do not need to re-enter them from the command line.

---

template: data-set

## Import the data into MongoDB

Import the CSV data file into a MongoDB collection named `jobs`:

```bash
mongoimport --headerline --type=csv --host=database_host --db=your_database_name --collection=jobs --file=./NYC_jobs.csv --username=your_username --password=your_password
```

--

- this assumes the `NYC_Jobs.csv` file is located within the current working directory.

--

- replace `database_host`, `your_database_name`, `your_username`, and `your_password` with the correct credentials.

--

- if you are running a local MongoDB sever on your own machine, you can remove the `--db=your_database_name` part of the command.

---

name: sanity-check

# Basics

--

## Connect to the database

Before going into aggregation, let's check basic queries on the database to ensure they produce the expected results.

--

```bash
mongo your_database_name --host database_host -u your_username -p
```

- replace `your_database_name`, `database_host`, and `your_username` with the correct credentials.

--

- you will be asked to supply your MongoDB password... enter it when asked.

--

- if running a MongoDB server locally on your own machine, you do not need to supply these credentials.

---

template: sanity-check

## View a list of collections

Let's verify that a `jobs` collection has indeed been created in the database.

--

- select the correct database on this database server where `your_database_name` is replaced with the correct database name:

```mongodb
use your_database_name
```

--

- show a list of all the collections within the selected database:

```mongodb
show collections
```

--

- you should see the `jobs` collection listed.

---

template: sanity-check

## Retrieve and counting documents

Let's try a few simple retrievals of documents from the `jobs` collection.

--

- Retrieve just one document:

```javascript
db.jobs.findOne();
```

--

Retrieve `10` documents:

```javascript
db.jobs.find().limit(10);
```

--

Retrieve all documents:

```javascript
db.jobs.find();
```

--

Count documents in the result set:

```javascript
db.jobs.find().count();
```

---

template: sanity-check

## Find distinct values

The `db.collection.distinct()` function allows us to retrieve distinct values for a given field.

--

- find the distinct values in the `Agency` field:

```javascript
db.jobs.distinct("Agency");
```

--

- find the distinct values in the `Full-Time/Part-Time indicator` field:

```javascript
db.jobs.distinct("Full-Time/Part-Time indicator");
```

---

template: sanity-check

## Sorting results

The `db.collection.find().sort()` function sorts results. For example, sort all documents by the `Job ID` field, and show just the top `3` results, and show the documents in a pretty format.

```javascript
db.jobs.find().sort({ "Job ID": 1 }).limit(3).pretty();
```

--

- same as above, but only retrieve the `Job ID`, `Agency`, and `Business Title` fields:

```javascript
let fields = { _id: 0, "Job ID": 1, Agency: 1, "Business Title": 1 };
db.jobs.find({}, fields).sort({ "Job ID": 1 }).limit(3).pretty();
```

--

- same as above, but only retrieve documents that have `POLICE DEPARTMENT` in the `Agency` field, with no limit.

```javascript
let filter = { Agency: "POLICE DEPARTMENT" };
db.jobs.find(filter, fields).sort({ "Job ID": 1 }).pretty();
```

---

template: sanity-check

## Sorting results (continued)

Let's put our database skills to good use and find the `20` top-paying jobs in city government:

--

```javascript
let fields = {
  _id: 0,
  "Job ID": 1,
  "Business Title": 1,
  "Posting Date": 1,
  "Salary Range To": 1,
};

let orderBy = { "Salary Range To": -1 };
db.jobs.find({}, fields).sort(orderBy).limit(20).pretty();
```

--

- we have used a **projection** to limit the retrieved fields to the `Job ID`, `Business Title`, `Posting Data`, and `Salary Range To`.

---

name: aggregation

# Aggregation

--

## Concept

As with relational SQL databases, MongoDB supports aggregate functions and grouping of data. There are a few ways to do this in MongoDB.

--

- Aggregation pipeline

--

- Single purpose aggregation operations

--

- Map-reduce

--

We will focus on the **aggregation pipeline** technique.

---

template: aggregation

## Aggregation pipeline

The aggregation pipeline is a multi-stage process that transforms documents into an aggregated result.

--

- the stages and order of execution are determined by the user

--

- the output from one stage becomes the input for the next stage

--

To start an aggregation, we call the `aggregate()` function on a collection:

```javascript
db.collection.aggregate();
```

---

template: aggregation

## Aggregation pipeline (continued)

Into the `db.collection.aggregate()` function, we pass in an array containing a sequence of aggregation pipeline stages. These stages could include:

--

- `$match` - to filter documents by criteria

--

- `$count` - to count the number documents at this stage

--

- `$project` - to calculate or select particular fields

--

- `$group` - to group documents by a common attribute

--

These pipeline **stages** have counterparts in the simple MongoDB `db.collection.find()` function queries - the criteria argument, `count()` function, the projection, and so on.

--

- Using these special aggregation pipeline stage operators, instead of the regular features of a `find()` function call, allows them to be piped or chained together, so that the input of one becomes the output of another.

---

template: aggregation

## Aggregation pipeline (continued again)

There are more aggregation pipeline stage operators, although these are less often used.

--

- `$addFields` (similar to $project)

--

- `$bucket` - binning values

--

- `$sample` - to select a random number of documents from its input

--

- `$sort` - to sort results within a pipeline

--

- `$limit` - to limit results within a pipeline

--

A full list of aggregation pipeline operators is available in [the docs](https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/).

---

template: aggregation

## "$fieldName" Syntax

You'll often see syntax that looks like `"$fieldName"` - a field name prefixed with dollar, and quoted as a string.

--

These dollar filed names represent the value at that `fieldName`.

--

- this syntax differentiates this from a hardcoded value.

--

- for example `{fieldName: "foo"}` is different from `{fieldName: "$foo"}`

--

- the first sets the value to exactly `"foo"`, but the second sets the value to whatever is contained in the field named `foo`

---

template: aggregation

## $match

The `$match` operator filters documents in the pipeline. Here is the operator unattached to any particular pipeline.

```javascript
{
  $match: {
    city: "Brooklyn";
  }
}
```

--

- the value to assign the `$match` field is a query object, like in regular `find()` queries.

---

template: aggregation

## $count

As the name implies, `$count` counts the number of documents incoming from the previous stage.

```javascript
{
  $count: "countPolicyAnalysts";
}
```

--

For example, if the `$match` and `$count` operators were placed within a pipeline, it might look like:

```javascript
db.jobs.aggregate([
  { $match: { "Business Title": "Policy Analyst" } },
  { $count: "countPolicyAnalysts" },
]);
```

---

template: aggregation

## $project

The `$project` stage can modify the shape of a document by adding, suppressing and calculating fields.

--

- think of this as the `SELECT` list in SQL (where you can choose columns, create calculated columns, etc.)

--

- the value is a document that contains specifications for the transformations to be applied. It can contain:

--

    - `fieldName` or `_id` as `1`, `true`, `0`, `false` for inclusion and suppression
    - `fieldName` as an expression

--

For example,

```javascript
let fields = { _id: 0, "Job ID": 1, "Business Title": 1 };
db.jobs.aggregate([{ $project: fields }]);
```

---

template: aggregation

## $project (continued)

For example, uppercasing a field called business title →

```javascript
let projection = {
  _id: 0,
  "Job ID": 1,
  title: { $toUpper: "$Business Title" },
};
db.jobs.aggregate([{ $project: projection }]);
```

---

template: aggregation

## $project (continued again)

For example, combining `$match` and `$project` to show jobs that have "External" Posting Type with a subset of fields.

--

First, a projection for only the fields `Job ID`, `Posting Type` as `ptype`, and an uppercased `Business Title` as `title`:

```javascript
var projection = {
  _id: 0,
  "Job ID": 1,
  ptype: "$Posting Type",
  title: { $toUpper: "$Business Title" },
};
```

--

Pipe the external job postings to this projection:

```javascript
db.jobs.aggregate([
  { $match: { "Posting Type": "External" } },
  { $project: projection },
]);
```

---

template: aggregation

## More operators

Because a projection can result in calculated fields, there are a [large number of aggregation pipeline operators](https://docs.mongodb.com/manual/reference/operator/aggregation/) for manipulating strings, dates, performing simple arithmetic, etc.

--

Some examples:

--

- `$convert` to convert from one type to another: {$convert: {input: "$fieldName", to: "int"}}

--

- `$split` to break up a string into an array of substrings using some delimiter: {$split: ["$fieldName", ","]}

--

- `$substrCP` to extract a substring from another string by code point: {$substrCP: ["$fieldName", 0, 4]} // first three characters

---

template: aggregation

## More operators (continued)

Additional operations… and expressions, include:

--

- `$add`, `$subtract`, `$divide`, and `$multiply`, etc.

--

- e.g.

```javascript
{
  $subtract: ["$field1", "$field2"]; // i.e. field1 - field2
}
```

--

and [many more](https://docs.mongodb.com/manual/reference/operator/aggregation/), like `$toUpper`, `$trim`, `{$arrayElemAt: someArray, someIndex}`, etc.

--

- Note that in most cases, the values can be arbitrary expressions that are: values at fields (e.g. `"$fieldName"`), a hardcoded value (e.g. `5`) or even the result of another operation (e.g. `{ $op: [arg1, arg2] }`)

---

template: aggregation

## $group

The `$group` operator creates distinct groups as separate documents.

--

- similar to `GROUP BY` in SQL

--

```javascript
// counts the number of documents per Agency
{$group: {
  _id: "$Agency",
  listingCount: {$sum: 1}
}}
```

--

- The `_id` value is the field to group by, prefixed with a dollar sign `$`, and surrounded by quotes.

--

- the second field is given a value that is the aggregate operation to perform on each group.

--

- there is a [long list of aggregate operators](https://docs.mongodb.com/manual/reference/operator/aggregation/group/#accumulators-group), similar to those in SQL, including `$sum`, `$avg`, `$min`, `$max`, `$stdDevSamp`, and more.

---

name: pipeline-examples

# Pipeline Examples

---

template: pipeline-examples

## Match only

Filter such that the minimum `Salary Range From` in our results is $200,000:

```javascript
let min_from = { $match: { "Salary Range From": { $gt: 200000 } } };

db.jobs.aggregate([min_from]);
```

--

- A one-stage filter like this could easily have been done using just `db.collection.find()`, without a pipeline.

---

template: pipeline-examples

## Match and project

For all positions that are paid annually (see `Salary Frequency`), show the top `10` positions that have the largest range of possible salaries.

```javascript
let salaryGap = { $subtract: ["$Salary Range To", "$Salary Range From"] };

let fields = {
  $project: {
    _id: 0,
    "Business Title": 1,
    "Salary Gap": salaryGap,
  },
};

let annualExternal = {
  $match: {
    "Salary Frequency": "Annual",
    "Posting Type": "External",
  },
};

let sortGapDesc = { $sort: { "Salary Gap": -1 } };

db.jobs.aggregate([annualExternal, fields, sortGapDesc, { $limit: 10 }]);
```

---

template: pipeline-examples

## Match, project, and match

Same as previous example, but only show the positions where the salary range is lower than $5,000, but not $0.

```javascript
let salaryGap = { $subtract: ["$Salary Range To", "$Salary Range From"] };

let fields = {
  $project: {
    _id: 0,
    "Business Title": 1,
    "Salary Gap": salaryGap,
  },
};

let annualExternal = {
  $match: {
    "Salary Frequency": "Annual",
    "Posting Type": "External",
  },
};

let maxDiff = { $match: { "Salary Gap": { $lt: 5000, $gt: 0 } } };

db.jobs.aggregate([annualExternal, fields, maxDiff]);
```

---

template: pipeline-examples

## Group

Let's calculate the average each city agency pays for the low end of the salary range for Career Level "`Entry-Level`", without including agencies with an average lower than $30,000.

```javascript
let matchEntryLevel = { $match: { "Career Level": "Entry-Level" } };

let avgSalaryAgencyGroup = {
  $group: {
    _id: "$Agency",
    avgSalaryFrom: { $avg: "$Salary Range From" },
  },
};

let match30K = {
  $match: {
    avgSalaryFrom: { $gte: 30000 },
  },
};

db.jobs.aggregate([matchEntryLevel, avgSalaryAgencyGroup, match30K]);
```

---

template: pipeline-examples

## Group

Let's see how many jobs were posted for every year

```javascript
let extractYear = { $arrayElemAt: [{ $split: ["$Posting Date", "/"] }, -1] };

let fields = { $project: { year: extractYear } };

let countByYear = { $group: { _id: "$year", count: { $sum: 1 } } };

let orderByYear = { $sort: { _id: -1 } };

db.jobs.aggregate([fields, countByYear, orderByYear]);
```

---

name: conclusions

# Conclusions

--

Thank you. Bye.

```

```
