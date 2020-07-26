CREATE 
VIEW `vwOrderCompleted` AS
    SELECT 
        `vwOrder`.`CustomerID` AS `CustomerID`,
        `vwOrder`.`OrderID` AS `OrderID`,
        `vwOrder`.`OrderDate` AS `OrderDate`,
        `vwOrder`.`OrderStatus` AS `OrderStatus`,
        `vwOrder`.`PaymentMethod` AS `PaymentMethod`,
        `vwOrder`.`PaidDate` AS `PaidDate`,
        `vwOrder`.`CompleteDate` AS `CompleteDate`
    FROM
        `vwOrder`
    WHERE
        (`vwOrder`.`OrderStatus` = 'wc-completed')