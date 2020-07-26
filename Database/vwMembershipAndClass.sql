CREATE 
VIEW `vwMembershipAndClass` AS
    SELECT 
        `U`.`user_login` AS `user_login`,
        `U`.`first_name` AS `first_name`,
        `U`.`last_name` AS `last_name`,
        `U`.`user_email` AS `user_email`,
        `U`.`nick_name` AS `nick_name`,
        `U`.`DateRegistered` AS `DateRegistered`,
        `O`.`Product` AS `Product`,
        `O`.`PaidDate` AS `DatePaid`,
        `O`.`ItemAmount` AS `AmountPaid`,
        `O`.`PaymentMethod` AS `PaymentMethod`,
        `U`.`wechat_id` AS `wechat_id`,
        `O`.`OrderID` AS `OrderID`,
        `O`.`OrderDate` AS `OrderDate`,
        `O`.`OrderStatus` AS `OrderStatus`
    FROM
        (`vwUserInfo` `U`
        JOIN `vwOrderStatus` `O` ON ((`U`.`UserId` = `O`.`CustomerID`)))
    WHERE
        ((`O`.`OrderStatus` = 'wc-completed')
            AND (`O`.`Product` = '2019年书院会员+网络班'))