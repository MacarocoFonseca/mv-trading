SELECT
    emp_id,
    SUM(CASE WHEN is_buggy = 0 THEN 1 ELSE 0 END) AS good_commits,
    SUM(CASE WHEN is_buggy = 1 THEN 1 ELSE 0 END) AS buggy_commits
FROM COMMITS
GROUP BY emp_id
ORDER BY emp_id