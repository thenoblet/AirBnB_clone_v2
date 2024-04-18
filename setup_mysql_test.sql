-- A script that prepares a MySQL server for testing purposes

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant necessary privileges to the user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush the privileges to apply changes
FLUSH PRIVILEGES;
