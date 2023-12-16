-- created a procedure tto compute avg weighted score
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT 
            SUM(c.score * p.weight) / SUM(p.weight)
        FROM 
            corrections c
        INNER JOIN 
            projects p ON p.id = c.project_id
        WHERE 
            c.user_id = user_id
    )
    WHERE 
        id = user_id;
END //
DELIMITER ;
