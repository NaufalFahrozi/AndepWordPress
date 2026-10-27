<?php
$css_file = __DIR__ . '/../assets/custom.css';
$css = file_get_contents($css_file);
if ($css === false) {
    fwrite(STDERR, "Could not read CSS file.\n");
    exit(1);
}
$post = wp_update_custom_css_post($css);
if (is_wp_error($post)) {
    fwrite(STDERR, $post->get_error_message() . "\n");
    exit(1);
}
echo "CSS updated: " . strlen($css) . " bytes, post ID " . $post->ID . "\n";

