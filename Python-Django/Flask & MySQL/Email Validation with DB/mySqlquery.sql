                SELECT * FROM world.cities;

-- 1.
select * from world.languages; 

select name, language, percentage from world.languages left join world.countries on world.languages.country_id = world.countries.id where language = "Slovene";

-- 2.
select world.countries.name, count(*) as cities from world.cities left join world.countries on world.cities.country_id = world.countries.id GROUP BY world.countries.id ORDER BY cities DESCemailsemails;
select * from world.countries;

-- 3. 
select world.cities.name, world.cities.population from world.cities left join world.countries on world.cities.country_id = world.countries.id where country_id = 136 and world.cities.population > 500000;

-- 4.
select name, language, percentage from languages left join world.countries on world.languages.country_id = world.countries.id where percentage > 89;

-- 5.
select name, surface_area, population from world.countries where surface_area < 501 and population > 100000;

-- 6. 
select name, government_form, capital, life_expectancy from world.countries where life_expectancy > 75 and capital > 200;

-- 7. 
select world.countries.name, world.cities.name, world.cities.district, world.cities.population from world.cities left join world.countries on world.cities.country_id = world.countries.id where district = 'Buenos Aires' and world.cities.population > 500;

-- 8. 
select region, count(*) as countries from world.countries GROUP BY region ORDER BY countries DESC;


CREATE DATABASE  IF NOT EXISTS `mydb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `mydb`;

DROP TABLE IF EXISTS `emails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
select * from mydb.emails;