-- Welcome to my detective agency!
-- Complete revised MySQL script: run against a NEW/EMPTY database.
-- UNIQUE contact details prevent duplicate non-NULL values, not every possible
-- duplicate person (e.g. missing or changed contact details). 

CREATE DATABASE IF NOT EXISTS detective_agency;
USE detective_agency;

-- creating key tables for my agency 

-- first the detectives who work there
CREATE TABLE tbl_Detectives(
	detective_id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(50),
	last_name varchar(50),
	specialisation varchar(50),
	hourly_rate DEC(10,2),
	active BOOL
);

-- clients who hire the agency
CREATE TABLE tbl_Clients(
	client_id INT AUTO_INCREMENT PRIMARY KEY,
	first_name varchar(50),
	last_name varchar(50),
	contact_number varchar(20) UNIQUE,
	email varchar(100) UNIQUE,
	date_added DATE
	);

-- the cases the agency is working on 
CREATE TABLE tbl_Cases(
	case_id INT AUTO_INCREMENT PRIMARY KEY,
	case_name varchar(50),
	status varchar(20) NOT NULL -- constraint
		CHECK (status IN('IN PROGRESS','CLOSED')), -- constraint
	case_type varchar(30)
		CHECK (case_type IN('Missing Persons', 'Surveillance', 'Corporate/Financial Crime','Theft', 'Cyber Crime','Espionage')), -- constraint
	client_id INT,
	case_opened_date DATE,
	case_closed_date DATE,
	FOREIGN KEY(client_id) REFERENCES tbl_Clients(client_id) ON DELETE SET NULL
	);

-- NEW: a case can have several detectives, and a detective can work on several cases.
CREATE TABLE tbl_CaseDetectives (
    case_id INT NOT NULL,
    detective_id INT NOT NULL,
    PRIMARY KEY (case_id, detective_id),
    FOREIGN KEY (case_id) REFERENCES tbl_Cases(case_id),
    FOREIGN KEY (detective_id) REFERENCES tbl_Detectives(detective_id)
);

-- suspects identified
CREATE TABLE tbl_Suspects(
	suspect_id INT AUTO_INCREMENT PRIMARY KEY,
	first_name varchar(50),
	last_name varchar(50),
	contact_number varchar(20) UNIQUE,
	location varchar(100)
);

-- junction table for suspects and cases (as many to many relationship)
CREATE TABLE tbl_CaseSuspects(
	CS_id INT AUTO_INCREMENT PRIMARY KEY,
	case_id INT,
	suspect_id INT,
	relationship_to_case varchar(50),
	date_identified DATE,
	notes TEXT,
	suspicion_level INT
		CHECK(suspicion_level IN(1,2,3)), -- constraint
		-- Where 1 = high/prime suspect, 2 = medium/ person of interest, 3 = low
	culprit BOOL, -- if case is closed, this will be true for whichever suspect was guilty
	FOREIGN KEY(case_id) REFERENCES tbl_Cases(case_id),
	FOREIGN KEY(suspect_id) REFERENCES tbl_Suspects(suspect_id)	
	);

-- mock data for each table
	
INSERT INTO tbl_Detectives
	(first_name, last_name, specialisation, hourly_rate, active)
VALUES
    ('Sherlock', 'Holmesby', 'Surveillance', 85.00, TRUE),
    ('Hercule', 'Poirotton', 'Corporate/Financial Crime', 95.00, TRUE),
    ('Nancy', 'Drewson', 'Missing Persons', 70.00, TRUE),
    ('Jessica', 'Fletcher', 'Theft', 65.00, TRUE),
    ('Columbo', 'Columbine', 'Surveillance', 75.00, TRUE),
    ('Veronica', 'Marsden', 'Cyber Crime', 90.00, TRUE),
    ('Jane', 'Marpleton', 'Corporate/Financial Crime', 100.00, FALSE),
    ('Sam', 'Spadewell', 'Missing Persons', 80.00, TRUE),
    ('Johnny', 'Englishton', 'Espionage', 50.00, TRUE),
    ('Ethan', 'Hunter', 'Espionage', 120.00, TRUE),
    ('James', 'Bonder', 'Espionage', 200.00, TRUE),
    ('Indiana', 'Jonesy', 'Theft', 100.00, TRUE);

