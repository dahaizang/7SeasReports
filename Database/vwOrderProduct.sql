CREATE 
VIEW `vwOrderProduct` AS
    SELECT 
        `OI`.`order_id` AS `OrderID`,
        `OIM`.`meta_value` AS `ProductID`
    FROM
        (`wp_2c6779b6av_woocommerce_order_items` `OI`
        JOIN `wp_2c6779b6av_woocommerce_order_itemmeta` `OIM` ON (((`OI`.`order_item_id` = `OIM`.`order_item_id`)
            AND (`OIM`.`meta_key` = '_product_id'))))