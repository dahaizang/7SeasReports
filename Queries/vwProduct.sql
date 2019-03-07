CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `e7se41220768516`@`%` 
    SQL SECURITY DEFINER
VIEW `e7se41220768516`.`vwProduct` AS
    SELECT 
        `P`.`ID` AS `ProductID`,
        `P`.`post_name` AS `Code`,
        `P`.`post_author` AS `CreatedBy`,
        `P`.`post_date` AS `CreatedOn`,
        `P`.`post_title` AS `ProductName`,
        `P`.`post_content` AS `Description`,
        `P`.`post_status` AS `ProductStatus`,
        `P`.`post_modified` AS `LastModifiedOn`,
        `P`.`post_parent` AS `SubTo`,
        `P`.`post_mime_type` AS `MimeType`,
        `P`.`comment_count` AS `TotalComment`
    FROM
        `e7se41220768516`.`wp_2c6779b6av_posts` `P`
    WHERE
        ((`P`.`post_type` = 'product')
            AND (`P`.`post_status` <> 'trash'))