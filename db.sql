CREATE DATABASE NPI;

DROP TABLE IF EXISTS NPIData;
CREATE TABLE NPIData (
    NPI BIGINT PRIMARY KEY NOT NULL,
    EntityType INT NOT NULL,
    ProviderOrganization VARCHAR(256),
    ProviderLastName VARCHAR(128),
    ProviderFirstName VARCHAR(128),
    ProviderMiddleName VARCHAR(128),
    ProviderNamePrefix CHAR(16),
    ProviderNameSuffix CHAR(16),
    ProviderCredentials VARCHAR(64),
    ProviderAddress1 VARCHAR(128),
    ProviderAddress2 VARCHAR(128),
    ProviderCity VARCHAR(64),
    ProviderState VARCHAR(64),
    ProviderPostalCode VARCHAR(32),
    ProviderTelephoneNumber VARCHAR(32),
    ProviderFaxNumber VARCHAR(32),
    INDEX (EntityType),
    INDEX (ProviderLastName),
    INDEX (ProviderState),
    INDEX (ProviderCity)
);
