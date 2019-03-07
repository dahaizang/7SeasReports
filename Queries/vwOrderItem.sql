CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `e7se41220768516`@`%` 
    SQL SECURITY DEFINER
VIEW `e7se41220768516`.`vwOrderItem` AS
    SELECT 
        `OI`.`order_id` AS `OrderID`,
        `OI`.`order_item_id` AS `OrderItemID`,
        `OI`.`order_item_name` AS `OrderItemName`,
        `OIMProduct`.`meta_value` AS `ItemProduct`,
        `OIMAmount`.`meta_value` AS `ItemAmount`
    FROM
        ((`e7se41220768516`.`wp_2c6779b6av_woocommerce_order_items` `OI`
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_woocommerce_order_itemmeta` `OIMProduct` ON (((`OI`.`order_item_id` = `OIMProduct`.`order_item_id`)
            AND (`OIMProduct`.`meta_key` = '_product_id'))))
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_woocommerce_order_itemmeta` `OIMAmount` ON (((`OI`.`order_item_id` = `OIMAmount`.`order_item_id`)
            AND (`OIMAmount`.`meta_key` = '_line_total'))))