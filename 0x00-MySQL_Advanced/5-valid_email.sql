-- Updates valid_email after email change
DELIMITER //
CREATE TRIGGER aftter_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        UPDATE users
        SET valid_email = 0
        WHERE id = NEW.id;
    END IF;
END;
//
DELIMITER ;