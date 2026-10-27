<?php
/**
 * Router for PHP's built-in web server.
 * Serves real files from /public directly; everything else goes to WordPress.
 */

$root = __DIR__ . DIRECTORY_SEPARATOR . 'public';
$rootReal = realpath($root);
$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$path = urldecode($path);

if ($path !== '/' && $rootReal !== false) {
    $candidate = realpath($root . $path);
    if ($candidate !== false && is_file($candidate)) {
        $candidateNorm = str_replace('\\', '/', $candidate);
        $rootNorm = str_replace('\\', '/', $rootReal);
        if (strpos($candidateNorm, $rootNorm . '/') === 0) {
            return false;
        }
    }
}

require $root . DIRECTORY_SEPARATOR . 'index.php';
