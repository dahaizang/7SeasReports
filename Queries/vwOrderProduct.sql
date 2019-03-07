CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `e7se41220768516`@`%` 
    SQL SECURITY DEFINER
VIEW `e7se41220768516`.`vwOrderProduct` AS
    SELECT 
        `O`.`UserID` AS `UserID`,
        `O`.`OrderID` AS `OrderID`,
        `O`.`OrderDate` AS `OrderDate`,
        `O`.`OrderStatus` AS `OrderStatus`,
        `OIM`.`meta_value` AS `ProductID`
    FROM
        ((`e7se41220768516`.`vwOrder` `O`
        JOIN `e7se41220768516`.`wp_2c6779b6av_woocommerce_order_items` `OI` ON ((`O`.`OrderID` = `OI`.`order_id`)))
        JOIN `e7se41220768516`.`wp_2c6779b6av_woocommerce_order_itemmeta` `OIM` ON (((`OI`.`order_item_id` = `OIM`.`order_item_id`)
            AND (`OIM`.`meta_key` = '_product_id'))))