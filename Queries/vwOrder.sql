CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `e7se41220768516`@`%` 
    SQL SECURITY DEFINER
VIEW `e7se41220768516`.`vwOrder` AS
    SELECT 
        `PM`.`meta_value` AS `CustomerID`,
        `P`.`ID` AS `OrderID`,
        `P`.`post_date` AS `OrderDate`,
        `P`.`post_status` AS `OrderStatus`,
        `PMPaymentMethod`.`meta_value` AS `PaymentMethod`,
        `PMPaidDate`.`meta_value` AS `PaidDate`,
        `PMCompleteDate`.`meta_value` AS `CompleteDate`
    FROM
        ((((`e7se41220768516`.`wp_2c6779b6av_posts` `P`
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_postmeta` `PM` ON (((`P`.`ID` = `PM`.`post_id`)
            AND (`PM`.`meta_key` = '_customer_user'))))
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_postmeta` `PMPaymentMethod` ON (((`P`.`ID` = `PMPaymentMethod`.`post_id`)
            AND (`PMPaymentMethod`.`meta_key` = '_payment_method_title'))))
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_postmeta` `PMPaidDate` ON (((`P`.`ID` = `PMPaidDate`.`post_id`)
            AND (`PMPaidDate`.`meta_key` = '_paid_date'))))
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_postmeta` `PMCompleteDate` ON (((`P`.`ID` = `PMCompleteDate`.`post_id`)
            AND (`PMCompleteDate`.`meta_key` = '_completed_date'))))
    WHERE
        ((`P`.`post_type` = 'shop_order')
            AND (`P`.`post_status` <> 'trash'))