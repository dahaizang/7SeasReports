<?php
/**
 * Template Name: Database View Template
 */
get_header();
?>

<?php
function enqueue_datatables_scripts() {
    /*
    wp_enqueue_style('datatables-css', get_template_directory_uri() . '/datatables/datatables.min.css');
    wp_enqueue_style('datatables-fixedheader-css', get_template_directory_uri() . '/datatables/fixedHeader.dataTables.min.css');
    wp_enqueue_script('datatables-js', get_template_directory_uri() . '/datatables/datatables.min.js', array('jquery'), null, true);
    wp_enqueue_script('datatables-fixedheader-js', get_template_directory_uri() . '/datatables/dataTables.fixedHeader.min.js', array('jquery', 'datatables-js'), null, true);
    */
    wp_enqueue_style('datatables-css', 'https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css');
    wp_enqueue_style('datatables-fixedheader-css', 'https://cdn.datatables.net/fixedheader/3.2.1/css/fixedHeader.dataTables.min.css');
    wp_enqueue_style('datatables-colreorder-css', 'https://cdn.datatables.net/colreorder/1.5.6/css/colReorder.dataTables.min.css');
    wp_enqueue_script('datatables-js', 'https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js', array('jquery'), null, true);
    wp_enqueue_script('datatables-fixedheader-js', 'https://cdn.datatables.net/fixedheader/3.2.1/js/dataTables.fixedHeader.min.js', array('jquery', 'datatables-js'), null, true);
    wp_enqueue_script('datatables-colreorder-js', 'https://cdn.datatables.net/colreorder/1.5.6/js/dataTables.colReorder.min.js', array('jquery', 'datatables-js'), null, true);

}
add_action('wp_enqueue_scripts', 'enqueue_datatables_scripts');
?>

<?php
global $wpdb;

// Query the view v2025MemberShort
$results = $wpdb->get_results("SELECT * FROM v2025MemberShort");

echo "<br>2025 会员名单<br>";
// Display the results in a DataTable
echo '<div class="table-wrapper">';
echo '<table id="db-view-table-1" class="display nowrap" style="width:100%">';
echo '<thead><tr>';
foreach ($results[0] as $column => $value) {
    echo '<th>' . esc_html($column) . '</th>';
}
echo '</tr></thead>';
echo '<tbody>';
foreach ($results as $row) {
    echo '<tr>';
    foreach ($row as $value) {
        echo '<td>' . esc_html($value) . '</td>';
    }
    echo '</tr>';
}
echo '</tbody>';
echo '</table>';
echo '</div>';
?>

<?php
global $wpdb;

echo "<br>2025 春季选课<br>";

// Query the view v2025SpringClassShort
$results1 = $wpdb->get_results("SELECT * FROM v2025SpringClassShort");

// Display the results in a DataTable
echo '<div class="table-wrapper">';
echo '<table id="db-view-table-2" class="display nowrap" style="width:100%">';
echo '<thead><tr>';
foreach ($results1[0] as $column => $value) {
    echo '<th>' . esc_html($column) . '</th>';
}
echo '</tr></thead>';
echo '<tbody>';
foreach ($results1 as $row) {
    echo '<tr>';
    foreach ($row as $value) {
        echo '<td>' . esc_html($value) . '</td>';
    }
    echo '</tr>';
}
echo '</tbody>';
echo '</table>';
echo '</div>';
?>

<script>
jQuery(document).ready(function($) {
    $('#db-view-table-1').DataTable({
        "scrollX": true,
        "autoWidth": true,
        "scrollY": true, // "calc(100vh - 200px)", // Adjust the value to fit your window height
        "scrollCollapse": true,
        "paging": true,
        fixedHeader: {
            header: true
        }
    });
    $('#db-view-table-2').DataTable({
        "scrollX": true,
        "autoWidth": true,
        "scrollY": true, //"calc(100vh - 200px)", // Adjust the value to fit your window height
        "scrollCollapse": true,
        "paging": true,
        fixedHeader: {
            header: true
        }
    });
});
</script>

<style>
.table-wrapper {
    width: 100%;
    overflow: auto;
    padding: 10px;
    border: 1px solid #ccc;
    max-height: 100vh; /* Adjust this value to fit your window */
}
table.dataTable td {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    word-wrap: break-word; /* Break long words */
    word-break: break-all; /* Break long words */
}
</style>


<?php get_footer(); ?>
