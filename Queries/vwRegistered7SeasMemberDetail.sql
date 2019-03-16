CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `e7se41220768516`@`%` 
    SQL SECURITY DEFINER
VIEW `e7se41220768516`.`vwRegistered7SeasMemberDetail` AS
    SELECT 
        `OS`.`CustomerID` AS `CustomerID`,
        `OS`.`OrderID` AS `OrderID`,
        `OS`.`OrderDate` AS `OrderDate`,
        `OS`.`OrderStatus` AS `OrderStatus`,
        `OS`.`PaymentMethod` AS `PaymentMethod`,
        `OS`.`PaidDate` AS `PaidDate`,
        `OS`.`CompleteDate` AS `CompleteDate`,
        `OS`.`OrderItemID` AS `OrderItemID`,
        `OS`.`OrderItemName` AS `OrderItemName`,
        `OS`.`ItemAmount` AS `ItemAmount`,
        `OS`.`ProductID` AS `ProductID`,
        `OS`.`Product` AS `Product`,
        `C`.`user_login` AS `user_login`,
        `C`.`user_email` AS `user_email`,
        `C`.`DateRegistered` AS `DateRegistered`,
        `C`.`first_name` AS `first_name`,
        `C`.`last_name` AS `last_name`,
        `C`.`nick_name` AS `nick_name`,
        `C`.`wechat_id` AS `wechat_id`,
        `P`.`Code` AS `Code`,
        `P`.`CreatedBy` AS `CreatedBy`,
        `P`.`CreatedOn` AS `CreatedOn`,
        `P`.`ProductName` AS `ProductName`,
        `P`.`Description` AS `Description`,
        `P`.`ProductStatus` AS `ProductStatus`,
        `P`.`LastModifiedOn` AS `LastModifiedOn`,
        `P`.`TotalComment` AS `TotalComment`
    FROM
        ((`e7se41220768516`.`vwCustomer` `C`
        JOIN `e7se41220768516`.`vwOrderStatus` `OS` ON ((`C`.`CustomerID` = `OS`.`CustomerID`)))
        JOIN `e7se41220768516`.`vwProduct` `P` ON ((`OS`.`ProductID` = `P`.`ProductID`)))
    WHERE
        ((`OS`.`OrderStatus` = 'wc-completed')
            AND (`P`.`ProductName` LIKE '2019年书院会员%'))