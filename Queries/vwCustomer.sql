CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `e7se41220768516`@`%` 
    SQL SECURITY DEFINER
VIEW `e7se41220768516`.`vwCustomer` AS
    SELECT DISTINCT
        `PM`.`meta_value` AS `CustomerID`,
        `U`.`user_login` AS `user_login`,
        `U`.`user_email` AS `user_email`,
        DATE_FORMAT(`U`.`user_registered`, '%Y-%m-%d') AS `DateRegistered`,
        `FName`.`meta_value` AS `first_name`,
        `LName`.`meta_value` AS `last_name`,
        `NName`.`meta_value` AS `nick_name`,
        `WeChatID`.`meta_value` AS `wechat_id`
    FROM
        (((((`e7se41220768516`.`wp_2c6779b6av_users` `U`
        JOIN `e7se41220768516`.`wp_2c6779b6av_postmeta` `PM` ON (((`U`.`ID` = `PM`.`meta_value`)
            AND (`PM`.`meta_key` = '_customer_user'))))
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_usermeta` `FName` ON (((`U`.`ID` = `FName`.`user_id`)
            AND (`FName`.`meta_key` = 'first_name'))))
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_usermeta` `LName` ON (((`U`.`ID` = `LName`.`user_id`)
            AND (`LName`.`meta_key` = 'last_name'))))
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_usermeta` `NName` ON (((`U`.`ID` = `NName`.`user_id`)
            AND (`NName`.`meta_key` = 'nickname'))))
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_usermeta` `WeChatID` ON (((`U`.`ID` = `WeChatID`.`user_id`)
            AND (`WeChatID`.`meta_key` = 'wechat_id'))))
    ORDER BY `LName`.`meta_value` , `FName`.`meta_value`