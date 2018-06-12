use FlaskDB;

CREATE TABLE FlaskDB.tbl_user ( user_id BIGINT NOT NULL UNIQUE AUTO_INCREMENT, 
                                user_name VARCHAR(255) NOT NULL UNIQUE, 
                                user_pass VARCHAR(255) NOT NULL, 
                                PRIMARY KEY (user_id) );

CREATE TABLE FlaskDB.tbl_session ( user_id BIGINT NOT NULL UNIQUE, 
                                   session_key VARCHAR(64) NULL,
                                   time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                                   PRIMARY KEY (user_id),
                                   FOREIGN KEY (user_id) REFERENCES tbl_user(user_id) );                                


DELIMITER //
CREATE PROCEDURE signup(user VARCHAR(255), pass VARCHAR(255))
BEGIN
    IF NOT ( SELECT EXISTS ( SELECT * FROM tbl_user WHERE user_name=user ) ) THEN
        INSERT INTO tbl_user (user_name, user_pass) VALUES(user, pass);
        SET @user_id := (SELECT user_id FROM tbl_user WHERE user_name=user AND user_pass=pass LIMIT 1);
        INSERT INTO tbl_session (user_id) VALUES (@user_id);
        SELECT session_key FROM tbl_session WHERE user_id=@user_id;
    END IF;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE login(user VARCHAR(255), pass VARCHAR(255))
BEGIN
    SET @user_id := (SELECT user_id FROM tbl_user WHERE user_name=user AND user_pass=pass LIMIT 1);
    IF ( SELECT @user_id IS NOT NULL ) THEN
        DELETE FROM tbl_session WHERE user_id=@user_id;
        INSERT INTO tbl_session (user_id) VALUES (@user_id);
        SELECT * FROM tbl_session WHERE user_id=@user_id;
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER before_insert_tbl_session
BEFORE INSERT ON tbl_session
FOR EACH ROW
BEGIN
  IF NEW.session_key IS NULL THEN
    SET NEW.session_key = uuid();
  END IF;
END
//
