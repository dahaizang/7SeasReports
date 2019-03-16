CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `e7se41220768516`@`%` 
    SQL SECURITY DEFINER
VIEW `e7se41220768516`.`vwOrderNonCompleted` AS
    SELECT 
        `vwOrder`.`CustomerID` AS `CustomerID`,
        `vwOrder`.`OrderID` AS `OrderID`,
        `vwOrder`.`OrderDate` AS `OrderDate`,
        `vwOrder`.`OrderStatus` AS `OrderStatus`,
        `vwOrder`.`PaymentMethod` AS `PaymentMethod`,
        `vwOrder`.`PaidDate` AS `PaidDate`,
        `vwOrder`.`CompleteDate` AS `CompleteDate`
    FROM
        `e7se41220768516`.`vwOrder`
    WHERE
        (`vwOrder`.`OrderStatus` <> 'wc-completed')