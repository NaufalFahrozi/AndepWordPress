<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * Localized language
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'studio_karya_nusa' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', '127.0.0.1:3307' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',          '@L^w5)k,C`#1]o4(~~Uc<s_M8P/fpWsc4XXm~VSP2m)S^XA^df[t%I2s3e1O[+LT' );
define( 'SECURE_AUTH_KEY',   ',k2Ebx27@W,@d|v3m%Y>*FrCc20BPx%Rzy>!!V|g;2?VG,CDSrj@4J;mqhhS#W%Y' );
define( 'LOGGED_IN_KEY',     '{$Om$]d`OaGP6Sk9fH_x5Jy5ZJSr]5<T)t6OVN*B{rwZ:h@Qz|,%F;+Hh`Ti!#wf' );
define( 'NONCE_KEY',         '/=tAU I/,#K}Oh4=2PZ?+/M}12!2>$s= X`oU6 C-/,{hzkMwOAErN,vHg>(b0_C' );
define( 'AUTH_SALT',         '6#YjD!CZ%jJSl<XwOie**o89?Kz]%DHTvfT0b0<4Eqvhudr#bDgm,[#IK6{*q>`/' );
define( 'SECURE_AUTH_SALT',  '=lwFOR2huDAWq5/sO.:l`m3%gr!X|rth`tt/]8sM9h_)2Dwc-I^.cPEmlET&gD3+' );
define( 'LOGGED_IN_SALT',    '_?PP7@XU3%*- yh%y9PQBiS7Is|#N$-eJ2ez1ZkoNa.isqouGEe?$K82DE/tg#R|' );
define( 'NONCE_SALT',        '17pV8KcJ#^SMZ%~bER!U*(_B0#bFhoe4Y1/*ma5dq|GnDD|I(uv1Y CO^VxZM{9%' );
define( 'WP_CACHE_KEY_SALT', '}i+,%C&II3F9oZD&p`-/eXbOU|Q.^~EpCrmId@uKU_Edu/-QSwOuk7IlF%*y{DRH' );


/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';


/* Add any custom values between this line and the "stop editing" line. */



/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
if ( ! defined( 'WP_DEBUG' ) ) {
	define( 'WP_DEBUG', false );
}

define( 'WP_HTTP_BLOCK_EXTERNAL', true );
/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
