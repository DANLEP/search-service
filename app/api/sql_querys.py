get_new_attraction_preview_for_user = """
SELECT
    a.id_attraction,
    a.name,
    a.latitude,
    a.longitude,
    a.rating,
    COUNT(r.id_review) AS review_count,
    (SELECT COUNT(*)
     FROM user_attraction_preference uap
     WHERE uap.fk_attraction = a.id_attraction
     AND uap.preference_type = 'like') AS like_count
FROM
    attraction a
LEFT JOIN user_attraction_preference uap ON a.id_attraction = uap.fk_attraction AND uap.fk_user = :id
LEFT JOIN review r ON a.id_attraction = r.fk_attraction
WHERE
    uap.fk_user IS NULL OR uap.fk_user != :id
GROUP BY
    a.id_attraction
ORDER BY like_count DESC
LIMIT 10;
"""