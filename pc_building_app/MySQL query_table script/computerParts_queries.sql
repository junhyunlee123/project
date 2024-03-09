SET SQL_SAFE_UPDATES = 0;

SELECT * FROM computerParts.processors;

SELECT * FROM computerParts.amdMotherboards;
SELECT * FROM computerParts.intelMotherboards;

SELECT * FROM computerParts.amdGraphicsCards;
SELECT * FROM computerParts.nvidiaGraphicsCards;
-- delete from computerParts.amdGraphicsCards;
-- delete from computerParts.nvidiaGraphicsCards;

SELECT * FROM computerParts.cases;

SELECT * FROM computerParts.memories;

SELECT * FROM computerParts.hddStorages;
SELECT * FROM computerParts.ssdStorages where productName like '%512GB%';

SELECT * FROM computerParts.powerSupplies;

SELECT * FROM computerParts.cpuAirCoolerCoolings;
SELECT * FROM computerParts.liquidOrWaterCoolerCoolings;
SELECT * FROM computerParts.pcCaseFanCoolings;

set global time_zone = '-6:00'