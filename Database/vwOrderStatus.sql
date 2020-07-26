CREATE 
VIEW `vwOrderStatus` AS
    SELECT 
        `O`.`CustomerID` AS `CustomerID`,
        `O`.`OrderID` AS `OrderID`,
        `O`.`OrderDate` AS `OrderDate`,
        `O`.`OrderStatus` AS `OrderStatus`,
        `O`.`PaymentMethod` AS `PaymentMethod`,
        `O`.`PaidDate` AS `PaidDate`,
        `O`.`CompleteDate` AS `CompleteDate`,
        `OI`.`OrderItemID` AS `OrderItemID`,
        `OI`.`OrderItemName` AS `OrderItemName`,
        `OI`.`ItemAmount` AS `ItemAmount`,
        `OI`.`ItemProduct` AS `ProductID`,
        `P`.`ProductName` AS `Product`
    FROM
        ((`vwOrder` `O`
        JOIN `vwOrderItem` `OI` ON ((`O`.`OrderID` = `OI`.`OrderID`)))
        JOIN `vwProduct` `P` ON ((`OI`.`ItemProduct` = `P`.`ProductID`)))