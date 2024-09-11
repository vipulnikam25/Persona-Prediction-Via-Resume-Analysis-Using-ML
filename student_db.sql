/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.0.77-community-nt : Database - student_db
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`student_db` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `personality`;

/*Table structure for table `job_details` */

DROP TABLE IF EXISTS `job_details`;

CREATE TABLE `job_details` (
  `Designation` varchar(255) default NULL,
  `Salary` varchar(255) default NULL,
  `Place` varchar(255) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `job_details` */

insert  into `job_details`(`Designation`,`Salary`,`Place`) values ('Junior Python Developer','18000','Pune');

/*Table structure for table `question_details` */

DROP TABLE IF EXISTS `question_details`;

CREATE TABLE `question_details` (
  `Question` varchar(255) default NULL,
  `Answer1` varchar(255) default NULL,
  `Answer2` varchar(255) default NULL,
  `Answer3` varchar(255) default NULL,
  `Answer4` varchar(255) default NULL,
  `Answer5` varchar(255) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `question_details` */

insert  into `question_details`(`Question`,`Answer1`,`Answer2`,`Answer3`,`Answer4`,`Answer5`) values ('Your birthplace','New Delhi','Mumbai','Hydrabad','Banglore','Himachal Pradesh');

/*Table structure for table `register_details` */

DROP TABLE IF EXISTS `register_details`;

CREATE TABLE `register_details` (
  `Firstname` varchar(255) default NULL,
  `Lastname` varchar(255) default NULL,
  `Email_Id` varchar(255) default NULL,
  `Password` varchar(255) default NULL,
  `Address` varchar(255) default NULL,
  `Contact` varchar(255) default NULL,
  `City` varchar(255) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `register_details` */

insert  into `register_details`(`Firstname`,`Lastname`,`Email_Id`,`Password`,`Address`,`Contact`,`City`) values ('Vivek','Kumar','vivek.kumar24','vivek','Delhi','9205093312','New Delhi');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
