-- SQLite
-- Everything is starting to tie together. You can use the sqlite explorer in VS code
-- to see the information stored for your website. You could also use mysql workbench, postgresql, etc.
SELECT 
  folder_name

FROM
  Video

GROUP BY 
  file_path


;