CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `e7se41220768516`@`%` 
    SQL SECURITY DEFINER
VIEW `e7se41220768516`.`vwOrderStatus` AS
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
        ((`e7se41220768516`.`vwOrder` `O`
        JOIN `e7se41220768516`.`vwOrderItem` `OI` ON ((`O`.`OrderID` = `OI`.`OrderID`)))
        JOIN `e7se41220768516`.`vwProduct` `P` ON ((`OI`.`ItemProduct` = `P`.`ProductID`)))