CREATE 
VIEW `vwMembershipStatus` AS
    SELECT 
        `U`.`user_login` AS `user_login`,
        `U`.`user_email` AS `user_email`,
        `U`.`DateRegistered` AS `DateRegistered`,
        `U`.`first_name` AS `first_name`,
        `U`.`last_name` AS `last_name`,
        `U`.`nick_name` AS `nick_name`,
        `U`.`wechat_id` AS `wechat_id`,
        `O`.`OrderID` AS `OrderID`,
        `O`.`OrderDate` AS `OrderDate`,
        `O`.`OrderStatus` AS `OrderStatus`,
        `O`.`PaidDate` AS `DatePaid`,
        `O`.`PaymentMethod` AS `PaymentMethod`,
        `O`.`ItemAmount` AS `AmountPaid`,
        `O`.`Product` AS `Product`
    FROM
        (`vwUserInfo` `U`
        JOIN `vwOrderStatus` `O` ON ((`U`.`UserId` = `O`.`CustomerID`)))
    WHERE
        ((`O`.`Product` = '2019年书院会员')
            AND (`O`.`OrderStatus` = 'wc-completed'))