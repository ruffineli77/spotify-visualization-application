-- SQLite
-- Everything is starting to tie together. You can use the sqlite explorer in VS code
-- to see the information stored for your website. You could also use mysql workbench, postgresql, etc.
SELECT
  file_path,
  COUNT(file_path) AS `value_occurrence` 

FROM
  Video

GROUP BY 
  file_path

ORDER BY 
  `value_occurrence` DESC

;