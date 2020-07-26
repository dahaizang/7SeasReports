CREATE 
VIEW `vwOrderItem` AS
    SELECT 
        `OI`.`order_id` AS `OrderID`,
        `OI`.`order_item_id` AS `OrderItemID`,
        `OI`.`order_item_name` AS `OrderItemName`,
        `OIMProduct`.`meta_value` AS `ItemProduct`,
        `OIMQty`.`meta_value` AS `ItemQty`,
        `OIMAmount`.`meta_value` AS `ItemAmount`
    FROM
        (((`wp_2c6779b6av_woocommerce_order_items` `OI`
        LEFT JOIN `wp_2c6779b6av_woocommerce_order_itemmeta` `OIMProduct` ON (((`OI`.`order_item_id` = `OIMProduct`.`order_item_id`)
            AND (`OIMProduct`.`meta_key` = '_product_id'))))
        LEFT JOIN `wp_2c6779b6av_woocommerce_order_itemmeta` `OIMQty` ON (((`OI`.`order_item_id` = `OIMQty`.`order_item_id`)
            AND (`OIMQty`.`meta_key` = '_qty'))))
        LEFT JOIN `wp_2c6779b6av_woocommerce_order_itemmeta` `OIMAmount` ON (((`OI`.`order_item_id` = `OIMAmount`.`order_item_id`)
            AND (`OIMAmount`.`meta_key` = '_line_total'))))