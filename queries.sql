--SELECT 
--    name
--FROM 
--    sqlite_master
--WHERE 
--    type ='table' AND 
--    name NOT LIKE 'sqlite_%';
SELECT * FROM checkbook_category ORDER BY category_name;
SELECT * FROM checkbook_account;
SELECT * FROM checkbook_transaction;