<?php

/**
 * The file that defines the core plugin class
 *
 * A class definition that includes attributes and functions used across both the
 * public-facing side of the site and the admin area.
 *
 * @link       http://huzaifairfan.com/
 * @since      1.0.0
 *
 * @package    stcourier_scraper_api_plugin
 * @subpackage stcourier_scraper_api_plugin/includes
 */

/**
 * The core plugin class.
 *
 * This is used to define internationalization, admin-specific hooks, and
 * public-facing site hooks.
 *
 * Also maintains the unique identifier of this plugin as well as the current
 * version of the plugin.
 *
 * @since      1.0.0
 * @package    stcourier_scraper_api_plugin
 * @subpackage stcourier_scraper_api_plugin/includes
 * @author     Huzaifa Irfan <huzaifairfan2001@gmail.com>
 */

 
class madhurcouriers_Scraper_Api_Plugin_Shortcode
{

	public static function run()
	{



function madhurcouriers_in_track_form_func(){


	ob_start();
	include_once plugin_dir_path(dirname(__FILE__)) . 'public/partials/madhurcouriers_in_scraper_api_plugin-public-form-display.php';
	$output = ob_get_contents();
	ob_end_clean();

	return $output;
}



add_shortcode('madhurcouriers_in_track_form','madhurcouriers_in_track_form_func');



// Plugin Tracking Deatils ShortCode




function madhurcouriers_in_track_submit_func(){


	ob_start();
	include_once plugin_dir_path(dirname(__FILE__)) . 'public/partials/madhurcouriers_in_scraper_api_plugin-public-display.php';
	$output = ob_get_contents();
	ob_end_clean();

	return $output;
};

add_shortcode('madhurcouriers_in_track_details','madhurcouriers_in_track_submit_func');


	}
}

madhurcouriers_Scraper_Api_Plugin_Shortcode::run();




