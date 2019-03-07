CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `e7se41220768516`@`%` 
    SQL SECURITY DEFINER
VIEW `e7se41220768516`.`vwRegisterAndPaidFor7SeasMembership` AS
    SELECT 
        `U`.`user_login` AS `user_login`,
        `U`.`user_email` AS `user_email`,
        `U`.`DateRegistered` AS `DateRegistered`,
        `U`.`first_name` AS `first_name`,
        `U`.`last_name` AS `last_name`,
        `U`.`nick_name` AS `nick_name`,
        `U`.`wechat_id` AS `wechat_id`,
        `P`.`post_date` AS `order_date`,
        `Product`.`post_title` AS `Product`,
        `OIMLineTotal`.`meta_value` AS `AmountPaid`,
        `P`.`post_type` AS `post_type`,
        `P`.`post_status` AS `post_status`,
        `U`.`ID` AS `ID`,
        `P`.`ID` AS `OrderID`,
        `Product`.`ID` AS `ProductID`
    FROM
        ((((((`e7se41220768516`.`wp_2c6779b6av_posts` `P`
        JOIN `e7se41220768516`.`wp_2c6779b6av_woocommerce_order_items` `OI` ON ((`P`.`ID` = `OI`.`order_id`)))
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_woocommerce_order_itemmeta` `OIM` ON (((`OI`.`order_item_id` = `OIM`.`order_item_id`)
            AND (`OIM`.`meta_key` = '_product_id'))))
        JOIN `e7se41220768516`.`wp_2c6779b6av_posts` `Product` ON (((`Product`.`ID` = `OIM`.`meta_value`)
            AND (`OI`.`order_item_id` = `OIM`.`order_item_id`)
            AND (`OIM`.`meta_key` = '_product_id')
            AND (`Product`.`post_type` = 'product'))))
        LEFT JOIN `e7se41220768516`.`wp_2c6779b6av_woocommerce_order_itemmeta` `OIMLineTotal` ON (((`OI`.`order_item_id` = `OIMLineTotal`.`order_item_id`)
            AND (`OIMLineTotal`.`meta_key` = '_line_total'))))
        JOIN `e7se41220768516`.`wp_2c6779b6av_postmeta` `PMCustomer` ON (((`P`.`ID` = `PMCustomer`.`post_id`)
            AND (`PMCustomer`.`meta_key` = '_customer_user'))))
        JOIN `e7se41220768516`.`vwUserInfo` `U` ON ((`PMCustomer`.`meta_value` = `U`.`ID`)))
    WHERE
        (((`P`.`post_status` = 'wc-refunded')
            OR (`P`.`post_status` = 'wc-completed')
            OR (`P`.`post_status` = 'wc-processing'))
            AND (`Product`.`post_type` = 'product')
            AND (`Product`.`post_title` = '2019年书院会员'))