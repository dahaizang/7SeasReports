SELECT P.post_date, P.ID, P.post_content,P.post_title, P.comment_status,P.post_type,P.post_status, U.user_login, U.display_name, U.user_email, PM_regular_price.meta_value AS Regular_Price,
PM_order_total.meta_value AS Order_Total,
PM_stripe_net.meta_value AS Stripe_Net,
PM_stripe_fee.meta_value AS Stripe_Fee
FROM wp_2c6779b6av_posts P 
inner join wp_2c6779b6av_postmeta PMCustomer ON P.ID=PMCustomer.post_id AND PMCustomer.meta_key='_customer_user' 
inner join wp_2c6779b6av_users U on PMCustomer.meta_value=U.ID
left join wp_2c6779b6av_postmeta PM_regular_price on P.ID=PM_regular_price.post_id AND PM_regular_price .meta_key='_regular_price' 
left join wp_2c6779b6av_postmeta PM_order_total on P.ID=PM_order_total.post_id AND PM_order_total.meta_key='_order_total'
left join wp_2c6779b6av_postmeta PM_stripe_net on P.ID=PM_stripe_net.post_id AND PM_stripe_net.meta_key='_stripe_net'
left join wp_2c6779b6av_postmeta PM_stripe_fee on P.ID=PM_stripe_fee.post_id AND PM_stripe_fee.meta_key='_stripe_fee'
WHERE P.post_status= 'wc-refunded' OR P.post_status ='wc-completed' OR P.post_status ='wc-processing'
;



SELECT comment_post_ID, comment_id, comment_date, comment_content 
FROM  `wp_2c6779b6av_comments` 
ORDER BY  `wp_2c6779b6av_comments`.`comment_post_ID` DESC 
LIMIT 0 , 30

SELECT meta_key from wp_2c6779b6av_postmeta where post_id=2303 order by meta_key;



SELECT * from wp_2c6779b6av_posts where post_type in ('product', 'um_directory', 'um_form', 'shop_order')
or post_status like 'wc-%' order by post_type, ID;


SELECT P.post_date, P.ID, Product.ID, P.post_type,P.post_status, 
Product.post_title,
U.user_login, U.display_name, U.user_email, PM_regular_price.meta_value AS Regular_Price,
PM_order_total.meta_value AS Order_Total,
PM_stripe_net.meta_value AS Stripe_Net,
PM_stripe_fee.meta_value AS Stripe_Fee
FROM wp_2c6779b6av_posts P 
inner join wp_2c6779b6av_woocommerce_order_items OI ON P.ID=OI.order_id 
inner join wp_2c6779b6av_woocommerce_order_itemmeta OIM ON OI.order_item_id=OIM.order_item_id AND OIM.meta_key='_product_id' 
inner join wp_2c6779b6av_posts Product ON Product.ID=OIM.meta_value AND OI.order_item_id=OIM.order_item_id AND OIM.meta_key='_product_id' AND Product.post_type='product'
inner join wp_2c6779b6av_postmeta PMCustomer ON P.ID=PMCustomer.post_id AND PMCustomer.meta_key='_customer_user' 
inner join wp_2c6779b6av_users U on PMCustomer.meta_value=U.ID
left join wp_2c6779b6av_postmeta PM_regular_price on P.ID=PM_regular_price.post_id AND PM_regular_price .meta_key='_regular_price' 
left join wp_2c6779b6av_postmeta PM_order_total on P.ID=PM_order_total.post_id AND PM_order_total.meta_key='_order_total'
left join wp_2c6779b6av_postmeta PM_stripe_net on P.ID=PM_stripe_net.post_id AND PM_stripe_net.meta_key='_stripe_net'
left join wp_2c6779b6av_postmeta PM_stripe_fee on P.ID=PM_stripe_fee.post_id AND PM_stripe_fee.meta_key='_stripe_fee'
WHERE (P.post_status= 'wc-refunded' OR P.post_status ='wc-completed' OR P.post_status ='wc-processing')
AND OIM.meta_value IN ('2042', '2292')
;


SELECT P.post_date, P.ID AS OrderID, Product.ID As ProductID, P.post_type,P.post_status, 
Product.post_title AS Product,
U.user_login, U.display_name, U.user_email, PM_regular_price.meta_value AS Regular_Price,
OIMLineTotal.meta_value AS ItemPaid,
PM_order_total.meta_value AS Order_Total
FROM wp_2c6779b6av_posts P 
inner join wp_2c6779b6av_woocommerce_order_items OI ON P.ID=OI.order_id 
LEFT join wp_2c6779b6av_woocommerce_order_itemmeta OIM ON OI.order_item_id=OIM.order_item_id AND OIM.meta_key='_product_id' 
inner join wp_2c6779b6av_posts Product ON Product.ID=OIM.meta_value AND OI.order_item_id=OIM.order_item_id AND OIM.meta_key='_product_id' AND Product.post_type='product'
LEFT join wp_2c6779b6av_woocommerce_order_itemmeta OIMLineTotal ON OI.order_item_id=OIMLineTotal.order_item_id AND OIMLineTotal.meta_key='_line_total' 
inner join wp_2c6779b6av_postmeta PMCustomer ON P.ID=PMCustomer.post_id AND PMCustomer.meta_key='_customer_user' 
inner join wp_2c6779b6av_users U on PMCustomer.meta_value=U.ID
left join wp_2c6779b6av_postmeta PM_regular_price on P.ID=PM_regular_price.post_id AND PM_regular_price .meta_key='_regular_price' 
left join wp_2c6779b6av_postmeta PM_order_total on P.ID=PM_order_total.post_id AND PM_order_total.meta_key='_order_total'
left join wp_2c6779b6av_postmeta PM_stripe_net on P.ID=PM_stripe_net.post_id AND PM_stripe_net.meta_key='_stripe_net'
left join wp_2c6779b6av_postmeta PM_stripe_fee on P.ID=PM_stripe_fee.post_id AND PM_stripe_fee.meta_key='_stripe_fee'
WHERE (P.post_status= 'wc-refunded' OR P.post_status ='wc-completed' OR P.post_status ='wc-processing')
AND OIM.meta_value IN ('2042', '2292')
;