INSERT INTO tbl_Clients
	(first_name, last_name, contact_number, email, date_added)
VALUES
	('Arthur', 'Pendleton', '07700900101', 'arthur.pendleton@email.com', '2026-01-12'),
    ('Beatrice', 'Bramble', '07700900102', 'beatrice.bramble@email.com', '2026-02-03'),
    ('Percival', 'Pemberton', '07700900103', 'percival.pemberton@email.com', '2026-02-19'),
    ('Evangeline', 'Wickham', '07700900104', 'evangeline.wickham@email.com', '2026-03-07'),
    ('Montgomery', 'Crumpet', '07700900105', 'montgomery.crumpet@email.com', '2026-03-21'),
    ('Penelope', 'Featherstone', '07700900106', 'penelope.featherstone@email.com', '2026-04-14'),
    ('Rupert', 'Tanglewood', '07700900107', 'rupert.tanglewood@email.com', '2026-05-02'),
    ('Clementine', 'Blackwood', '07700900108', 'clementine.blackwood@email.com', '2026-05-28');

INSERT INTO tbl_Cases
	(case_name, status, case_type, client_id, case_opened_date, case_closed_date)
VALUES
	('The Case of the Missing Pie', 'CLOSED', 'Theft', 1, '2026-01-08', '2026-01-12'),
    ('The Vanishing Violinist', 'IN PROGRESS', 'Missing Persons', 2, '2026-02-01', NULL),
    ('The Mystery of the Midnight Moustache', 'CLOSED', 'Surveillance', 3, '2026-01-15', '2026-01-29'),
    ('Who Stole the Crown Jewels?', 'IN PROGRESS', 'Theft', 4, '2026-06-03', NULL),
    ('The Curious Case of the Empty Office', 'IN PROGRESS', 'Corporate/Financial Crime', 5, '2026-04-18', NULL),
	('The Disappearing Biscuit Tin', 'CLOSED', 'Theft', 6, '2026-02-22', '2026-02-27'),
	('The Phantom Emailer', 'IN PROGRESS', 'Cyber Crime', 7, '2026-05-11', NULL),
    ('The Case of the Missing Butler', 'CLOSED', 'Missing Persons', 8, '2026-03-04', '2026-03-19'),
    ('The Suspicious Sandwich', 'IN PROGRESS', 'Surveillance', 1, '2026-07-02', NULL),
    ('The Great Spreadsheet Swindle', 'IN PROGRESS', 'Corporate/Financial Crime', 2, '2026-05-26', NULL),
    ('The Mystery of the Stolen Tuba', 'CLOSED', 'Theft', 3, '2026-03-28', '2026-04-05'),
    ('The Case of the Disappearing Heiress', 'IN PROGRESS', 'Missing Persons', 4, '2026-07-14', NULL),
    ('The Anonymous Avocado Account', 'CLOSED', 'Cyber Crime', 5, '2026-04-02', '2026-04-21'),
    ('The Man Who Watched the Pigeon', 'IN PROGRESS', 'Surveillance', 6, '2026-06-17', NULL),
    ('The Great Office Coffee Heist', 'CLOSED', 'Corporate/Financial Crime', 7, '2026-01-27', '2026-02-14');

-- NEW: preserve the original detective assignments in the junction table.
INSERT INTO tbl_CaseDetectives (case_id, detective_id)
VALUES
    (1, 4),
    (2, 3),
    (3, 1),
    (4, 4),
    (5, 2),
    (6, 4),
    (7, 6),
    (8, 8),
    (9, 1),
    (10, 2),
    (11, 4),
    (12, 3),
    (13, 6),
    (14, 5),
    (15, 2);

INSERT INTO tbl_Suspects
	(first_name, last_name, contact_number, location)
