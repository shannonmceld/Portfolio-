-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema
-- get all the crime for the day
SELECT description FROM crime_scene_reports
WHERE month = '7' AND day = '28' AND year = '2021';
-- i learn 3 witnesses was interview and were there at the time of theft. lets look at the interview transcript
.schema
SELECT transcript, name FROM interviews WHERE month = '7'
ANDday = '28' AND year = '2021';
-- i learned barbara ruth and eugene were the name of the witnessess and their statement included the thief leaving the scene of the crime in a car
-- so maybe check and see if we have video footage of humprey street around 10am
--ruth says she saw the theif at the atm before the robbery
-- check the atm cameras on Legett Street
--and Eugene said he over heard the thief calling for some one to book them a flight out of fiftville for 7/29/21 morning
-- check the airport and see the flight list for the day of flights

SELECT * FROM atm_transactions WHERE month = '7'
AND day = '28' AND year = '2021' AND atm_location = 'Leggett Street';
-- there were eight withdrawals from the atm on that day & street
-- they are not time stamped but i bet i can get a name with the account numbers
--28500762, 28296815, 76054385, 762544385, 49610011, 16153065, 25506511, 81061156, 26013199
.schema

SELECT * FROM bakery_security_logs WHERE month = '7'
AND day = '28' AND year = '2021' AND hour = '10';
-- the crime scene report the theft happening at 10:15am
-- looking at the security logs i see that some enterred the stome at 10.14 am with the liscence plate 13fnh73, r3g7486
-- exit at 10:16 license plate 5p2bi95,94kl13x

SELECT * FROM flights WHERE month = '7' and day = '29'
AND year = '2021';
-- crossed reference the flight table with the airport

SELECT * FROM flights JOIN airports ON flights.origin_airport_id = airports.id
WHERE month = '7' and day = '29' AND year = '2021'
AND destination_airport_id = '1'
OR destination_airport_id = '4';

-- two flight on the 29 in the am id 36 and 43
-- let cross reference this table with the passenger table to see if i can get a name

SELECT * FROM flights JOIN airports ON flights.origin_airport_id = airports.id JOIN passengers ON flights.id = passengers.flight_id WHERE month = '7' and day = '29' AND year = '2021' AND destination_airport_id = '1' OR destination_airport_id = '4' AND flight_id = '36' OR flight_id = '43';
-- lets just get the passport_ and seat numbers
SELECT passport_number, seat FROM flights JOIN airports
ON flights.origin_airport_id = airports.id JOIN passengers
ON flights.id = passengers.flight_id WHERE month = '7'
AND day = '29' AND year = '2021' AND destination_airport_id = '1'
OR destination_airport_id = '4' AND flight_id = '36' OR flight_id = '43';
--7214083635 seat 2A, 1695452385 seat 3B, 5773159633 seat 4A, 1540955065 5C, 8294398571 6C, 1988161715 6D, 9878712108 7A, 8496433585 7B, 6128131458 8A, 6264773605 9A, 3642612721 2C, 4356447308 3B, 7441135547 4A
.schema
-- let go back to eight transactions and see can we get a name from the account number to cross refernce with passport names
SELECT DISTINCT account_number, (person_id) FROM bank_accounts
WHERE account_number = '26013199' OR account_number = '81061156'
OR account_number = '25506511' OR account_number = '16153065'
OR account_number = '49610011' OR account_number = '762544385'
OR account_number = '76054385' OR account_number = '28500762'
OR account_number = '28296815';
-- SO I HAVE 8 PEOPLE ID NUMBER LETS GET A NAME FOR... 686048, 514354, 458378, 395717, 396669, 467400, 449774, 438727
-- i see the people table also have a liscense plate column
-- let cross reference id # with paasport # and liscense plate # and see what we get

SELECT name FROM people WHERE passport_number = '7214083635'
OR passport_number = '1695452385' OR passport_number = '5773159633'
OR passport_number = '1540955065' OR passport_number = '8294398571'
OR passport_number = '1988161715' OR passport_number = '9878712108'
OR passport_number = '8496433585' OR passport_number = '6128131458'
OR passport_number = '6264773605' OR passport_number = '3642612721'
OR passport_number = '4356447308' OR passport_number = '7441135547';

SELECT name FROM people WHERE id = '686048' OR id = '14354'
OR id = '458378' OR id = '395717' OR id = '396669'
OR id = '467400' OR id = '449774' OR id = '438727';

SELECT name FROM people WHERE license_plate = '5P2BI95'
OR license_plate = '94KL13X'
-- BRUCE IS STICKING OUT LIKE A SORE THUMB HERE...
-- Lets see where the flight took brucy bruce 5773159633

SELECT city FROM airports WHERE id = '4';
--BOOM lil brucy in NEW YORK CITY

SELECT phone_number FROM people where name = 'Bruce';
-- bruce phone number is (367)5555533
-- lets see who bruce was talking to when he was thieving

SELECT * FROM phone_calls WHERE month = '7' and day = '28'
AND year = '2021' AND caller = '(367) 555-5533'
OR receiver = '(367) 555-5533' ;
-- bruce called 4 people that day 3755558161, 3445559601, 02255554052, 7045555790
--lets see if any of these people was the plane with him

SELECT name FROM people WHERE phone_number = '(375) 555-8161'
OR phone_number = '(344) 555-9601'
OR phone_number = '(022) 555-54052'
OR phone_number = '(704) 555-5790'
--ROBIN DO NOT HAVE  passport number
--but robin talk to Bruce the least on that day
-- robin is the accomplice