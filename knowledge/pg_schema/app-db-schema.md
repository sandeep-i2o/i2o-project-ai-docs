# Schema: i2oretail_dev  —  Database Documentation

---

## Table of Contents

- [abc](#abc)
- [account](#account)
- [account_activity_otp_details](#account_activity_otp_details)
- [account_brand](#account_brand)
- [account_config](#account_config)
- [account_fields](#account_fields)
- [account_notice_settings](#account_notice_settings)
- [accounts](#accounts)
- [add_entries_salestagging](#add_entries_salestagging)
- [ae_salesanalysisinsights_queries](#ae_salesanalysisinsights_queries)
- [agency](#agency)
- [agency_session_details](#agency_session_details)
- [ai_tokens_per_author](#ai_tokens_per_author)
- [all_sub_categories](#all_sub_categories)
- [all_sub_categories_bak](#all_sub_categories_bak)
- [app_user_tracking](#app_user_tracking)
- [application_properties](#application_properties)
- [atf_standard](#atf_standard)
- [attachment](#attachment)
- [audit](#audit)
- [audit_group](#audit_group)
- [audit_object](#audit_object)
- [basic_standard](#basic_standard)
- [bp_wbr_execution_details](#bp_wbr_execution_details)
- [brand_master](#brand_master)
- [brand_violation_plugin_capture_log](#brand_violation_plugin_capture_log)
- [brand_violations_filtered](#brand_violations_filtered)
- [brand_violations_filtered_20250627](#brand_violations_filtered_20250627)
- [brand_violations_filtered_backup](#brand_violations_filtered_backup)
- [brand_violations_filtered_stg](#brand_violations_filtered_stg)
- [brand_violations_interactions](#brand_violations_interactions)
- [brand_violations_review](#brand_violations_review)
- [brand_violations_stg_dev_final](#brand_violations_stg_dev_final)
- [bucket4j_buckets](#bucket4j_buckets)
- [business_unit](#business_unit)
- [buy_box_details](#buy_box_details)
- [buybox_delivery_reports](#buybox_delivery_reports)
- [catalog_temp](#catalog_temp)
- [category](#category)
- [category_master](#category_master)
- [categorymaster_marketplaceids](#categorymaster_marketplaceids)
- [channel](#channel)
- [client_platform_category_mapping](#client_platform_category_mapping)
- [cloud_scheduler_execution_details](#cloud_scheduler_execution_details)
- [col](#col)
- [column_definition](#column_definition)
- [columnbackup](#columnbackup)
- [component](#component)
- [context](#context)
- [data_event_backup](#data_event_backup)
- [data_feed_feature](#data_feed_feature)
- [data_feeds](#data_feeds)
- [data_last_publish](#data_last_publish)
- [dataload_allocation](#dataload_allocation)
- [dataproduct_request_details](#dataproduct_request_details)
- [dataproduct_test](#dataproduct_test)
- [digishare_combined_metrics](#digishare_combined_metrics)
- [digishare_combined_metrics1](#digishare_combined_metrics1)
- [digishare_combined_metrics_2025_09_15](#digishare_combined_metrics_2025_09_15)
- [digishare_combined_metrics_26_july](#digishare_combined_metrics_26_july)
- [digishare_combined_metrics_bulk_load](#digishare_combined_metrics_bulk_load)
- [digishare_combined_metrics_load_test](#digishare_combined_metrics_load_test)
- [digishare_combined_metrics_stg](#digishare_combined_metrics_stg)
- [digishare_details](#digishare_details)
- [digishare_test](#digishare_test)
- [distribution_list](#distribution_list)
- [distribution_list_schedule_master](#distribution_list_schedule_master)
- [drop_temp](#drop_temp)
- [ecom_pltfrm](#ecom_pltfrm)
- [email_attachment](#email_attachment)
- [email_message](#email_message)
- [enforcement_queue](#enforcement_queue)
- [enforcement_queue_stats](#enforcement_queue_stats)
- [enforecemt](#enforecemt)
- [event_definition](#event_definition)
- [event_has_organization](#event_has_organization)
- [event_results](#event_results)
- [event_types](#event_types)
- [events](#events)
- [events_history](#events_history)
- [fcst_supply_worksheet_hstry_data](#fcst_supply_worksheet_hstry_data)
- [features](#features)
- [feedback_details](#feedback_details)
- [filter](#filter)
- [filter_dr](#filter_dr)
- [filter_org_type](#filter_org_type)
- [filterback](#filterback)
- [forecast_data](#forecast_data)
- [ga_user_details](#ga_user_details)
- [gallery_standard](#gallery_standard)
- [header](#header)
- [header_backup](#header_backup)
- [header_meta_info](#header_meta_info)
- [hibernate_sequences](#hibernate_sequences)
- [highlight_priority](#highlight_priority)
- [hourly_dataload_details](#hourly_dataload_details)
- [industry](#industry)
- [invoice](#invoice)
- [invoice_line_item](#invoice_line_item)
- [job_execution](#job_execution)
- [job_type](#job_type)
- [job_type_marketplace](#job_type_marketplace)
- [keepa_batch_details_to_delete](#keepa_batch_details_to_delete)
- [keepa_product_download_progress](#keepa_product_download_progress)
- [keepa_progress_to_delete](#keepa_progress_to_delete)
- [listing_master](#listing_master)
- [listing_master_stg](#listing_master_stg)
- [lookup_config](#lookup_config)
- [lookupentity](#lookupentity)
- [manual_measures](#manual_measures)
- [map_enforcement_history](#map_enforcement_history)
- [map_enforcement_history_stg](#map_enforcement_history_stg)
- [map_enforcement_tracker](#map_enforcement_tracker)
- [map_enforcement_tracker_stg](#map_enforcement_tracker_stg)
- [marketplace](#marketplace)
- [marketplace_search_terms](#marketplace_search_terms)
- [master_data_quota](#master_data_quota)
- [master_data_resource](#master_data_resource)
- [master_data_review](#master_data_review)
- [master_metadata](#master_metadata)
- [metric](#metric)
- [metric_ex](#metric_ex)
- [notice_config](#notice_config)
- [notice_delivery_attempt_ops](#notice_delivery_attempt_ops)
- [notice_status](#notice_status)
- [notice_template](#notice_template)
- [notification](#notification)
- [notifications](#notifications)
- [onboarding_queries](#onboarding_queries)
- [org_brands](#org_brands)
- [org_contacts](#org_contacts)
- [org_data_metadata](#org_data_metadata)
- [org_dummy_table_preprod](#org_dummy_table_preprod)
- [org_hourly_mapping](#org_hourly_mapping)
- [org_market_mapping](#org_market_mapping)
- [org_marketplace](#org_marketplace)
- [org_marketplace_account](#org_marketplace_account)
- [org_marketplace_data_feed](#org_marketplace_data_feed)
- [org_marketplace_features](#org_marketplace_features)
- [org_qprofiles](#org_qprofiles)
- [org_report](#org_report)
- [organization](#organization)
- [organization_types](#organization_types)
- [parsehub_project_details](#parsehub_project_details)
- [perm_templates_groups](#perm_templates_groups)
- [perm_templates_users](#perm_templates_users)
- [perm_tpl_characteristics](#perm_tpl_characteristics)
- [permission_templates](#permission_templates)
- [platform_org_channel_mapping](#platform_org_channel_mapping)
- [plugins](#plugins)
- [potential_brands](#potential_brands)
- [premium_standard](#premium_standard)
- [prime_day_report_execution](#prime_day_report_execution)
- [product_catalog](#product_catalog)
- [product_catalog_check](#product_catalog_check)
- [product_catalog_stg](#product_catalog_stg)
- [product_category](#product_category)
- [product_category_detail](#product_category_detail)
- [product_channel_master](#product_channel_master)
- [product_content_latest](#product_content_latest)
- [product_content_latest_20241007](#product_content_latest_20241007)
- [product_content_latest_stg](#product_content_latest_stg)
- [product_content_locked](#product_content_locked)
- [product_data_resouces](#product_data_resouces)
- [product_details](#product_details)
- [product_discovery_scraping_input](#product_discovery_scraping_input)
- [product_keywords](#product_keywords)
- [product_master](#product_master)
- [product_master_20241007](#product_master_20241007)
- [product_master_bq_dump](#product_master_bq_dump)
- [product_master_drop](#product_master_drop)
- [product_master_locked_test](#product_master_locked_test)
- [product_master_scraping_config](#product_master_scraping_config)
- [product_master_scraping_input](#product_master_scraping_input)
- [product_master_test](#product_master_test)
- [product_master_tracking](#product_master_tracking)
- [product_master_tracking_20241007](#product_master_tracking_20241007)
- [product_master_user_comment](#product_master_user_comment)
- [product_matching_input](#product_matching_input)
- [product_matching_output](#product_matching_output)
- [product_matching_output_bk](#product_matching_output_bk)
- [product_matching_output_demo](#product_matching_output_demo)
- [product_matching_output_pp](#product_matching_output_pp)
- [product_matching_output_stg](#product_matching_output_stg)
- [product_matching_output_stg_test](#product_matching_output_stg_test)
- [product_matching_output_temp](#product_matching_output_temp)
- [product_matching_output_updated](#product_matching_output_updated)
- [product_sales_velocity_grouping](#product_sales_velocity_grouping)
- [product_upc_matching_output](#product_upc_matching_output)
- [project_alm_settings](#project_alm_settings)
- [project_branches](#project_branches)
- [project_links](#project_links)
- [project_mappings](#project_mappings)
- [project_measures](#project_measures)
- [project_qgates](#project_qgates)
- [project_qprofiles](#project_qprofiles)
- [projects](#projects)
- [properties](#properties)
- [pub_sub_event_ops](#pub_sub_event_ops)
- [q](#q)
- [qprofile_changes](#qprofile_changes)
- [qprofile_edit_groups](#qprofile_edit_groups)
- [qprofile_edit_users](#qprofile_edit_users)
- [quality_gate_conditions](#quality_gate_conditions)
- [quality_gates](#quality_gates)
- [query](#query)
- [query_01_03_2024_back](#query_01_03_2024_back)
- [query_20230311](#query_20230311)
- [query_20240229](#query_20240229)
- [query_20240304](#query_20240304)
- [query_20240308](#query_20240308)
- [query_20240315](#query_20240315)
- [query_20240326](#query_20240326)
- [query_20240401](#query_20240401)
- [query_amogh](#query_amogh)
- [query_backup](#query_backup)
- [query_backup_29_02_2024](#query_backup_29_02_2024)
- [query_bck_today31](#query_bck_today31)
- [query_bckp](#query_bckp)
- [rainforest_output_stg](#rainforest_output_stg)
- [rating](#rating)
- [region_zone_id_mapping](#region_zone_id_mapping)
- [rep](#rep)
- [report](#report)
- [report_column](#report_column)
- [report_column_back127](#report_column_back127)
- [report_column_backup_detail](#report_column_backup_detail)
- [report_column_rahul](#report_column_rahul)
- [report_filter](#report_filter)
- [report_org_config](#report_org_config)
- [reports_schedule_report](#reports_schedule_report)
- [reprt_column_backup](#reprt_column_backup)
- [research_enqueue_audit](#research_enqueue_audit)
- [reseller](#reseller)
- [reseller_benefits](#reseller_benefits)
- [reseller_enforcement_prioritization](#reseller_enforcement_prioritization)
- [reseller_enforcement_tracker](#reseller_enforcement_tracker)
- [reseller_enforcement_tracker_stg](#reseller_enforcement_tracker_stg)
- [reseller_geocode](#reseller_geocode)
- [reseller_library_master](#reseller_library_master)
- [reseller_library_master_backup](#reseller_library_master_backup)
- [reseller_library_master_pipeline](#reseller_library_master_pipeline)
- [reseller_library_master_stg](#reseller_library_master_stg)
- [reseller_library_master_validation_20250730](#reseller_library_master_validation_20250730)
- [reseller_master](#reseller_master)
- [reseller_metadata](#reseller_metadata)
- [reseller_org_master](#reseller_org_master)
- [reseller_org_master_stg](#reseller_org_master_stg)
- [reseller_research_agent](#reseller_research_agent)
- [ret_brand_map](#ret_brand_map)
- [rule_repositories](#rule_repositories)
- [rules](#rules)
- [rules_metadata](#rules_metadata)
- [rules_parameters](#rules_parameters)
- [rules_profiles](#rules_profiles)
- [sales_insights_metric](#sales_insights_metric)
- [sales_insights_metric_config](#sales_insights_metric_config)
- [saml_message_ids](#saml_message_ids)
- [samsung_audit_history](#samsung_audit_history)
- [sanity_automation_clients](#sanity_automation_clients)
- [schedule_data_event](#schedule_data_event)
- [schedule_details](#schedule_details)
- [schedule_execution_details](#schedule_execution_details)
- [schedule_master](#schedule_master)
- [schedule_pending_status](#schedule_pending_status)
- [schedule_promo_details](#schedule_promo_details)
- [schedule_wbr_details](#schedule_wbr_details)
- [scheduler_controller](#scheduler_controller)
- [scheduler_filters](#scheduler_filters)
- [scheduler_filters_back](#scheduler_filters_back)
- [schema_migrations](#schema_migrations)
- [scrapehero_input_files](#scrapehero_input_files)
- [scrapehero_output_files](#scrapehero_output_files)
- [scrapehero_output_files_format](#scrapehero_output_files_format)
- [search_term_groups](#search_term_groups)
- [search_terms](#search_terms)
- [self_authorized_info_table](#self_authorized_info_table)
- [seller](#seller)
- [seller_attribute](#seller_attribute)
- [sendgrid_apikey](#sendgrid_apikey)
- [sendgrid_events](#sendgrid_events)
- [session_tokens](#session_tokens)
- [share_link_details](#share_link_details)
- [snapshots](#snapshots)
- [state_persistance](#state_persistance)
- [sub_category](#sub_category)
- [subscription_screen_mapping](#subscription_screen_mapping)
- [subscription_type](#subscription_type)
- [summarize_review](#summarize_review)
- [support_ticket](#support_ticket)
- [sv](#sv)
- [teams_feedback](#teams_feedback)
- [teams_user](#teams_user)
- [temp](#temp)
- [temp_product_master_parent_asins](#temp_product_master_parent_asins)
- [test_buy](#test_buy)
- [time_range_favourites](#time_range_favourites)
- [tooltip_config](#tooltip_config)
- [translation_table](#translation_table)
- [ui_config](#ui_config)
- [ui_config_bck](#ui_config_bck)
- [ui_layout](#ui_layout)
- [ui_layout_lbb](#ui_layout_lbb)
- [uiconf](#uiconf)
- [upload_dump](#upload_dump)
- [upload_history](#upload_history)
- [upload_master](#upload_master)
- [upload_type](#upload_type)
- [upload_type_org_config](#upload_type_org_config)
- [user_audit](#user_audit)
- [user_dismissed_messages](#user_dismissed_messages)
- [user_filter_config](#user_filter_config)
- [user_header_config](#user_header_config)
- [user_properties](#user_properties)
- [user_roles](#user_roles)
- [user_tokens](#user_tokens)
- [users](#users)
- [users_details](#users_details)
- [vc_product_master_catalog](#vc_product_master_catalog)
- [viz_as_dataproduct_summs_holistics](#viz_as_dataproduct_summs_holistics)
- [viz_as_dataproduct_summs_specific_week](#viz_as_dataproduct_summs_specific_week)
- [viz_latest_product_details_dump](#viz_latest_product_details_dump)
- [wbr_client_config](#wbr_client_config)
- [wbr_queries](#wbr_queries)
- [wbr_validations_summary](#wbr_validations_summary)
- [webhook](#webhook)
- [weekly_highlight](#weekly_highlight)
- [won_buybox](#won_buybox)

---

## abc

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_type_cd | varchar(20) | Yes |  |  | No |  |
| ui_screen_cd | varchar(40) | Yes |  |  | No |  |
| property_cd | varchar(100) | Yes |  |  | No |  |
| property_label | varchar(10000) | Yes |  |  | No |  |
| url | varchar(200) | Yes |  |  | No |  |
| permission_id | int4(32) | Yes |  |  | No |  |
| icon_name | varchar(40) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| filter_metadata | jsonb | Yes |  |  | No |  |

---

## account

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | int4(32) | No | nextval('i2oretail_dev.account_account_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY, UNIQUE | Yes |  |
| account_name | text | No |  | UNIQUE | Yes |  |
| is_active | bool | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY, UNIQUE | Yes |  |
| source | text | Yes |  |  | No |  |
| created_by | text | Yes |  |  | No |  |
| updated_by | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |

---

## account_activity_otp_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| account_activity_otp_id | int4(32) | No | nextval('i2oretail_dev.account_activity_otp_details_account_activity_otp_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| org_name | varchar(150) | No |  |  | No |  |
| type | varchar(150) | No |  |  | No |  |
| source | varchar(150) | Yes |  |  | No |  |
| marketplace | varchar(150) | No |  |  | No |  |

---

## account_brand

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | int4(32) | No | nextval('i2oretail_dev.account_brand_account_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int8(64) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| brand_id | int8(64) | Yes |  |  | No |  |
| is_active | bool | Yes |  |  | No |  |
| enforcement_provider | text | Yes |  |  | No |  |
| legal_provider | text | Yes |  |  | No |  |
| created_by | text | Yes |  |  | No |  |
| updated_by | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |

---

## account_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.account_config_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| account_id | int8(64) | Yes |  | FOREIGN KEY | No |  |
| min_emails_per_month | int8(64) | Yes |  |  | No |  |
| max_emails_per_month | int8(64) | Yes |  |  | No |  |
| daily_window_from | time | Yes | '08:00:00'::time without time zone |  | No |  |
| daily_window_to | time | Yes | '10:00:00'::time without time zone |  | No |  |
| created_by | text | Yes |  |  | No |  |
| updated_by | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |

---

## account_fields

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| field_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| account_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| field_name | varchar(50) | Yes |  |  | No |  |
| datatype | varchar(50) | Yes |  |  | No |  |
| lookup | varchar(50) | Yes |  |  | No |  |

---

## account_notice_settings

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| weekly_cap | int4(32) | No | 15 |  | No |  |
| new_seller_cap | int4(32) | No | 8 |  | No |  |
| notified_cap | int4(32) | No | 7 |  | No |  |
| n2_spacing_days | int4(32) | No | 4 |  | No |  |
| n3_spacing_days | int4(32) | No | 3 |  | No |  |
| fw_spacing_days | int4(32) | No | 30 |  | No |  |
| region_tz | text | No | 'Asia/Kolkata'::text |  | No |  |

---

## accounts

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| account_name | varchar(50) | Yes |  |  | No |  |
| url | varchar(200) | Yes |  |  | No |  |
| validation_type | varchar(50) | Yes |  |  | No |  |
| dp_source | varchar(50) | Yes |  |  | No |  |
| otp_required | bool | Yes |  |  | No |  |
| account_metadata | json | Yes |  |  | No |  |

---

## add_entries_salestagging

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.add_entries_salestagging_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| code | varchar(100) | Yes |  |  | No |  |
| label | varchar(100) | Yes |  |  | No |  |
| category | varchar(100) | Yes |  |  | No |  |
| module_name | varchar(100) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |

---

## ae_salesanalysisinsights_queries

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## agency

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| agency_id | int4(32) | No | nextval('i2oretail_dev.agency_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| agency_name | varchar(250) | Yes |  |  | No |  |
| agency_alias | varchar(100) | Yes |  |  | No |  |
| agency_subscription_status | varchar(200) | Yes |  |  | No |  |
| subscription_start_date | date | Yes |  |  | No |  |
| subscription_end_date | date | Yes |  |  | No |  |
| agency_banner_logo_name | varchar(200) | Yes |  |  | No |  |

---

## agency_session_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| i2o_id | varchar(100) | No |  | PRIMARY KEY | Yes |  |
| agency_org_id | int4(32) | No |  |  | No |  |
| user_email_id | varchar(100) | No |  |  | No |  |
| agency_access_token | varchar(1000) | No |  |  | No |  |
| token_expiry_time | timestamp | Yes |  |  | No |  |

---

## ai_tokens_per_author

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.ai_tokens_per_author_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| project_name | varchar(255) | No |  | UNIQUE | Yes |  |
| file_path | text | No |  | UNIQUE | Yes |  |
| author | varchar(255) | No |  | UNIQUE | Yes |  |
| tokens | int4(32) | No |  |  | No |  |
| run_date | date | No |  | UNIQUE | Yes |  |

---

## all_sub_categories

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| sub_category | varchar(250) | Yes |  |  | No |  |
| org_id_dp | int4(32) | Yes |  |  | No |  |
| org_name | varchar(100) | Yes |  |  | No |  |

---

## all_sub_categories_bak

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| subcategories | varchar(500) | Yes |  |  | No |  |

---

## app_user_tracking

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| app_user_tracking_id | int4(32) | No | nextval('i2oretail_dev.app_user_tracking_app_user_tracking_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| email_id | varchar(255) | Yes |  |  | No |  |
| page_url | varchar(300) | Yes |  |  | No |  |
| tab_name | varchar(100) | Yes |  |  | No |  |
| tab_index | varchar(50) | Yes |  |  | No |  |
| landing_time | varchar(255) | Yes |  |  | No |  |
| session_duration | varchar(255) | Yes |  |  | No |  |
| exit_time | varchar(255) | Yes |  |  | No |  |
| tab_id | varchar(255) | Yes |  |  | No |  |

---

## application_properties

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| module | varchar(100) | Yes |  |  | No |  |
| property | varchar(100) | No |  | PRIMARY KEY | Yes |  |
| value | varchar(60000) | Yes |  |  | No |  |
| default_value | varchar(200) | Yes |  |  | No |  |
| org_id | int4(32) | No |  | PRIMARY KEY | Yes |  |

---

## atf_standard

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| asin | text | Yes |  |  | No |  |
| image_url | text | Yes |  |  | No |  |
| region_name | text | Yes |  |  | No |  |
| region_code | text | Yes |  |  | No |  |
| product_code | text | Yes |  |  | No |  |
| product_name | text | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| ean | text | Yes |  |  | No |  |
| bullet_points | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| platform | text | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| searchkeywords | text | Yes |  |  | No |  |
| boxtitle | text | Yes |  |  | No |  |
| category_name | text | Yes |  |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |
| file_type | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| long_description | text | Yes |  |  | No |  |
| id | int4(32) | No | nextval('i2oretail_dev.atf_standard_id_seq'::regclass) | PRIMARY KEY | Yes |  |

---

## attachment

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dev.attachment_id_seq'::regclass) |  | No |  |
| entity_id | int4(32) | Yes |  |  | No |  |
| entity | text | Yes |  |  | No |  |
| filename | text | No |  |  | No |  |
| mime_type | text | Yes |  |  | No |  |
| size_bytes | int8(64) | Yes |  |  | No |  |
| url | text | Yes |  |  | No |  |
| raw_data | text | Yes |  |  | No |  |
| notice_type | text | Yes |  |  | No |  |
| metadata | jsonb | Yes |  |  | No |  |
| uploaded_by | text | Yes |  |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |

---

## audit

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| entity | varchar(50) | No |  |  | No |  |
| action | varchar(50) | No |  |  | No |  |
| description | varchar(150) | Yes |  |  | No |  |
| modifier | varchar(50) | No |  |  | No |  |
| modification_date | timestamp | Yes |  |  | No |  |
| row_data | json | Yes |  |  | No |  |
| pk_modified | varchar(200) | Yes |  |  | No |  |

---

## audit_group

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.audit_group_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| createdby | varchar(255) | Yes |  |  | No |  |
| createdon | timestamp | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| processid | int4(32) | Yes |  |  | No |  |

---

## audit_object

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.audit_object_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| table_name | varchar(255) | Yes |  |  | No |  |
| column_name | varchar(255) | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| is_deleted | bool | Yes |  |  | No |  |
| new_value | text | Yes |  |  | No |  |
| old_value | text | Yes |  |  | No |  |
| resource_id | int4(32) | Yes |  |  | No |  |
| auditgroup_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| update_process | varchar(255) | Yes |  |  | No |  |

---

## basic_standard

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| asin | varchar(20) | No |  |  | No |  |
| image_url | text | Yes |  |  | No |  |
| region_name | varchar(100) | Yes |  |  | No |  |
| region_code | varchar(10) | Yes |  |  | No |  |
| product_code | varchar(50) | Yes |  |  | No |  |
| product_name | text | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| ean | varchar(20) | Yes |  |  | No |  |
| bullet_points | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| platform | text | Yes |  |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| searchkeywords | text | Yes |  |  | No |  |
| boxtitle | text | Yes |  |  | No |  |
| category_name | text | Yes |  |  | No |  |

---

## bp_wbr_execution_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| period | date | No |  | PRIMARY KEY | Yes |  |
| org_name | varchar(250) | No |  |  | No |  |
| start_time | timestamptz | Yes |  |  | No |  |
| end_time | timestamptz | Yes |  |  | No |  |
| schedule_status | varchar(250) | Yes |  |  | No |  |
| gcs_location | varchar(250) | Yes |  |  | No |  |
| comments | varchar(250) | Yes |  |  | No |  |

---

## brand_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.brand_master_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| brand | varchar(255) | Yes |  |  | No |  |
| brand_alias | int4(32) | Yes |  | FOREIGN KEY | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| parent_brand | int4(32) | Yes |  | FOREIGN KEY | No |  |
| is_active | varchar(25) | Yes | 'Yes'::character varying |  | No |  |
| marketplace_ids | _int4 | Yes |  |  | No |  |
| brandalias | bytea | Yes |  |  | No |  |
| potential_brand_id | int4(32) | Yes |  | FOREIGN KEY | No |  |

---

## brand_violation_plugin_capture_log

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dev.brand_violation_plugin_capture_log_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| suspect_product_code | text | No |  |  | No |  |
| suspect_product_url | text | No |  |  | No |  |
| suspect_brand | text | No |  |  | No |  |
| master_product_code | text | Yes |  |  | No |  |
| violation_type | _text | No |  |  | No |  |
| tags | text | Yes |  |  | No |  |
| keywords | text | Yes |  |  | No |  |
| screenshot_gcs_url | text | Yes |  |  | No |  |
| captured_at | timestamptz | No | now() |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| reviewed_by | varchar(255) | Yes |  |  | No |  |

---

## brand_violations_filtered

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | Yes |  |  | No | i2o App Org ID |
| org_name | text | Yes |  |  | No | i2o App Org name |
| marketplace | text | Yes |  |  | No | Platform e.g. Amazon |
| region | text | Yes |  |  | No | Region e.g. US |
| period | date | Yes |  |  | No | Date of Reporting - YYYY-MM-DD |
| reporting_range | text | Yes |  |  | No | Frequency of job E.g. weekly |
| suspect_product_code | text | Yes |  |  | No | Suspect Product Code |
| suspect_url | text | Yes |  |  | No | Suspect URL |
| suspect_title | text | Yes |  |  | No | Suspect Title |
| suspect_brand | text | Yes |  |  | No | Suspect Brand |
| suspect_reseller_name | text | Yes |  |  | No | Suspect Reseller Name |
| product_code | text | Yes |  |  | No | Master Product Code |
| master_url | text | Yes |  |  | No | Master Product URL |
| master_brand | text | Yes |  |  | No | Master Brand |
| product_title | text | Yes |  |  | No | Product Title |
| product_tags | text | Yes |  |  | No | Product Tags |
| short_name | text | Yes |  |  | No | Short Name |
| category | text | Yes |  |  | No | Category |
| confidence_score | float8(53) | Yes |  |  | No | Confidence Score for Violation |
| difference | text | Yes |  |  | No | Comparison Difference |
| violation_type | text | Yes |  |  | No | Violation Type E.g. Duplicate, Bundle, Trademark |
| valid_detection | text | Yes |  |  | No | Is a Valid Detection - Yes or No |
| corrected_product_code | text | Yes |  |  | No | Corrected Master Product Code By RT Team |
| comment | text | Yes |  |  | No | Comments Provided |
| reviewed_by | text | Yes |  |  | No | Name of the Reviewer |
| ds_team_comments | text | Yes |  |  | No | DS Team Comments |
| suspect_reseller_url | text | Yes |  |  | No | Suspect Reseller URL |
| corrected_asin | text | Yes |  |  | No |  |
| suspect_reseller_id | text | Yes |  |  | No |  |

---

## brand_violations_filtered_20250627

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | Yes |  |  | No |  |
| org_name | text | Yes |  |  | No |  |
| marketplace | text | Yes |  |  | No |  |
| region | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| reporting_range | text | Yes |  |  | No |  |
| suspect_product_code | text | Yes |  |  | No |  |
| suspect_url | text | Yes |  |  | No |  |
| suspect_title | text | Yes |  |  | No |  |
| suspect_brand | text | Yes |  |  | No |  |
| suspect_reseller_name | text | Yes |  |  | No |  |
| product_code | text | Yes |  |  | No |  |
| master_url | text | Yes |  |  | No |  |
| master_brand | text | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| product_tags | text | Yes |  |  | No |  |
| short_name | text | Yes |  |  | No |  |
| category | text | Yes |  |  | No |  |
| confidence_score | float8(53) | Yes |  |  | No |  |
| difference | text | Yes |  |  | No |  |
| violation_type | text | Yes |  |  | No |  |
| valid_detection | text | Yes |  |  | No |  |
| corrected_product_code | text | Yes |  |  | No |  |
| comment | text | Yes |  |  | No |  |
| reviewed_by | text | Yes |  |  | No |  |
| ds_team_comments | text | Yes |  |  | No |  |

---

## brand_violations_filtered_backup

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| marketplace | text | Yes |  |  | No |  |
| region | text | Yes |  |  | No |  |
| product_code | text | Yes |  |  | No |  |
| master_url | text | Yes |  |  | No |  |
| short_name | text | Yes |  |  | No |  |
| period | text | Yes |  |  | No |  |
| reporting_range | text | Yes |  |  | No |  |
| org_name | text | Yes |  |  | No |  |
| master_brand | text | Yes |  |  | No |  |
| category | text | Yes |  |  | No |  |
| master_title | text | Yes |  |  | No |  |
| product_tags | text | Yes |  |  | No |  |
| violation_type | text | Yes |  |  | No |  |
| suspect_product_code | text | Yes |  |  | No |  |
| suspect_url | text | Yes |  |  | No |  |
| suspect_title | text | Yes |  |  | No |  |
| suspect_brand | text | Yes |  |  | No |  |
| suspect_reseller_name | text | Yes |  |  | No |  |
| suspect_reseller_url | text | Yes |  |  | No |  |
| comment | text | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| confidence_score | text | Yes |  |  | No |  |
| differences | text | Yes |  |  | No |  |
| reviewed_by | text | Yes |  |  | No |  |
| valid_detection | text | Yes |  |  | No |  |
| corrected_product_code | text | Yes |  |  | No |  |

---

## brand_violations_filtered_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | Yes |  |  | No |  |
| org_name | varchar | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | No |  |
| region | varchar | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| reporting_range | varchar | Yes |  |  | No |  |
| suspect_product_code | varchar | Yes |  |  | No |  |
| suspect_url | varchar | Yes |  |  | No |  |
| suspect_title | varchar | Yes |  |  | No |  |
| suspect_brand | varchar | Yes |  |  | No |  |
| suspect_reseller_name | varchar | Yes |  |  | No |  |
| product_code | varchar | Yes |  |  | No |  |
| master_url | varchar | Yes |  |  | No |  |
| master_brand | varchar | Yes |  |  | No |  |
| product_title | varchar | Yes |  |  | No |  |
| product_tags | float8(53) | Yes |  |  | No |  |
| short_name | text | Yes |  |  | No |  |
| category | text | Yes |  |  | No |  |
| confidence_score | varchar | Yes |  |  | No |  |
| difference | varchar | Yes |  |  | No |  |
| violation_type | varchar | Yes |  |  | No |  |
| valid_detection | varchar | Yes |  |  | No |  |
| corrected_product_code | varchar | Yes |  |  | No |  |
| comment | varchar | Yes |  |  | No |  |
| reviewed_by | varchar | Yes |  |  | No |  |
| suspect_reseller_url | text | Yes |  |  | No |  |

---

## brand_violations_interactions

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| suspect_product_code | text | No |  | PRIMARY KEY | Yes |  |
| user_name | text | No |  | PRIMARY KEY | Yes |  |
| violation_types | jsonb | Yes |  |  | No |  |
| selected_master_rank | int4(32) | Yes |  |  | No |  |
| custom_master_url | text | Yes |  |  | No |  |
| action_taken | text | Yes |  |  | No |  |
| inconclusive | bool | Yes | false |  | No |  |
| partial_match | bool | Yes | false |  | No |  |
| notes | text | Yes |  |  | No |  |
| updated_at | timestamptz | Yes | CURRENT_TIMESTAMP |  | No |  |
| created_at | timestamptz | Yes | CURRENT_TIMESTAMP |  | No |  |
| follow_up_required | bool | Yes | false |  | No |  |

---

## brand_violations_review

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| suspect_product_code | text | No |  |  | No |  |
| org_id | int4(32) | No |  |  | No |  |
| org_name | text | No |  |  | Yes |  |
| marketplace | text | No |  |  | No |  |
| region | text | No |  |  | No |  |
| period | date | No |  |  | Yes |  |
| reporting_range | text | No |  |  | No |  |
| product_code | text | No |  |  | No |  |
| master_url | text | No |  |  | No |  |
| master_brand | text | No |  |  | No |  |
| product_title | text | No |  |  | No |  |
| suspect_url | text | No |  |  | No |  |
| suspect_title | text | No |  |  | No |  |
| suspect_brand | text | No |  |  | No |  |
| suspect_images | text | Yes |  |  | No |  |
| suspect_reseller_name | text | Yes |  |  | No |  |
| confidence_score | float8(53) | No |  |  | No |  |
| difference | text | Yes |  |  | No |  |
| valid_detection | bool | No |  |  | No |  |
| violation_type | text | Yes |  |  | No |  |
| corrected_product_code | text | Yes |  |  | No |  |
| top_5_masters | text | No |  |  | No |  |
| comment | text | Yes |  |  | No |  |
| reviewed_by | text | Yes |  |  | No |  |
| priority_flag | bool | Yes | false |  | No |  |
| master_asin_1 | text | Yes |  |  | No |  |
| master_asin_2 | text | Yes |  |  | No |  |
| master_asin_3 | text | Yes |  |  | No |  |
| master_asin_4 | text | Yes |  |  | No |  |
| master_asin_5 | text | Yes |  |  | No |  |
| master_brand_1 | text | Yes |  |  | No |  |
| master_title_1 | text | Yes |  |  | No |  |
| master_images_1 | text | Yes |  |  | No |  |
| master_brand_2 | text | Yes |  |  | No |  |
| master_title_2 | text | Yes |  |  | No |  |
| master_images_2 | text | Yes |  |  | No |  |
| master_brand_3 | text | Yes |  |  | No |  |
| master_title_3 | text | Yes |  |  | No |  |
| master_images_3 | text | Yes |  |  | No |  |
| master_brand_4 | text | Yes |  |  | No |  |
| master_title_4 | text | Yes |  |  | No |  |
| master_images_4 | text | Yes |  |  | No |  |
| master_brand_5 | text | Yes |  |  | No |  |
| master_title_5 | text | Yes |  |  | No |  |
| master_images_5 | text | Yes |  |  | No |  |
| action_taken | text | Yes |  |  | No |  |
| inconclusive | bool | Yes | false |  | No |  |
| violation_types | jsonb | Yes |  |  | No |  |
| selected_master_rank | int4(32) | Yes |  |  | No |  |
| custom_master_url | text | Yes |  |  | No |  |
| user_name | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |
| partial_match | bool | No | false |  | No |  |
| asin | varchar(255) | Yes |  |  | No |  |
| selected_master_asin | varchar(500) | Yes |  |  | No |  |
| rt_team_status | varchar(50) | Yes | 'Pending'::character varying |  | No |  |
| notes | text | Yes |  |  | No |  |
| suspect_reseller_url | text | Yes |  |  | No |  |

---

## brand_violations_stg_dev_final

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | Yes |  | UNIQUE | Yes |  |
| org_name | text | Yes |  |  | No |  |
| marketplace | text | Yes |  | UNIQUE | Yes |  |
| region | text | Yes |  | UNIQUE | Yes |  |
| period | date | Yes |  | UNIQUE | Yes |  |
| reporting_range | text | Yes |  |  | No |  |
| suspect_product_code | text | Yes |  | UNIQUE | Yes |  |
| suspect_url | text | Yes |  |  | No |  |
| suspect_title | text | Yes |  |  | No |  |
| suspect_brand | text | Yes |  |  | No |  |
| suspect_reseller_name | text | Yes |  |  | No |  |
| product_code | text | Yes |  | UNIQUE | Yes |  |
| master_url | text | Yes |  |  | No |  |
| master_brand | text | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| confidence_score | text | Yes |  |  | No |  |
| difference | text | Yes |  |  | No |  |
| violation_type | text | Yes |  |  | No |  |
| valid_detection | text | Yes |  |  | No |  |
| corrected_product_code | text | Yes |  |  | No |  |
| comment | text | Yes |  |  | No |  |
| reviewed_by | text | Yes |  |  | No |  |
| ds_team_comments | text | Yes |  |  | No |  |

---

## bucket4j_buckets

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No |  | PRIMARY KEY | Yes |  |
| state | bytea | Yes |  |  | No |  |

---

## business_unit

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| business_unit_id | int4(32) | No | nextval('i2oretail_dev.business_unit_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| business_name | varchar(255) | No |  |  | No |  |
| legal_entity_name | varchar(255) | Yes |  |  | No |  |
| address | text | Yes |  |  | No |  |
| billing_address | text | Yes |  |  | No |  |
| is_active | bool | Yes | true |  | No |  |
| is_trial_period | bool | Yes | false |  | No |  |
| created_on | timestamp | Yes | CURRENT_TIMESTAMP |  | No |  |
| created_by | varchar(100) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes | CURRENT_TIMESTAMP |  | No |  |
| last_modified_by | varchar(100) | Yes |  |  | No |  |

---

## buy_box_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| date_and_time | date | Yes |  |  | No |  |
| latest_bbx_status | int4(32) | Yes |  |  | No |  |
| bbx_percentage | int4(32) | Yes |  |  | No |  |
| hourly_bbx_status | json | Yes |  |  | No |  |
| current_bbx_winner | varchar | Yes |  |  | No |  |
| prev_bbx_winner | varchar | Yes |  |  | No |  |
| current_bbx_price | int4(32) | Yes |  |  | No |  |
| previous_bbx_price | int4(32) | Yes |  |  | No |  |

---

## buybox_delivery_reports

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.buybox_delivery_reports_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| region | varchar | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | No |  |
| msg_identifier | varchar | Yes |  |  | No |  |
| attempted_at | timestamptz | Yes |  |  | No |  |
| report_status | varchar | Yes |  |  | No |  |
| retry_count | int4(32) | Yes |  |  | No |  |
| data | json | Yes |  |  | No |  |

---

## catalog_temp

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_type | varchar(255) | Yes |  |  | No |  |
| region | varchar(255) | Yes |  |  | No |  |
| marketplace | varchar(255) | Yes |  |  | No |  |
| asin | bpchar(10) | Yes |  |  | No |  |
| attributes | json | Yes |  |  | No |  |
| dimensions | json | Yes |  |  | No |  |
| identifiers | json | Yes |  |  | No |  |
| images | json | Yes |  |  | No |  |
| producttypes | json | Yes |  |  | No |  |
| relationships | json | Yes |  |  | No |  |
| salesranks | json | Yes |  |  | No |  |
| summaries | json | Yes |  |  | No |  |
| vendordetails | json | Yes |  |  | No |  |
| parentasins | json | Yes |  |  | No |  |
| childasins | json | Yes |  |  | No |  |
| reporting_range | varchar(255) | Yes |  |  | No |  |
| product_code_type | varchar(255) | Yes |  |  | No |  |
| source_system_id | varchar(255) | Yes |  |  | No |  |

---

## category

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| category_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| category | varchar(150) | Yes |  |  | No |  |
| category_title | varchar(250) | Yes |  |  | No |  |
| category_description | varchar(350) | Yes |  |  | No |  |
| source | varchar(50) | Yes |  |  | No |  |
| query_id | int4(32) | Yes |  | FOREIGN KEY | No |  |

---

## category_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.category_master_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| organization_category | varchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| marketplace_category | varchar(255) | Yes |  |  | No |  |
| is_active | varchar(25) | Yes | 'Yes'::character varying |  | No |  |
| category | varchar(255) | Yes |  |  | No |  |
| marketplace_ids | _int4 | Yes |  |  | No |  |
| organization | bytea | Yes |  |  | No |  |

---

## categorymaster_marketplaceids

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| categorymaster_id | int4(32) | No |  | FOREIGN KEY | No |  |
| marketplace_ids | int4(32) | Yes |  |  | No |  |

---

## channel

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| channel_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| channel | varchar(50) | Yes |  | UNIQUE | Yes |  |
| channel_type_id | int4(32) | Yes |  |  | No |  |

---

## client_platform_category_mapping

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.client_platform_category_mapping_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| marketplace_category | varchar(255) | Yes |  |  | No |  |
| category_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| is_active | varchar(255) | Yes |  |  | No |  |
| clientcategory | bytea | Yes |  |  | No |  |

---

## cloud_scheduler_execution_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| schedule_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| period | date | No |  | PRIMARY KEY | Yes |  |
| time_of_day | int4(32) | No |  | PRIMARY KEY | Yes |  |
| reporting_range | varchar(255) | Yes |  |  | No |  |
| gcs_location | varchar | Yes |  |  | No |  |
| archive_location | varchar(255) | Yes |  |  | No |  |
| stage | varchar(255) | Yes |  |  | No |  |
| status | varchar(255) | Yes |  |  | No |  |
| metadata | json | Yes |  |  | No |  |
| detail_id | int4(32) | Yes |  |  | No |  |
| start_datetime | timestamptz | Yes |  |  | No |  |
| end_datetime | timestamp | Yes |  |  | No |  |
| retry_config | json | Yes |  |  | No |  |
| retry_count | int4(32) | Yes |  |  | No |  |
| errors | json | Yes |  |  | No |  |
| run_id | uuid | No |  |  | No |  |
| report_id | int4(32) | Yes |  | FOREIGN KEY | No |  |

---

## col

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| column_id | int4(32) | Yes |  |  | No |  |
| db_column_name | varchar(100) | Yes |  |  | No |  |
| label | varchar(150) | Yes |  |  | No |  |
| datatype | varchar(30) | Yes |  |  | No |  |
| format | varchar(30) | Yes |  |  | No |  |
| width | int4(32) | Yes |  |  | No |  |
| suppress_menu | bool | Yes |  |  | No |  |
| cell_class | varchar(50) | Yes |  |  | No |  |
| cell_style | varchar(500) | Yes |  |  | No |  |
| header_class | varchar(50) | Yes |  |  | No |  |

---

## column_definition

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| column_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| db_column_name | varchar(255) | No |  |  | No |  |
| label | varchar(255) | No |  |  | No |  |
| datatype | varchar(255) | Yes |  |  | No |  |
| format | varchar(255) | Yes |  |  | No |  |
| width | int4(32) | Yes |  |  | No |  |
| suppress_menu | bool | Yes |  |  | No |  |
| cell_class | varchar(255) | Yes |  |  | No |  |
| cell_style | varchar(255) | Yes |  |  | No |  |
| header_class | varchar(255) | Yes |  |  | No |  |

---

## columnbackup

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| column_id | int4(32) | Yes |  |  | No |  |
| db_column_name | varchar(100) | Yes |  |  | No |  |
| label | varchar(150) | Yes |  |  | No |  |
| datatype | varchar(30) | Yes |  |  | No |  |
| format | varchar(30) | Yes |  |  | No |  |
| width | int4(32) | Yes |  |  | No |  |
| suppress_menu | bool | Yes |  |  | No |  |
| cell_class | varchar(50) | Yes |  |  | No |  |
| cell_style | varchar(500) | Yes |  |  | No |  |
| header_class | varchar(50) | Yes |  |  | No |  |

---

## component

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| component_id | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| title | varchar(255) | Yes |  |  | No |  |
| query_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| module_name | varchar(255) | Yes |  |  | No |  |

---

## context

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| context_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| context_name | varchar(255) | No |  | UNIQUE | Yes |  |

---

## data_event_backup

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| report_identifier | varchar(45) | Yes |  |  | No |  |
| org_type_cd | varchar(10) | Yes |  |  | No |  |
| data_event | varchar(45) | Yes |  |  | No |  |
| process | json | Yes |  |  | No |  |
| query_id | int4(32) | Yes |  |  | No |  |
| id | int4(32) | Yes |  |  | No |  |
| latest_report_only | bpchar(1) | Yes |  |  | No |  |

---

## data_feed_feature

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| data_feed_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| feature_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| optional | bool | Yes |  |  | No |  |

---

## data_feeds

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| data_feed_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| data_feed_name | varchar(50) | Yes |  |  | No |  |
| account_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| data_feed_category | varchar(100) | Yes |  |  | No |  |
| data_feed_metadata | json | Yes |  |  | No |  |

---

## data_last_publish

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| publish_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| last_publish_time | timestamp | Yes |  |  | No |  |
| publish_table_name | varchar(255) | Yes |  |  | No |  |
| publish_target_name | varchar(255) | Yes |  |  | No |  |
| publisher | varchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | Yes |  |  | No |  |

---

## dataload_allocation

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| dataload_allocation_id | int4(32) | No | nextval('i2oretail_dev.dataload_allocation_dataload_allocation_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| period | timestamp | Yes |  |  | No |  |
| target_date | timestamp | Yes |  |  | No |  |
| data_load_allocation | varchar(150) | Yes |  |  | No |  |
| sanity_allocation | varchar(150) | Yes |  |  | No |  |

---

## dataproduct_request_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| dataproduct_request_id | int4(32) | No | nextval('i2oretail_dev.dataproduct_request_details_dataproduct_request_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| user_name | varchar | No |  |  | No |  |
| email_id | varchar | No |  |  | No |  |
| sub_category | varchar | No |  |  | No |  |
| brand_name | varchar | No |  |  | No |  |
| submission_time | varchar | No |  |  | No |  |
| action_item | varchar | No |  |  | No |  |
| comments | varchar | No |  |  | No |  |

---

## dataproduct_test

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.dataproduct_test_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| name | varchar | No |  |  | No |  |

---

## digishare_combined_metrics

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| image_url | varchar(255) | Yes |  |  | No |  |
| region_name | varchar(255) | Yes |  |  | No |  |
| region_code | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| product_name | varchar(255) | Yes |  |  | No |  |
| product_code | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| ean | varchar(255) | Yes |  |  | No |  |
| product_title | varchar(255) | Yes |  |  | No |  |
| bullet_points | text | Yes |  |  | No |  |
| searchkeywords | text | Yes |  |  | No |  |
| boxtitle | text | Yes |  |  | No |  |
| category_name | varchar(255) | Yes |  |  | No |  |
| long_description | text | Yes |  |  | No |  |
| images_gallery | text | Yes |  |  | No |  |
| images_background | text | Yes |  |  | No |  |
| highlights | text | Yes |  |  | No |  |
| preview_images | varchar(255) | Yes |  |  | No |  |
| video_urls | varchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| platform | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| period | timestamp | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| updated_at | varchar(255) | Yes | now() |  | No |  |
| reference_id | int4(32) | No | nextval('i2oretail_dev.digishare_combined_metrics_reference_id_seq'::regclass) |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| source | varchar(255) | Yes |  |  | No |  |
| metadata | jsonb | Yes |  |  | No |  |

---

## digishare_combined_metrics1

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| asin | varchar(20) | Yes |  |  | No |  |
| image_url | text | Yes |  |  | No |  |
| region_name | varchar(100) | Yes |  |  | No |  |
| region_code | varchar(10) | Yes |  |  | No |  |
| product_code | varchar(50) | Yes |  |  | No |  |
| product_name | text | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| ean | varchar(20) | Yes |  |  | No |  |
| bullet_points | text | Yes |  |  | No |  |
| images_gallery | text | Yes |  |  | No |  |
| images_background | text | Yes |  |  | No |  |
| highlights | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| platform | text | Yes |  |  | No |  |
| updated_at | timestamptz | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| reference_id | int4(32) | Yes |  |  | No |  |
| boxtitle | text | Yes |  |  | No |  |
| category_name | text | Yes |  |  | No |  |
| searchkeywords | text | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| preview_images | text | Yes |  |  | No |  |
| video_urls | text | Yes |  |  | No |  |
| file_type | text | Yes |  |  | No |  |
| product_description | varchar(255) | Yes |  |  | No |  |

---

## digishare_combined_metrics_2025_09_15

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| image_url | text | Yes |  |  | No |  |
| region_name | text | Yes |  |  | No |  |
| region_code | text | Yes |  |  | No |  |
| product_name | text | Yes |  |  | No |  |
| product_code | text | Yes |  |  | No |  |
| ean | text | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| bullet_points | text | Yes |  |  | No |  |
| searchkeywords | text | Yes |  |  | No |  |
| boxtitle | text | Yes |  |  | No |  |
| category_name | text | Yes |  |  | No |  |
| long_description | text | Yes |  |  | No |  |
| images_gallery | text | Yes |  |  | No |  |
| images_background | text | Yes |  |  | No |  |
| highlights | text | Yes |  |  | No |  |
| preview_images | text | Yes |  |  | No |  |
| video_urls | text | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| platform | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| created_at | timestamptz | Yes |  |  | No |  |
| updated_at | timestamptz | Yes |  |  | No |  |
| reference_id | int4(32) | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| source | varchar(255) | Yes |  |  | No |  |
| metadata | jsonb | Yes |  |  | No |  |

---

## digishare_combined_metrics_26_july

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| asin | text | Yes |  |  | No |  |
| image_url | text | Yes |  |  | No |  |
| region_name | text | Yes |  |  | No |  |
| region_code | text | Yes |  |  | No |  |
| product_name | text | Yes |  |  | No |  |
| product_code | text | Yes |  |  | No |  |
| ean | text | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| bullet_points | text | Yes |  |  | No |  |
| searchkeywords | text | Yes |  |  | No |  |
| boxtitle | text | Yes |  |  | No |  |
| category_name | text | Yes |  |  | No |  |
| long_description | text | Yes |  |  | No |  |
| images_gallery | text | Yes |  |  | No |  |
| images_background | text | Yes |  |  | No |  |
| highlights | text | Yes |  |  | No |  |
| preview_images | text | Yes |  |  | No |  |
| video_urls | text | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| platform | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| created_at | timestamptz | Yes |  |  | No |  |
| updated_at | timestamptz | Yes |  |  | No |  |
| reference_id | int4(32) | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| source | varchar(255) | Yes |  |  | No |  |

---

## digishare_combined_metrics_bulk_load

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.digishare_combined_metrics_bulk_load_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| asin | varchar(20) | Yes |  |  | No |  |
| image_url | varchar | Yes |  |  | No |  |
| region_name | varchar(100) | Yes |  |  | No |  |
| region_code | varchar(10) | Yes |  |  | No |  |
| product_code | varchar(50) | Yes |  |  | No |  |
| product_name | varchar | Yes |  |  | No |  |
| product_title | varchar | Yes |  |  | No |  |
| product_description | varchar | Yes |  |  | No |  |
| ean | varchar(20) | Yes |  |  | No |  |
| bullet_points | varchar | Yes |  |  | No |  |
| images_gallery | varchar | Yes |  |  | No |  |
| images_background | varchar | Yes |  |  | No |  |
| highlights | varchar | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| platform | varchar | Yes |  |  | No |  |
| updated_at | timestamptz | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| reference_id | int4(32) | Yes |  |  | No |  |
| boxtitle | varchar | Yes |  |  | No |  |
| category_name | varchar | Yes |  |  | No |  |
| searchkeywords | varchar | Yes |  |  | No |  |
| video_list | varchar | Yes |  |  | No |  |

---

## digishare_combined_metrics_load_test

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| asin | text | Yes |  |  | No |  |
| image_url | text | Yes |  |  | No |  |
| region_name | text | Yes |  |  | No |  |
| region_code | text | Yes |  |  | No |  |
| product_name | text | Yes |  |  | No |  |
| product_code | text | Yes |  |  | No |  |
| ean | text | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| bullet_points | text | Yes |  |  | No |  |
| searchkeywords | text | Yes |  |  | No |  |
| boxtitle | text | Yes |  |  | No |  |
| category_name | text | Yes |  |  | No |  |
| long_description | text | Yes |  |  | No |  |
| images_gallery | text | Yes |  |  | No |  |
| images_background | text | Yes |  |  | No |  |
| highlights | text | Yes |  |  | No |  |
| preview_images | text | Yes |  |  | No |  |
| video_urls | text | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| platform | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| created_at | timestamptz | Yes |  |  | No |  |
| updated_at | timestamptz | Yes |  |  | No |  |
| reference_id | int4(32) | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| source | varchar(255) | Yes |  |  | No |  |

---

## digishare_combined_metrics_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| asin | varchar(20) | Yes |  |  | No |  |
| image_url | text | Yes |  |  | No |  |
| region_name | varchar(100) | Yes |  |  | No |  |
| region_code | varchar(10) | Yes |  |  | No |  |
| product_code | varchar(50) | Yes |  |  | No |  |
| product_name | text | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| ean | varchar(20) | Yes |  |  | No |  |
| bullet_points | text | Yes |  |  | No |  |
| images_gallery | text | Yes |  |  | No |  |
| images_background | text | Yes |  |  | No |  |
| highlights | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| platform | text | Yes |  |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| category_name | text | Yes |  |  | No |  |
| searchkeywords | text | Yes |  |  | No |  |
| boxtitle | text | Yes |  |  | No |  |
| preview_images | text | Yes |  |  | No |  |
| video_urls | text | Yes |  |  | No |  |
| file_type | text | Yes |  |  | No |  |

---

## digishare_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| file_type | text | Yes |  |  | No |  |
| asin | text | Yes |  |  | No |  |
| platform | text | Yes |  |  | No |  |
| region | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| updated_at | timestamptz | Yes |  |  | No |  |

---

## digishare_test

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.digishare_test_digi_share_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| asin | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| bullet_points | text | Yes |  |  | No |  |
| ean | varchar(255) | Yes |  |  | No |  |
| highlights | text | Yes |  |  | No |  |
| image_url | text | Yes |  |  | No |  |
| images_background | text | Yes |  |  | No |  |
| images_gallery | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| platform | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| product_name | text | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| region_code | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| region_name | varchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| category_name | varchar(255) | Yes |  |  | No |  |
| product_description | text | Yes |  |  | No |  |
| updated_at | timestamptz | Yes |  |  | No |  |

---

## distribution_list

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| distribution_list_id | int4(32) | No | nextval('i2oretail_dev.distribution_list_distribution_list_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| name | varchar(255) | Yes |  |  | Yes |  |
| emails | varchar(65000) | Yes |  |  | No |  |
| emails_count | int4(32) | Yes |  |  | No |  |
| description | varchar(500) | Yes |  |  | No |  |
| created_by_user_email | varchar(255) | Yes |  |  | No |  |
| updated_by_user_email | varchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | Yes |  |
| is_deleted | bool | No |  |  | No |  |
| creation_date | timestamp | Yes |  |  | No |  |
| last_updated | timestamp | Yes |  |  | No |  |
| list_type | varchar(255) | Yes |  |  | No |  |

---

## distribution_list_schedule_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| distribution_list_id | int4(32) | No |  | FOREIGN KEY | No |  |
| schedule_id | int4(32) | No |  | FOREIGN KEY | No |  |

---

## drop_temp

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | varchar(500) | Yes |  |  | No |  |
| created_by | varchar(500) | Yes |  |  | No |  |
| created_on | varchar(500) | Yes |  |  | No |  |
| last_modified_by | varchar(500) | Yes |  |  | No |  |
| last_modified_on | varchar(500) | Yes |  |  | No |  |
| customer_name | varchar(500) | Yes |  |  | No |  |
| i2o_product_id | varchar(500) | Yes |  |  | No |  |
| match_timestamp | varchar(500) | Yes |  |  | No |  |
| platform | varchar(500) | Yes |  |  | No |  |
| product_code | varchar(500) | Yes |  |  | No |  |
| product_match_status | varchar(500) | Yes |  |  | No |  |
| product_title | varchar(500) | Yes |  |  | No |  |
| region | varchar(500) | Yes |  |  | No |  |
| source_product_url | varchar(500) | Yes |  |  | No |  |
| status_code | varchar(500) | Yes |  |  | No |  |
| target_product_code | varchar(500) | Yes |  |  | No |  |
| target_product_url | varchar(1000) | Yes |  |  | No |  |

---

## ecom_pltfrm

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| ecom_pltfrm_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| ecom_pltfm_name | varchar(40) | No |  | UNIQUE | Yes |  |
| ecom_pltfm_desc | text | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| created_by | varchar(100) | Yes |  |  | No |  |
| updated_by | varchar(100) | Yes |  |  | No |  |

---

## email_attachment

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dev.email_attachment_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| email_message_id | int8(64) | Yes |  | FOREIGN KEY | No |  |
| filename | text | No |  |  | No |  |
| mime_type | text | Yes |  |  | No |  |
| size_bytes | int8(64) | Yes |  |  | No |  |
| url | text | Yes |  |  | No |  |
| raw_data | text | Yes |  |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |
| published_at | timestamptz | Yes |  |  | No |  |
| publish_id | text | Yes |  |  | No |  |
| agent_status | text | Yes |  |  | No |  |
| is_invoice | bool | Yes |  |  | No |  |
| invoice_status_detail | text | Yes |  |  | No |  |

---

## email_message

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dev.email_message_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| message_id | text | Yes |  |  | No |  |
| in_reply_to | text | Yes |  |  | No |  |
| reference_ids | text | Yes |  |  | No |  |
| subject | text | No |  |  | No |  |
| from_name | text | Yes |  |  | No |  |
| from_email | text | No |  |  | No |  |
| to_email | text | No |  |  | No |  |
| reply_to_list | text | Yes |  |  | No |  |
| email_date | timestamptz | No |  |  | No |  |
| body_text | text | Yes |  |  | No |  |
| body_html | text | Yes |  |  | No |  |
| direction | text | No |  |  | No |  |
| status | text | Yes |  |  | No |  |
| headers | jsonb | Yes |  |  | No |  |
| custom_args | jsonb | Yes |  |  | No |  |
| correlation_id | text | Yes |  |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |
| entity_id | text | Yes |  |  | No |  |
| is_read | bool | Yes |  |  | No |  |

---

## enforcement_queue

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dev.enforcement_queue_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| account_id | int4(32) | No |  |  | Yes |  |
| enforcement_tracker_id | int4(32) | No |  |  | Yes |  |
| week_start_date | date | No |  |  | Yes |  |
| position | int4(32) | No |  |  | No |  |
| bucket | text | No |  |  | Yes |  |
| due_at | timestamptz | Yes |  |  | No |  |
| send_at | timestamptz | No |  |  | No |  |
| status | text | No | 'queued'::text |  | No |  |
| css | bool | No | false |  | No |  |
| notes | text | Yes |  |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| status_detail | text | Yes |  |  | No |  |
| mode | text | Yes |  |  | No |  |

---

## enforcement_queue_stats

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| week_start_date | date | No |  | PRIMARY KEY | Yes |  |
| target_n1 | int4(32) | No |  |  | No |  |
| scheduled_n1 | int4(32) | No | 0 |  | No |  |
| accumulated_shortfall | int4(32) | No | 0 |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |

---

## enforecemt

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| reseller_name | varchar(255) | Yes |  |  | No |  |
| reseller_id | varchar(255) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| reporting_range | varchar | Yes |  |  | No |  |
| scrape_timestamp | timestamptz | Yes |  |  | No |  |
| map | float8(53) | Yes |  |  | No |  |
| listing_price | float8(53) | Yes |  |  | No |  |
| status | varchar(255) | Yes |  |  | No |  |
| days_in_violation | varchar | Yes |  |  | No |  |
| violation_detection_date | timestamptz | Yes |  |  | No |  |
| metadata | jsonb | Yes |  |  | No |  |
| created_by | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes |  |  | No |  |
| history_data | jsonb | Yes |  |  | No |  |
| seven_day_trend | jsonb | Yes |  |  | No |  |
| current_buybox_winner_reseller_status | varchar | Yes |  |  | No |  |
| is_automation_paused | bool | Yes |  |  | No |  |
| time_of_day | int4(32) | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |

---

## event_definition

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.event_definition_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_at | timestamp | Yes |  |  | No |  |
| cron_expression | varchar(255) | Yes |  |  | No |  |
| description | varchar(255) | Yes |  |  | No |  |
| direct_bq_query | varchar(15000) | Yes |  |  | No |  |
| direct_beam_query | varchar(15000) | Yes |  |  | No |  |
| event_category | varchar | Yes |  |  | No |  |
| event_dataset | varchar(255) | Yes |  |  | No |  |
| event_frequency | varchar(255) | Yes |  |  | No |  |
| is_enabled | bool | Yes |  |  | No |  |
| metric_impacted | varchar(255) | Yes |  |  | No |  |
| modified_at | timestamp | Yes |  |  | No |  |
| monitor_json | jsonb | Yes |  |  | No |  |
| name | varchar(255) | Yes |  |  | No |  |
| skip_bq_query_building | bool | Yes |  |  | No |  |
| skip_beam_query_building | bool | Yes |  |  | No |  |
| skip_beam_sql | bool | Yes |  |  | No |  |
| source_json | jsonb | Yes |  |  | No |  |
| tracked | int4(32) | Yes |  |  | No |  |

---

## event_has_organization

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| event_id | int4(32) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| project_id | varchar | Yes |  |  | No |  |
| event_status | varchar | Yes |  |  | No |  |

---

## event_results

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.event_results_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| name | text | No |  |  | No |  |
| message | text | No |  |  | No |  |
| generated_at | timestamp | No | now() |  | No |  |

---

## event_types

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.event_types_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| name | text | No |  |  | No |  |
| message | text | No |  |  | No |  |
| source_location | bpchar(500) | Yes |  |  | No |  |
| select_fields | bpchar(800) | Yes |  |  | No |  |
| column_and_values | varchar(1000) | Yes |  |  | No |  |
| date_field | varchar(500) | Yes |  |  | No |  |
| monitor_field | varchar(500) | Yes |  |  | No |  |
| monitor_field_type | varchar(500) | Yes |  |  | No |  |
| condition_rules | varchar(1000) | Yes |  |  | No |  |
| cadence | varchar(50) | Yes |  |  | No |  |
| display_list | varchar(500) | Yes |  |  | No |  |
| created_at | timestamp | No | now() |  | No |  |
| is_enabled | bool | Yes | true |  | No |  |

---

## events

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.events_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| event_id | int4(32) | Yes |  |  | No |  |
| result_json | text | Yes |  |  | No |  |
| generated_at | timestamp | No | now() |  | No |  |

---

## events_history

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| job_id | uuid | Yes |  |  | No |  |
| parameters | text | Yes |  |  | No |  |
| event_id | int8(64) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| is_active | bool | Yes | true |  | No |  |

---

## fcst_supply_worksheet_hstry_data

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| supply_worksheet_hstry_data_id | int4(32) | No | nextval('i2oretail_dev.fcst_supply_worksheet_hstry_d_supply_worksheet_hstry_data_i_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_type | varchar(20) | No |  |  | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| platform | varchar(20) | No |  |  | No |  |
| product_code | varchar(20) | No |  |  | No |  |
| reporting_range | varchar(15) | No |  |  | No |  |
| period | varchar(10) | No |  |  | No |  |
| start_date | varchar(10) | No |  |  | No |  |
| end_date | varchar(10) | No |  |  | No |  |
| measure | varchar(200) | No |  |  | No |  |
| period0 | int4(32) | Yes |  |  | No |  |
| period1 | int4(32) | Yes |  |  | No |  |
| period2 | int4(32) | Yes |  |  | No |  |
| period3 | int4(32) | Yes |  |  | No |  |
| period4 | int4(32) | Yes |  |  | No |  |
| period5 | int4(32) | Yes |  |  | No |  |
| period6 | int4(32) | Yes |  |  | No |  |
| period7 | int4(32) | Yes |  |  | No |  |
| period8 | int4(32) | Yes |  |  | No |  |
| period9 | int4(32) | Yes |  |  | No |  |
| period10 | int4(32) | Yes |  |  | No |  |
| period11 | int4(32) | Yes |  |  | No |  |
| period12 | int4(32) | Yes |  |  | No |  |
| period13 | int4(32) | Yes |  |  | No |  |
| period14 | int4(32) | Yes |  |  | No |  |
| period15 | int4(32) | Yes |  |  | No |  |
| period16 | int4(32) | Yes |  |  | No |  |
| period17 | int4(32) | Yes |  |  | No |  |
| period18 | int4(32) | Yes |  |  | No |  |
| period19 | int4(32) | Yes |  |  | No |  |
| period20 | int4(32) | Yes |  |  | No |  |
| period21 | int4(32) | Yes |  |  | No |  |
| period22 | int4(32) | Yes |  |  | No |  |
| period23 | int4(32) | Yes |  |  | No |  |
| period24 | int4(32) | Yes |  |  | No |  |
| period25 | int4(32) | Yes |  |  | No |  |
| period26 | int4(32) | Yes |  |  | No |  |
| period27 | int4(32) | Yes |  |  | No |  |
| period28 | int4(32) | Yes |  |  | No |  |
| period29 | int4(32) | Yes |  |  | No |  |
| period30 | int4(32) | Yes |  |  | No |  |
| period31 | int4(32) | Yes |  |  | No |  |
| period32 | int4(32) | Yes |  |  | No |  |
| period33 | int4(32) | Yes |  |  | No |  |
| period34 | int4(32) | Yes |  |  | No |  |
| period35 | int4(32) | Yes |  |  | No |  |
| period36 | int4(32) | Yes |  |  | No |  |
| period37 | int4(32) | Yes |  |  | No |  |
| period38 | int4(32) | Yes |  |  | No |  |
| period39 | int4(32) | Yes |  |  | No |  |
| period40 | int4(32) | Yes |  |  | No |  |
| period41 | int4(32) | Yes |  |  | No |  |
| period42 | int4(32) | Yes |  |  | No |  |
| period43 | int4(32) | Yes |  |  | No |  |
| period44 | int4(32) | Yes |  |  | No |  |
| period45 | int4(32) | Yes |  |  | No |  |
| period46 | int4(32) | Yes |  |  | No |  |
| period47 | int4(32) | Yes |  |  | No |  |
| period48 | int4(32) | Yes |  |  | No |  |
| period49 | int4(32) | Yes |  |  | No |  |
| period50 | int4(32) | Yes |  |  | No |  |
| period51 | int4(32) | Yes |  |  | No |  |
| period52 | int4(32) | Yes |  |  | No |  |

---

## features

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| feature_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| feature_category | varchar(50) | Yes |  |  | No |  |
| feature_sub_category | varchar(50) | Yes |  |  | No |  |
| feature_category_desc | varchar(200) | Yes |  |  | No |  |
| feature_sub_category_desc | varchar(200) | Yes |  |  | No |  |
| activation_date_offset | int4(32) | Yes |  |  | No |  |
| channel_id | int4(32) | No |  |  | No |  |

---

## feedback_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| feedback_id | int4(32) | No | nextval('i2oretail_dev.feedback_details_feedback_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| email | varchar(150) | No |  |  | No |  |
| name | varchar(150) | No |  |  | No |  |
| summary | varchar(350) | No |  |  | No |  |
| feature_screen | varchar(150) | Yes |  |  | No |  |
| description | varchar(10000) | No |  |  | No |  |
| submission_time | timestamp | Yes |  |  | No |  |
| gcs_image_location | varchar(1000) | Yes |  |  | No |  |

---

## filter

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| filter_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| filter_screen_cd | varchar(255) | Yes |  |  | Yes |  |
| filter_type | varchar(255) | Yes |  |  | No |  |
| filter_value | varchar(255) | Yes |  |  | No |  |
| filter_display_name | varchar(255) | Yes |  |  | No |  |
| filter_source | varchar(255) | Yes |  |  | No |  |
| filter_source_location | varchar(255) | Yes |  |  | No |  |
| filter_display_order | int4(32) | Yes |  |  | No |  |

---

## filter_dr

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| filter_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| label | varchar(255) | No |  |  | No |  |
| widget | varchar(255) | No |  |  | No |  |
| parameter_name | varchar(255) | No |  |  | No |  |
| default_value | varchar(255) | Yes |  |  | No |  |
| db_column_name | varchar(255) | Yes |  |  | No |  |
| filter_limit | int4(32) | Yes |  |  | No |  |

---

## filter_org_type

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| filter_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| org_type_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |

---

## filterback

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| filter_id | int4(32) | Yes |  |  | No |  |
| filter_screen_cd | varchar(100) | Yes |  |  | No |  |
| filter_type | varchar(45) | Yes |  |  | No |  |
| filter_value | varchar(45) | Yes |  |  | No |  |
| filter_display_name | varchar(224) | Yes |  |  | No |  |
| filter_source | varchar(45) | Yes |  |  | No |  |
| filter_source_location | varchar(224) | Yes |  |  | No |  |
| filter_display_order | int4(32) | Yes |  |  | No |  |

---

## forecast_data

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| forecast_name | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| project_id | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| client | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| product_code | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| error_text | text | Yes |  |  | No |  |
| forecast_data | jsonb | Yes |  |  | No |  |
| created_at | timestamp | Yes | now() |  | No |  |
| updated_at | timestamp | Yes | now() |  | No |  |
| request_message | jsonb | Yes |  |  | No |  |
| forecast_start_date | date | Yes |  |  | No |  |
| forecast_end_date | date | Yes |  |  | No |  |

---

## ga_user_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| ga_user_id | int4(32) | No | nextval('i2oretail_dev.ga_user_details_ga_user_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| email | varchar(255) | Yes |  |  | No |  |
| name | varchar(255) | Yes |  |  | No |  |
| submission_time | timestamp | Yes |  |  | No |  |

---

## gallery_standard

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| asin | varchar(20) | No |  |  | No |  |
| image_url | text | Yes |  |  | No |  |
| region_name | varchar(100) | Yes |  |  | No |  |
| region_code | varchar(10) | Yes |  |  | No |  |
| product_code | varchar(50) | Yes |  |  | No |  |
| product_name | text | Yes |  |  | No |  |
| ean | varchar(20) | Yes |  |  | No |  |
| images_gallery | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |
| platform | text | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| category_name | text | Yes |  |  | No |  |
| file_type | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| id | int4(32) | No | nextval('i2oretail_dev.gallery_standard_id_seq'::regclass) | PRIMARY KEY | Yes |  |

---

## header

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| header_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| context_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| header_name | varchar(255) | Yes |  |  | No |  |
| header_config | json | Yes |  |  | No |  |
| visible | bool | Yes |  |  | No |  |
| display_order | int4(32) | Yes |  |  | No |  |
| editable | bool | Yes |  |  | No |  |
| pinned | varchar(255) | Yes |  |  | No |  |
| width | int4(32) | Yes |  |  | No |  |
| text_align | varchar(255) | Yes |  |  | No |  |

---

## header_backup

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| header_id | int4(32) | Yes |  |  | No |  |
| context_id | int4(32) | Yes |  |  | No |  |
| header_name | varchar(100) | Yes |  |  | No |  |
| header_config | json | Yes |  |  | No |  |
| visible | bool | Yes |  |  | No |  |
| display_order | int4(32) | Yes |  |  | No |  |
| editable | bool | Yes |  |  | No |  |
| pinned | varchar(50) | Yes |  |  | No |  |
| width | int4(32) | Yes |  |  | No |  |
| text_align | varchar(10) | Yes |  |  | No |  |

---

## header_meta_info

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| header_meta_info_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| header_id | int4(32) | Yes |  | FOREIGN KEY, UNIQUE | Yes |  |
| org_type_id | int4(32) | Yes |  | FOREIGN KEY, UNIQUE | Yes |  |
| header_display_name | varchar(255) | Yes |  |  | No |  |
| widget | varchar(255) | Yes |  |  | No |  |

---

## hibernate_sequences

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| sequence_name | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| next_val | int8(64) | Yes |  |  | No |  |

---

## highlight_priority

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.highlight_priority_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| value | varchar(255) | No |  |  | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| type | varchar(255) | No |  |  | No |  |
| top_priority | bool | No | false |  | No |  |

---

## hourly_dataload_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  |  | No |  |
| meta_data | varchar(1000) | Yes |  |  | No |  |
| dataload_status | bool | Yes |  |  | No |  |
| time_of_day | varchar(10) | Yes |  |  | No |  |

---

## industry

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| industry_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| industry_name | varchar(50) | Yes |  |  | No |  |

---

## invoice

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dev.invoice_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| attachment_id | int8(64) | Yes |  |  | No |  |
| enforcement_tracker_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| invoice_number | text | Yes |  |  | No |  |
| supplier_name | text | Yes |  |  | No |  |
| supplier_address | text | Yes |  |  | No |  |
| supplier_contact | text | Yes |  |  | No |  |
| invoice_date | date | Yes |  |  | No |  |
| transaction_id | text | Yes |  |  | No |  |
| shipping_address | text | Yes |  |  | No |  |
| billing_address | text | Yes |  |  | No |  |
| tax_identifier | text | Yes |  |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |
| invoice_status | text | Yes |  |  | No |  |

---

## invoice_line_item

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dev.invoice_line_item_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| invoice_id | int8(64) | Yes |  | FOREIGN KEY | No |  |
| product_code | text | Yes |  |  | No |  |
| product_name | text | Yes |  |  | No |  |
| item_number | text | Yes |  |  | No |  |
| model_number | text | Yes |  |  | No |  |
| price_without_tax | float8(53) | Yes |  |  | No |  |
| total_price | float8(53) | Yes |  |  | No |  |
| discount | float8(53) | Yes |  |  | No |  |
| sku | text | Yes |  |  | No |  |
| description | text | Yes |  |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |

---

## job_execution

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| job_id | int4(32) | No | nextval('i2oretail_dev.job_execution_sequence'::regclass) | PRIMARY KEY | Yes |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| parent_job_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| job_type_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| job_name | varchar(100) | Yes |  |  | No |  |
| end_time | timestamp | Yes |  |  | No |  |
| stage | varchar(50) | Yes |  |  | No |  |
| status | varchar(50) | Yes |  |  | No |  |
| response | json | Yes |  |  | No |  |
| dp_job_id | varchar(40) | Yes |  |  | No |  |
| url | varchar(200) | Yes |  |  | No |  |
| input_params | json | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| created_by | varchar(50) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |

---

## job_type

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| job_type_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| job_type_name | varchar(100) | Yes |  |  | No |  |
| parent_job_type_id | int4(32) | Yes |  | FOREIGN KEY | No |  |

---

## job_type_marketplace

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| job_type_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| job_display_name | varchar(100) | Yes |  |  | No |  |
| job_metadata | json | Yes |  |  | No |  |

---

## keepa_batch_details_to_delete

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| batch_id | uuid | No |  | PRIMARY KEY | Yes |  |
| output_location | text | Yes |  |  | No |  |
| output_format | varchar | Yes |  |  | No |  |
| status | varchar | No | 'Started'::character varying |  | No | One of Started, Error, Done |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |
| error_text | text | Yes |  |  | No |  |
| retry_count | int4(32) | No | 0 |  | No |  |

---

## keepa_product_download_progress

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| input_folder | text | No |  |  | No | Input folder containing list of asins in gcs |
| keepa_json_folder | text | Yes |  |  | No | Keepa output file stored in gcs |
| output_folder | text | Yes |  |  | No | Output file location in gcs |
| dp_sub_process_audit_detail_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| start_date | date | No |  |  | Yes | Should be Sunday for weekly |
| frequency | varchar(20) | No |  |  | Yes | One of daily, weekly, monthly, quarterly, or yearly |
| priority | int4(32) | Yes | 0 |  | Yes | Any natural number with 0 being lowest priority |
| dp_org_id | int4(32) | No |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |
| is_done | bool | No | false |  | Yes |  |
| total_splits | int4(32) | No |  |  | No |  |
| current_split | int4(32) | No | 0 |  | No |  |
| error_text | text | Yes |  |  | No |  |
| finished_at | timestamptz | Yes |  |  | No |  |
| end_date | date | No |  |  | Yes | Should be Saturday for weekly |
| domain | varchar | No | 'US'::character varying |  | No | Short hand code for region, ex: US, MX etc |
| current_period | date | No |  |  | No |  |
| source | text | Yes |  |  | No |  |
| source_type | text | Yes |  |  | No |  |

---

## keepa_progress_to_delete

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| entity_type | varchar | No |  | PRIMARY KEY | Yes |  |
| entity_name | varchar | No |  | PRIMARY KEY | Yes |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |
| status | varchar | Yes |  |  | No | One of null, InProgress, Error, Done |
| batch_id | uuid | Yes |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| error_text | text | Yes |  |  | No |  |
| retry_count | int4(32) | No | 0 |  | No |  |

---

## listing_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| listing_id | int4(32) | No | nextval('i2oretail_dev.listing_master_listing_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  |  | No |  |
| account_id | int4(32) | Yes |  |  | No |  |
| product_code | text | Yes |  |  | No |  |
| reseller_name | text | Yes |  |  | No |  |
| reseller_id | text | Yes |  |  | No |  |
| is_active | bool | Yes |  |  | No |  |
| fulfilment_type | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| last_seen | date | Yes |  |  | No |  |

---

## listing_master_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id_dp | int4(32) | Yes |  |  | No |  |
| marketplace | text | Yes |  |  | No |  |
| region | text | Yes |  |  | No |  |
| account_name | text | Yes |  |  | No |  |
| product_code | text | Yes |  |  | No |  |
| reseller_name | text | Yes |  |  | No |  |
| reseller_id | text | Yes |  |  | No |  |
| last_seen | date | Yes |  |  | No |  |
| is_active | bool | Yes |  |  | No |  |
| fulfilment_type | text | Yes |  |  | No |  |

---

## lookup_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| code | varchar(100) | Yes |  |  | No |  |
| label | varchar(100) | Yes |  |  | No |  |
| category | varchar(100) | Yes |  |  | No |  |
| module_name | varchar(80) | Yes |  |  | No |  |

---

## lookupentity

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| category | varchar(255) | Yes |  |  | No |  |
| code | varchar(255) | Yes |  |  | No |  |
| label | varchar(255) | Yes |  |  | No |  |

---

## manual_measures

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| value | numeric(38,20) | Yes |  |  | No |  |
| text_value | varchar(4000) | Yes |  |  | No |  |
| user_uuid | varchar(255) | Yes |  |  | No |  |
| description | varchar(4000) | Yes |  |  | No |  |
| created_at | int8(64) | Yes |  |  | No |  |
| updated_at | int8(64) | Yes |  |  | No |  |
| component_uuid | varchar(50) | No |  |  | Yes |  |
| metric_uuid | varchar(40) | No |  |  | No |  |

---

## map_enforcement_history

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| map_enforcement_tracker_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| period | date | No |  | PRIMARY KEY | Yes |  |
| status | text | No |  |  | Yes |  |

---

## map_enforcement_history_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | Yes |  |  | No |  |
| product_code | varchar(255) | No |  |  | No |  |
| reseller_name | varchar(255) | Yes |  |  | No |  |
| reseller_id | varchar(255) | Yes |  |  | No |  |
| marketplace | varchar(255) | No |  |  | No |  |
| region | varchar(255) | No |  |  | No |  |
| period | date | No |  |  | No |  |
| reporting_range | varchar(255) | No |  |  | No |  |
| time_of_day | int4(32) | No |  |  | No |  |
| history_data | jsonb | Yes |  |  | No |  |

---

## map_enforcement_tracker

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.map_enforcement_tracker_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  |  | Yes |  |
| product_code | varchar(255) | No |  |  | No |  |
| reseller_name | varchar(255) | Yes |  |  | No |  |
| reseller_id | varchar(255) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  |  | No |  |
| period | date | No |  |  | No |  |
| reporting_range | varchar | Yes |  |  | No |  |
| scrape_timestamp | timestamp | Yes |  |  | No |  |
| map | float8(53) | Yes |  |  | No |  |
| reseller_price | float8(53) | Yes |  |  | No |  |
| status | varchar(255) | No |  |  | No |  |
| days_in_violation | varchar | Yes |  |  | No |  |
| violation_detection_date | timestamp | Yes |  |  | No |  |
| metadata | jsonb | Yes |  |  | No |  |
| created_by | text | Yes |  |  | No |  |
| created_at | timestamp | Yes | now() |  | No |  |
| history_data | jsonb | Yes |  |  | Yes |  |
| seven_day_trend | jsonb | Yes |  |  | No |  |
| reseller_status | varchar | Yes |  |  | No |  |
| is_automation_paused | bool | Yes | false |  | No |  |
| time_of_day | int4(32) | Yes |  |  | No |  |
| updated_at | timestamp | Yes | now() |  | No |  |
| is_testbuy_recommended | bool | Yes |  |  | No |  |
| is_testbuy_withdrawn | bool | Yes |  |  | No |  |
| is_testbuy_approved | bool | Yes |  |  | No |  |
| testbuy_metadata | jsonb | Yes |  |  | No |  |
| proof_of_violation | text | Yes |  |  | No |  |
| latest_violation_detection_date | timestamp | Yes |  |  | No |  |

---

## map_enforcement_tracker_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | Yes |  |  | No |  |
| product_code | varchar | Yes |  |  | No |  |
| reseller_name | varchar | Yes |  |  | No |  |
| reseller_id | varchar | Yes |  |  | No |  |
| marketplace | text | Yes |  |  | No |  |
| region | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| reporting_range | text | Yes |  |  | No |  |
| scrape_timestamp | timestamptz | Yes |  |  | No |  |
| time_of_day | int8(64) | Yes |  |  | No |  |
| map | float8(53) | Yes |  |  | No |  |
| reseller_price | float8(53) | Yes |  |  | No |  |
| status | text | Yes |  |  | No |  |
| days_in_violation | text | Yes |  |  | No |  |
| violation_detection_date | timestamptz | Yes |  |  | No |  |
| reseller_status | text | Yes |  |  | No |  |
| history_data | jsonb | Yes |  |  | No |  |
| seven_day_trend | jsonb | Yes |  |  | No |  |
| proof_of_violation | text | Yes |  |  | No |  |
| latest_violation_detection_date | timestamp | Yes |  |  | No |  |

---

## marketplace

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| marketplace_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| platform | varchar(255) | Yes |  |  | No |  |
| region | varchar(255) | Yes |  |  | No |  |
| platform_icon | json | Yes |  |  | No |  |
| region_icon | json | Yes |  |  | No |  |
| url | varchar(255) | Yes |  |  | No |  |
| created_at | timestamp | Yes | timezone('utc'::text, now()) |  | No |  |
| updated_at | timestamp | Yes | timezone('utc'::text, now()) |  | No |  |
| platform_priority_order | int4(32) | Yes |  |  | No |  |
| region_priority_order | int4(32) | Yes |  |  | No |  |
| platform_url | varchar(255) | Yes |  |  | No |  |
| color_code | varchar(50) | Yes |  |  | No |  |
| is_marketplace | bool | Yes | false |  | No |  |
| marketplace_priority_order | int4(32) | Yes |  |  | No |  |
| currency_alphabetic_code | varchar(50) | Yes |  |  | No |  |
| currency_symbol | varchar(50) | Yes |  |  | No |  |
| timezone | varchar | Yes |  |  | No |  |

---

## marketplace_search_terms

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| search_term_group_id | int4(32) | No | nextval('i2oretail_dev.marketplace_search_terms_sequence'::regclass) | PRIMARY KEY | Yes |  |
| search_term_group_name | varchar(50) | Yes |  |  | No |  |
| product_category_detail_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| search_terms | varchar(200) | Yes |  |  | No |  |

---

## master_data_quota

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.master_data_quota_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| maxcount | int4(32) | No |  |  | No |  |
| mincount | int4(32) | No |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| resource_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| default_value | int4(32) | Yes | 0 |  | No |  |
| quota_limit_increased | bool | Yes | false |  | No |  |
| quota_limit_increased_by_css | int4(32) | Yes | 0 |  | No |  |

---

## master_data_resource

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.master_data_resouce_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| resource_type | varchar(255) | Yes |  |  | No |  |
| upload_type_id | int4(32) | Yes |  |  | No |  |
| resource_sub_type | varchar(255) | Yes |  |  | No |  |

---

## master_data_review

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.master_data_review_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| column_name | varchar(255) | Yes |  |  | No |  |
| resource_id | int4(32) | Yes |  |  | No |  |
| table_name | varchar(255) | Yes |  |  | No |  |
| reviewed | bool | Yes |  |  | No |  |

---

## master_metadata

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.master_metadata_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| value | varchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| resource_id | int4(32) | No |  | FOREIGN KEY | No |  |

---

## metric

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| metric_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| metric_display_name | varchar(150) | Yes |  |  | No |  |
| metric_source | varchar(50) | Yes |  |  | No |  |
| metric_category | varchar(150) | Yes |  |  | No |  |
| metric_sub_category | varchar(250) | Yes |  |  | No |  |

---

## metric_ex

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| metric_id | int4(32) | Yes |  |  | No |  |
| metric_display_name | varchar(150) | Yes |  |  | No |  |
| metric_source | varchar(50) | Yes |  |  | No |  |
| metric_category | varchar(150) | Yes |  |  | No |  |
| metric_sub_category | varchar(250) | Yes |  |  | No |  |

---

## notice_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.notice_config_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | UNIQUE | Yes |  |
| entity | varchar(100) | No |  |  | No |  |
| notice_type | varchar(100) | No |  |  | No |  |
| entity_id | int8(64) | No |  | UNIQUE | Yes |  |
| max_notice | int4(32) | Yes |  |  | No |  |
| limit_range | varchar(50) | Yes |  |  | No |  |
| limit_value | numeric | Yes |  |  | No |  |
| metadata | jsonb | Yes |  |  | No |  |
| disable_enforcement | bool | Yes | false |  | No |  |
| created_at | timestamp | Yes | now() |  | No |  |
| updated_at | timestamp | Yes | now() |  | No |  |

---

## notice_delivery_attempt_ops

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dev.notice_delivery_attempt_ops_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| notice_id | int4(32) | Yes |  | FOREIGN KEY, UNIQUE | Yes |  |
| attempt_no | int4(32) | No |  | UNIQUE | Yes |  |
| transport | text | No |  |  | No |  |
| provider_msg_id | text | Yes |  |  | No |  |
| status_delivery_status | text | Yes | 'PENDING'::text |  | No |  |
| status_code | text | Yes |  |  | No |  |
| status_detail | text | Yes |  |  | No |  |
| attempted_at | timestamptz | Yes | now() |  | No |  |

---

## notice_status

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| notice_id | int4(32) | No | nextval('i2oretail_dev.notice_status_notice_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| template_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| account_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| enforcement_tracker_id | int4(32) | Yes |  |  | Yes |  |
| event_id | int8(64) | Yes |  | FOREIGN KEY | No |  |
| notice_type | text | Yes |  |  | No |  |
| notice_number | int4(32) | Yes |  |  | Yes |  |
| state | text | Yes |  |  | No |  |
| priority | int8(64) | Yes |  |  | No |  |
| is_escalated | bool | Yes |  |  | No |  |
| retry_count | int4(32) | Yes | 0 |  | No |  |
| transport | text | Yes |  |  | No |  |
| queued_at | timestamptz | Yes |  |  | No |  |
| sent_at | timestamptz | Yes |  |  | Yes |  |
| delivered_at | timestamptz | Yes |  |  | No |  |
| opened_at | timestamptz | Yes |  |  | No |  |
| bounced_at | timestamptz | Yes |  |  | No |  |
| response_received | bool | Yes |  |  | No |  |
| responded_at | timestamptz | Yes |  |  | No |  |
| correlation_id | text | Yes |  |  | No |  |
| invoice_received | bool | Yes |  |  | No |  |
| invoice_id | int8(64) | Yes |  |  | No |  |
| sent_by | text | Yes |  |  | No |  |
| map_metadata | jsonb | Yes |  |  | No |  |
| cnd_metadata | jsonb | Yes |  |  | No |  |
| testbuy_metadata | jsonb | Yes |  |  | No |  |
| time_of_day | int4(32) | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |

---

## notice_template

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| template_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| account_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| external_template_id | text | Yes |  |  | No |  |
| notice_type | text | Yes |  |  | No |  |
| version | int4(32) | Yes |  |  | No |  |
| subject | text | Yes |  |  | No |  |
| html_body | text | Yes |  |  | No |  |
| archive | bool | Yes |  |  | No |  |
| created_by | int8(64) | Yes |  | FOREIGN KEY | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |
| updated_by | text | Yes |  |  | No |  |
| notice_number | int4(32) | Yes |  |  | No |  |

---

## notification

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| notification_category | varchar(150) | Yes |  |  | No |  |
| notification_sub_category | varchar(150) | No |  |  | No |  |
| severity | varchar(50) | Yes |  |  | No |  |
| url | varchar(150) | Yes |  |  | No |  |
| short_title | varchar(250) | Yes |  |  | No |  |
| description | varchar(500) | Yes |  |  | No |  |
| notification_start_date | date | Yes |  |  | No |  |
| notification_end_date | date | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| active | varchar | Yes |  |  | No |  |
| region | varchar(50) | Yes |  |  | No |  |
| marketplace | varchar(50) | Yes |  |  | No |  |
| notification_id | int4(32) | No | nextval('i2oretail_dev.notification_seq'::regclass) | PRIMARY KEY | Yes |  |
| priority | int4(32) | Yes |  |  | No |  |

---

## notifications

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| data | bytea | Yes |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |

---

## onboarding_queries

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | No | nextval('i2oretail_dev.onboarding_queries_query_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| stage_id | int4(32) | No |  |  | No |  |
| sub_stage_id | int4(32) | No |  |  | No |  |
| query | text | No |  |  | No |  |
| validation_query | text | Yes |  |  | No |  |
| description | text | Yes |  |  | No |  |
| operation | varchar(500) | Yes |  |  | No |  |
| skip_query_in_lower_env | varchar(500) | Yes |  |  | No |  |

---

## org_brands

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_brand_id | int4(32) | No | nextval('i2oretail_dev.org_brands_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| brand | varchar | No |  |  | No |  |
| alias | text | Yes |  |  | No |  |

---

## org_contacts

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| contact_id | int4(32) | No | nextval('i2oretail_dev.org_contacts_sequence'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| contact_type_id | int4(32) | Yes |  |  | No |  |
| name | varchar(200) | Yes |  |  | No |  |
| role | varchar(200) | Yes |  |  | No |  |
| phone | varchar(50) | Yes |  |  | No |  |
| email | varchar(100) | Yes |  |  | No |  |
| deleted | bool | Yes | false |  | No |  |

---

## org_data_metadata

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| marketplace_id | int8(64) | No |  | PRIMARY KEY | Yes |  |
| data_type | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| data_set_location | varchar(1000) | No |  |  | No |  |

---

## org_dummy_table_preprod

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| subscription_id | int4(32) | No |  |  | No |  |
| org_id_dp | int4(32) | No |  |  | No |  |
| org_id | int4(32) | No |  |  | No |  |
| org_name | varchar | Yes |  |  | No |  |

---

## org_hourly_mapping

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| org_id_dp | int4(32) | Yes |  |  | No |  |
| org_name | varchar(100) | Yes |  |  | No |  |
| is_hourly_enabled | bool | Yes |  |  | No |  |

---

## org_market_mapping

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.org_market_mapping_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| enabled | bool | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| product_master_subscribed | bool | Yes |  |  | No |  |
| timezone | varchar | Yes |  |  | No |  |
| test | varchar | Yes |  |  | No |  |
| is_reseller_enabled | bool | Yes |  |  | No |  |

---

## org_marketplace

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| marketplace_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| channel_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| credential_status | varchar(50) | Yes |  |  | No |  |
| product_category_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| product_search_terms | text | Yes |  |  | No |  |
| selected_data_feeds | json | Yes |  |  | No |  |
| marketplace_onboarding_date | timestamp | Yes |  |  | No |  |

---

## org_marketplace_account

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_marketplace_account_id | int4(32) | No | nextval('i2oretail_dev.org_marketplace_account_sequence'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| account_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| account_status | varchar(50) | Yes |  |  | No |  |
| account_details | json | Yes |  |  | No |  |

---

## org_marketplace_data_feed

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| data_feed_id | int4(32) | Yes |  | FOREIGN KEY | No |  |

---

## org_marketplace_features

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| feature_id | int4(32) | Yes |  | FOREIGN KEY | No |  |

---

## org_qprofiles

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| rules_profile_uuid | varchar(255) | No |  |  | Yes |  |
| parent_uuid | varchar(255) | Yes |  |  | Yes |  |
| last_used | int8(64) | Yes |  |  | No |  |
| user_updated_at | int8(64) | Yes |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |
| updated_at | int8(64) | No |  |  | No |  |

---

## org_report

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | Yes |  |  | No |  |
| report_id | int4(32) | Yes |  |  | No |  |
| report_name | varchar(80) | Yes |  |  | No |  |
| org_type_id | int4(32) | Yes |  |  | No |  |
| org_report_metadata | json | Yes |  |  | No |  |

---

## organization

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No | nextval('i2oretail_dev.organisation_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_name | varchar(255) | No |  |  | No |  |
| org_type_id | int4(32) | No |  | FOREIGN KEY | No |  |
| url | varchar(255) | Yes | NULL::character varying |  | No |  |
| duns_no | varchar(255) | Yes | NULL::character varying |  | No |  |
| address_1 | varchar(255) | Yes | NULL::character varying |  | No |  |
| address_2 | varchar(255) | Yes | NULL::character varying |  | No |  |
| city | varchar(255) | Yes | NULL::character varying |  | No |  |
| state | varchar(255) | Yes | NULL::character varying |  | No |  |
| zip | varchar(255) | Yes | NULL::character varying |  | No |  |
| country | varchar(255) | Yes | NULL::character varying |  | No |  |
| org_banner_display_name | varchar(255) | Yes | NULL::character varying |  | No |  |
| org_banner_logo_name | varchar(255) | Yes | NULL::character varying |  | No |  |
| active | bool | Yes |  |  | No |  |
| parent_org_id | int4(32) | Yes |  |  | No |  |
| org_id_dp | int4(32) | Yes |  |  | No |  |
| industry_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| deleted | bool | Yes |  |  | No |  |
| org_onboarding_start_date | timestamp | Yes |  |  | No |  |
| customer_activation_date | timestamp | Yes |  |  | No |  |
| org_alias_name_dp | varchar(255) | Yes |  |  | No |  |
| org_subscription_type_id | int4(32) | Yes |  |  | No |  |
| agency_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| trial_metadata | varchar(500) | Yes |  |  | No |  |
| status | varchar(255) | Yes |  |  | No |  |
| client_info | text | Yes |  |  | No |  |
| subscription_status | varchar(50) | Yes |  |  | No |  |
| subscription_start_date | date | Yes |  |  | No |  |
| subscription_end_date | date | Yes |  |  | No |  |
| business_unit_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| id | int4(32) | No | nextval('i2oretail_dev.organization_id_seq'::regclass) |  | No |  |

---

## organization_types

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_type_cd | varchar(255) | No |  | UNIQUE | Yes |  |
| name | varchar(255) | No |  |  | No |  |
| org_type_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| org_type_config | json | Yes |  |  | No |  |
| org_type_value | varchar(255) | Yes |  |  | No |  |
| orgtypeconfig | json | Yes |  |  | No |  |

---

## parsehub_project_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| project_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| project_token | varchar | No |  |  | No |  |
| bq_table_name | varchar | No |  |  | No |  |
| start_value | varchar | Yes |  |  | No |  |

---

## perm_templates_groups

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| permission_reference | varchar(64) | No |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| template_uuid | varchar(40) | No |  |  | No |  |
| group_uuid | varchar(40) | Yes |  |  | No |  |

---

## perm_templates_users

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| permission_reference | varchar(64) | No |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| template_uuid | varchar(40) | No |  |  | No |  |
| user_uuid | varchar(255) | No |  |  | No |  |

---

## perm_tpl_characteristics

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| permission_key | varchar(64) | No |  |  | Yes |  |
| with_project_creator | bool | No | false |  | No |  |
| created_at | int8(64) | No |  |  | No |  |
| updated_at | int8(64) | No |  |  | No |  |
| template_uuid | varchar(40) | No |  |  | Yes |  |

---

## permission_templates

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| name | varchar(100) | No |  |  | No |  |
| description | varchar(4000) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| key_pattern | varchar(500) | Yes |  |  | No |  |

---

## platform_org_channel_mapping

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| channel_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| platform | varchar(125) | No |  |  | No |  |
| org_type_id | int4(32) | No |  | FOREIGN KEY | No |  |

---

## plugins

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| kee | varchar(200) | No |  |  | Yes |  |
| base_plugin_key | varchar(200) | Yes |  |  | No |  |
| file_hash | varchar(200) | No |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |
| updated_at | int8(64) | No |  |  | No |  |
| type | varchar(10) | No |  |  | No |  |

---

## potential_brands

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.potential_brands_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| brand | varchar(255) | No |  |  | No |  |
| keywords | varchar(1000) | Yes |  |  | No |  |
| account_manager | varchar(255) | Yes |  |  | No |  |

---

## premium_standard

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| asin | varchar(20) | No |  |  | No |  |
| image_url | text | Yes |  |  | No |  |
| region_name | varchar(100) | Yes |  |  | No |  |
| region_code | varchar(10) | Yes |  |  | No |  |
| product_code | varchar(50) | Yes |  |  | No |  |
| product_name | text | Yes |  |  | No |  |
| images_background | text | Yes |  |  | No |  |
| ean | varchar(20) | Yes |  |  | No |  |
| highlights | text | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |
| platform | text | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| category_name | text | Yes |  |  | No |  |
| preview_images | text | Yes |  |  | No |  |
| video_urls | text | Yes |  |  | No |  |
| file_type | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| id | int4(32) | No | nextval('i2oretail_dev.premium_standard_id_seq'::regclass) | PRIMARY KEY | Yes |  |

---

## prime_day_report_execution

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| execution_id | int4(32) | No | nextval('i2oretail_dev.prime_day_report_execution_execution_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| report_name | varchar | Yes |  |  | No |  |
| report_type | varchar | Yes |  |  | No |  |
| time_of_day | int4(32) | Yes |  |  | No |  |
| recipient_list | text | Yes |  |  | No |  |
| execution_date_time | timestamp | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| gcs_location | varchar | Yes |  |  | No |  |

---

## product_catalog

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.product_catalog_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_on | timestamp | Yes | CURRENT_TIMESTAMP |  | No |  |
| created_by | varchar(100) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes | CURRENT_TIMESTAMP |  | No |  |
| last_modified_by | varchar(100) | Yes |  |  | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY, UNIQUE | Yes |  |
| product_code | varchar(255) | No |  | UNIQUE | Yes |  |
| marketplace_id | int4(32) | No |  | FOREIGN KEY, UNIQUE | Yes |  |
| keyword_search_terms | varchar(255) | Yes |  |  | No |  |
| brand_id | int4(32) | No |  | FOREIGN KEY | Yes |  |
| is_relevant | bool | Yes | false |  | No |  |
| is_active | bool | Yes | true |  | No |  |
| is_css_enabled | bool | Yes | false |  | No |  |
| product_center_css_enabled | bool | Yes | false |  | No |  |
| product_title | text | Yes |  |  | No |  |
| product_tags | varchar(255) | Yes |  |  | No |  |
| source | varchar(255) | Yes |  |  | No |  |
| closure_perc | float8(53) | Yes |  |  | No |  |
| product_url | text | Yes |  |  | No |  |
| i2o_product_id | varchar(255) | Yes |  |  | No |  |
| active_offers | int4(32) | Yes |  |  | No |  |
| total_offers | int4(32) | Yes |  |  | No |  |
| title | text | Yes |  |  | No |  |
| derived_brand | varchar(255) | Yes |  |  | No |  |
| keepa_brand | varchar(255) | Yes |  |  | No |  |
| keyword_brand_id | int4(32) | Yes |  |  | No |  |
| brand_keyword | varchar(255) | Yes |  |  | No |  |
| product_image_url | text | Yes |  |  | No |  |
| is_tracked | bool | Yes | false |  | No |  |

---

## product_catalog_check

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| created_by | varchar(100) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(100) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  |  | No |  |
| brand_keyword | varchar(255) | Yes |  |  | No |  |
| brand_id | int4(32) | Yes |  |  | No |  |
| is_relevant | bool | Yes |  |  | No |  |
| is_active | bool | Yes |  |  | No |  |
| is_css_enabled | bool | Yes |  |  | No |  |
| product_center_css_enabled | bool | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| product_tags | varchar(255) | Yes |  |  | No |  |
| source | varchar(255) | Yes |  |  | No |  |
| closure_perc | numeric | Yes |  |  | No |  |
| product_url | text | Yes |  |  | No |  |
| i2o_product_id | varchar(255) | Yes |  |  | No |  |
| active_offers | int4(32) | Yes |  |  | No |  |
| total_offers | int4(32) | Yes |  |  | No |  |
| title | text | Yes |  |  | No |  |

---

## product_catalog_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_code | varchar | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | No |  |
| region | varchar | Yes |  |  | No |  |
| keyword | varchar | Yes |  |  | No |  |
| is_relevant | bool | Yes |  |  | No |  |
| brand | varchar | Yes |  |  | No |  |
| title | varchar | Yes |  |  | No |  |
| source | varchar | Yes |  |  | No |  |
| closure_percentage | float8(53) | Yes |  |  | No |  |
| product_tags | varchar | Yes |  |  | No |  |

---

## product_category

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_category_id | int4(32) | No | nextval('i2oretail_dev.product_category_sequence'::regclass) | PRIMARY KEY | Yes |  |
| category_group_name | varchar(50) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |

---

## product_category_detail

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_category_detail_id | int4(32) | No | nextval('i2oretail_dev.product_category_detail_sequence'::regclass) | PRIMARY KEY | Yes |  |
| product_category_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| org_category_name | varchar(50) | Yes |  |  | No |  |
| parent_category_name | varchar(50) | Yes |  |  | No |  |
| organization_full_classification | varchar(200) | Yes |  |  | No |  |
| marketplace_full_classfication | varchar(200) | Yes |  |  | No |  |
| is_leaf_node | bool | Yes |  |  | No |  |
| marketplace_category_name | varchar | Yes |  |  | No |  |

---

## product_channel_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_channel_id | int4(32) | No | nextval('i2oretail_dev.product_channel_master_product_channel_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| product_master_id | int4(32) | No |  | FOREIGN KEY | No |  |
| org_type_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| sales_velocity_group | varchar(255) | Yes |  |  | No |  |
| target | varchar(255) | Yes |  |  | No |  |
| forecast_enabled | bool | Yes |  |  | No |  |
| segment | varchar(255) | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| is_active | varchar(25) | Yes | 'Yes'::character varying |  | No |  |
| productmaster | bytea | Yes |  |  | No |  |

---

## product_content_latest

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_content_latest_id | int4(32) | No | nextval('i2oretail_dev.product_content_latest_product_content_latest_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| product_master_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| product_categorization | varchar(255) | Yes |  |  | No |  |
| product_dimensions | varchar(255) | Yes |  |  | No |  |
| product_weight | varchar(255) | Yes |  |  | No |  |
| legal_disclaimer | varchar(1000) | Yes |  |  | No |  |
| safety_information | varchar(1000) | Yes |  |  | No |  |
| ingredients | varchar(1000) | Yes |  |  | No |  |
| thumbnail_list | text | Yes |  |  | No |  |
| period | varchar(100) | Yes |  |  | No |  |
| source | varchar(255) | Yes |  |  | No |  |
| time_of_day | varchar(100) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| a_plus | varchar(255) | Yes |  |  | No |  |
| org_id_dp | int4(32) | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| bullet_point_list | text | Yes |  |  | No |  |
| image_list | text | Yes |  |  | No |  |
| video_list | text | Yes |  |  | No |  |
| product_description | text | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |

---

## product_content_latest_20241007

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_content_latest_id | int4(32) | Yes |  |  | No |  |
| product_master_id | int4(32) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  |  | No |  |
| product_code | varchar(50) | Yes |  |  | No |  |
| product_categorization | varchar(1000) | Yes |  |  | No |  |
| product_dimensions | varchar(1000) | Yes |  |  | No |  |
| product_weight | varchar(1000) | Yes |  |  | No |  |
| legal_disclaimer | varchar(1000) | Yes |  |  | No |  |
| safety_information | varchar(1000) | Yes |  |  | No |  |
| ingredients | varchar(1000) | Yes |  |  | No |  |
| thumbnail_list | text | Yes |  |  | No |  |
| period | varchar(100) | Yes |  |  | No |  |
| source | varchar(200) | Yes |  |  | No |  |
| time_of_day | varchar(100) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| a_plus | varchar(10) | Yes |  |  | No |  |
| org_id_dp | int4(32) | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| bullet_point_list | text | Yes |  |  | No |  |
| image_list | text | Yes |  |  | No |  |
| video_list | text | Yes |  |  | No |  |
| product_description | text | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |

---

## product_content_latest_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| a_plus | varchar | Yes |  |  | No |  |
| bullet_point_text | varchar | Yes |  |  | No |  |
| images_url | varchar | Yes |  |  | No |  |
| ingredients | varchar | Yes |  |  | No |  |
| legal_disclaimer | varchar | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | No |  |
| region | varchar | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| product_category | varchar | Yes |  |  | No |  |
| product_code | varchar | Yes |  |  | No |  |
| full_description | varchar | Yes |  |  | No |  |
| product_dimensions | varchar | Yes |  |  | No |  |
| product_title | varchar | Yes |  |  | No |  |
| shipping_weight | varchar | Yes |  |  | No |  |
| safety_information | varchar | Yes |  |  | No |  |
| video_thumbnail_url | varchar | Yes |  |  | No |  |
| time_of_day | varchar | Yes |  |  | No |  |
| video_url | varchar | Yes |  |  | No |  |
| sh_row | int4(32) | Yes |  |  | No |  |
| org_id_dp | varchar | Yes |  |  | No |  |
| load_id | varchar | Yes |  |  | No |  |

---

## product_content_locked

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_content_locked_id | int4(32) | No | nextval('i2oretail_dev.product_content_locked_product_content_locked_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| product_master_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| product_lock_status | varchar(255) | Yes |  |  | No |  |
| product_title | varchar(255) | Yes |  |  | No |  |
| product_description | text | Yes |  |  | No |  |
| product_categorization | varchar(255) | Yes |  |  | No |  |
| bullet_point_list | text | Yes |  |  | No |  |
| image_list | varchar(4000) | Yes |  |  | No |  |
| product_dimensions | varchar(255) | Yes |  |  | No |  |
| product_weight | varchar(255) | Yes |  |  | No |  |
| legal_disclaimer | varchar(1000) | Yes |  |  | No |  |
| safety_information | varchar(1000) | Yes |  |  | No |  |
| ingredients | varchar(1000) | Yes |  |  | No |  |
| video_list | text | Yes |  |  | No |  |
| thumbnail_list | text | Yes |  |  | No |  |
| source | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| a_plus | varchar(255) | Yes |  |  | No |  |

---

## product_data_resouces

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.product_data_resouces_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| resource_type | varchar(255) | Yes |  |  | No |  |
| upload_type_id | int4(32) | Yes |  |  | No |  |

---

## product_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_code | text | No |  |  | No |  |
| brand | text | Yes |  |  | No |  |
| category | text | Yes |  |  | No |  |
| buy_box_price | float8(53) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| page_rank | int4(32) | Yes |  |  | No |  |
| amazon_choice | bool | Yes |  |  | No |  |
| id | int4(32) | No |  | PRIMARY KEY | Yes |  |

---

## product_discovery_scraping_input

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| scraping_input_id | int4(32) | No | nextval('i2oretail_dev.product_discovery_scraping_input_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_on | timestamp | Yes | CURRENT_TIMESTAMP |  | No |  |
| created_by | varchar(100) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes | CURRENT_TIMESTAMP |  | No |  |
| last_modified_by | varchar(100) | Yes |  |  | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY | Yes |  |
| marketplace_id | int4(32) | No |  | FOREIGN KEY | Yes |  |
| product_code | varchar(255) | Yes |  |  | Yes |  |
| i2o_product_id | varchar(255) | Yes |  |  | Yes |  |
| productdetails_scrape | bool | Yes | false |  | No |  |
| resellerdetails_scrape | bool | Yes | false |  | No |  |
| resellerinventory_scrape | bool | Yes | false |  | No |  |
| customerreviews_scrape | bool | Yes | false |  | No |  |
| productdiscovery_scrape | bool | Yes | false |  | No |  |
| html | bool | Yes | false |  | No |  |
| frequency | varchar(50) | Yes | 'DEFAULT'::character varying |  | No |  |
| source_product_code | varchar(255) | Yes |  |  | No |  |

---

## product_keywords

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| marketplace_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| product_code | varchar | No |  | PRIMARY KEY | Yes |  |
| keywords | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |

---

## product_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_master_id | int4(32) | No | nextval('i2oretail_dev.product_master_product_master_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| catalog_price | float8(53) | Yes |  |  | No |  |
| ean | varchar(255) | Yes |  |  | No |  |
| gcs_bucket | varchar(255) | Yes |  |  | No |  |
| isbn | varchar(255) | Yes |  |  | No |  |
| map | float8(53) | Yes |  |  | No |  |
| model_number | varchar(255) | Yes |  |  | No |  |
| pasin | varchar(255) | Yes |  |  | No |  |
| product_code | varchar(255) | Yes |  |  | Yes |  |
| product_code_type | varchar(255) | Yes |  |  | No |  |
| product_status | varchar(255) | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| product_url | text | Yes |  |  | No |  |
| rank | int4(32) | Yes |  |  | No |  |
| rank_1p | int4(32) | Yes |  |  | No |  |
| rank_3p | int4(32) | Yes |  |  | No |  |
| release_date | date | Yes |  |  | No |  |
| replenishment_status | varchar(255) | Yes |  |  | No |  |
| search_terms_group | varchar(255) | Yes |  |  | No |  |
| short_name | varchar(1024) | Yes |  |  | No |  |
| sku | varchar(255) | Yes |  |  | No |  |
| source_system_id | varchar(255) | Yes |  |  | No |  |
| tags | varchar(255) | Yes |  |  | No |  |
| upc | varchar(255) | Yes |  |  | No |  |
| valid_from | date | Yes |  |  | No |  |
| valid_to | date | Yes |  |  | No |  |
| brand_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| category_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY | Yes |  |
| product_image_url | text | Yes |  |  | No |  |
| daily_alerts | bool | Yes |  |  | No |  |
| i2o_product_id | varchar(255) | Yes |  |  | No |  |
| auditgroup_id | int4(32) | Yes |  |  | No | Used in trigger for inserting audit records |
| sub_category | varchar(255) | Yes |  |  | No |  |
| sales_rank | int4(32) | Yes |  |  | No |  |
| upload_type | varchar(250) | Yes |  |  | No |  |
| source | varchar(255) | Yes |  |  | No |  |
| is_active | varchar(25) | Yes | 'Yes'::character varying |  | No |  |
| watchlist | bool | Yes |  |  | No |  |
| org_type | varchar(255) | Yes |  |  | No |  |
| sales_velocity_group | varchar(255) | Yes |  |  | No |  |
| segment | varchar(255) | Yes |  |  | No |  |
| target | varchar(255) | Yes |  |  | No |  |

---

## product_master_20241007

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_master_id | int4(32) | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| catalog_price | float8(53) | Yes |  |  | No |  |
| ean | varchar(255) | Yes |  |  | No |  |
| gcs_bucket | varchar(255) | Yes |  |  | No |  |
| isbn | varchar(255) | Yes |  |  | No |  |
| map | float8(53) | Yes |  |  | No |  |
| model_number | varchar(255) | Yes |  |  | No |  |
| org_type | varchar(255) | Yes |  |  | No |  |
| pasin | varchar(255) | Yes |  |  | No |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| product_code_type | varchar(255) | Yes |  |  | No |  |
| product_status | varchar(255) | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| product_url | text | Yes |  |  | No |  |
| rank | int4(32) | Yes |  |  | No |  |
| rank_1p | int4(32) | Yes |  |  | No |  |
| rank_3p | int4(32) | Yes |  |  | No |  |
| release_date | date | Yes |  |  | No |  |
| replenishment_status | varchar(255) | Yes |  |  | No |  |
| search_terms_group | varchar(255) | Yes |  |  | No |  |
| short_name | varchar(1024) | Yes |  |  | No |  |
| sku | varchar(255) | Yes |  |  | No |  |
| source_system_id | varchar(255) | Yes |  |  | No |  |
| tags | varchar(255) | Yes |  |  | No |  |
| upc | varchar(255) | Yes |  |  | No |  |
| valid_from | date | Yes |  |  | No |  |
| valid_to | date | Yes |  |  | No |  |
| watchlist | bool | Yes |  |  | No |  |
| brand_id | int4(32) | Yes |  |  | No |  |
| category_id | int4(32) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| product_image_url | text | Yes |  |  | No |  |
| daily_alerts | bool | Yes |  |  | No |  |
| i2o_product_id | varchar(255) | Yes |  |  | No |  |
| auditgroup_id | int4(32) | Yes |  |  | No |  |
| sub_category | varchar(255) | Yes |  |  | No |  |
| sales_velocity_group | varchar(255) | Yes |  |  | No |  |
| target | varchar(255) | Yes |  |  | No |  |
| sales_rank | int4(32) | Yes |  |  | No |  |
| segment | varchar(200) | Yes |  |  | No |  |
| upload_type | varchar(250) | Yes |  |  | No |  |
| source | varchar(255) | Yes |  |  | No |  |
| is_active | varchar(25) | Yes |  |  | No |  |

---

## product_master_bq_dump

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| alerts_exceptions_enabled | bool | Yes |  |  | No |  |
| bcm_enabled | bool | Yes |  |  | No |  |
| brand | varchar(255) | Yes |  |  | No |  |
| brand_code | varchar(255) | Yes |  |  | No |  |
| buybox_alerts_daily | varchar(255) | Yes |  |  | No |  |
| buybox_alerts_hourly | varchar(255) | Yes |  |  | No |  |
| buybox_html | varchar(255) | Yes |  |  | No |  |
| catalog_price | float4(24) | Yes |  |  | No |  |
| category | varchar(255) | Yes |  |  | No |  |
| competitor_enabled | bool | Yes |  |  | No |  |
| customer_review_enabled | bool | Yes |  |  | No |  |
| ean | varchar(255) | Yes |  |  | No |  |
| eol | varchar(255) | Yes |  |  | No |  |
| forecast_enabled | bool | Yes |  |  | No |  |
| isbn | varchar(255) | Yes |  |  | No |  |
| item_number | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| load_id | varchar(255) | Yes |  |  | No |  |
| map | varchar(255) | Yes |  |  | No |  |
| marketplace | varchar(255) | Yes |  |  | No |  |
| master_enabled | bool | Yes |  |  | No |  |
| model_number | varchar(255) | Yes |  |  | No |  |
| multiplatform_enabled | bool | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| org_type | varchar(255) | Yes |  |  | No |  |
| pasin | varchar(255) | Yes |  |  | No |  |
| pricemonitor_enabled | bool | Yes |  |  | No |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| product_code_type | varchar(255) | Yes |  |  | No |  |
| product_image_url | text | Yes |  |  | No |  |
| product_status | varchar(255) | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| product_url | text | Yes |  |  | No |  |
| record_valid_from | date | Yes |  |  | No |  |
| record_valid_to | date | Yes |  |  | No |  |
| region | varchar(255) | Yes |  |  | No |  |
| release_date | date | Yes |  |  | No |  |
| replenishment_status | varchar(255) | Yes |  |  | No |  |
| reseller_enabled | bool | Yes |  |  | No |  |
| search_rank_enabled | bool | Yes |  |  | No |  |
| search_terms_group | varchar(255) | Yes |  |  | No |  |
| short_name | text | Yes |  |  | No |  |
| sku | varchar(255) | Yes |  |  | No |  |
| source_system_id | varchar(255) | Yes |  |  | No |  |
| sub_category | varchar(255) | Yes |  |  | No |  |
| upc | varchar(255) | Yes |  |  | No |  |
| valid_from | varchar(255) | Yes |  |  | No |  |
| valid_to | varchar(255) | Yes |  |  | No |  |
| watchlist | varchar(255) | Yes |  |  | No |  |
| wbr | bool | Yes |  |  | No |  |
| daily_alerts | bool | Yes |  |  | No |  |
| i2o_product_id | varchar(255) | Yes |  |  | No |  |

---

## product_master_drop

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_master_id | varchar(2000) | Yes |  |  | No |  |
| created_by | varchar(2000) | Yes |  |  | No |  |
| created_on | varchar(2000) | Yes |  |  | No |  |
| last_modified_by | varchar(2000) | Yes |  |  | No |  |
| last_modified_on | varchar(2000) | Yes |  |  | No |  |
| catalog_price | varchar(2000) | Yes |  |  | No |  |
| ean | varchar(2000) | Yes |  |  | No |  |
| gcs_bucket | varchar(2000) | Yes |  |  | No |  |
| isbn | varchar(2000) | Yes |  |  | No |  |
| map | varchar(2000) | Yes |  |  | No |  |
| model_number | varchar(2000) | Yes |  |  | No |  |
| org_type | varchar(2000) | Yes |  |  | No |  |
| pasin | varchar(2000) | Yes |  |  | No |  |
| product_code | varchar(2000) | Yes |  |  | No |  |
| product_code_type | varchar(2000) | Yes |  |  | No |  |
| product_status | varchar(2000) | Yes |  |  | No |  |
| product_title | varchar(2000) | Yes |  |  | No |  |
| product_url | varchar(2000) | Yes |  |  | No |  |
| rank | varchar(2000) | Yes |  |  | No |  |
| rank_1p | varchar(2000) | Yes |  |  | No |  |
| rank_3p | varchar(2000) | Yes |  |  | No |  |
| release_date | varchar(2000) | Yes |  |  | No |  |
| replenishment_status | varchar(2000) | Yes |  |  | No |  |
| search_terms_group | varchar(2000) | Yes |  |  | No |  |
| short_name | varchar(2000) | Yes |  |  | No |  |
| sku | varchar(2000) | Yes |  |  | No |  |
| source_system_id | varchar(2000) | Yes |  |  | No |  |
| tags | varchar(2000) | Yes |  |  | No |  |
| upc | varchar(2000) | Yes |  |  | No |  |
| valid_from | varchar(2000) | Yes |  |  | No |  |
| valid_to | varchar(2000) | Yes |  |  | No |  |
| watchlist | varchar(2000) | Yes |  |  | No |  |
| brand_id | varchar(2000) | Yes |  |  | No |  |
| category_id | varchar(2000) | Yes |  |  | No |  |
| marketplace_id | varchar(2000) | Yes |  |  | No |  |
| org_id | varchar(2000) | Yes |  |  | No |  |
| product_image_url | varchar(2000) | Yes |  |  | No |  |
| daily_alerts | varchar(2000) | Yes |  |  | No |  |
| i2o_product_id | varchar(2000) | Yes |  |  | No |  |
| auditgroup_id | varchar(2000) | Yes |  |  | No |  |
| sub_category | varchar(2000) | Yes |  |  | No |  |
| sales_velocity_group | varchar(2000) | Yes |  |  | No |  |
| target | varchar(2000) | Yes |  |  | No |  |
| sales_rank | varchar(2000) | Yes |  |  | No |  |
| segment | varchar(2000) | Yes |  |  | No |  |
| upload_type | varchar(2000) | Yes |  |  | No |  |
| source | varchar(2000) | Yes |  |  | No |  |
| is_active | varchar(2000) | Yes |  |  | No |  |

---

## product_master_locked_test

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_content_locked_id | int4(32) | No | nextval('i2oretail_dev.product_master_locked_test_product_content_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| bullet_point_list | varchar(255) | Yes |  |  | No |  |
| image_list | varchar(255) | Yes |  |  | No |  |
| ingredients | varchar(255) | Yes |  |  | No |  |
| legal_disclaimer | varchar(255) | Yes |  |  | No |  |
| product_locked_status | varchar(255) | Yes |  |  | No |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| product_description | varchar(255) | Yes |  |  | No |  |
| product_dimensions | varchar(255) | Yes |  |  | No |  |
| product_master_id | varchar(255) | Yes |  |  | No |  |
| product_title | varchar(255) | Yes |  |  | No |  |
| product_weight | varchar(255) | Yes |  |  | No |  |
| product_categorization | varchar(255) | Yes |  |  | No |  |
| source | varchar(255) | Yes |  |  | No |  |
| thumbnail_list | varchar(255) | Yes |  |  | No |  |
| video_list | varchar(255) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| locked_status | varchar(255) | Yes |  |  | No |  |

---

## product_master_scraping_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.product_master_scraping_config_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| asin | varchar(255) | Yes |  |  | No |  |
| brand | varchar(255) | Yes |  |  | No |  |
| customerreviews_scrape | bool | Yes |  |  | No |  |
| customerreviews_scrape_frequency | varchar(255) | Yes |  |  | No |  |
| customerreviews_scrape_startdate | date | Yes |  |  | No |  |
| customerreviews_scrape_time | varchar(255) | Yes |  |  | No |  |
| html | bool | Yes |  |  | No |  |
| html_scrape_time | varchar(255) | Yes |  |  | No |  |
| html_scraping_frequency | varchar(255) | Yes |  |  | No |  |
| html_start_date | date | Yes |  |  | No |  |
| html_weekofday_scraping | varchar(255) | Yes |  |  | No |  |
| market_place | varchar(255) | Yes |  |  | No |  |
| model_number | varchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| productdetail_scrape_frequency | varchar(255) | Yes |  |  | No |  |
| productdetail_scrape_time | varchar(255) | Yes |  |  | No |  |
| productdetails_scrape | bool | Yes |  |  | No |  |
| productdetails_scrape_startdate | date | Yes |  |  | No |  |
| product_title | text | Yes |  |  | No |  |
| product_url | text | Yes |  |  | No |  |
| region | varchar(255) | Yes |  |  | No |  |
| resellerdetails_scrape | bool | Yes |  |  | No |  |
| resellerdetails_scrape_frequency | varchar(255) | Yes |  |  | No |  |
| resellerdetails_scrape_startdate | date | Yes |  |  | No |  |
| resellerdetails_scrape_time | varchar(255) | Yes |  |  | No |  |
| reseller_inventory | bool | Yes |  |  | No |  |
| reseller_inventory_scrape_time | varchar(255) | Yes |  |  | No |  |
| reseller_inventory_scraping_frequency | varchar(255) | Yes |  |  | No |  |
| reseller_inventory_start_date | date | Yes |  |  | No |  |
| reseller_inventory_weekofday_scraping | varchar(255) | Yes |  |  | No |  |
| scraper | int4(32) | Yes |  |  | No |  |
| searchrankdetails_scrape | bool | Yes |  |  | No |  |
| searchrankdetails_scrape_frequency | varchar(255) | Yes |  |  | No |  |
| searchrankdetails_scrape_startdate | date | Yes |  |  | No |  |
| searchrankdetails_scrape_time | varchar(255) | Yes |  |  | No |  |
| searchrank_weekofday_scraping | varchar(255) | Yes |  |  | No |  |
| upc | varchar(255) | Yes |  |  | No |  |
| product_master_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| productmaster | bytea | Yes |  |  | No |  |

---

## product_master_scraping_input

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| scraping_input_id | int4(32) | No | nextval('i2oretail_dev.product_master_scraping_input_scraping_input_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| customerreviews_scrape | bool | Yes |  |  | No |  |
| html | bool | Yes |  |  | No |  |
| i2o_product_id | varchar(255) | Yes |  | UNIQUE | Yes |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| productdetails_scrape | bool | Yes |  |  | No |  |
| productdiscovery_scrape | bool | Yes |  |  | No |  |
| resellerdetails_scrape | bool | Yes |  |  | No |  |
| resellerinventory_scrape | bool | Yes |  |  | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | No |  | FOREIGN KEY, UNIQUE | Yes |  |
| frequency | varchar(255) | Yes |  |  | No |  |
| source_product_code | varchar(255) | Yes |  |  | No |  |
| marketplace | bytea | Yes |  |  | No |  |
| organization | bytea | Yes |  |  | No |  |
| product_url | text | Yes |  |  | No |  |
| input_type | varchar(255) | Yes |  |  | No |  |

---

## product_master_test

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dev.product_master_test_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| i2o_product_id | varchar(255) | Yes |  |  | No |  |
| client_name | varchar(255) | Yes |  |  | No |  |
| marketplace | varchar(255) | Yes |  |  | No |  |
| region | varchar(255) | Yes |  |  | No |  |
| product_id | varchar(255) | Yes |  |  | No |  |
| short_name | varchar(500) | Yes |  |  | No |  |
| brand | varchar(255) | Yes |  |  | No |  |
| category | varchar(255) | Yes |  |  | No |  |
| product_title | varchar(255) | Yes |  |  | No |  |
| model_number | varchar(255) | Yes |  |  | No |  |
| parent_product_id | varchar(255) | Yes |  |  | No |  |
| sub_category | varchar(255) | Yes |  |  | No |  |
| upc | varchar(50) | Yes |  |  | No |  |
| list_price | varchar(255) | Yes |  |  | No |  |
| map | varchar(255) | Yes |  |  | No |  |
| sku | varchar(255) | Yes |  |  | No |  |
| replenishment_status | varchar(255) | Yes |  |  | No |  |
| release_date | varchar(255) | Yes |  |  | No |  |
| ean | varchar(50) | Yes |  |  | No |  |
| isbn | varchar(50) | Yes |  |  | No |  |
| product_tags | varchar(255) | Yes |  |  | No |  |
| search_terms_group | varchar(255) | Yes |  |  | No |  |
| product_url | varchar(1000) | Yes |  |  | No |  |
| active | bool | Yes | true |  | No |  |
| activate_for_monitoring | bool | Yes | false |  | No |  |
| track_reseller_inventory | bool | Yes | false |  | No |  |
| add_to_daily_alerts_email | bool | Yes | false |  | No |  |
| activate_forecasting | varchar(255) | Yes |  |  | No |  |
| activate_hourly_monitoring | bool | Yes | false |  | No |  |
| added | bool | Yes | false |  | No |  |

---

## product_master_tracking

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.product_master_tracking_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| alerts_exception_enabled | bool | Yes |  |  | No |  |
| bcm_enabled | bool | Yes |  |  | No |  |
| buybox_alerts_daily | bool | Yes |  |  | No |  |
| buybox_alerts_hourly | bool | Yes |  |  | No |  |
| buybox_html | bool | Yes |  |  | No |  |
| competitor_enabled | bool | Yes |  |  | No |  |
| customer_review_enabled | bool | Yes |  |  | No |  |
| eol | bool | Yes |  |  | No |  |
| master_enabled | bool | Yes |  |  | No |  |
| multiplatform_enabled | bool | Yes |  |  | No |  |
| pricemonitor_enabled | bool | Yes |  |  | No |  |
| reseller_enabled | bool | Yes |  |  | No |  |
| search_rank_enabled | bool | Yes |  |  | No |  |
| wbr | bool | Yes |  |  | No |  |
| product_master_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| reseller_inventory | bool | Yes |  |  | No |  |
| resellerinventory | bool | Yes |  |  | No |  |
| hourly_scraping | bool | Yes |  |  | No |  |
| productmaster | bytea | Yes |  |  | No |  |

---

## product_master_tracking_20241007

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| alerts_exception_enabled | bool | Yes |  |  | No |  |
| bcm_enabled | bool | Yes |  |  | No |  |
| buybox_alerts_daily | bool | Yes |  |  | No |  |
| buybox_alerts_hourly | bool | Yes |  |  | No |  |
| buybox_html | bool | Yes |  |  | No |  |
| competitor_enabled | bool | Yes |  |  | No |  |
| customer_review_enabled | bool | Yes |  |  | No |  |
| eol | bool | Yes |  |  | No |  |
| forecast_enabled | bool | Yes |  |  | No |  |
| master_enabled | bool | Yes |  |  | No |  |
| multiplatform_enabled | bool | Yes |  |  | No |  |
| pricemonitor_enabled | bool | Yes |  |  | No |  |
| reseller_enabled | bool | Yes |  |  | No |  |
| search_rank_enabled | bool | Yes |  |  | No |  |
| wbr | bool | Yes |  |  | No |  |
| product_master_id | int4(32) | Yes |  |  | No |  |
| reseller_inventory | bool | Yes |  |  | No |  |
| resellerinventory | bool | Yes |  |  | No |  |
| hourly_scraping | bool | Yes |  |  | No |  |

---

## product_master_user_comment

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| comment_id | int4(32) | No | nextval('i2oretail_dev.product_master_user_comment_sequence'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| product_code | varchar(100) | Yes |  |  | No |  |
| region | varchar(50) | Yes |  |  | No |  |
| platform | varchar(50) | Yes |  |  | No |  |
| org_type | varchar(100) | Yes |  |  | No |  |
| comment | text | Yes |  |  | No |  |
| user_email | varchar(255) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |

---

## product_matching_input

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.product_matching_input_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_on | timestamp | Yes |  |  | No |  |
| vendorid | int4(32) | Yes |  |  | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY | Yes |  |
| product_master_id | int4(32) | Yes |  | FOREIGN KEY | Yes |  |
| is_active | bool | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| target_marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| target_platform | varchar(255) | Yes |  |  | No |  |
| target_region | varchar(255) | Yes |  |  | No |  |
| marketplace | bytea | Yes |  |  | No |  |
| productmaster | bytea | Yes |  |  | No |  |

---

## product_matching_output

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.product_matching_output_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| customer_name | varchar(255) | Yes |  | UNIQUE | Yes |  |
| i2o_product_id | varchar(255) | Yes |  | UNIQUE | Yes |  |
| match_timestamp | timestamp | Yes |  |  | No |  |
| model_number | varchar(255) | Yes |  |  | No |  |
| platform | varchar(255) | Yes |  | UNIQUE | Yes |  |
| product_code | varchar(255) | Yes |  | UNIQUE | Yes |  |
| product_match_status | varchar(255) | Yes |  |  | No |  |
| product_title | varchar(1024) | Yes |  |  | No |  |
| region | varchar(255) | Yes |  | UNIQUE | Yes |  |
| source_product_url | varchar(1024) | Yes |  |  | No |  |
| status_code | int4(32) | Yes |  |  | No |  |
| target_product_code | varchar(255) | Yes |  |  | No |  |
| target_product_url | varchar | Yes |  |  | No |  |

---

## product_matching_output_bk

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | Yes |  |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| customer_name | varchar(255) | Yes |  |  | No |  |
| i2o_product_id | varchar(255) | Yes |  |  | No |  |
| match_timestamp | timestamp | Yes |  |  | No |  |
| model_number | varchar(255) | Yes |  |  | No |  |
| platform | varchar(255) | Yes |  |  | No |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| product_match_status | varchar(255) | Yes |  |  | No |  |
| product_title | varchar(255) | Yes |  |  | No |  |
| region | varchar(255) | Yes |  |  | No |  |
| source_product_url | varchar(255) | Yes |  |  | No |  |
| status_code | int4(32) | Yes |  |  | No |  |
| target_product_code | varchar(255) | Yes |  |  | No |  |
| target_product_url | varchar(255) | Yes |  |  | No |  |

---

## product_matching_output_demo

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.product_matching_output_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| customer_name | varchar(255) | Yes |  | UNIQUE | Yes |  |
| i2o_product_id | varchar(255) | Yes |  | UNIQUE | Yes |  |
| match_timestamp | timestamp | Yes |  |  | No |  |
| model_number | varchar(255) | Yes |  |  | No |  |
| platform | varchar(255) | Yes |  | UNIQUE | Yes |  |
| product_code | varchar(255) | Yes |  | UNIQUE | Yes |  |
| product_match_status | varchar(255) | Yes |  |  | No |  |
| product_title | varchar(255) | Yes |  |  | No |  |
| region | varchar(255) | Yes |  | UNIQUE | Yes |  |
| source_product_url | varchar(255) | Yes |  |  | No |  |
| status_code | int4(32) | Yes |  |  | No |  |
| target_product_code | varchar(255) | Yes |  |  | No |  |
| target_product_url | varchar(255) | Yes |  |  | No |  |

---

## product_matching_output_pp

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.product_matching_output_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| customer_name | varchar(255) | Yes |  | UNIQUE | Yes |  |
| i2o_product_id | varchar(255) | Yes |  | UNIQUE | Yes |  |
| match_timestamp | timestamp | Yes |  |  | No |  |
| model_number | varchar(255) | Yes |  |  | No |  |
| platform | varchar(255) | Yes |  | UNIQUE | Yes |  |
| product_code | varchar(255) | Yes |  | UNIQUE | Yes |  |
| product_match_status | varchar(255) | Yes |  |  | No |  |
| product_title | varchar(255) | Yes |  |  | No |  |
| region | varchar(255) | Yes |  | UNIQUE | Yes |  |
| source_product_url | varchar(255) | Yes |  |  | No |  |
| status_code | int4(32) | Yes |  |  | No |  |
| target_product_code | varchar(255) | Yes |  |  | No |  |
| target_product_url | varchar(1000) | Yes |  |  | No |  |

---

## product_matching_output_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| i2o_product_id | varchar(10000) | Yes |  |  | No |  |
| product_code | varchar(10000) | Yes |  |  | No |  |
| customer_name | varchar(10000) | Yes |  |  | No |  |
| region | varchar(10000) | Yes |  |  | No |  |
| source_product_url | varchar(10000) | Yes |  |  | No |  |
| product_title | varchar(10000) | Yes |  |  | No |  |
| platform | varchar(10000) | Yes |  |  | No |  |
| match_status | varchar(10000) | Yes |  |  | No |  |
| platform_product_url | varchar(10000) | Yes |  |  | No |  |
| platform_identifier | varchar(10000) | Yes |  |  | No |  |
| status_code | int4(32) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| match_timestamp | timestamp | Yes |  |  | No |  |
| source_system_id | varchar(100) | Yes |  |  | No |  |

---

## product_matching_output_stg_test

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| i2o_product_id | varchar(10000) | Yes |  |  | No |  |
| product_code | varchar(10000) | Yes |  |  | No |  |
| customer_name | varchar(10000) | Yes |  |  | No |  |
| region | varchar(10000) | Yes |  |  | No |  |
| source_product_url | varchar(10000) | Yes |  |  | No |  |
| product_title | varchar(10000) | Yes |  |  | No |  |
| platform | varchar(10000) | Yes |  |  | No |  |
| match_status | varchar(10000) | Yes |  |  | No |  |
| platform_product_url | varchar(10000) | Yes |  |  | No |  |
| platform_identifier | varchar(10000) | Yes |  |  | No |  |
| status_code | int4(32) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| match_timestamp | timestamp | Yes |  |  | No |  |

---

## product_matching_output_temp

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| i2o_product_id | varchar(255) | Yes |  |  | No |  |
| model_number | varchar(255) | Yes |  |  | No |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| product_match_status | varchar(255) | Yes |  |  | No |  |
| product_title | varchar(255) | Yes |  |  | No |  |
| short_name | varchar(255) | Yes |  |  | No |  |
| source_product_url | varchar(255) | Yes |  |  | No |  |
| target_product_url | varchar(255) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| target_product_code | varchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| id | int4(32) | Yes |  |  | No |  |
| match_status | varchar(255) | Yes |  |  | No |  |
| scrape_date | varchar(255) | Yes |  |  | No |  |
| scrape_timestamp | varchar(255) | Yes |  |  | No |  |

---

## product_matching_output_updated

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| i2o_product_id | varchar(60000) | Yes |  |  | No |  |
| product_code | varchar(60000) | Yes |  |  | No |  |
| customer_name | varchar(60000) | Yes |  |  | No |  |
| region | varchar(60000) | Yes |  |  | No |  |
| source_product_url | varchar(60000) | Yes |  |  | No |  |
| product_title | varchar(60000) | Yes |  |  | No |  |
| platform | varchar(60000) | Yes |  |  | No |  |
| match_status | varchar(60000) | Yes |  |  | No |  |
| platform_product_url | varchar(60000) | Yes |  |  | No |  |
| platform_identifier | varchar(60000) | Yes |  |  | No |  |
| status_code | varchar(60000) | Yes |  |  | No |  |
| created_on | varchar(60000) | Yes |  |  | No |  |
| match_timestamp | varchar(60000) | Yes |  |  | No |  |

---

## product_sales_velocity_grouping

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_velocity_id | int4(32) | No | nextval('i2oretail_dev.product_sales_velocity_grouping_product_velocity_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| product_code | varchar(255) | Yes |  | UNIQUE | Yes |  |
| product_sales | int4(32) | No |  |  | No |  |
| org_type | varchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| marketplace | varchar(255) | Yes |  |  | No |  |
| region | varchar(255) | Yes |  |  | No |  |
| sales_velocity_tag | varchar(255) | Yes |  |  | No |  |
| target | varchar(255) | Yes |  |  | No |  |

---

## product_upc_matching_output

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.product_upc_matching_output_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_on | timestamp | Yes | CURRENT_TIMESTAMP |  | No |  |
| input_created_on | timestamp | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| created_by | varchar(100) | Yes |  |  | No |  |
| last_modified_by | varchar(100) | Yes |  |  | No |  |
| product_code | varchar(100) | Yes |  | UNIQUE | Yes |  |
| customer_name | varchar(200) | Yes |  | UNIQUE | Yes |  |
| region | varchar(100) | Yes |  | UNIQUE | Yes |  |
| source_product_url | text | Yes |  |  | No |  |
| upc | varchar(100) | Yes |  | UNIQUE | Yes |  |
| product_title | text | Yes |  |  | No |  |
| platform | varchar(100) | Yes |  | UNIQUE | Yes |  |
| match_status | varchar(50) | Yes |  |  | Yes |  |
| platform_product_url | text | Yes |  |  | No |  |
| platform_identifier | varchar(150) | Yes |  | UNIQUE | Yes |  |
| match_timestamp | timestamp | Yes |  |  | No |  |
| status_code | int4(32) | Yes |  |  | No |  |
| is_active | bool | Yes | true |  | No |  |

---

## project_alm_settings

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| alm_setting_uuid | varchar(40) | No |  |  | Yes |  |
| project_uuid | varchar(50) | No |  |  | Yes |  |
| alm_repo | varchar(256) | Yes |  |  | No |  |
| alm_slug | varchar(256) | Yes |  |  | Yes |  |
| updated_at | int8(64) | No |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |
| summary_comment_enabled | bool | Yes |  |  | No |  |
| monorepo | bool | No |  |  | No |  |

---

## project_branches

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(50) | No |  | PRIMARY KEY | Yes |  |
| project_uuid | varchar(50) | No |  |  | Yes |  |
| kee | varchar(255) | No |  |  | Yes |  |
| branch_type | varchar(12) | No |  |  | Yes |  |
| merge_branch_uuid | varchar(50) | Yes |  |  | No |  |
| pull_request_binary | bytea | Yes |  |  | No |  |
| manual_baseline_analysis_uuid | varchar(40) | Yes |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |
| updated_at | int8(64) | No |  |  | No |  |
| exclude_from_purge | bool | No | false |  | No |  |
| need_issue_sync | bool | No |  |  | No |  |

---

## project_links

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| project_uuid | varchar(40) | No |  |  | Yes |  |
| link_type | varchar(20) | No |  |  | No |  |
| name | varchar(128) | Yes |  |  | No |  |
| href | varchar(2048) | No |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |
| updated_at | int8(64) | No |  |  | No |  |

---

## project_mappings

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| key_type | varchar(200) | No |  |  | Yes |  |
| kee | varchar(4000) | No |  |  | Yes |  |
| project_uuid | varchar(40) | No |  |  | Yes |  |
| created_at | int8(64) | No |  |  | No |  |

---

## project_measures

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| value | numeric(38,20) | Yes |  |  | No |  |
| analysis_uuid | varchar(50) | No |  |  | Yes |  |
| component_uuid | varchar(50) | No |  |  | Yes |  |
| text_value | varchar(4000) | Yes |  |  | No |  |
| alert_status | varchar(5) | Yes |  |  | No |  |
| alert_text | varchar(4000) | Yes |  |  | No |  |
| person_id | int4(32) | Yes |  |  | No |  |
| variation_value_1 | numeric(38,20) | Yes |  |  | No |  |
| measure_data | bytea | Yes |  |  | No |  |
| metric_uuid | varchar(40) | No |  |  | Yes |  |

---

## project_qgates

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| project_uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| quality_gate_uuid | varchar(40) | No |  |  | Yes |  |

---

## project_qprofiles

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| project_uuid | varchar(50) | No |  |  | Yes |  |
| profile_key | varchar(50) | No |  |  | Yes |  |

---

## projects

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| kee | varchar(400) | No |  |  | Yes |  |
| qualifier | varchar(10) | No |  |  | Yes |  |
| name | varchar(2000) | Yes |  |  | No |  |
| description | varchar(2000) | Yes |  |  | No |  |
| private | bool | No |  |  | No |  |
| tags | varchar(500) | Yes |  |  | No |  |
| created_at | int8(64) | Yes |  |  | No |  |
| updated_at | int8(64) | No |  |  | No |  |

---

## properties

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| prop_key | varchar(512) | No |  |  | Yes |  |
| is_empty | bool | No |  |  | No |  |
| text_value | varchar(4000) | Yes |  |  | No |  |
| clob_value | text | Yes |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |
| component_uuid | varchar(40) | Yes |  |  | No |  |
| user_uuid | varchar(255) | Yes |  |  | No |  |

---

## pub_sub_event_ops

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| event_id | int8(64) | No | nextval('i2oretail_dev.pub_sub_event_ops_event_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| aggregate_type | text | Yes |  |  | No |  |
| aggregate_id | text | Yes |  |  | No |  |
| event_type | text | Yes |  |  | No |  |
| payload_json | jsonb | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |

---

## q

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## qprofile_changes

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| kee | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| rules_profile_uuid | varchar(255) | No |  |  | Yes |  |
| change_type | varchar(20) | No |  |  | No |  |
| user_uuid | varchar(255) | Yes |  |  | No |  |
| change_data | text | Yes |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |

---

## qprofile_edit_groups

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| qprofile_uuid | varchar(255) | No |  |  | Yes |  |
| created_at | int8(64) | No |  |  | No |  |
| group_uuid | varchar(40) | No |  |  | Yes |  |

---

## qprofile_edit_users

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| qprofile_uuid | varchar(255) | No |  |  | Yes |  |
| created_at | int8(64) | No |  |  | No |  |
| user_uuid | varchar(255) | No |  |  | Yes |  |

---

## quality_gate_conditions

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| operator | varchar(3) | Yes |  |  | No |  |
| value_error | varchar(64) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| metric_uuid | varchar(40) | No |  |  | No |  |
| qgate_uuid | varchar(40) | No |  |  | No |  |

---

## quality_gates

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| name | varchar(100) | No |  |  | No |  |
| is_built_in | bool | No |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |

---

## query

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| query_string | text | No |  |  | No |  |
| group_by | varchar(255) | Yes |  |  | No |  |
| order_by | varchar(255) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(255) | Yes |  |  | No |  |

---

## query_01_03_2024_back

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## query_20230311

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## query_20240229

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## query_20240304

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## query_20240308

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## query_20240315

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## query_20240326

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## query_20240401

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## query_amogh

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(255) | Yes |  |  | No |  |
| order_by | varchar(255) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(255) | Yes |  |  | No |  |

---

## query_backup

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## query_backup_29_02_2024

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## query_bck_today31

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## query_bckp

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## rainforest_output_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | varchar | Yes |  |  | No |  |
| custom_id | text | Yes |  |  | No |  |
| success | bool | Yes |  |  | No |  |
| type | varchar | Yes |  |  | No |  |
| amazon_domain | varchar | Yes |  |  | No |  |
| search_term | varchar | Yes |  |  | No |  |
| sort_by | varchar | Yes |  |  | No |  |
| request_page | int4(32) | Yes |  |  | No |  |
| result_position | int8(64) | Yes |  |  | No |  |
| result_title | text | Yes |  |  | No |  |
| asin | varchar | Yes |  |  | No |  |
| link | varchar | Yes |  |  | No |  |
| image | varchar | Yes |  |  | No |  |
| rating | float8(53) | Yes |  |  | No |  |
| ratings_total | int4(32) | Yes |  |  | No |  |
| is_prime | bool | Yes |  |  | No |  |
| sponsored | bool | Yes |  |  | No |  |
| currency | varchar | Yes |  |  | No |  |
| value | float8(53) | Yes |  |  | No |  |
| page | int8(64) | Yes |  |  | No |  |
| is_add_on_item | bool | Yes |  |  | No |  |
| recent_sales | varchar | Yes |  |  | No |  |
| load_id | varchar | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | No |  |
| region | varchar | Yes |  |  | No |  |

---

## rating

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| rating_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| context_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| metric_type | varchar(100) | Yes |  |  | No |  |
| metric_properties | json | Yes |  |  | No |  |
| rating_source | varchar(10) | Yes |  |  | No |  |
| rating_souce_location | varchar(200) | Yes |  |  | No |  |

---

## region_zone_id_mapping

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| region | varchar | No |  | PRIMARY KEY | Yes |  |
| zone_id | varchar | No |  | PRIMARY KEY | Yes |  |
| region_alias_name | varchar(100) | Yes |  |  | No |  |

---

## rep

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| report_column_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| report_id | int4(32) | Yes |  |  | No |  |
| column_id | int4(32) | Yes |  |  | No |  |
| pinned | varchar(10) | Yes |  |  | No |  |
| is_visible | varchar(1) | Yes |  |  | No |  |
| is_default_visible | varchar(1) | Yes |  |  | No |  |
| org_types | varchar(50) | Yes |  |  | No |  |
| cell_renderer_framework | varchar(50) | Yes |  |  | No |  |
| cell_renderer_params | varchar(500) | Yes |  |  | No |  |

---

## report

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| report_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| report_title | varchar(255) | No |  |  | No |  |
| query_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| response_dto | varchar(255) | Yes |  |  | No |  |
| report_layout | json | Yes |  |  | No |  |
| report_type | varchar(255) | Yes |  |  | No |  |
| report_metadata | json | Yes |  |  | No |  |

---

## report_column

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| report_column_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| report_id | int4(32) | No |  | FOREIGN KEY | No |  |
| column_id | int4(32) | No |  | FOREIGN KEY | No |  |
| pinned | varchar(255) | Yes |  |  | No |  |
| is_visible | varchar(255) | No |  |  | No |  |
| is_default_visible | varchar(255) | No |  |  | No |  |
| org_types | varchar(255) | Yes |  |  | No |  |
| cell_renderer_framework | varchar(255) | Yes |  |  | No |  |
| cell_renderer_params | varchar(500) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| custom_header_tooltip | varchar(255) | Yes |  |  | No |  |

---

## report_column_back127

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| report_column_id | int4(32) | Yes |  |  | No |  |
| report_id | int4(32) | Yes |  |  | No |  |
| column_id | int4(32) | Yes |  |  | No |  |
| pinned | varchar(10) | Yes |  |  | No |  |
| is_visible | varchar(1) | Yes |  |  | No |  |
| is_default_visible | varchar(1) | Yes |  |  | No |  |
| org_types | varchar(50) | Yes |  |  | No |  |
| cell_renderer_framework | varchar(50) | Yes |  |  | No |  |
| cell_renderer_params | varchar(500) | Yes |  |  | No |  |

---

## report_column_backup_detail

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| report_column_id | int4(32) | Yes |  |  | No |  |
| report_id | int4(32) | Yes |  |  | No |  |
| column_id | int4(32) | Yes |  |  | No |  |
| pinned | varchar(10) | Yes |  |  | No |  |
| is_visible | varchar(1) | Yes |  |  | No |  |
| is_default_visible | varchar(1) | Yes |  |  | No |  |
| org_types | varchar(50) | Yes |  |  | No |  |
| cell_renderer_framework | varchar(50) | Yes |  |  | No |  |
| cell_renderer_params | varchar(500) | Yes |  |  | No |  |

---

## report_column_rahul

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| report_column_id | int4(32) | Yes |  |  | No |  |
| report_id | int4(32) | Yes |  |  | No |  |
| column_id | int4(32) | Yes |  |  | No |  |
| pinned | varchar(10) | Yes |  |  | No |  |
| is_visible | varchar(1) | Yes |  |  | No |  |
| is_default_visible | varchar(1) | Yes |  |  | No |  |
| org_types | varchar(50) | Yes |  |  | No |  |
| cell_renderer_framework | varchar(50) | Yes |  |  | No |  |
| cell_renderer_params | varchar(500) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| custom_header_tooltip | varchar(1000) | Yes |  |  | No |  |

---

## report_filter

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| report_filter_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| report_id | int4(32) | No |  | FOREIGN KEY | No |  |
| filter_id | int4(32) | No |  | FOREIGN KEY | No |  |
| display_order | int4(32) | Yes |  |  | No |  |
| master_query_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| allowed_subscription_types | varchar(255) | Yes |  |  | No |  |
| config | varchar(255) | Yes |  |  | No |  |

---

## report_org_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| report_config_id | int4(32) | No | nextval('i2oretail_dev.report_org_config_report_config_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| report_id | int4(32) | No |  |  | No |  |
| org_id | int4(32) | No |  |  | No |  |
| metadata | json | Yes |  |  | No |  |
| report_title | varchar(255) | Yes |  |  | No |  |
| report_title_alias | varchar(255) | Yes |  |  | No |  |

---

## reports_schedule_report

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| client_name | varchar | Yes |  |  | No |  |
| report_name | varchar | Yes |  |  | No |  |
| reporting_range | varchar | Yes |  |  | No |  |
| email_id | varchar | Yes |  |  | No |  |
| delivery_status | varchar | Yes |  |  | No |  |
| delivery_time | varchar | Yes |  |  | No |  |
| scheduled_time | varchar | Yes |  |  | No |  |
| difference | varchar | Yes |  |  | No |  |
| comment | varchar | Yes |  |  | No |  |

---

## reprt_column_backup

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| report_column_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| report_id | int4(32) | Yes |  |  | No |  |
| column_id | int4(32) | Yes |  |  | No |  |
| pinned | varchar(10) | Yes |  |  | No |  |
| is_visible | varchar(1) | Yes |  |  | No |  |
| is_default_visible | varchar(1) | Yes |  |  | No |  |
| org_types | varchar(50) | Yes |  |  | No |  |
| cell_renderer_framework | varchar(50) | Yes |  |  | No |  |
| cell_renderer_params | varchar(500) | Yes |  |  | No |  |

---

## research_enqueue_audit

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| audit_id | int8(64) | No | nextval('i2oretail_dev.research_enqueue_audit_audit_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| started_at | timestamptz | No | now() |  | No |  |
| ended_at | timestamptz | Yes |  |  | No |  |
| status | text | No | 'RUNNING'::text |  | No |  |
| rows_inserted | int4(32) | Yes | 0 |  | No |  |
| limit_requested | int4(32) | Yes |  |  | No |  |
| error_text | text | Yes |  |  | No |  |
| details | jsonb | Yes |  |  | No |  |
| function_name | text | Yes |  |  | No |  |

---

## reseller

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| reseller_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| reseller_name | varchar(100) | No |  |  | No |  |
| reseller_contact | varchar(20) | Yes |  |  | No |  |
| alias_name | text | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| created_by | varchar(100) | Yes |  |  | No |  |
| updated_by | varchar(100) | Yes |  |  | No |  |

---

## reseller_benefits

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.reseller_benefits_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| reseller | varchar(255) | Yes |  |  | No |  |
| products | varchar(255) | Yes |  |  | No |  |
| trend | varchar(255) | Yes |  |  | No |  |
| lost_sales | int4(32) | Yes |  |  | No |  |
| fulfilment_type | varchar(255) | Yes |  |  | No |  |
| enforcement_status | varchar(255) | Yes |  |  | No |  |
| average_reseller_inventory | int4(32) | Yes |  |  | No |  |

---

## reseller_enforcement_prioritization

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | UNIQUE | Yes |  |
| reseller_name | varchar(255) | No |  | UNIQUE | Yes |  |
| orgname_resellername | varchar(255) | No |  |  | No |  |
| status | bpchar(50) | Yes |  |  | No |  |
| email | varchar(255) | Yes |  |  | No |  |
| account_name | varchar(255) | Yes |  | UNIQUE | Yes |  |
| id | int4(32) | No | nextval('i2oretail_dev.reseller_enforcement_prioritization_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_at | timestamp | Yes | now() |  | No |  |
| updated_at | timestamp | Yes | now() |  | No |  |

---

## reseller_enforcement_tracker

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.reseller_enforcement_tracker_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| reseller_library_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| account_id | int4(32) | No |  | FOREIGN KEY | No |  |
| discovery_date | date | Yes |  |  | No |  |
| threat_score | numeric | Yes |  |  | No |  |
| is_active | bool | Yes | true |  | No |  |
| is_escalated | bool | Yes |  |  | No |  |
| push_status | bool | Yes | true |  | No |  |
| notification_status | text | Yes |  |  | No |  |
| notification_comments | text | Yes |  |  | No |  |
| recommended_approach | text | Yes |  |  | No |  |
| invoice_received | bool | Yes |  |  | No |  |
| updated_by | text | Yes |  |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |
| last_seen_at | date | Yes |  |  | No |  |
| notification_sub_status | text | Yes |  |  | No |  |
| date_of_invoice_received | date | Yes |  |  | No |  |
| buyer_account_details | jsonb | Yes |  |  | No |  |
| physical_mail_details | jsonb | Yes |  |  | No |  |
| created_by | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| is_paused | bool | Yes |  |  | No |  |
| paused_at | timestamptz | Yes |  |  | No |  |
| resumed_at | timestamptz | Yes |  |  | No |  |
| css_flag | bool | Yes |  |  | No |  |
| date_of_authorization | date | Yes |  |  | No |  |
| invoice_summary_status | text | Yes | 'Not Started'::text |  | No |  |
| is_cnd_recommended | bool | Yes |  |  | No |  |
| cnd_reasoning | text | Yes |  |  | No |  |
| is_map_violator | bool | Yes |  |  | No |  |
| fulfillment_type | text | Yes |  |  | No |  |
| cnd_metadata | jsonb | Yes |  |  | No |  |
| is_cnd_approved | bool | Yes |  |  | No |  |
| is_cnd_withdrawn | bool | Yes |  |  | No |  |
| fulfilment_type | text | Yes |  |  | No |  |
| avg_lost_sales | float8(53) | Yes |  |  | No |  |
| active_listings | int4(32) | Yes |  |  | No |  |
| lost_sales | float8(53) | Yes |  |  | No |  |
| cnd_report_enabled | bool | Yes | false |  | No |  |
| cnd_research_done | bool | Yes | false |  | No |  |

---

## reseller_enforcement_tracker_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| reseller_name | text | Yes |  |  | No |  |
| account_name | text | Yes |  |  | No |  |
| marketplace | text | Yes |  |  | No |  |
| region | text | Yes |  |  | No |  |
| inactive | text | Yes |  |  | No |  |
| date_of_discovery | date | Yes |  |  | No |  |
| last_seen | date | Yes |  |  | No |  |
| reseller_status | text | Yes |  |  | No |  |
| org_id_dp | int4(32) | Yes |  |  | No |  |
| reseller_id | text | Yes |  |  | No |  |
| reseller_threat_score | float8(53) | Yes |  |  | No |  |
| is_css_enabled_reseller | bool | Yes |  |  | No |  |
| fulfilment_type | text | Yes |  |  | No |  |
| is_map_violator | bool | Yes |  |  | No |  |
| cnd_reasoning | text | Yes |  |  | No |  |
| is_cnd_recommended | bool | Yes |  |  | No |  |
| avg_lost_sales | float8(53) | Yes |  |  | No |  |
| active_listings | int4(32) | Yes |  |  | No |  |

---

## reseller_geocode

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.reseller_geocode_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| reseller_library_id | int4(32) | No |  | FOREIGN KEY | No |  |
| lat | float8(53) | No |  |  | No |  |
| lng | float8(53) | No |  |  | No |  |
| state | varchar(100) | Yes |  |  | No |  |
| city | varchar(100) | Yes |  |  | No |  |
| country | varchar(100) | Yes |  |  | No |  |
| timestamp | timestamptz | No | now() |  | No |  |
| status | varchar(50) | No |  |  | No |  |

---

## reseller_library_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.reseller_library_master_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| reseller_id | text | No |  |  | No |  |
| reseller_name | text | Yes |  |  | No |  |
| reseller_url | text | Yes |  |  | No |  |
| business_name | text | Yes |  |  | No |  |
| business_address | text | Yes |  |  | No |  |
| business_contact | text | Yes |  |  | No |  |
| reseller_email | text | Yes |  |  | No |  |
| reseller_address | text | Yes |  |  | No |  |
| website | text | Yes |  |  | No |  |
| year_established | int4(32) | Yes |  |  | No |  |
| external_links | text | Yes |  |  | No |  |
| additional_attributes | jsonb | Yes |  |  | No |  |
| research_status | text | Yes |  |  | No |  |
| research_comments | text | Yes |  |  | No |  |
| primary_category | text | Yes |  |  | No |  |
| point_of_contact | text | Yes |  |  | No |  |
| sources | text | Yes |  |  | No |  |
| created_by | text | Yes |  |  | No |  |
| updated_by | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| updated_at | timestamptz | Yes | now() |  | No |  |

---

## reseller_library_master_backup

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  |  | No |  |
| reseller_id | text | Yes |  |  | No |  |
| reseller_name | text | Yes |  |  | No |  |
| reseller_url | text | Yes |  |  | No |  |
| business_name | text | Yes |  |  | No |  |
| business_address | text | Yes |  |  | No |  |
| business_contact | text | Yes |  |  | No |  |
| reseller_email | text | Yes |  |  | No |  |
| reseller_address | text | Yes |  |  | No |  |
| website | text | Yes |  |  | No |  |
| year_established | int4(32) | Yes |  |  | No |  |
| external_links | text | Yes |  |  | No |  |
| additional_attributes | jsonb | Yes |  |  | No |  |
| research_status | text | Yes |  |  | No |  |
| research_comments | text | Yes |  |  | No |  |
| primary_category | text | Yes |  |  | No |  |
| point_of_contact | text | Yes |  |  | No |  |
| sources | text | Yes |  |  | No |  |
| created_by | text | Yes |  |  | No |  |
| updated_by | text | Yes |  |  | No |  |
| created_at | timestamptz | Yes |  |  | No |  |
| updated_at | timestamptz | Yes |  |  | No |  |

---

## reseller_library_master_pipeline

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | Yes |  |  | No |  |
| marketplace_id | int8(64) | Yes |  |  | No |  |
| reseller_id | text | Yes |  |  | No |  |
| reseller_name | text | Yes |  |  | No |  |
| reseller_url | text | Yes |  |  | No |  |
| business_name | text | Yes |  |  | No |  |
| business_address | text | Yes |  |  | No |  |
| business_contact | text | Yes |  |  | No |  |
| reseller_email | text | Yes |  |  | No |  |
| reseller_address | text | Yes |  |  | No |  |
| website | text | Yes |  |  | No |  |
| year_established | int4(32) | Yes |  |  | No |  |
| external_links | text | Yes |  |  | No |  |
| additional_attributes | jsonb | Yes |  |  | No |  |
| research_status | text | Yes |  |  | No |  |
| research_comments | text | Yes |  |  | No |  |

---

## reseller_library_master_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| reseller_id | varchar | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | No |  |
| region | varchar | Yes |  |  | No |  |
| reseller_name | varchar | Yes |  |  | No |  |
| reseller_url | varchar | Yes |  |  | No |  |
| business_name | varchar | Yes |  |  | No |  |
| business_address | varchar | Yes |  |  | No |  |
| business_contact | varchar | Yes |  |  | No |  |
| reseller_email | varchar | Yes |  |  | No |  |
| website | varchar | Yes |  |  | No |  |
| year_established | date | Yes |  |  | No |  |
| external_links | varchar | Yes |  |  | No |  |
| research_status | varchar | Yes |  |  | No |  |
| scrape_timestamp | timestamp | Yes |  |  | No |  |
| additional_attributes | varchar | Yes |  |  | No |  |

---

## reseller_library_master_validation_20250730

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | Yes |  |  | No |  |
| marketplace_id | int8(64) | Yes |  |  | No |  |
| reseller_id | text | Yes |  |  | No |  |
| reseller_name | text | Yes |  |  | No |  |
| reseller_url | text | Yes |  |  | No |  |
| business_name | text | Yes |  |  | No |  |
| business_address | text | Yes |  |  | No |  |
| business_contact | text | Yes |  |  | No |  |
| reseller_email | text | Yes |  |  | No |  |
| reseller_address | text | Yes |  |  | No |  |
| website | text | Yes |  |  | No |  |
| year_established | int4(32) | Yes |  |  | No |  |
| external_links | text | Yes |  |  | No |  |
| additional_attributes | jsonb | Yes |  |  | No |  |
| research_status | text | Yes |  |  | No |  |
| research_comments | text | Yes |  |  | No |  |

---

## reseller_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| reseller_id | int4(32) | No | nextval('i2oretail_dev.reseller_master_reseller_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| reseller_name | varchar(255) | Yes |  |  | No |  |
| reseller_url | varchar(255) | Yes |  |  | No |  |
| self | varchar(255) | Yes |  |  | No |  |
| brand_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| category_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| reseller_metadata_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| is_active | bool | Yes | true |  | No |  |
| is_active_reseller | bool | Yes | true |  | No |  |
| alpha_seller | varchar(255) | Yes | 'FALSE'::character varying |  | No |  |
| email_id | varchar(255) | Yes |  |  | No |  |
| bcc_contacts | varchar(60000) | Yes |  |  | No |  |
| is_auto_enforced | varchar(255) | Yes |  |  | No |  |

---

## reseller_metadata

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| reseller_metadata_id | int4(32) | No | nextval('i2oretail_dev.reseller_metadata_reseller_metadata_id_seq'::regclass) | FOREIGN KEY, PRIMARY KEY | Yes |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| reseller_name | varchar(255) | Yes |  |  | No |  |
| product_code | varchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| self | varchar(255) | Yes |  |  | No |  |
| reseller_url | varchar(255) | Yes |  |  | No |  |
| is_active_reseller | bool | Yes | true |  | No |  |
| is_authorized_reseller | varchar(255) | Yes |  |  | No |  |
| processed | varchar(255) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| category_ids | varchar(255) | Yes |  |  | No |  |
| brand_ids | varchar(255) | Yes |  |  | No |  |
| unique_reseller_id | int4(32) | Yes |  |  | No |  |
| unique_id | int4(32) | Yes |  |  | No |  |
| is_active | varchar(25) | Yes | 'Yes'::character varying |  | No |  |
| brand | varchar(255) | Yes |  |  | No |  |
| brand_id | varchar(255) | Yes |  |  | No |  |
| category | varchar(255) | Yes |  |  | No |  |
| category_id | varchar(255) | Yes |  |  | No |  |
| region | varchar(255) | Yes |  |  | No |  |
| org_type | varchar(255) | Yes |  |  | No |  |
| alpha_seller | varchar(255) | Yes | 'FALSE'::character varying |  | No |  |
| email_id | varchar(255) | Yes |  |  | No |  |
| bcc_contacts | varchar(60000) | Yes |  |  | No |  |
| is_auto_enforced | varchar(255) | Yes |  |  | No |  |

---

## reseller_org_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.reseller_org_master_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY, UNIQUE | Yes |  |
| reseller_id | varchar(255) | Yes |  |  | No |  |
| reseller_name | varchar(255) | No |  | UNIQUE | Yes |  |
| reseller_address | text | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY, UNIQUE | Yes |  |
| is_authorized | bool | Yes |  |  | No |  |
| reseller_email | text | Yes |  |  | No |  |
| account_manager_email | varchar(255) | Yes |  |  | No |  |
| reseller_agreement_link | varchar(255) | Yes |  |  | No |  |
| created_on | timestamptz | Yes | now() |  | No |  |
| last_modified_on | timestamptz | Yes | now() |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| reseller_url | varchar(255) | Yes |  |  | No |  |
| auto_enforcement | varchar(255) | Yes |  |  | No |  |
| agreement_status | varchar(255) | Yes |  |  | No |  |
| agreement_type | varchar(255) | Yes |  |  | No |  |
| reseller_agreement_id | varchar(255) | Yes |  |  | No |  |

---

## reseller_org_master_stg

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.reseller_org_master_stg_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  |  | No |  |
| reseller_id | varchar(255) | Yes |  |  | No |  |
| reseller_name | varchar(255) | Yes |  |  | No |  |
| reseller_address | text | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  |  | No |  |
| is_authorized | bool | Yes |  |  | No |  |
| reseller_email | text | Yes |  |  | No |  |
| account_manager_email | varchar(255) | Yes |  |  | No |  |
| reseller_agreement_link | varchar(255) | Yes |  |  | No |  |
| created_on | timestamptz | Yes | now() |  | No |  |
| last_modified_on | timestamptz | Yes | now() |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |
| reseller_url | varchar(255) | Yes |  |  | No |  |
| auto_enforcement | varchar(255) | Yes |  |  | No |  |
| agreement_status | varchar(255) | Yes |  |  | No |  |
| agreement_type | varchar(255) | Yes |  |  | No |  |
| reseller_agreement_id | varchar(255) | Yes |  |  | No |  |

---

## reseller_research_agent

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.reseller_research_agent_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| reseller_library_id | int4(32) | No |  | FOREIGN KEY, UNIQUE | Yes |  |
| business_name | jsonb | Yes |  |  | No |  |
| business_address | jsonb | Yes |  |  | No |  |
| business_contact | jsonb | Yes |  |  | No |  |
| reseller_email | jsonb | Yes |  |  | No |  |
| reseller_address | jsonb | Yes |  |  | No |  |
| website | jsonb | Yes |  |  | No |  |
| year_established | jsonb | Yes |  |  | No |  |
| external_links | jsonb | Yes |  |  | No |  |
| additional_attributes | jsonb | Yes |  |  | No |  |
| agent_status | text | No | 'Not Ready'::text |  | No |  |
| research_comments | text | Yes |  |  | No |  |
| primary_category | jsonb | Yes |  |  | No |  |
| point_of_contact | jsonb | Yes |  |  | No |  |
| attachments | text | Yes |  |  | No |  |
| task_start | timestamptz | Yes |  |  | No |  |
| task_end | timestamptz | Yes |  |  | No |  |
| run_id | text | Yes |  |  | No |  |
| attempts | int4(32) | Yes |  |  | No |  |
| error_reason | text | Yes |  |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |
| is_accepted | bool | Yes |  |  | No |  |
| feedback | text | Yes |  |  | No |  |
| queue_status | text | Yes |  |  | No |  |

---

## ret_brand_map

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int8(64) | No |  |  | Yes |  |
| enforcement_tracker_id | int8(64) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| brand_id | int8(64) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| created_at | timestamp | No | CURRENT_TIMESTAMP |  | No |  |
| created_by | varchar(100) | Yes |  |  | No |  |

---

## rule_repositories

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| kee | varchar(200) | No |  | PRIMARY KEY | Yes |  |
| language | varchar(20) | No |  |  | No |  |
| name | varchar(4000) | No |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |

---

## rules

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| name | varchar(200) | Yes |  |  | No |  |
| plugin_rule_key | varchar(200) | No |  |  | Yes |  |
| plugin_key | varchar(200) | Yes |  |  | No |  |
| plugin_config_key | varchar(200) | Yes |  |  | No |  |
| plugin_name | varchar(255) | No |  |  | Yes |  |
| scope | varchar(20) | No |  |  | No |  |
| description | text | Yes |  |  | No |  |
| priority | int4(32) | Yes |  |  | No |  |
| status | varchar(40) | Yes |  |  | No |  |
| language | varchar(20) | Yes |  |  | No |  |
| def_remediation_function | varchar(20) | Yes |  |  | No |  |
| def_remediation_gap_mult | varchar(20) | Yes |  |  | No |  |
| def_remediation_base_effort | varchar(20) | Yes |  |  | No |  |
| gap_description | varchar(4000) | Yes |  |  | No |  |
| system_tags | varchar(4000) | Yes |  |  | No |  |
| is_template | bool | No | false |  | No |  |
| description_format | varchar(20) | Yes |  |  | No |  |
| rule_type | int2(16) | Yes |  |  | No |  |
| security_standards | varchar(4000) | Yes |  |  | No |  |
| is_ad_hoc | bool | No |  |  | No |  |
| is_external | bool | No |  |  | No |  |
| created_at | int8(64) | Yes |  |  | No |  |
| updated_at | int8(64) | Yes |  |  | No |  |
| template_uuid | varchar(40) | Yes |  |  | No |  |

---

## rules_metadata

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| rule_uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| note_data | text | Yes |  |  | No |  |
| note_user_uuid | varchar(255) | Yes |  |  | No |  |
| note_created_at | int8(64) | Yes |  |  | No |  |
| note_updated_at | int8(64) | Yes |  |  | No |  |
| remediation_function | varchar(20) | Yes |  |  | No |  |
| remediation_gap_mult | varchar(20) | Yes |  |  | No |  |
| remediation_base_effort | varchar(20) | Yes |  |  | No |  |
| tags | varchar(4000) | Yes |  |  | No |  |
| ad_hoc_name | varchar(200) | Yes |  |  | No |  |
| ad_hoc_description | text | Yes |  |  | No |  |
| ad_hoc_severity | varchar(10) | Yes |  |  | No |  |
| ad_hoc_type | int2(16) | Yes |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |
| updated_at | int8(64) | No |  |  | No |  |

---

## rules_parameters

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| name | varchar(128) | No |  |  | Yes |  |
| description | varchar(4000) | Yes |  |  | No |  |
| param_type | varchar(512) | No |  |  | No |  |
| default_value | varchar(4000) | Yes |  |  | No |  |
| rule_uuid | varchar(40) | No |  |  | Yes |  |

---

## rules_profiles

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| name | varchar(100) | No |  |  | No |  |
| language | varchar(20) | Yes |  |  | No |  |
| is_built_in | bool | No |  |  | No |  |
| rules_updated_at | varchar(100) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |

---

## sales_insights_metric

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| metric_id | int4(32) | No | nextval('i2oretail_dev.sales_insights_metric_metric_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| metric_name | varchar(255) | Yes |  |  | No |  |
| query_id | int4(32) | Yes |  |  | No |  |
| org_type | varchar(255) | Yes |  |  | No |  |
| order_id | int4(32) | Yes |  |  | No |  |

---

## sales_insights_metric_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| metric_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| org_type | varchar(10) | No |  | PRIMARY KEY | Yes |  |
| email | varchar(250) | No |  | PRIMARY KEY | Yes |  |
| time_range | varchar(25) | No |  | PRIMARY KEY | Yes |  |

---

## saml_message_ids

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| message_id | varchar(255) | No |  |  | Yes |  |
| expiration_date | int8(64) | No |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |

---

## samsung_audit_history

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.samsung_audit_history_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  |  | No |  |
| status | varchar | No |  |  | No |  |
| uploaded_file_gcs | varchar | Yes |  |  | No |  |
| created_by | varchar | Yes |  |  | No |  |
| updated_by | varchar | Yes |  |  | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |
| updated_at | timestamptz | Yes |  |  | No |  |
| processed_at | timestamptz | Yes |  |  | No |  |
| error_file_gcs | varchar | Yes |  |  | No |  |

---

## sanity_automation_clients

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| client_id | varchar(50) | No |  | PRIMARY KEY | Yes |  |
| client_file_location | varchar(100) | Yes |  |  | No |  |
| execution_status | varchar(20) | Yes |  |  | No |  |

---

## schedule_data_event

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | Yes |  |  | No |  |
| report_identifier | varchar(250) | Yes |  |  | No |  |
| org_type_cd | varchar(10) | Yes |  |  | No |  |
| data_event | varchar(45) | Yes |  |  | No |  |
| process | json | Yes |  |  | No |  |
| query_id | int4(32) | Yes |  |  | No |  |
| latest_report_only | bpchar(1) | Yes |  |  | No |  |

---

## schedule_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| schedule_detail_id | int4(32) | No | nextval('i2oretail_dev.schedule_details_seq'::regclass) | PRIMARY KEY | Yes |  |
| schedule_id | int4(32) | Yes | nextval('i2oretail_dev.schedule_details_seq'::regclass) | FOREIGN KEY, UNIQUE | Yes |  |
| report_id | int4(32) | Yes |  | FOREIGN KEY, UNIQUE | Yes |  |
| added_by | varchar(255) | Yes |  |  | No |  |
| filter | json | Yes |  |  | No |  |
| report_added_time | timestamp | Yes |  |  | No |  |
| component_id | varchar(255) | Yes |  | FOREIGN KEY, UNIQUE | Yes |  |
| component_column_definition | json | Yes |  |  | No |  |
| offset_value | int4(32) | Yes |  |  | No |  |
| no_of_periods | int4(32) | Yes |  |  | No |  |
| day_difference | int4(32) | Yes |  |  | No |  |
| saved_filter_id | int4(32) | Yes |  | UNIQUE | Yes |  |
| time_range | varchar(255) | Yes |  | UNIQUE | Yes |  |
| frequency | varchar(50) | Yes |  |  | No |  |

---

## schedule_execution_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| execution_id | int4(32) | No | nextval('i2oretail_dev.schedule_execution_details_seq1'::regclass) | PRIMARY KEY | Yes |  |
| schedule_id | int4(32) | Yes |  |  | No |  |
| run_time | timestamp | Yes |  |  | No |  |
| files_sent | varchar(500) | Yes |  |  | No |  |
| sent_to | varchar(1000) | Yes |  |  | No |  |
| source | varchar(25) | Yes |  |  | No |  |
| periodicity | int4(32) | Yes |  |  | No |  |
| dataload_condition | int4(32) | Yes |  |  | No |  |
| message_identifier | varchar | Yes |  |  | No |  |

---

## schedule_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| schedule_id | int4(32) | No | nextval('i2oretail_dev.schedule_master_seq'::regclass) | PRIMARY KEY | Yes |  |
| schedule_name | varchar(255) | Yes |  | UNIQUE | Yes |  |
| schedule_type | int4(32) | Yes |  |  | No |  |
| schedule_period | int4(32) | Yes |  |  | No |  |
| schedule_start_date | timestamp | Yes |  |  | No |  |
| schedule_end_date | timestamp | Yes |  |  | No |  |
| scheduled_time | time | Yes |  |  | No |  |
| schedule_days_of_period | int4(32) | Yes |  |  | No |  |
| scheduled_by | varchar(255) | Yes |  |  | No |  |
| email_to | varchar(10000) | Yes |  |  | No |  |
| scheduler_status | bpchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| creation_date | timestamp | Yes |  |  | No |  |
| last_updated | timestamp | Yes |  |  | No |  |
| trigger_type | int4(32) | Yes |  |  | No |  |
| weekly_schedule_day | int4(32) | Yes |  |  | No |  |
| format_type | int4(32) | Yes |  |  | No |  |
| issuspended | varchar(255) | Yes |  |  | No |  |
| dataload_condition | int4(32) | Yes |  |  | No |  |
| client_json_config | json | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| is_consolidated_email | bool | Yes |  |  | No |  |

---

## schedule_pending_status

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| pending_id | int4(32) | No | nextval('i2oretail_dev.schedule_pending_status_seq'::regclass) | PRIMARY KEY | Yes |  |
| schedule_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| pending_status | bpchar(1) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| report_id | varchar(100) | Yes |  |  | No |  |
| last_updated_at | timestamp | Yes |  |  | No |  |
| fail_count | int4(32) | Yes |  |  | No |  |
| component_id | varchar(100) | Yes |  |  | No |  |
| period | timestamp | Yes |  |  | No |  |
| fail_reason | varchar(2000) | Yes |  |  | No |  |
| status | varchar(255) | Yes |  |  | No |  |

---

## schedule_promo_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| schedule_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| period | date | No |  | PRIMARY KEY | Yes |  |
| start_datetime | timestamp | Yes |  |  | No |  |
| end_datetime | timestamp | Yes |  |  | No |  |
| gcs_location | varchar(255) | Yes |  |  | No |  |
| stage | varchar(255) | Yes |  |  | No |  |
| retry_count | int4(32) | Yes |  |  | No |  |
| status | varchar(255) | Yes |  |  | No |  |

---

## schedule_wbr_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| schedule_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| period | date | No |  | PRIMARY KEY | Yes |  |
| reporting_range | varchar(255) | Yes |  |  | No |  |
| gcs_location | varchar | Yes |  |  | No |  |
| archive_location | varchar(255) | Yes |  |  | No |  |
| stage | varchar(255) | No |  |  | No |  |
| status | varchar(255) | Yes |  |  | No |  |
| metadata | json | Yes |  |  | No |  |
| detail_id | int4(32) | Yes |  |  | No |  |
| start_datetime | timestamptz | Yes |  |  | No |  |
| end_datetime | timestamp | Yes |  |  | No |  |
| retry_config | json | Yes |  |  | No |  |
| retry_count | int4(32) | Yes |  |  | No |  |
| errors | json | Yes |  |  | No |  |
| run_id | uuid | No |  | PRIMARY KEY | Yes |  |

---

## scheduler_controller

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.scheduler_controller_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| scheduler_name | varchar(255) | No |  | UNIQUE | Yes |  |
| cron_expression | varchar(100) | No |  |  | No |  |
| is_active | bool | Yes | true |  | No |  |
| last_updated | timestamp | Yes | CURRENT_TIMESTAMP |  | No |  |

---

## scheduler_filters

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| scheduler_filter_id | int4(32) | No | nextval('i2oretail_dev.scheduler_filters_scheduler_filter_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| filters | json | Yes |  |  | No |  |
| component_column_definition | json | Yes |  |  | No |  |
| component_id | varchar(255) | Yes |  |  | No |  |
| query_id | int4(32) | Yes |  |  | No |  |
| priority | int4(32) | Yes |  |  | No |  |
| report_id | int4(32) | Yes |  |  | No |  |
| report_name | varchar(255) | Yes |  |  | No |  |
| report_format | varchar(255) | Yes |  |  | No |  |
| time_range | json | Yes |  |  | No |  |
| module_name | varchar(255) | Yes |  |  | No |  |
| tree_data | bool | No | false |  | No |  |
| schedule_type | varchar(255) | Yes |  |  | No |  |
| mandatory_filters | json | Yes | '{"Hourly": false, "Daily": false, "Weekly": false, "Monthly": false, "Quaterly": false, "Yearly": false}'::json |  | No |  |

---

## scheduler_filters_back

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| scheduler_filter_id | int4(32) | Yes |  |  | No |  |
| filters | json | Yes |  |  | No |  |
| component_column_definition | json | Yes |  |  | No |  |
| component_id | varchar(255) | Yes |  |  | No |  |
| query_id | int4(32) | Yes |  |  | No |  |
| priority | int4(32) | Yes |  |  | No |  |
| report_id | int4(32) | Yes |  |  | No |  |
| report_name | varchar(100) | Yes |  |  | No |  |
| report_format | varchar(100) | Yes |  |  | No |  |
| time_range | json | Yes |  |  | No |  |
| module_name | varchar(100) | Yes |  |  | No |  |
| tree_data | bool | Yes |  |  | No |  |

---

## schema_migrations

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| version | varchar(255) | No |  |  | No |  |

---

## scrapehero_input_files

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| client | text | Yes |  |  | No |  |
| source | text | Yes |  |  | No |  |
| version | int8(64) | Yes |  |  | No |  |
| gs_file | text | Yes |  |  | No |  |

---

## scrapehero_output_files

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| client | text | Yes |  |  | No |  |
| file | text | Yes |  |  | No |  |
| version | int8(64) | Yes |  |  | No |  |
| status | text | Yes |  |  | No |  |
| frequency | text | Yes |  |  | No |  |
| load_day | text | Yes |  |  | No |  |
| expected_time_UTC | time | Yes |  |  | No |  |
| expected_time_EDT | time | Yes |  |  | No |  |
| expected_time_IST | time | Yes |  |  | No |  |

---

## scrapehero_output_files_format

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| source | text | Yes |  |  | No |  |
| version | varchar | Yes |  |  | No |  |
| file_name_convention | text | Yes |  |  | No |  |
| file_format | text | Yes |  |  | No |  |
| file_columns | text | Yes |  |  | No |  |

---

## search_term_groups

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| search_term_group_id | int4(32) | No | nextval('i2oretail_dev.search_term_groups_search_term_group_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| search_terms_group | varchar(70) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |

---

## search_terms

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| search_term_id | int4(32) | No | nextval('i2oretail_dev.search_terms_search_term_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| search_term | varchar(70) | Yes |  |  | No |  |
| search_term_group_id | int4(32) | Yes |  | FOREIGN KEY | No |  |

---

## self_authorized_info_table

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.self_authorized_info_table_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| authorized_resellers | varchar(100) | Yes |  |  | No |  |
| region | varchar(10) | Yes |  |  | No |  |
| platform | varchar(50) | Yes |  |  | No |  |
| org_type | varchar(50) | Yes |  |  | No |  |

---

## seller

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| brand_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| seller_id | int8(64) | No | nextval('i2oretail_dev.seller_seller_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| marketplace | varchar(255) | No |  |  | No |  |
| marketplace_id | varchar(255) | Yes |  |  | No |  |
| display_name | varchar(255) | Yes |  |  | No |  |
| state | varchar(50) | Yes |  |  | No |  |
| first_seen_at | timestamptz | No |  |  | No |  |
| last_seen_at | timestamptz | Yes |  |  | No |  |
| threat_score | numeric(5,2) | Yes |  |  | No |  |
| created_by | int4(32) | Yes |  | FOREIGN KEY | No |  |
| created_at | timestamptz | Yes | now() |  | No |  |

---

## seller_attribute

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| seller_id | int8(64) | No | nextval('i2oretail_dev.seller_attribute_seller_id_seq'::regclass) | FOREIGN KEY, PRIMARY KEY | Yes |  |
| attributes | jsonb | Yes |  |  | No |  |
| verified | bool | Yes | false |  | No |  |

---

## sendgrid_apikey

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dev.sendgrid_apikey_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| key_name | varchar(255) | No |  |  | No |  |
| api_key | varchar(255) | No |  |  | No |  |

---

## sendgrid_events

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| useragent | varchar | Yes |  |  | No |  |
| url_offset | varchar | Yes |  |  | No |  |
| url | varchar | Yes |  |  | No |  |
| type | varchar | Yes |  |  | No |  |
| status | varchar | Yes |  |  | No |  |
| smtp_id | varchar | Yes |  |  | No |  |
| sg_message_id | varchar | Yes |  |  | No |  |
| sg_event_id | varchar | Yes |  |  | No |  |
| response | varchar | Yes |  |  | No |  |
| reason | varchar | Yes |  |  | No |  |
| message_identifier | varchar | Yes |  |  | No |  |
| marketing_campaign_version | varchar | Yes |  |  | No |  |
| marketing_campaign_name | varchar | Yes |  |  | No |  |
| ip | varchar | Yes |  |  | No |  |
| event_id | int4(32) | No | nextval('i2oretail_dev.sendgrid_events_event_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| event | varchar | No |  |  | No |  |
| email | varchar | No |  |  | No |  |
| date | varchar | Yes |  |  | No |  |
| time | varchar | Yes |  |  | No |  |
| tls | int4(32) | Yes |  |  | No |  |
| sg_machine_open | bool | Yes |  |  | No |  |
| marketing_campaign_id | int8(64) | Yes |  |  | No |  |
| attempt | int4(32) | Yes |  |  | No |  |
| asm_group_id | int8(64) | Yes |  |  | No |  |
| timestamp | int8(64) | Yes |  |  | No |  |

---

## session_tokens

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| user_uuid | varchar(255) | No |  |  | Yes |  |
| expiration_date | int8(64) | No |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |
| updated_at | int8(64) | No |  |  | No |  |

---

## share_link_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| share_link_details_id | int4(32) | No | nextval('i2oretail_dev.share_link_details_share_link_details_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| share_id | varchar(50) | Yes |  | UNIQUE | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| selected_org_type_cd | varchar(50) | Yes |  |  | No |  |
| sender_email_id | varchar(50) | Yes |  |  | No |  |
| route_url | varchar(250) | Yes |  |  | No |  |
| allowed_org_types | json | Yes |  |  | No |  |
| filters | json | Yes |  |  | No |  |
| sender_first_name | varchar(50) | Yes |  |  | No |  |
| receiver_email_id | varchar(5000) | Yes |  |  | No |  |
| link_expiry_date | date | Yes |  |  | No |  |
| start_date | date | Yes |  |  | No |  |
| end_date | date | Yes |  |  | No |  |
| time_range | varchar(50) | Yes |  |  | No |  |
| shared_page_name | varchar(250) | Yes |  |  | No |  |
| message | varchar(5000) | Yes |  |  | No |  |
| sendgrid_errors | json | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| org_logo_name | varchar(100) | Yes |  |  | No |  |
| tab_index | varchar(100) | Yes |  |  | No |  |
| org_display_name | varchar(70) | Yes |  |  | No |  |
| email_subject | varchar(500) | Yes |  |  | No |  |
| selected_business_view_id | int4(32) | Yes |  |  | No |  |

---

## snapshots

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(50) | No |  | PRIMARY KEY | Yes |  |
| component_uuid | varchar(50) | No |  |  | Yes |  |
| status | varchar(4) | No | 'U'::character varying |  | No |  |
| islast | bool | No | false |  | No |  |
| version | varchar(500) | Yes |  |  | No |  |
| purge_status | int4(32) | Yes |  |  | No |  |
| build_string | varchar(100) | Yes |  |  | No |  |
| revision | varchar(100) | Yes |  |  | No |  |
| build_date | int8(64) | Yes |  |  | No |  |
| period1_mode | varchar(100) | Yes |  |  | No |  |
| period1_param | varchar(100) | Yes |  |  | No |  |
| period1_date | int8(64) | Yes |  |  | No |  |
| created_at | int8(64) | Yes |  |  | No |  |

---

## state_persistance

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| st_per_id | int4(32) | No |  |  | No |  |
| state | varchar(255) | No |  |  | No |  |
| email | varchar(255) | No |  |  | No |  |
| location | varchar(255) | No |  |  | No |  |

---

## sub_category

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| sub_category_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| category_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| sub_category_name | varchar(150) | Yes |  |  | No |  |
| sub_category_description | varchar(200) | Yes |  |  | No |  |
| severity | varchar(50) | Yes |  |  | No |  |
| template_title | varchar(500) | Yes |  |  | No |  |
| template_message | varchar(1000) | Yes |  |  | No |  |
| priority | int4(32) | Yes |  |  | No |  |

---

## subscription_screen_mapping

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| subcription_screen_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| subcription_id | int4(32) | No |  |  | No |  |
| screen_id | varchar(100) | Yes |  |  | No |  |

---

## subscription_type

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| subscription_id | int4(32) | Yes |  |  | No |  |
| subscription_type_name | varchar(255) | Yes |  |  | No |  |
| subscription_config | json | Yes |  |  | No |  |
| active | bool | Yes |  |  | No |  |

---

## summarize_review

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| email | varchar(255) | Yes |  |  | No |  |

---

## support_ticket

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| ticket_id | int4(32) | No | nextval('i2oretail_dev.support_ticket_ticket_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| name | varchar | No |  |  | No |  |
| work_email_id | varchar | No |  |  | No |  |
| sub_category | varchar | No |  |  | No |  |
| brand_name | varchar | No |  |  | No |  |

---

## sv

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | text | Yes |  |  | No |  |
| group_by | varchar(250) | Yes |  |  | No |  |
| order_by | varchar(250) | Yes |  |  | No |  |
| additional_info | json | Yes |  |  | No |  |
| table_type | varchar(50) | Yes |  |  | No |  |

---

## teams_feedback

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | uuid | No |  | PRIMARY KEY | Yes |  |
| user_id | varchar(255) | Yes |  |  | No |  |
| conversation_id | varchar(255) | Yes |  |  | No |  |
| teams_recipient_id | varchar(255) | Yes |  |  | No |  |
| service_url | varchar(255) | Yes |  |  | No |  |
| current_org_id | int4(32) | Yes |  |  | No |  |
| query_timestamp | timestamp | Yes |  |  | No |  |
| feedback_timestamp | timestamp | Yes |  |  | No |  |
| feedback_given | bool | Yes |  |  | No |  |
| feedback_positive | bool | Yes |  |  | No |  |
| typed_query | varchar(255) | Yes |  |  | No |  |
| interpreted_input | json | Yes |  |  | No |  |
| feedback | json | Yes |  |  | No |  |

---

## teams_user

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| user_id | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| email | varchar(255) | No |  | UNIQUE | Yes |  |
| conversation_id | varchar(255) | No |  |  | No |  |
| teams_recipient_id | varchar(255) | No |  |  | No |  |
| service_url | varchar(255) | No |  |  | No |  |
| current_org_id | int4(32) | Yes |  |  | No |  |
| org_report_dates | json | Yes |  |  | No |  |

---

## temp

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| column_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| db_column_name | varchar(100) | No |  |  | No |  |
| label | varchar(150) | No |  |  | No |  |
| datatype | varchar(30) | Yes |  |  | No |  |
| format | varchar(30) | Yes |  |  | No |  |
| width | int4(32) | Yes |  |  | No |  |
| suppress_menu | bool | Yes |  |  | No |  |
| cell_class | varchar(50) | Yes |  |  | No |  |
| cell_style | varchar(500) | Yes |  |  | No |  |
| header_class | varchar(50) | Yes |  |  | No |  |

---

## temp_product_master_parent_asins

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| platform | text | Yes |  |  | No |  |
| region | text | Yes |  |  | No |  |
| product_code | text | Yes |  |  | No |  |
| pasin | text | Yes |  |  | No |  |
| is_missing | bool | Yes |  |  | No |  |

---

## test_buy

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.test_buy_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| listing_master_id | int8(64) | No |  |  | No |  |
| state | text | No |  |  | No |  |
| assigned_to | text | Yes |  |  | No |  |
| email_sent_to_assignee | bool | Yes | false |  | No |  |
| recommended_on | timestamptz | Yes |  |  | No |  |
| score | float8(53) | Yes |  |  | No |  |
| status | text | Yes |  |  | No |  |
| created_by | text | Yes |  |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |
| updated_by | text | Yes |  |  | No |  |
| reason | text | Yes |  |  | No |  |
| approved_meta | jsonb | Yes |  |  | No |  |
| withdrawn_meta | jsonb | Yes |  |  | No |  |
| completed_meta | jsonb | Yes |  |  | No |  |

---

## time_range_favourites

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | Yes |  |  | No |  |
| display_name | varchar(100) | Yes |  |  | No |  |
| period | varchar(100) | Yes |  |  | No |  |
| no_of_periods | int4(32) | Yes |  |  | No |  |
| order_number | int4(32) | Yes |  |  | No |  |
| reporting_range | varchar(100) | Yes |  |  | No |  |
| is_default | bool | Yes |  |  | No |  |

---

## tooltip_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| tooltip_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| tooltip_label | varchar(250) | Yes |  |  | No |  |
| tooltip_text | varchar(1000) | Yes |  |  | No |  |
| org_type_cd | varchar(100) | Yes |  |  | No |  |
| ui_screen_code | varchar(50) | Yes |  |  | No |  |

---

## translation_table

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| region | varchar(50) | Yes |  |  | No |  |
| key | varchar(50) | Yes |  |  | No |  |
| value | varchar(250) | Yes |  |  | No |  |

---

## ui_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_type_cd | varchar(20) | No |  |  | No |  |
| ui_screen_cd | varchar(40) | No |  |  | No |  |
| property_cd | varchar(100) | No |  |  | No |  |
| property_label | varchar(10000) | Yes |  |  | No |  |
| url | varchar(200) | Yes |  |  | No |  |
| permission_id | int4(32) | Yes |  |  | No |  |
| icon_name | varchar(40) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| filter_metadata | jsonb | Yes |  |  | No |  |

---

## ui_config_bck

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_type_cd | varchar(20) | Yes |  |  | No |  |
| ui_screen_cd | varchar(40) | Yes |  |  | No |  |
| property_cd | varchar(100) | Yes |  |  | No |  |
| property_label | varchar(3000) | Yes |  |  | No |  |
| url | varchar(200) | Yes |  |  | No |  |
| permission_id | int4(32) | Yes |  |  | No |  |
| icon_name | varchar(40) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |

---

## ui_layout

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| ui_screen_cd | varchar(50) | No |  | PRIMARY KEY | Yes |  |
| layout_cd | varchar(20) | No |  |  | No |  |
| layout_json | json | No |  |  | No |  |
| platform | varchar(255) | No | 'Amazon'::character varying | PRIMARY KEY | Yes |  |

---

## ui_layout_lbb

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| ui_screen_cd | varchar(50) | Yes |  |  | No |  |
| layout_cd | varchar(20) | Yes |  |  | No |  |
| layout_json | json | Yes |  |  | No |  |

---

## uiconf

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_type_cd | varchar(20) | Yes |  |  | No |  |
| ui_screen_cd | varchar(40) | Yes |  |  | No |  |
| property_cd | varchar(100) | Yes |  |  | No |  |
| property_label | varchar(3000) | Yes |  |  | No |  |
| url | varchar(200) | Yes |  |  | No |  |
| permission_id | int4(32) | Yes |  |  | No |  |
| icon_name | varchar(40) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |

---

## upload_dump

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.upload_dump_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| created_at | timestamp | No |  |  | No |  |
| json_dump | json | Yes |  |  | No |  |
| last_modified_at | timestamp | No |  |  | No |  |
| row_number | varchar(255) | Yes |  |  | No |  |
| upload_history_id | int4(32) | No |  | FOREIGN KEY | No |  |
| upload_master_id | int4(32) | No |  | FOREIGN KEY | No |  |

---

## upload_history

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.upload_history_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  |  | No |  |
| status | uploadjobstatus | Yes |  |  | No |  |
| job_result | uploadjobresult | Yes |  |  | No |  |
| upload_master_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| uploaded_file_gcs | varchar | Yes |  |  | No |  |
| created_by | varchar | Yes |  |  | No |  |
| updated_by | varchar | Yes |  |  | No |  |
| created_at | timestamptz | Yes |  |  | No |  |
| updated_at | timestamptz | Yes |  |  | No |  |
| scheduled_at | timestamptz | Yes |  |  | No |  |
| processed_at | timestamptz | Yes |  |  | No |  |
| rejection_file_gcs | varchar | Yes |  |  | No |  |
| notification_emails | varchar(500) | Yes |  |  | No |  |

---

## upload_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.upload_master_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| upload_type | varchar | Yes |  |  | No |  |
| template_file_gcs_location | varchar | Yes |  |  | No |  |
| column_definition | json | Yes |  |  | No |  |
| destination_table | varchar | Yes |  |  | No |  |
| upload_type_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| marketplace_id | _int4 | Yes |  |  | No |  |

---

## upload_type

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.upload_type_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| code | varchar(50) | Yes |  |  | No |  |
| label | varchar(50) | Yes |  |  | No |  |
| provide_template_download | bool | Yes |  |  | No |  |

---

## upload_type_org_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.upload_type_org_config_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| upload_type_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| orgid | int4(32) | Yes |  |  | No |  |
| user_email | varchar(50) | Yes |  |  | No |  |
| custom_label | varchar(50) | Yes |  |  | No |  |

---

## user_audit

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.user_audit_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| user_id | varchar | No |  |  | No |  |
| modifier | varchar(50) | No |  |  | No |  |
| action | varchar(50) | Yes |  |  | No |  |
| field | varchar | Yes |  |  | No |  |
| prev_value | varchar | Yes |  |  | No |  |
| curr_value | varchar | Yes |  |  | No |  |
| modification_time | timestamp | Yes | now() |  | No |  |
| username | varchar | Yes |  |  | No |  |

---

## user_dismissed_messages

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| user_uuid | varchar(255) | No |  |  | Yes |  |
| project_uuid | varchar(40) | No |  |  | Yes |  |
| message_type | varchar(255) | No |  |  | Yes |  |
| created_at | int8(64) | No |  |  | No |  |

---

## user_filter_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| user_filter_config_id | int4(32) | No | nextval('i2oretail_dev.user_filter_config_user_filter_config_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| widget | varchar(255) | Yes | NULL::character varying |  | No |  |
| filter_details | json | Yes |  |  | No |  |
| ui_screen_cd | varchar(255) | Yes |  |  | No |  |
| is_public | bool | Yes |  |  | No |  |
| is_deleted | bool | Yes |  |  | No |  |
| filter_name | varchar(255) | Yes |  |  | No |  |
| email | varchar(255) | Yes |  |  | No |  |
| edited_by | varchar(255) | Yes |  |  | No |  |
| no_of_times_used | int4(32) | Yes | 0 |  | No |  |
| marketplace_id | _int4 | Yes |  |  | No |  |
| is_global_preset | bool | Yes | false |  | No |  |

---

## user_header_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| user_header_config_id | int4(32) | No | nextval('i2oretail_dev.user_header_config_user_header_config_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY, UNIQUE | Yes |  |
| org_type_id | int4(32) | Yes |  | FOREIGN KEY, UNIQUE | Yes |  |
| context_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| widget | varchar(255) | Yes | NULL::character varying | UNIQUE | Yes |  |
| header_details | json | Yes |  |  | No |  |
| report_id | int4(32) | Yes |  | FOREIGN KEY | Yes |  |
| ui_screen_cd | varchar(255) | Yes |  | UNIQUE | Yes |  |
| email | varchar(255) | Yes |  | UNIQUE | Yes |  |
| created_on | timestamp | Yes |  |  | No |  |
| last_modified_on | timestamp | Yes |  |  | No |  |
| marketplace_id | _int4 | Yes |  | UNIQUE | Yes |  |

---

## user_properties

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| user_uuid | varchar(255) | No |  |  | Yes |  |
| kee | varchar(100) | No |  |  | Yes |  |
| text_value | varchar(4000) | No |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |
| updated_at | int8(64) | No |  |  | No |  |

---

## user_roles

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| role | varchar(64) | No |  |  | No |  |
| component_uuid | varchar(40) | Yes |  |  | Yes |  |
| user_uuid | varchar(255) | Yes |  |  | Yes |  |

---

## user_tokens

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| uuid | varchar(40) | No |  | PRIMARY KEY | Yes |  |
| user_uuid | varchar(255) | No |  |  | Yes |  |
| name | varchar(100) | No |  |  | Yes |  |
| token_hash | varchar(255) | No |  |  | Yes |  |
| last_connection_date | int8(64) | Yes |  |  | No |  |
| created_at | int8(64) | No |  |  | No |  |

---

## users

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| user_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| active | bool | Yes |  |  | No |  |
| address_1 | varchar(255) | Yes |  |  | No |  |
| address_2 | varchar(255) | Yes |  |  | No |  |
| city | varchar(255) | Yes |  |  | No |  |
| country | varchar(255) | Yes |  |  | No |  |
| first_name | varchar(255) | Yes |  |  | No |  |
| last_name | varchar(255) | Yes |  |  | No |  |
| middle_name | varchar(255) | Yes |  |  | No |  |
| phone_no | varchar(255) | Yes |  |  | No |  |
| pwd | varchar(255) | Yes |  |  | No |  |
| state | varchar(255) | Yes |  |  | No |  |
| user_email_id | varchar(255) | Yes |  |  | No |  |
| zip | varchar(255) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |

---

## users_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.users_details_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| email | varchar(255) | No |  | UNIQUE | Yes |  |
| is_validated | bool | Yes | false |  | No |  |
| first_name | varchar(255) | Yes |  |  | No |  |
| last_name | varchar(255) | Yes |  |  | No |  |
| is_free_trail | bool | Yes | false |  | No |  |
| password | varchar(255) | Yes |  |  | No |  |

---

## vc_product_master_catalog

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| org_type | varchar(100) | Yes |  |  | No |  |
| marketplace | varchar(100) | Yes |  |  | No |  |
| region | varchar(100) | Yes |  |  | No |  |
| product_code_type | varchar(100) | Yes |  |  | No |  |
| product_code | varchar(100) | Yes |  |  | No |  |
| product_title | varchar(1000) | Yes |  |  | No |  |
| short_name | varchar(300) | Yes |  |  | No |  |
| brand | varchar(200) | Yes |  |  | No |  |
| brand_code | varchar(200) | Yes |  |  | No |  |
| category | varchar(200) | Yes |  |  | No |  |
| model_number | varchar(200) | Yes |  |  | No |  |
| sku | varchar(200) | Yes |  |  | No |  |
| upc | varchar(200) | Yes |  |  | No |  |
| release_date | date | Yes |  |  | No |  |
| catalog_price | float8(53) | Yes |  |  | No |  |
| replenishment_status | varchar(200) | Yes |  |  | No |  |
| source_system_id | varchar(200) | Yes |  |  | No |  |
| isbn | varchar(200) | Yes |  |  | No |  |
| ean | varchar(200) | Yes |  |  | No |  |
| record_valid_from | date | Yes |  |  | No |  |
| record_valid_to | date | Yes |  |  | No |  |
| load_id | varchar(200) | Yes |  |  | No |  |
| bcm_enabled | bool | Yes |  |  | No |  |
| competitor_enabled | bool | Yes |  |  | No |  |
| customer_review_enabled | bool | Yes |  |  | No |  |
| master_enabled | bool | Yes |  |  | No |  |
| multiplatform_enabled | bool | Yes |  |  | No |  |
| reseller_enabled | bool | Yes |  |  | No |  |
| search_rank_enabled | bool | Yes |  |  | No |  |
| alerts_exceptions_enabled | bool | Yes |  |  | No |  |
| pricemonitor_enabled | bool | Yes |  |  | No |  |
| product_url | varchar(1000) | Yes |  |  | No |  |
| product_image_url | varchar(2000) | Yes |  |  | No |  |
| amazon_category | varchar(200) | Yes |  |  | No |  |
| amazon_sub_category | varchar(200) | Yes |  |  | No |  |
| item_number | varchar(200) | Yes |  |  | No |  |
| product_status | varchar(300) | Yes |  |  | No |  |
| pasin | varchar(200) | Yes |  |  | No |  |
| modified_date | date | Yes |  |  | No |  |
| expired_date | date | Yes |  |  | No |  |
| flag | int4(32) | Yes |  |  | No |  |
| search_terms_group | varchar(1000) | Yes |  |  | No |  |
| bbx_daily_report_enabled | bool | Yes |  |  | No |  |

---

## viz_as_dataproduct_summs_holistics

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| data_month | date | Yes |  |  | No |  |
| data_period | date | Yes |  |  | No |  |
| period_type | int4(32) | Yes |  |  | No |  |
| category | varchar(500) | Yes |  |  | No |  |
| sub_category | varchar(500) | Yes |  |  | No |  |
| brand | varchar(500) | Yes |  |  | No |  |
| freq_brand | int4(32) | Yes |  |  | No |  |
| freq_subcat | int4(32) | Yes |  |  | No |  |
| d_brand_sov_organic | float8(53) | Yes |  |  | No |  |
| d_brand_sov_sponsored | float8(53) | Yes |  |  | No |  |
| d_per_page1 | float8(53) | Yes |  |  | No |  |
| d_per_page2 | int4(32) | Yes |  |  | No |  |
| d_per_bestseller | float8(53) | Yes |  |  | No |  |
| d_per_amzchoice | float8(53) | Yes |  |  | No |  |
| d_avg_reviews | float8(53) | Yes |  |  | No |  |
| d_avg_rating | float8(53) | Yes |  |  | No |  |
| d_avg_bbx_price | float8(53) | Yes |  |  | No |  |
| d_avg_discountedprice | float8(53) | Yes |  |  | No |  |
| d_per_prime | float8(53) | Yes |  |  | No |  |
| c_avg_1_2_star | float8(53) | Yes |  |  | No |  |
| c_avg_qarich | float8(53) | Yes |  |  | No |  |
| c_avg_bsr | float8(53) | Yes |  |  | No |  |
| c_avg_photosvideos | float8(53) | Yes |  |  | No |  |
| c_avg_contentrich | float8(53) | Yes |  |  | No |  |
| c_avg_prodvariations | float8(53) | Yes |  |  | No |  |
| c_per_buyboxavail | float8(53) | Yes |  |  | No |  |
| dn_avg_listpricerealization | float8(53) | Yes |  |  | No |  |
| dn_per_bbx_wins | float8(53) | Yes |  |  | No |  |
| d_brand_sov_organic_min | float8(53) | Yes |  |  | No |  |
| d_brand_sov_organic_max | float8(53) | Yes |  |  | No |  |
| d_brand_sov_sponsored_min | float8(53) | Yes |  |  | No |  |
| d_brand_sov_sponsored_max | float8(53) | Yes |  |  | No |  |
| d_per_page1_min | float8(53) | Yes |  |  | No |  |
| d_per_page1_max | float8(53) | Yes |  |  | No |  |
| d_per_page2_min | int4(32) | Yes |  |  | No |  |
| d_per_page2_max | int4(32) | Yes |  |  | No |  |
| d_per_bestseller_min | float8(53) | Yes |  |  | No |  |
| d_per_bestseller_max | float8(53) | Yes |  |  | No |  |
| d_per_amzchoice_min | float8(53) | Yes |  |  | No |  |
| d_per_amzchoice_max | float8(53) | Yes |  |  | No |  |
| d_avg_reviews_min | float8(53) | Yes |  |  | No |  |
| d_avg_reviews_max | float8(53) | Yes |  |  | No |  |
| d_avg_rating_min | float8(53) | Yes |  |  | No |  |
| d_avg_rating_max | float8(53) | Yes |  |  | No |  |
| d_avg_bbx_price_min | float8(53) | Yes |  |  | No |  |
| d_avg_bbx_price_max | float8(53) | Yes |  |  | No |  |
| d_avg_discountedprice_min | float8(53) | Yes |  |  | No |  |
| d_avg_discountedprice_max | float8(53) | Yes |  |  | No |  |
| d_per_prime_min | float8(53) | Yes |  |  | No |  |
| d_per_prime_max | float8(53) | Yes |  |  | No |  |
| c_avg_1_2_star_min | float8(53) | Yes |  |  | No |  |
| c_avg_1_2_star_max | float8(53) | Yes |  |  | No |  |
| c_avg_qarich_min | float8(53) | Yes |  |  | No |  |
| c_avg_qarich_max | float8(53) | Yes |  |  | No |  |
| c_avg_bsr_min | float8(53) | Yes |  |  | No |  |
| c_avg_bsr_max | float8(53) | Yes |  |  | No |  |
| c_avg_photosvideos_min | float8(53) | Yes |  |  | No |  |
| c_avg_photosvideos_max | float8(53) | Yes |  |  | No |  |
| c_avg_contentrich_min | float8(53) | Yes |  |  | No |  |
| c_avg_contentrich_max | float8(53) | Yes |  |  | No |  |
| c_avg_prodvariations_min | float8(53) | Yes |  |  | No |  |
| c_avg_prodvariations_max | float8(53) | Yes |  |  | No |  |
| c_per_buyboxavail_min | float8(53) | Yes |  |  | No |  |
| c_per_buyboxavail_max | float8(53) | Yes |  |  | No |  |
| dn_avg_listpricerealization_min | float8(53) | Yes |  |  | No |  |
| dn_avg_listpricerealization_max | float8(53) | Yes |  |  | No |  |
| dn_per_bbx_wins_min | float8(53) | Yes |  |  | No |  |
| dn_per_bbx_wins_max | float8(53) | Yes |  |  | No |  |
| d_brand_sov_organic_w | int4(32) | Yes |  |  | No |  |
| d_brand_sov_sponsored_w | float8(53) | Yes |  |  | No |  |
| d_per_page1_w | int4(32) | Yes |  |  | No |  |
| d_per_page2_w | float8(53) | Yes |  |  | No |  |
| d_per_bestseller_w | int4(32) | Yes |  |  | No |  |
| d_per_amzchoice_w | float8(53) | Yes |  |  | No |  |
| d_avg_reviews_w | int4(32) | Yes |  |  | No |  |
| d_avg_rating_w | int4(32) | Yes |  |  | No |  |
| d_avg_bbx_price_w | int4(32) | Yes |  |  | No |  |
| d_avg_discountedprice_w | float8(53) | Yes |  |  | No |  |
| d_per_prime_w | float8(53) | Yes |  |  | No |  |
| c_avg_1_2_star_w | float8(53) | Yes |  |  | No |  |
| c_avg_qarich_w | float8(53) | Yes |  |  | No |  |
| c_avg_bsr_w | float8(53) | Yes |  |  | No |  |
| c_avg_photosvideos_w | int4(32) | Yes |  |  | No |  |
| c_avg_contentrich_w | float8(53) | Yes |  |  | No |  |
| c_avg_prodvariations_w | float8(53) | Yes |  |  | No |  |
| c_per_buyboxavail_w | int4(32) | Yes |  |  | No |  |
| dn_avg_listpricerealization_w | float8(53) | Yes |  |  | No |  |
| dn_per_bbx_wins_w | int4(32) | Yes |  |  | No |  |
| d_brand_sov_organic_nw | float8(53) | Yes |  |  | No |  |
| d_brand_sov_sponsored_nw | float8(53) | Yes |  |  | No |  |
| d_per_page1_nw | float8(53) | Yes |  |  | No |  |
| d_per_page2_nw | float8(53) | Yes |  |  | No |  |
| d_per_bestseller_nw | float8(53) | Yes |  |  | No |  |
| d_per_amzchoice_nw | float8(53) | Yes |  |  | No |  |
| d_avg_reviews_nw | float8(53) | Yes |  |  | No |  |
| d_avg_rating_nw | float8(53) | Yes |  |  | No |  |
| d_avg_bbx_price_nw | float8(53) | Yes |  |  | No |  |
| d_avg_discountedprice_nw | float8(53) | Yes |  |  | No |  |
| d_per_prime_nw | float8(53) | Yes |  |  | No |  |
| c_avg_1_2_star_nw | float8(53) | Yes |  |  | No |  |
| c_avg_qarich_nw | float8(53) | Yes |  |  | No |  |
| c_avg_bsr_nw | float8(53) | Yes |  |  | No |  |
| c_avg_photosvideos_nw | float8(53) | Yes |  |  | No |  |
| c_avg_contentrich_nw | float8(53) | Yes |  |  | No |  |
| c_avg_prodvariations_nw | float8(53) | Yes |  |  | No |  |
| c_per_buyboxavail_nw | float8(53) | Yes |  |  | No |  |
| dn_avg_listpricerealization_nw | float8(53) | Yes |  |  | No |  |
| dn_per_bbx_wins_nw | float8(53) | Yes |  |  | No |  |
| discoverability_agg | float8(53) | Yes |  |  | No |  |
| conversion_agg | float8(53) | Yes |  |  | No |  |
| distribution_agg | float8(53) | Yes |  |  | No |  |
| discoverability_score | float8(53) | Yes |  |  | No |  |
| conversion_score | float8(53) | Yes |  |  | No |  |
| distribution_score | float8(53) | Yes |  |  | No |  |
| ippa_score | float8(53) | Yes |  |  | No |  |
| d_brand_sov_organic_rnk | int4(32) | Yes |  |  | No |  |
| d_brand_sov_sponsored_rnk | int4(32) | Yes |  |  | No |  |
| d_per_page1_rnk | int4(32) | Yes |  |  | No |  |
| d_per_page2_rnk | int4(32) | Yes |  |  | No |  |
| d_per_bestseller_rnk | int4(32) | Yes |  |  | No |  |
| d_per_amzchoice_rnk | int4(32) | Yes |  |  | No |  |
| d_avg_reviews_rnk | int4(32) | Yes |  |  | No |  |
| d_avg_rating_rnk | int4(32) | Yes |  |  | No |  |
| d_avg_bbx_price_rnk | int4(32) | Yes |  |  | No |  |
| d_avg_discountedprice_rnk | int4(32) | Yes |  |  | No |  |
| d_per_prime_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_1_2_star_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_qarich_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_bsr_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_photosvideos_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_contentrich_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_prodvariations_rnk | int4(32) | Yes |  |  | No |  |
| c_per_buyboxavail_rnk | int4(32) | Yes |  |  | No |  |
| dn_avg_listpricerealization_rnk | int4(32) | Yes |  |  | No |  |
| dn_per_bbx_wins_rnk | int4(32) | Yes |  |  | No |  |
| discoverability_score_rnk | int4(32) | Yes |  |  | No |  |
| conversion_score_rnk | int4(32) | Yes |  |  | No |  |
| distribution_score_rnk | int4(32) | Yes |  |  | No |  |
| ippa_score_rnk | int4(32) | Yes |  |  | No |  |
| no_of_products_in_top50 | int4(32) | Yes |  |  | No |  |

---

## viz_as_dataproduct_summs_specific_week

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_clients | varchar(500) | Yes |  |  | No |  |
| data_month | date | Yes |  |  | No |  |
| data_period | date | Yes |  |  | No |  |
| period_type | int4(32) | Yes |  |  | No |  |
| category | varchar(500) | Yes |  |  | No |  |
| sub_category | varchar(500) | Yes |  |  | No |  |
| brand | varchar(500) | Yes |  |  | No |  |
| freq_brand | int4(32) | Yes |  |  | No |  |
| freq_subcat | int4(32) | Yes |  |  | No |  |
| d_brand_sov_organic | float8(53) | Yes |  |  | No |  |
| d_brand_sov_sponsored | float8(53) | Yes |  |  | No |  |
| d_per_page1 | float8(53) | Yes |  |  | No |  |
| d_per_page2 | float8(53) | Yes |  |  | No |  |
| d_per_bestseller | float8(53) | Yes |  |  | No |  |
| d_per_amzchoice | float8(53) | Yes |  |  | No |  |
| d_avg_reviews | float8(53) | Yes |  |  | No |  |
| d_avg_rating | float8(53) | Yes |  |  | No |  |
| d_avg_coupon | int4(32) | Yes |  |  | No |  |
| d_avg_ltd | int4(32) | Yes |  |  | No |  |
| d_per_prime | float8(53) | Yes |  |  | No |  |
| c_avg_1_2_star | float8(53) | Yes |  |  | No |  |
| c_avg_qarich | float8(53) | Yes |  |  | No |  |
| c_avg_bsr | float8(53) | Yes |  |  | No |  |
| c_avg_photosvideos | float8(53) | Yes |  |  | No |  |
| c_avg_contentrich | float8(53) | Yes |  |  | No |  |
| c_avg_prodvariations | float8(53) | Yes |  |  | No |  |
| c_per_buyboxavail | float8(53) | Yes |  |  | No |  |
| dn_per_bbx_wins | float8(53) | Yes |  |  | No |  |
| dn_avg_reseller_cnt | float8(53) | Yes |  |  | No |  |
| d_avg_bbx_price | float8(53) | Yes |  |  | No |  |
| dn_avg_listpricerealization | float8(53) | Yes |  |  | No |  |
| d_avg_discountedprice | float8(53) | Yes |  |  | No |  |
| d_brand_sov_organic_min | float8(53) | Yes |  |  | No |  |
| d_brand_sov_organic_max | float8(53) | Yes |  |  | No |  |
| d_brand_sov_sponsored_min | float8(53) | Yes |  |  | No |  |
| d_brand_sov_sponsored_max | float8(53) | Yes |  |  | No |  |
| d_per_page1_min | float8(53) | Yes |  |  | No |  |
| d_per_page1_max | float8(53) | Yes |  |  | No |  |
| d_per_page2_min | float8(53) | Yes |  |  | No |  |
| d_per_page2_max | float8(53) | Yes |  |  | No |  |
| d_per_bestseller_min | float8(53) | Yes |  |  | No |  |
| d_per_bestseller_max | float8(53) | Yes |  |  | No |  |
| d_per_amzchoice_min | float8(53) | Yes |  |  | No |  |
| d_per_amzchoice_max | float8(53) | Yes |  |  | No |  |
| d_avg_reviews_min | float8(53) | Yes |  |  | No |  |
| d_avg_reviews_max | float8(53) | Yes |  |  | No |  |
| d_avg_rating_min | float8(53) | Yes |  |  | No |  |
| d_avg_rating_max | float8(53) | Yes |  |  | No |  |
| d_avg_bbx_price_min | float8(53) | Yes |  |  | No |  |
| d_avg_bbx_price_max | float8(53) | Yes |  |  | No |  |
| d_avg_discountedprice_min | float8(53) | Yes |  |  | No |  |
| d_avg_discountedprice_max | float8(53) | Yes |  |  | No |  |
| d_avg_coupon_min | int4(32) | Yes |  |  | No |  |
| d_avg_coupon_max | int4(32) | Yes |  |  | No |  |
| d_avg_ltd_min | int4(32) | Yes |  |  | No |  |
| d_avg_ltd_max | int4(32) | Yes |  |  | No |  |
| d_per_prime_min | float8(53) | Yes |  |  | No |  |
| d_per_prime_max | float8(53) | Yes |  |  | No |  |
| c_avg_1_2_star_min | float8(53) | Yes |  |  | No |  |
| c_avg_1_2_star_max | float8(53) | Yes |  |  | No |  |
| c_avg_qarich_min | float8(53) | Yes |  |  | No |  |
| c_avg_qarich_max | float8(53) | Yes |  |  | No |  |
| c_avg_bsr_min | float8(53) | Yes |  |  | No |  |
| c_avg_bsr_max | float8(53) | Yes |  |  | No |  |
| c_avg_photosvideos_min | float8(53) | Yes |  |  | No |  |
| c_avg_photosvideos_max | float8(53) | Yes |  |  | No |  |
| c_avg_contentrich_min | float8(53) | Yes |  |  | No |  |
| c_avg_contentrich_max | float8(53) | Yes |  |  | No |  |
| c_avg_prodvariations_min | float8(53) | Yes |  |  | No |  |
| c_avg_prodvariations_max | float8(53) | Yes |  |  | No |  |
| c_per_buyboxavail_min | float8(53) | Yes |  |  | No |  |
| c_per_buyboxavail_max | float8(53) | Yes |  |  | No |  |
| dn_avg_listpricerealization_min | float8(53) | Yes |  |  | No |  |
| dn_avg_listpricerealization_max | float8(53) | Yes |  |  | No |  |
| dn_per_bbx_wins_min | float8(53) | Yes |  |  | No |  |
| dn_per_bbx_wins_max | float8(53) | Yes |  |  | No |  |
| dn_avg_reseller_cnt_min | float8(53) | Yes |  |  | No |  |
| dn_avg_reseller_cnt_max | float8(53) | Yes |  |  | No |  |
| d_brand_sov_organic_w | int4(32) | Yes |  |  | No |  |
| d_brand_sov_sponsored_w | float8(53) | Yes |  |  | No |  |
| d_per_page1_w | int4(32) | Yes |  |  | No |  |
| d_per_page2_w | float8(53) | Yes |  |  | No |  |
| d_per_bestseller_w | int4(32) | Yes |  |  | No |  |
| d_per_amzchoice_w | float8(53) | Yes |  |  | No |  |
| d_avg_reviews_w | int4(32) | Yes |  |  | No |  |
| d_avg_rating_w | float8(53) | Yes |  |  | No |  |
| d_avg_bbx_price_w | float8(53) | Yes |  |  | No |  |
| d_avg_discountedprice_w | float8(53) | Yes |  |  | No |  |
| d_per_prime_w | float8(53) | Yes |  |  | No |  |
| d_avg_coupon_w | float8(53) | Yes |  |  | No |  |
| d_avg_ltd_w | float8(53) | Yes |  |  | No |  |
| c_avg_1_2_star_w | float8(53) | Yes |  |  | No |  |
| c_avg_qarich_w | float8(53) | Yes |  |  | No |  |
| c_avg_bsr_w | float8(53) | Yes |  |  | No |  |
| c_avg_photosvideos_w | int4(32) | Yes |  |  | No |  |
| c_avg_contentrich_w | float8(53) | Yes |  |  | No |  |
| c_avg_prodvariations_w | float8(53) | Yes |  |  | No |  |
| c_per_buyboxavail_w | int4(32) | Yes |  |  | No |  |
| dn_avg_listpricerealization_w | float8(53) | Yes |  |  | No |  |
| dn_per_bbx_wins_w | float8(53) | Yes |  |  | No |  |
| dn_avg_reseller_cnt_w | int4(32) | Yes |  |  | No |  |
| d_brand_sov_organic_nw | float8(53) | Yes |  |  | No |  |
| d_brand_sov_sponsored_nw | float8(53) | Yes |  |  | No |  |
| d_per_page1_nw | float8(53) | Yes |  |  | No |  |
| d_per_page2_nw | float8(53) | Yes |  |  | No |  |
| d_per_bestseller_nw | float8(53) | Yes |  |  | No |  |
| d_per_amzchoice_nw | float8(53) | Yes |  |  | No |  |
| d_avg_reviews_nw | float8(53) | Yes |  |  | No |  |
| d_avg_rating_nw | float8(53) | Yes |  |  | No |  |
| d_avg_bbx_price_nw | float8(53) | Yes |  |  | No |  |
| d_avg_discountedprice_nw | float8(53) | Yes |  |  | No |  |
| d_avg_coupon_nw | float8(53) | Yes |  |  | No |  |
| d_avg_ltd_nw | float8(53) | Yes |  |  | No |  |
| d_per_prime_nw | float8(53) | Yes |  |  | No |  |
| c_avg_1_2_star_nw | float8(53) | Yes |  |  | No |  |
| c_avg_qarich_nw | float8(53) | Yes |  |  | No |  |
| c_avg_bsr_nw | float8(53) | Yes |  |  | No |  |
| c_avg_photosvideos_nw | float8(53) | Yes |  |  | No |  |
| c_avg_contentrich_nw | float8(53) | Yes |  |  | No |  |
| c_avg_prodvariations_nw | float8(53) | Yes |  |  | No |  |
| c_per_buyboxavail_nw | float8(53) | Yes |  |  | No |  |
| dn_avg_listpricerealization_nw | float8(53) | Yes |  |  | No |  |
| dn_per_bbx_wins_nw | float8(53) | Yes |  |  | No |  |
| dn_avg_reseller_cnt_nw | float8(53) | Yes |  |  | No |  |
| discoverability_agg | float8(53) | Yes |  |  | No |  |
| conversion_agg | float8(53) | Yes |  |  | No |  |
| distribution_agg | float8(53) | Yes |  |  | No |  |
| discoverability_score | float8(53) | Yes |  |  | No |  |
| conversion_score | float8(53) | Yes |  |  | No |  |
| distribution_score | float8(53) | Yes |  |  | No |  |
| ippa_score | float8(53) | Yes |  |  | No |  |
| d_brand_sov_organic_rnk | int4(32) | Yes |  |  | No |  |
| d_brand_sov_sponsored_rnk | int4(32) | Yes |  |  | No |  |
| d_per_page1_rnk | int4(32) | Yes |  |  | No |  |
| d_per_page2_rnk | int4(32) | Yes |  |  | No |  |
| d_per_bestseller_rnk | int4(32) | Yes |  |  | No |  |
| d_per_amzchoice_rnk | int4(32) | Yes |  |  | No |  |
| d_avg_reviews_rnk | int4(32) | Yes |  |  | No |  |
| d_avg_rating_rnk | int4(32) | Yes |  |  | No |  |
| d_avg_bbx_price_rnk | int4(32) | Yes |  |  | No |  |
| d_avg_discountedprice_rnk | int4(32) | Yes |  |  | No |  |
| d_avg_coupon_rnk | int4(32) | Yes |  |  | No |  |
| d_avg_ltd_rnk | int4(32) | Yes |  |  | No |  |
| d_per_prime_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_1_2_star_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_qarich_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_bsr_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_photosvideos_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_contentrich_rnk | int4(32) | Yes |  |  | No |  |
| c_avg_prodvariations_rnk | int4(32) | Yes |  |  | No |  |
| c_per_buyboxavail_rnk | int4(32) | Yes |  |  | No |  |
| dn_avg_listpricerealization_rnk | int4(32) | Yes |  |  | No |  |
| dn_per_bbx_wins_rnk | int4(32) | Yes |  |  | No |  |
| dn_avg_reseller_cnt_rnk | int4(32) | Yes |  |  | No |  |
| discoverability_score_rnk | int4(32) | Yes |  |  | No |  |
| conversion_score_rnk | int4(32) | Yes |  |  | No |  |
| distribution_score_rnk | int4(32) | Yes |  |  | No |  |
| ippa_score_rnk | int4(32) | Yes |  |  | No |  |

---

## viz_latest_product_details_dump

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| asin | varchar | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| time_of_day | varchar | Yes |  |  | No |  |
| product_code | varchar | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | No |  |
| region | varchar | Yes |  |  | No |  |
| reporting_range | varchar | Yes |  |  | No |  |
| product_title | varchar | Yes |  |  | No |  |
| full_description | varchar | Yes |  |  | No |  |
| bullet_point_text | varchar | Yes |  |  | No |  |
| images_url | varchar | Yes |  |  | No |  |
| video_thumbnail_url | varchar | Yes |  |  | No |  |
| video_url | varchar | Yes |  |  | No |  |
| a_plus | varchar | Yes |  |  | No |  |
| product_category | varchar | Yes |  |  | No |  |
| product_dimensions | varchar | Yes |  |  | No |  |
| shipping_weight | varchar | Yes |  |  | No |  |
| buy_box_price | float8(53) | Yes |  |  | No |  |
| buy_box_winning_seller | varchar | Yes |  |  | No |  |
| average_rating | float8(53) | Yes |  |  | No |  |
| total_reviews | int4(32) | Yes |  |  | No |  |
| availability_quantity | float8(53) | Yes |  |  | No |  |
| buybox_price_availability | varchar | Yes |  |  | No |  |
| input_asin | varchar | Yes |  |  | No |  |
| scrape_timestamp | timestamp | Yes |  |  | No |  |
| parent_asin | varchar | Yes |  |  | No |  |
| sh_row | int4(32) | Yes |  |  | No |  |

---

## wbr_client_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int8(64) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| org_type | varchar(255) | No |  | PRIMARY KEY | Yes |  |
| json_config | json | Yes |  |  | No |  |
| frequency | varchar(255) | No |  | PRIMARY KEY | Yes |  |

---

## wbr_queries

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| query | text | No |  |  | No |  |
| type | varchar(255) | Yes |  |  | No | DELETE, APPEND |
| stage | varchar(255) | Yes |  |  | No | PRE_DATA_VALIDATION, PPT_GENERATION |
| run_order | int4(32) | Yes |  |  | No |  |
| org_type | int4(32) | Yes |  |  | No | 1 - 1P
2 - 3P
3 - 1P3P |
| target_table | varchar(255) | Yes |  |  | No |  |
| wbr_type | varchar(255) | Yes |  |  | No | WEEKLY,
MONTHLY,
QUARTERLY,
YEARLY |
| metric_name | varchar(255) | Yes |  |  | No |  |
| error_text | varchar(255) | Yes |  |  | No |  |
| slide_no | int4(32) | Yes |  |  | No |  |
| is_active | bool | Yes | true |  | No |  |
| report_id | int4(32) | Yes |  |  | No |  |
| update_status_in_bq | bool | Yes | false |  | No |  |
| criticality | varchar(500) | Yes |  |  | No |  |
| check_type | varchar(500) | Yes |  |  | No |  |

---

## wbr_validations_summary

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| schedule_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| period | date | No |  | PRIMARY KEY | Yes |  |
| wbr_query_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| is_success | bool | No | true |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |

---

## webhook

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dev.webhook_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| source | text | No |  |  | No |  |
| dedupe_key | text | Yes |  |  | No |  |
| sg_message_id | text | Yes |  |  | No |  |
| event_type | text | Yes |  |  | No |  |
| received_at | timestamptz | No | now() |  | No |  |
| payload_json | jsonb | No |  |  | No |  |
| status | text | No | 'pending'::text |  | No |  |
| attempts | int4(32) | No | 0 |  | No |  |
| last_error | text | Yes |  |  | No |  |
| processed_at | timestamptz | Yes |  |  | No |  |
| correlation_id | text | Yes |  |  | No |  |

---

## weekly_highlight

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dev.weekly_highlight_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| priority | int4(32) | Yes |  |  | No |  |
| highlight | text | Yes |  |  | No |  |
| created_date | timestamp | Yes |  |  | No |  |
| week_start_date | date | No |  |  | No |  |

---

## won_buybox

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| rank | int4(32) | No |  |  | No |  |
| org_type | varchar | No |  |  | No |  |
| short_name | varchar | No |  |  | No |  |
| trend | varchar | No |  |  | No |  |
| buybox_win_percentage | int4(32) | No |  |  | No |  |
| reseller_with_max_wins | varchar | No |  |  | No |  |
| map | int4(32) | No |  |  | No |  |
| average_buybox_price | int4(32) | No |  |  | No |  |
| product_image_url | varchar(10000) | Yes |  |  | No |  |
| product_code | varchar(20) | Yes |  |  | No |  |
| region | varchar(20) | Yes |  |  | No |  |
| marketplace | varchar(20) | Yes |  |  | No |  |

---