VALUES
	('Moriarty', 'Moriartyson', '07700900201', 'London'),
    ('Norman', 'Osborn', '07700900202', 'New York'),
    ('Lord', 'Voldemortson', '07700900203', 'Edinburgh'),
    ('Cruella', 'Deville', '07700900204', 'Brighton'),
    ('Hans', 'Gruber', '07700900205', 'Berlin'),
    ('Regina', 'Mills', '07700900206', 'London'),
    ('Loki', 'Laufeyson', '07700900207', 'Oslo'),
    ('Maleficent', 'Thornwood', '07700900208', 'Bath'),
    ('Joker', 'Jokerson', '07700900209', 'Gotham'),
    ('Harley', 'Quinnwell', '07700900210', 'Bristol'),
    ('Scar', 'Mufason', '07700900211', 'Manchester'),
    ('Ursula', 'Seawitch', '07700900212', 'Liverpool'),
    ('Norman', 'Bateson', '07700900213', 'Bournemouth'),
    ('Cersei', 'Lannister', '07700900214', 'London'),
    ('Sauron', 'Darkmore', '07700900215', 'Cambridge'),
    ('Bellatrix', 'Lestrange', '07700900216', 'Oxford'),
    ('Dr', 'Evilson', '07700900217', 'Cardiff'),
    ('The', 'Penguinson', '07700900218', 'Leeds'),
    ('Gaston', 'Villeneuve', '07700900219', 'Paris'),
    ('Palpatine', 'Sidiousson', '07700900220', 'Manchester');

INSERT INTO tbl_CaseSuspects
    (case_id, suspect_id, relationship_to_case, date_identified, notes, suspicion_level, culprit)
VALUES
    -- case 1
    (1, 1, 'Former Employee', '2026-01-08',
        'Seen leaving the bakery shortly before the pie disappeared.', 1, TRUE),
    (1, 4, 'Neighbour', '2026-01-09',
        'Reportedly had an unusual interest in the missing pie.', 2, FALSE),
    -- case 2
    (2, 3, 'Former Colleague', '2026-02-02',
        'Last person known to speak with the missing violinist.', 1, NULL),
    (2, 7, 'Friend', '2026-02-05',
        'Provided conflicting information about the violinist''s whereabouts.', 2, NULL),
    -- case 3
    (3, 6, 'Neighbour', '2026-01-17',
        'Frequently observed watching the client''s house.', 1, TRUE),
    (3, 9, 'Person of Interest', '2026-01-19',
        'Seen repeatedly near the client''s workplace.', 2, FALSE),
    -- case 4
    (4, 9, 'Former Employee', '2026-06-04',
        'Had access to the building where the crown jewels were displayed.', 1, NULL),
    (4, 11, 'Security Guard', '2026-06-05',
        'Security records show unusual activity during their shift.', 1, NULL),
    -- case 5
    (5, 2, 'Business Partner', '2026-04-19',
        'Had access to the company''s financial records.', 1, NULL),
    (5, 14, 'Employee', '2026-04-21',
        'Reportedly noticed suspicious financial transactions.', 2, NULL),
    -- case 6
    (6, 5, 'Housekeeper', '2026-02-23',
        'Was responsible for cleaning the kitchen where the biscuit tin vanished.', 1, TRUE),
    -- case 7
    (7, 17, 'Former Employee', '2026-05-12',
        'Had access to the company email system before leaving.', 1, NULL),
    (7, 20, 'Online Associate', '2026-05-14',
        'Known to communicate with the primary suspect online.', 2, NULL),
    -- case 8
    (8, 15, 'Family Member', '2026-03-05',
        'Last family member to see the missing butler.', 2, FALSE),
    (8, 8, 'Neighbour', '2026-03-07',
        'Reported seeing someone matching the butler''s description nearby.', 1, TRUE),
    -- case 9
    (9, 12, 'Colleague', '2026-07-03',
        'Was repeatedly seen near the client''s suspicious sandwich.', 1, NULL),
    (9, 18, 'Acquaintance', '2026-07-04',
        'Made several unusual comments about the sandwich.', 2, NULL),
    -- case 10
    (10, 2, 'Business Partner', '2026-05-27',
        'Had access to the financial spreadsheet in question.', 1, NULL),
    (10, 14, 'Employee', '2026-05-29',
        'Had permission to edit company financial documents.', 2, NULL),
    -- case 11
    (11, 11, 'Former Bandmate', '2026-03-29',
        'Had previously argued with the client about ownership of the tuba.', 2, FALSE),
    (11, 19, 'Neighbour', '2026-03-30',
        'Reported hearing unusual noises on the night of the theft.', 1, TRUE),
    -- case 12
    (12, 16, 'Family Member', '2026-07-15',
        'Was the last known person to contact the missing heiress.', 1, NULL),
    (12, 3, 'Former Associate', '2026-07-16',
        'Provided contradictory information about the heiress''s plans.', 2, NULL),
    -- case 13
    (13, 17, 'Former Employee', '2026-04-03',
        'Had previously accessed the client''s online accounts.', 2, FALSE),
    (13, 20, 'Online Associate', '2026-04-04',
        'Linked to suspicious activity originating from another account.', 1, TRUE),
    -- case 14
    (14, 10, 'Neighbour', '2026-06-18',
        'Observed repeatedly following the client''s local pigeon.', 1, NULL),
    -- case 15
    (15, 2, 'Manager', '2026-01-28',
        'Had access to the office accounts and expenditure records.', 1, TRUE),
    (15, 13, 'Employee', '2026-01-29',
        'Was responsible for ordering office supplies and coffee.', 2, FALSE);

