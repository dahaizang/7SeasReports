CREATE 
VIEW `vwUserInfo` AS
    SELECT 
        `U`.`ID` AS `UserId`,
        `U`.`user_login` AS `user_login`,
        `U`.`user_email` AS `user_email`,
        `U`.`user_registered` AS `DateRegistered`,
        `FName`.`meta_value` AS `first_name`,
        `LName`.`meta_value` AS `last_name`,
        `NName`.`meta_value` AS `nick_name`,
        `WeChatID`.`meta_value` AS `wechat_id`
    FROM
        ((((`wp_2c6779b6av_users` `U`
        LEFT JOIN `wp_2c6779b6av_usermeta` `FName` ON (((`U`.`ID` = `FName`.`user_id`)
            AND (`FName`.`meta_key` = 'first_name'))))
        LEFT JOIN `wp_2c6779b6av_usermeta` `LName` ON (((`U`.`ID` = `LName`.`user_id`)
            AND (`LName`.`meta_key` = 'last_name'))))
        LEFT JOIN `wp_2c6779b6av_usermeta` `NName` ON (((`U`.`ID` = `NName`.`user_id`)
            AND (`NName`.`meta_key` = 'nickname'))))
        LEFT JOIN `wp_2c6779b6av_usermeta` `WeChatID` ON (((`U`.`ID` = `WeChatID`.`user_id`)
            AND (`WeChatID`.`meta_key` = 'wechat_id'))))
    ORDER BY `LName`.`meta_value` , `FName`.`meta_value`