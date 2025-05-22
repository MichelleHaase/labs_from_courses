SELECT districts.name, SUM(expenditures.pupils) FROM districts JOIN expenditures ON districts.id = expenditures.district_id GROUP BY districts.name;