/* Inserting data:
 * Query 1: Detective Spadewell retires
 */
UPDATE tbl_Detectives
SET active = False
WHERE detective_id = 8;

/* Query 2: adding a status for each suspect */
ALTER TABLE tbl_CaseSuspects
ADD COLUMN suspect_status varchar(50)
	CHECK (suspect_status IN('Missing','Under Investigation','Arrested','Witness', 'Cleared')) -- constraint
;

/* Query 3: update the table with relevant status values */
-- Case 1
UPDATE tbl_CaseSuspects
SET suspect_status = 'Arrested'
WHERE case_id = 1 AND suspect_id = 1;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Cleared'
WHERE case_id = 1 AND suspect_id = 4;

-- Case 2
UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 2 AND suspect_id = 3;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 2 AND suspect_id = 7;

-- Case 3
UPDATE tbl_CaseSuspects
SET suspect_status = 'Arrested'
WHERE case_id = 3 AND suspect_id = 6;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Cleared'
WHERE case_id = 3 AND suspect_id = 9;

-- Case 4
UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 4 AND suspect_id = 9;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 4 AND suspect_id = 11;

-- Case 5
UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 5 AND suspect_id = 2;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Witness'
WHERE case_id = 5 AND suspect_id = 14;

-- Case 6
UPDATE tbl_CaseSuspects
SET suspect_status = 'Arrested'
WHERE case_id = 6 AND suspect_id = 5;

-- Case 7
UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 7 AND suspect_id = 17;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 7 AND suspect_id = 20;

-- Case 8
UPDATE tbl_CaseSuspects
SET suspect_status = 'Cleared'
WHERE case_id = 8 AND suspect_id = 15;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Arrested'
WHERE case_id = 8 AND suspect_id = 8;

-- Case 9
UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 9 AND suspect_id = 12;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 9 AND suspect_id = 18;

-- Case 10
UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 10 AND suspect_id = 2;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 10 AND suspect_id = 14;

-- Case 11
UPDATE tbl_CaseSuspects
SET suspect_status = 'Cleared'
WHERE case_id = 11 AND suspect_id = 11;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Arrested'
WHERE case_id = 11 AND suspect_id = 19;

-- Case 12
UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 12 AND suspect_id = 16;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 12 AND suspect_id = 3;

-- Case 13
UPDATE tbl_CaseSuspects
SET suspect_status = 'Cleared'
WHERE case_id = 13 AND suspect_id = 17;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Arrested'
WHERE case_id = 13 AND suspect_id = 20;

-- Case 14
UPDATE tbl_CaseSuspects
SET suspect_status = 'Under Investigation'
WHERE case_id = 14 AND suspect_id = 10;

-- Case 15
UPDATE tbl_CaseSuspects
SET suspect_status = 'Arrested'
WHERE case_id = 15 AND suspect_id = 2;

UPDATE tbl_CaseSuspects
SET suspect_status = 'Cleared'
WHERE case_id = 15 AND suspect_id = 13;

/* Query 4: changing the type and therefore detective working on a case */
UPDATE tbl_Cases
SET case_type = 'Espionage'
WHERE case_id = 12;

