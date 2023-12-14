-- Updates valid_email after email change
DELIMITER //
CREATE TRIGGER before_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;    
    END IF;
END;
//
DELIMITER ;