-- Replace the assigned detective for case 12.
DELETE FROM tbl_CaseDetectives WHERE case_id = 12;
INSERT INTO tbl_CaseDetectives (case_id, detective_id) VALUES (12, 12);

/* Retrieving data:
 * query 1: all active detectives
 */
SELECT CONCAT(first_name, ' ',last_name) AS detective_full_name, specialisation, hourly_rate -- built in function
FROM tbl_Detectives
WHERE active = TRUE
ORDER BY hourly_rate;


-- query 2: the busiest detectives, I used this to choose who should retire above
CREATE VIEW vw_detectives_with_cases AS
    SELECT d.detective_id,
           CONCAT(d.first_name, ' ', d.last_name) AS detective_full_name,
           COUNT(c.case_id) AS total_open_cases
    FROM tbl_Detectives d
    JOIN tbl_CaseDetectives cd ON d.detective_id = cd.detective_id
    JOIN tbl_Cases c ON cd.case_id = c.case_id
    WHERE c.status = 'IN PROGRESS'
    GROUP BY d.detective_id, d.first_name, d.last_name
    ORDER BY total_open_cases DESC;

SELECT * FROM vw_detectives_with_cases;

-- query 3: which suspect has been the top suspect in the most cases?
SELECT s.suspect_id, CONCAT(s.first_name, ' ',s.last_name) AS suspect_full_name, COUNT(cs.case_id) AS no_of_cases_top_suspect
FROM tbl_Suspects s LEFT JOIN tbl_CaseSuspects cs
	ON s.suspect_id = cs.suspect_id
WHERE cs.suspicion_level = 1
GROUP BY s.suspect_id, suspect_full_name
ORDER BY no_of_cases_top_suspect DESC
LIMIT 1;

-- query 4: which cases have been open the longest and which detectives are they assigned to?
SELECT c.case_id, c.case_name, d.detective_id,
       CONCAT(d.first_name, ' ', d.last_name) AS detective_full_name,
       DATEDIFF(CURDATE(), c.case_opened_date) AS days_ongoing
FROM tbl_Cases c
JOIN tbl_CaseDetectives cd ON c.case_id = cd.case_id
JOIN tbl_Detectives d ON cd.detective_id = d.detective_id
WHERE c.status = 'IN PROGRESS'
ORDER BY days_ongoing DESC;

-- query 5: what is the average hourly rate for each specialisation?
SELECT UPPER(specialisation), ROUND(AVG(hourly_rate),2) AS average_hourly_rate -- agg function + built-in function
FROM tbl_Detectives
GROUP BY specialisation
ORDER BY average_hourly_rate;

-- query 6: The culprits in the closed cases // 2 JOINS
SELECT s.suspect_id, CONCAT(s.first_name,' ', s.last_name) AS culprit_full_name, c.case_name,c.case_id, c.case_type
FROM tbl_Suspects s JOIN tbl_CaseSuspects cs
	ON s.suspect_id = cs.suspect_id
LEFT JOIN tbl_Cases c
	ON cs.case_id = c.case_id
WHERE c.status = 'CLOSED' AND cs.culprit = 1;

/* QUERY TO DELETE DATA
 * delete  a client based of their unique ID
 */
DELETE FROM tbl_Clients
WHERE client_id = 8;

/* Stored procedure/function to help agency find a suitable detective for a new case based on how many open cases they have
 */

DELIMITER //
CREATE PROCEDURE find_suitable_detective(IN required_specialisation VARCHAR(50))
BEGIN
    SELECT d.detective_id,
           CONCAT(d.first_name, ' ', d.last_name) AS detective_name,
           d.specialisation, d.hourly_rate,
           COUNT(c.case_id) AS open_cases
    FROM tbl_Detectives d
    LEFT JOIN tbl_CaseDetectives cd ON d.detective_id = cd.detective_id
    LEFT JOIN tbl_Cases c ON cd.case_id = c.case_id
                          AND c.status = 'IN PROGRESS'
    WHERE d.specialisation = required_specialisation
    GROUP BY d.detective_id, d.first_name, d.last_name,
             d.specialisation, d.hourly_rate
    ORDER BY open_cases;
END //
DELIMITER ;

CALL find_suitable_detective('Espionage');