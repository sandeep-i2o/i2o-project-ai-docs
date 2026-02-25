# Schema: i2oretail_dp  —  Database Documentation

---

## Table of Contents

- [account_activity_details](#account_activity_details)
- [account_brands](#account_brands)
- [account_id_status_logs](#account_id_status_logs)
- [account_status](#account_status)
- [ad_campaign_report_filtered](#ad_campaign_report_filtered)
- [ad_sp_api_config_backup](#ad_sp_api_config_backup)
- [agency](#agency)
- [api_claims](#api_claims)
- [application_properties](#application_properties)
- [asin_map_master](#asin_map_master)
- [auth_resellers_list](#auth_resellers_list)
- [brand_violation_plugin_capture_log](#brand_violation_plugin_capture_log) — Log of brand-violation captures from the browser plugin
- [client_onboarding_status](#client_onboarding_status)
- [dag](#dag)
- [data_last_publish](#data_last_publish)
- [data_loads_record_count](#data_loads_record_count)
- [dq_query](#dq_query)
- [dq_query_backup](#dq_query_backup)
- [dq_results](#dq_results)
- [email_messages_graph_api](#email_messages_graph_api)
- [email_receipients](#email_receipients)
- [email_templates](#email_templates)
- [image_comparison_job_status](#image_comparison_job_status)
- [image_comparison_metadata](#image_comparison_metadata)
- [image_comparison_metadata_local_test](#image_comparison_metadata_local_test)
- [image_content_comparison](#image_content_comparison)
- [image_content_comparison_backlog](#image_content_comparison_backlog)
- [image_content_comparison_local_test](#image_content_comparison_local_test)
- [image_content_comparison_temp](#image_content_comparison_temp)
- [marketplace](#marketplace)
- [marketplace_scraper_mapper](#marketplace_scraper_mapper)
- [onboarding_queries](#onboarding_queries)
- [onboarding_queries_test](#onboarding_queries_test)
- [onboarding_stage](#onboarding_stage)
- [onboarding_substage](#onboarding_substage)
- [ops_data_load_allocation](#ops_data_load_allocation)
- [ops_user_data](#ops_user_data)
- [org_accounts](#org_accounts)
- [org_dag_map](#org_dag_map)
- [org_data_metadata](#org_data_metadata)
- [org_report](#org_report)
- [org_sources](#org_sources)
- [organization](#organization)
- [process_audit](#process_audit)
- [process_org_market_place_param](#process_org_market_place_param)
- [processes](#processes)
- [product_matching_output](#product_matching_output)
- [product_pricing_range_filtered](#product_pricing_range_filtered)
- [product_pricing_range_filtered_ab_soft_reset](#product_pricing_range_filtered_ab_soft_reset)
- [scheduler_config](#scheduler_config)
- [scraper_subprocess_id_mapper](#scraper_subprocess_id_mapper)
- [search_terms](#search_terms)
- [search_terms_copy](#search_terms_copy)
- [sh_validations](#sh_validations)
- [sp_api_config](#sp_api_config)
- [sp_api_config_bck_25_04_2024](#sp_api_config_bck_25_04_2024)
- [sp_api_config_havingdatalevel](#sp_api_config_havingdatalevel)
- [sp_api_properties](#sp_api_properties)
- [sp_api_retry_config](#sp_api_retry_config)
- [sp_api_schema_change_alerts](#sp_api_schema_change_alerts)
- [sub_process_account_brand_type_param](#sub_process_account_brand_type_param)
- [sub_process_account_type_param](#sub_process_account_type_param)
- [sub_process_audit](#sub_process_audit)
- [sub_process_dq_query](#sub_process_dq_query)
- [sub_process_org_param](#sub_process_org_param)
- [sub_process_org_type_param](#sub_process_org_type_param)
- [sub_process_param](#sub_process_param)
- [sub_processes](#sub_processes)
- [translation_table](#translation_table)
- [vantage_record_count](#vantage_record_count)
- [viz_app_usage_metrics](#viz_app_usage_metrics)
- [viz_content_change](#viz_content_change)
- [viz_latest_product_details_dump](#viz_latest_product_details_dump)

---

## account_activity_details

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| account_activity_id | int4(32) | No | nextval('i2oretail_dp.account_activity_details_account_activity_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| client_id | varchar(150) | No |  |  | No |  |
| activity_time | timestamp | Yes |  |  | No |  |
| type | varchar(150) | No |  |  | No |  |
| activity | varchar(150) | No |  |  | No |  |
| source | varchar(150) | Yes |  |  | No |  |
| user_id | varchar(150) | No |  |  | No |  |
| activity_status | varchar(150) | No |  |  | No |  |
| source_ip | varchar(150) | No |  |  | No |  |

---

## account_brands

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| brand_id | int4(32) | No | nextval('i2oretail_dp.brand_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| account_id | int4(32) | No |  | FOREIGN KEY | No |  |
| brand_name | varchar(100) | Yes |  |  | No |  |
| is_active | varchar(50) | Yes |  |  | No |  |

---

## account_id_status_logs

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| log_id | int4(32) | No | nextval('i2oretail_dp.account_id_status_logs_log_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_name | varchar(150) | No |  |  | No |  |
| client_id | varchar(150) | No |  |  | No |  |
| modified_by | varchar(150) | No |  |  | No |  |
| data_updated | varchar(500) | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |

---

## account_status

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| program_name | varchar(250) | No |  |  | No |  |
| id | varchar(150) | No |  | PRIMARY KEY, UNIQUE | Yes |  |
| id_type | varchar(250) | No |  | PRIMARY KEY | Yes |  |
| rdp_ip | varchar(150) | Yes |  |  | No |  |
| source | varchar(250) | No |  |  | No |  |
| status | varchar(250) | Yes |  |  | No |  |
| is_primary_id | bool | Yes |  |  | No |  |
| working_id_locked_past | bool | Yes |  |  | No |  |
| id_onboard_date | timestamp | Yes |  |  | No |  |
| locked_date | timestamp | Yes |  |  | No |  |
| single_active_id | bool | Yes |  |  | No |  |
| scope | varchar(250) | Yes |  |  | No |  |
| required_access | varchar(250) | Yes |  |  | No |  |
| working_access | varchar(250) | Yes |  |  | No |  |
| last_updated | timestamp | Yes |  |  | No |  |
| secret_id | varchar(250) | Yes |  |  | No |  |
| marketplace_id | int4(32) | Yes |  |  | No |  |
| active_id_count | int4(32) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| is_active | varchar(100) | Yes |  |  | No |  |
| rdp_user_name | varchar(50) | Yes |  |  | No |  |
| rdp_password | varchar(50) | Yes |  |  | No |  |
| vault_user_id | varchar(50) | Yes |  |  | No |  |
| vault_master_password | varchar(50) | Yes |  |  | No |  |
| brands | varchar(6000) | Yes |  |  | No |  |
| account_metadata | json | Yes |  |  | No |  |
| seller_id | varchar(100) | Yes |  |  | No |  |

---

## ad_campaign_report_filtered

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| spend | numeric(38,9) | Yes |  |  | No |  |
| clicks | numeric(38,9) | Yes |  |  | No |  |
| period | varchar | Yes |  |  | Yes |  |
| region | varchar | Yes |  |  | Yes |  |
| platform | varchar | Yes |  |  | Yes |  |
| placement | varchar | Yes |  |  | No |  |
| campaign_id | varchar | Yes |  |  | Yes |  |
| impressions | numeric(38,9) | Yes |  |  | No |  |
| account_name | varchar | Yes |  |  | Yes |  |
| campaign_name | varchar | Yes |  |  | No |  |
| campaign_type | varchar | Yes |  |  | No |  |
| portfolio_name | varchar | Yes |  |  | No |  |
| campaign_status | varchar | Yes |  |  | No |  |
| reporting_range | varchar | Yes |  |  | Yes |  |
| attributed_sales | numeric(38,9) | Yes |  |  | No |  |
| campaign_end_date | varchar | Yes |  |  | No |  |
| campaign_targeting | varchar | Yes |  |  | No |  |
| campaign_start_date | varchar | Yes |  |  | No |  |
| attributed_conversion | numeric(38,9) | Yes |  |  | No |  |
| attributed_dpv_clicks | numeric(38,9) | Yes |  |  | No |  |
| campaign_daily_budget | numeric(38,9) | Yes |  |  | No |  |
| attributed_units_ordered | numeric(38,9) | Yes |  |  | No |  |
| attributed_sales_same_sku | numeric(38,9) | Yes |  |  | No |  |
| attributed_sales_new_to_brand | numeric(38,9) | Yes |  |  | No |  |
| attributed_units_new_to_brand | numeric(38,9) | Yes |  |  | No |  |
| attributed_conversion_same_sku | numeric(38,9) | Yes |  |  | No |  |
| attributed_orders_new_to_brand | numeric(38,9) | Yes |  |  | No |  |
| attributed_sales_new_to_brand__ | numeric(38,9) | Yes |  |  | No |  |
| attributed_units_new_to_brand__ | numeric(38,9) | Yes |  |  | No |  |
| attributed_orders_new_to_brand__ | numeric(38,9) | Yes |  |  | No |  |
| attributed_units_ordered_same_sku | numeric(38,9) | Yes |  |  | No |  |
| attribute_order_rate_new_to_brand_ntb_orders_clicks | numeric(38,9) | Yes |  |  | No |  |
| _airbyte_raw_id | varchar(36) | No |  |  | Yes |  |
| _airbyte_extracted_at | timestamptz | No |  |  | Yes |  |
| _airbyte_meta | jsonb | No |  |  | No |  |

---

## ad_sp_api_config_backup

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| sub_process_id | int4(32) | Yes |  |  | No |  |
| request_body | json | Yes |  |  | No |  |
| column_mapping | json | Yes |  |  | No |  |
| source_file_type | varchar(40) | Yes |  |  | No |  |
| api_type | varchar(128) | Yes |  |  | No |  |
| data_load_check | json | Yes |  |  | No |  |

---

## agency

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| agency_id | int4(32) | No | nextval('i2oretail_dp.agency_agency_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| agency_name | varchar(250) | Yes |  |  | No |  |
| agency_alias | varchar(100) | Yes |  |  | No |  |
| agency_banner_logo_name | varchar(200) | Yes |  |  | No |  |

---

## api_claims

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| api_type | varchar | No |  | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| marketplace_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| thread_id | uuid | No |  |  | No |  |
| expires_at | timestamp | Yes |  |  | No |  |
| source | varchar(256) | No |  | PRIMARY KEY | Yes |  |

---

## application_properties

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| module | varchar(100) | Yes |  |  | No |  |
| property | varchar(100) | No |  |  | No |  |
| value | json | Yes |  |  | No |  |
| description | varchar(500) | Yes |  |  | No |  |

---

## asin_map_master

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| row_id | int4(32) | No | nextval('i2oretail_dp.asin_map_master_row_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| asin | varchar(100) | Yes |  |  | No |  |
| map | varchar(100) | Yes |  |  | No |  |
| lpl | varchar(100) | Yes |  |  | No |  |
| region | varchar(100) | Yes |  |  | No |  |
| marketplace | varchar(100) | Yes |  |  | No |  |
| status | varchar(20) | Yes | NULL::character varying |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |

---

## auth_resellers_list

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| row_id | int4(32) | No | nextval('i2oretail_dp.auth_resellers_list_row_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| authorized_resellers | varchar(100) | Yes |  |  | No |  |
| brand | varchar(100) | Yes |  |  | No |  |
| product_code | varchar(100) | Yes |  |  | No |  |
| self | varchar(100) | Yes |  |  | No |  |
| reseller_start_date | varchar(100) | Yes |  |  | No |  |
| reseller_end_date | varchar(100) | Yes |  |  | No |  |
| org_type | varchar(100) | Yes |  |  | No |  |
| region | varchar(100) | Yes |  |  | No |  |
| marketplace | varchar(100) | Yes |  |  | No |  |
| status | varchar(20) | Yes | NULL::character varying |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |

---

## brand_violation_plugin_capture_log

_Log of brand-violation captures from the browser plugin_

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int8(64) | No | nextval('i2oretail_dp.brand_violation_plugin_capture_log_id_seq'::regclass) |  | Yes | Primary key (auto-increment) |
| suspect_product_code | text | No |  |  | Yes | Product code captured via plugin from the PDP page |
| suspect_product_url | text | No |  |  | No | Product URL captured via plugin from the PDP page |
| suspect_brand | text | No |  |  | Yes | Suspect brand captured via plugin from the PDP page |
| master_product_code | text | Yes |  |  | Yes | Master product code entered by end user/AM |
| violation_type | text | No |  |  | Yes | Type of violation (Duplication, Bundle, Trademark, etc.) |
| tags | text | Yes |  |  | No | Tags, if any |
| keywords | text | Yes |  |  | No | Keywords, if any |
| prev_violation_type | text | Yes |  |  | No | Previous violation type captured for suspect |
| screenshot_gcs_url | text | No |  |  | No | GCS URL of the captured screenshot |
| captured_at | timestamptz | No | now() |  | Yes | Timestamp of capture |

---

## client_onboarding_status

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| client_onboard_id | int4(32) | No | nextval('i2oretail_dp.client_onboarding_status_client_onboard_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  |  | No |  |
| marketplace_id | int4(32) | No |  |  | No |  |
| source | varchar(100) | No |  |  | No |  |
| operation | varchar(100) | No |  |  | No |  |
| onboarding_stage_id | int4(32) | No |  |  | No |  |
| onboarding_substage_id | int4(32) | No |  |  | No |  |
| status | varchar(100) | Yes |  |  | No |  |
| created_by | varchar(100) | Yes |  |  | No |  |
| created_on | timestamptz | Yes | now() |  | No |  |
| last_modified_on | timestamptz | Yes | now() |  | No |  |
| last_modified_by | varchar(100) | Yes |  |  | No |  |
| start_datetime | timestamp | Yes |  |  | No |  |
| end_datetime | timestamp | Yes |  |  | No |  |
| retry_attempts | int4(32) | Yes |  |  | No |  |
| error_msg | varchar | Yes |  |  | No |  |

---

## dag

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| dag_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| dag_env | text | No |  |  | No |  |
| description | text | No |  |  | No |  |

---

## data_last_publish

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| publish_id | int4(32) | No | nextval('i2oretail_dp.data_last_publish_publish_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| publish_table_name | varchar(100) | Yes |  |  | No |  |
| last_publish_time | timestamptz | No | '1990-01-01 00:00:00+00'::timestamp with time zone |  | No |  |
| publish_target_name | varchar(100) | Yes |  |  | No |  |
| publisher | varchar(100) | Yes |  |  | No |  |

---

## data_loads_record_count

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | int4(32) | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| org_name | varchar | Yes |  |  | No |  |
| account_name | varchar | Yes |  |  | No |  |
| report_name | varchar | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| job_id | int4(32) | Yes |  |  | No |  |
| load_id | timestamp | Yes |  |  | No |  |
| status | varchar | Yes |  |  | No |  |
| week_repo_date | date | Yes |  |  | No |  |
| source | varchar | Yes |  |  | No |  |
| current_record_count | int4(32) | Yes |  |  | No |  |
| previous_record_count | int4(32) | Yes |  |  | No |  |
| previous_period | date | Yes |  |  | No |  |
| portal_record_count | int4(32) | Yes |  |  | No |  |

---

## dq_query

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | No |  |  | No |  |
| query_string | varchar | No |  |  | No |  |
| query_description | varchar | Yes |  |  | No |  |
| additional_info | varchar | Yes |  |  | No |  |
| target | varchar | No | 'bq'::character varying |  | No |  |

---

## dq_query_backup

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| query_id | int4(32) | Yes |  |  | No |  |
| query_string | varchar | Yes |  |  | No |  |
| query_description | varchar | Yes |  |  | No |  |
| additional_info | varchar | Yes |  |  | No |  |

---

## dq_results

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| process_instance_id | int4(32) | No |  |  | No |  |
| sub_process_id | int4(32) | No |  |  | No |  |
| marketplace_id | int4(32) | No |  |  | No |  |
| frequency | varchar | Yes |  |  | No |  |
| run_id | int4(32) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| status | varchar | Yes |  |  | No |  |
| sub_process_dq_query_id | varchar | Yes |  |  | No |  |
| error_msg | varchar | Yes |  |  | No |  |

---

## email_messages_graph_api

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | varchar(255) | No |  |  | Yes |  |
| subject | varchar(500) | Yes |  |  | No |  |
| sender_email | varchar(255) | Yes |  |  | No |  |
| sender_name | varchar(255) | Yes |  |  | No |  |
| received_datetime | timestamp | Yes |  |  | No |  |
| body_preview | text | Yes |  |  | No |  |
| body_content | text | Yes |  |  | No |  |
| to_recipients | text | Yes |  |  | No |  |
| created_at | timestamp | Yes | now() |  | No |  |

---

## email_receipients

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| email_receipient_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| email_tmpl_id | int4(32) | No |  | FOREIGN KEY | No |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| email_id | varchar(200) | Yes |  |  | No |  |
| to_emails | varchar(300) | Yes |  |  | No |  |
| username | varchar(50) | Yes |  |  | No |  |
| cc_emails | varchar(500) | Yes |  |  | No |  |
| bcc_emails | varchar(500) | Yes |  |  | No |  |

---

## email_templates

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| email_tmpl_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| tmpl_name | varchar(100) | Yes |  |  | No |  |
| sendgrid_secret_id | varchar(200) | Yes |  |  | No |  |
| sub_process_id | int4(32) | No |  | FOREIGN KEY | No |  |
| sendgrid_tmpl_id | varchar(50) | Yes |  |  | No |  |

---

## image_comparison_job_status

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| job_id | varchar | No |  | PRIMARY KEY | Yes |  |
| product_code | varchar(20) | No |  | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| marketplace | varchar | Yes |  |  | No |  |
| region | varchar | Yes |  |  | No |  |
| status | varchar | Yes |  |  | No |  |
| number_of_comparisons | int4(32) | Yes |  |  | No |  |
| time_elapsed_in_ms | int4(32) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| total_records | int4(32) | Yes |  |  | No |  |

---

## image_comparison_metadata

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_code | varchar(100) | No |  | PRIMARY KEY | Yes |  |
| image_url_1 | varchar(500) | No |  | PRIMARY KEY | Yes |  |
| image_url_2 | varchar(500) | No |  | PRIMARY KEY | Yes |  |
| image_file_checksum_1 | varchar(100) | Yes |  |  | No |  |
| image_file_checksum_2 | varchar(100) | Yes |  |  | No |  |
| image_size_1 | int4(32) | Yes |  |  | No |  |
| image_size_2 | int4(32) | Yes |  |  | No |  |
| image_dimensions_1 | varchar(20) | Yes |  |  | No |  |
| image_dimensions_2 | varchar(20) | Yes |  |  | No |  |
| score | float8(53) | Yes |  |  | No |  |
| score_label | varchar(100) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| compare_algorithm | varchar | Yes | 'deep_feature'::character varying |  | No |  |

---

## image_comparison_metadata_local_test

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_code | varchar(100) | No |  | PRIMARY KEY | Yes |  |
| image_url_1 | varchar(500) | No |  | PRIMARY KEY | Yes |  |
| image_url_2 | varchar(500) | No |  | PRIMARY KEY | Yes |  |
| image_file_checksum_1 | varchar(100) | Yes |  |  | No |  |
| image_file_checksum_2 | varchar(100) | Yes |  |  | No |  |
| image_size_1 | int4(32) | Yes |  |  | No |  |
| image_size_2 | int4(32) | Yes |  |  | No |  |
| image_dimensions_1 | varchar(20) | Yes |  |  | No |  |
| image_dimensions_2 | varchar(20) | Yes |  |  | No |  |
| score | float8(53) | Yes |  |  | No |  |
| score_label | varchar(100) | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |

---

## image_content_comparison

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_code | varchar | No |  | PRIMARY KEY | Yes |  |
| period | date | No |  | PRIMARY KEY | Yes |  |
| time_of_day | varchar | No |  | PRIMARY KEY | Yes |  |
| marketplace | varchar | No |  | PRIMARY KEY | Yes |  |
| region | varchar | No |  | PRIMARY KEY | Yes |  |
| content_change_type | varchar | No |  | PRIMARY KEY | Yes |  |
| actual | varchar | Yes |  |  | No |  |
| alert | varchar | Yes |  |  | No |  |
| asin | varchar | Yes |  |  | No |  |
| change_status | varchar | Yes |  |  | No |  |
| compare_result_metadata | jsonb | No |  |  | No |  |
| expected | varchar | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| product_lock_status | varchar | Yes |  |  | No |  |
| project_id | varchar | Yes |  |  | No |  |
| source | varchar | Yes |  |  | No |  |
| scrape_timestamp | timestamptz | Yes |  |  | No |  |
| created_at | timestamp | No | now() |  | No |  |
| updated_at | timestamp | No | now() |  | No |  |
| reporting_range | varchar | Yes | 'daily'::character varying |  | No |  |
| locked_timestamp | timestamp | Yes |  |  | No |  |
| previous_period | date | Yes |  |  | No |  |
| previous_time_of_day | varchar | Yes |  |  | No |  |
| alert_tags | varchar | Yes |  |  | No |  |

---

## image_content_comparison_backlog

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_code | varchar | No |  | PRIMARY KEY | Yes |  |
| period | date | No |  | PRIMARY KEY | Yes |  |
| time_of_day | varchar | No |  | PRIMARY KEY | Yes |  |
| marketplace | varchar | No |  | PRIMARY KEY | Yes |  |
| region | varchar | No |  | PRIMARY KEY | Yes |  |
| content_change_type | varchar | No |  | PRIMARY KEY | Yes |  |
| actual | varchar | Yes |  |  | No |  |
| alert | varchar | Yes |  |  | No |  |
| asin | varchar | Yes |  |  | No |  |
| change_status | varchar | Yes |  |  | No |  |
| compare_result_metadata | jsonb | No |  |  | No |  |
| expected | varchar | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| product_lock_status | varchar | Yes |  |  | No |  |
| project_id | varchar | Yes |  |  | No |  |
| source | varchar | Yes |  |  | No |  |
| scrape_timestamp | timestamptz | Yes |  |  | No |  |
| created_at | timestamp | No | now() |  | No |  |
| updated_at | timestamp | No | now() |  | No |  |
| reporting_range | varchar | Yes | 'daily'::character varying |  | No |  |
| locked_timestamp | timestamp | Yes |  |  | No |  |
| previous_period | date | Yes |  |  | No |  |
| previous_time_of_day | varchar | Yes |  |  | No |  |

---

## image_content_comparison_local_test

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| actual | varchar | Yes |  |  | No |  |
| alert | varchar | Yes |  |  | No |  |
| asin | varchar | Yes |  |  | No |  |
| change_status | varchar | Yes |  |  | No |  |
| compare_result_metadata | jsonb | No |  |  | No |  |
| content_change_type | varchar | No |  | PRIMARY KEY | Yes |  |
| expected | varchar | Yes |  |  | No |  |
| marketplace | varchar | No |  | PRIMARY KEY | Yes |  |
| org_id | int4(32) | Yes |  |  | No |  |
| period | date | No |  | PRIMARY KEY | Yes |  |
| product_code | varchar | No |  | PRIMARY KEY | Yes |  |
| product_lock_status | varchar | Yes |  |  | No |  |
| project_id | varchar | Yes |  |  | No |  |
| region | varchar | No |  | PRIMARY KEY | Yes |  |
| source | varchar | Yes |  |  | No |  |
| time_of_day | varchar | No |  | PRIMARY KEY | Yes |  |
| scrape_timestamp | timestamptz | Yes |  |  | No |  |
| created_at | timestamp | No | now() |  | No |  |
| updated_at | timestamp | No | now() |  | No |  |
| reporting_range | varchar | Yes | 'daily'::character varying |  | No |  |
| locked_timestamp | timestamp | Yes |  |  | No |  |
| previous_period | date | Yes |  |  | No |  |
| previous_time_of_day | varchar | Yes |  |  | No |  |

---

## image_content_comparison_temp

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | Yes |  |  | No |  |
| actual | varchar | Yes |  |  | No |  |
| alert | varchar | Yes |  |  | No |  |
| asin | varchar | Yes |  |  | No |  |
| change_status | varchar | Yes |  |  | No |  |
| compare_result_metadata | jsonb | Yes |  |  | No |  |
| content_change_type | varchar | Yes |  |  | No |  |
| expected | varchar | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | No |  |
| org_id | int4(32) | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| product_code | varchar | Yes |  |  | No |  |
| product_lock_status | varchar | Yes |  |  | No |  |
| project_id | varchar | Yes |  |  | No |  |
| region | varchar | Yes |  |  | No |  |
| source | varchar | Yes |  |  | No |  |
| time_of_day | varchar | Yes |  |  | No |  |
| scrape_timestamp | timestamptz | Yes |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| reporting_range | varchar | Yes |  |  | No |  |

---

## marketplace

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| marketplace_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| platform | varchar(50) | No |  |  | No |  |
| region | varchar(50) | No |  |  | No |  |
| metadata | json | Yes |  |  | No |  |

---

## marketplace_scraper_mapper

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dp.marketplace_scraper_mapper_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| marketplace_id | int4(32) | No |  |  | No |  |
| scraper_type | varchar(50) | Yes |  |  | No |  |

---

## onboarding_queries

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dp.onboarding_query_id_seq'::regclass) |  | Yes |  |
| source | varchar(50) | No |  |  | No |  |
| query | text | No |  |  | No |  |
| priority | int4(32) | No |  |  | No |  |
| operation | varchar(50) | Yes |  |  | No |  |
| validation_query | text | Yes |  |  | No |  |
| stage_id | int4(32) | Yes |  |  | No |  |
| substage_id | int4(32) | Yes |  |  | No |  |

---

## onboarding_queries_test

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dp.onboarding_queries_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| source | varchar | No |  |  | No |  |
| query | text | No |  |  | No |  |
| priority | int4(32) | No |  |  | No |  |
| operation | varchar | Yes |  |  | No |  |
| validation_query | text | Yes |  |  | No |  |
| stage_id | int4(32) | Yes |  |  | No |  |
| substage_id | int4(32) | Yes |  |  | No |  |

---

## onboarding_stage

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| onboarding_stage_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| source | varchar(50) | Yes |  |  | No |  |
| operation_type | varchar(50) | Yes |  |  | No |  |
| stage | varchar(50) | Yes |  |  | No |  |
| priority | int4(32) | Yes |  |  | No |  |
| retry_threshold | int4(32) | Yes |  |  | No |  |
| metadata | varchar | Yes |  |  | No |  |
| max_retry_attempts | int4(32) | No | 3 |  | No |  |

---

## onboarding_substage

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| onboarding_substage_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| marketplace_id | int4(32) | Yes |  |  | No |  |
| onboarding_stage_id | int4(32) | Yes |  |  | No |  |
| sub_stage | varchar(100) | Yes |  |  | No |  |
| description | text | Yes |  |  | No |  |
| priority | int4(32) | Yes |  |  | No |  |
| operation | varchar(50) | Yes |  |  | No |  |
| team | varchar(50) | Yes |  |  | No |  |

---

## ops_data_load_allocation

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| data_load_allocation_id | int4(32) | No | nextval('i2oretail_dp.ops_data_load_allocation_data_load_allocation_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_name | varchar(150) | No |  |  | No |  |
| client_login_id | varchar(150) | No |  |  | No |  |
| rdp_ip | varchar(150) | Yes |  |  | No |  |
| team | varchar(150) | Yes |  |  | No |  |
| target_day | varchar(150) | Yes |  |  | No |  |
| download_allocation_user_name | varchar(150) | Yes |  |  | No |  |
| sanity_allocation_user_name | varchar(150) | Yes |  |  | No |  |
| reporting_range | varchar(100) | Yes |  |  | No |  |
| period | timestamp | Yes |  |  | No |  |
| reports | varchar(250) | Yes |  |  | No |  |
| comments | varchar(500) | Yes |  |  | No |  |

---

## ops_user_data

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| user_data_id | int4(32) | No | nextval('i2oretail_dp.ops_user_data_user_data_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| team | varchar(150) | No |  |  | No |  |
| user_name | varchar(150) | No |  |  | No |  |
| active | bool | No |  |  | No |  |
| created_at | timestamp | Yes |  |  | No |  |
| updated_at | timestamp | Yes |  |  | No |  |
| user_id | varchar(150) | Yes |  |  | No |  |

---

## org_accounts

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | int4(32) | No | nextval('i2oretail_dp.org_accounts_account_id_seq'::regclass) | PRIMARY KEY, UNIQUE | Yes |  |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | No |  |  | No |  |
| source_type | varchar(50) | No |  |  | No |  |
| account_name | varchar(100) | No |  |  | No |  |
| account_vgid | int4(32) | Yes |  | UNIQUE | Yes |  |
| account_type_cd | varchar(50) | No |  |  | No |  |
| is_active | varchar(50) | Yes |  |  | No |  |
| account_value | varchar(200) | Yes |  |  | No |  |
| account_metadata | json | Yes |  |  | No |  |

---

## org_dag_map

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  |  | No |  |
| dag_id | int4(32) | Yes |  |  | No |  |
| is_active | bool | Yes |  |  | No |  |

---

## org_data_metadata

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| marketplace_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| data_type | varchar(50) | No |  | PRIMARY KEY | Yes |  |
| data_set_location | varchar(200) | No |  |  | No |  |

---

## org_report

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| report_id | int4(32) | No | nextval('i2oretail_dp.org_report_report_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  |  | No |  |
| report_name | varchar(200) | Yes |  |  | No |  |
| ecom_pltfm | varchar(200) | Yes |  |  | No |  |
| org_type | varchar(50) | Yes |  |  | No |  |
| supports_history | varchar(100) | Yes |  |  | No |  |

---

## org_sources

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | No |  |  | No |  |
| source | varchar(50) | Yes |  |  | No |  |
| multiple_accounts | bool | Yes |  |  | No |  |
| login_page | varchar(100) | Yes |  |  | No |  |
| login_secret_id | varchar(100) | Yes |  |  | No |  |
| is_active | bool | Yes |  |  | No |  |
| scraper_login_failure | bool | Yes | false |  | No |  |
| dataload_type | varchar(10) | Yes | 'p1'::character varying |  | No |  |

---

## organization

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No | nextval('i2oretail_dp.organization_org_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_name | varchar(500) | No |  |  | No |  |
| org_type_cd | varchar(100) | No |  |  | No |  |
| version | float8(53) | Yes |  |  | No |  |
| url | varchar(200) | Yes |  |  | No |  |
| org_alias_name | varchar(50) | Yes |  |  | No |  |
| org_banner_logo_name | varchar(255) | Yes |  |  | No |  |
| is_active | varchar(10) | Yes |  |  | No |  |
| org_priority_weight | int4(32) | Yes | 0 |  | No |  |
| dag_active | varchar(10) | Yes |  |  | No |  |
| pipeline_batch_id | int4(32) | Yes | 1 |  | No |  |
| scraping_ip_addr | varchar(15) | Yes | NULL::character varying |  | No |  |
| agency_id | int4(32) | Yes |  | FOREIGN KEY | No |  |
| created_on | timestamp | Yes | now() |  | No |  |
| last_modified_on | timestamp | Yes | now() |  | No |  |
| created_by | varchar(255) | Yes |  |  | No |  |
| last_modified_by | varchar(255) | Yes |  |  | No |  |

---

## process_audit

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| process_instance_id | int4(32) | No | nextval('i2oretail_dp.process_audit_process_instance_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| org_id | int4(32) | No |  |  | Yes |  |
| marketplace_id | int4(32) | No |  |  | No |  |
| process_id | int4(32) | No |  |  | Yes |  |
| request_run_date | varchar(40) | Yes |  |  | No |  |
| start_datetime | timestamp | Yes |  |  | No |  |
| end_datetime | timestamp | Yes |  |  | No |  |
| status | varchar(80) | Yes |  |  | Yes |  |
| error_msg | text | Yes |  |  | No |  |
| stage | varchar(50) | Yes |  |  | Yes |  |
| period | date | Yes |  |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |
| job_run_timestamp | timestamp | Yes | '1900-01-01 00:00:00'::timestamp without time zone |  | No |  |
| time_of_day | int4(32) | Yes |  |  | No |  |

---

## process_org_market_place_param

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | No |  |  | No |  |
| process_id | int4(32) | No |  | FOREIGN KEY | No |  |
| input_directory | varchar(500) | Yes |  |  | No |  |
| processed_directory | varchar(500) | Yes |  |  | No |  |
| bq_directory | varchar(500) | Yes |  |  | No |  |
| archive_directory | varchar(500) | Yes |  |  | No |  |
| active | varchar(50) | Yes |  |  | No |  |

---

## processes

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| process_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| process_name | varchar(200) | Yes |  |  | No |  |
| source_type | varchar(50) | Yes |  |  | No |  |
| trigger_json | json | Yes |  |  | No |  |
| is_active | bool | Yes | true |  | No |  |
| display_name | varchar(150) | Yes |  |  | No |  |

---

## product_matching_output

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| Department | text | Yes |  |  | No |  |
| Search_Term | text | Yes |  |  | No |  |
| Search_Frequency_Rank | float8(53) | Yes |  |  | No |  |
| _1_Clicked_ASIN | text | Yes |  |  | No |  |
| _1_Product_Title | text | Yes |  |  | No |  |
| _1_Click_Share | float8(53) | Yes |  |  | No |  |
| _1_Conversion_Share | float8(53) | Yes |  |  | No |  |
| _2_Clicked_ASIN | text | Yes |  |  | No |  |
| _2_Product_Title | text | Yes |  |  | No |  |
| _2_Click_Share | float8(53) | Yes |  |  | No |  |
| _2_Conversion_Share | float8(53) | Yes |  |  | No |  |
| _3_Clicked_ASIN | text | Yes |  |  | No |  |
| _3_Product_Title | text | Yes |  |  | No |  |
| _3_Click_Share | float8(53) | Yes |  |  | No |  |
| _3_Conversion_Share | float8(53) | Yes |  |  | No |  |
| Enter_ASINs_or_Products | float8(53) | Yes |  |  | No |  |
| Reporting_Range | text | Yes |  |  | No |  |
| Viewing | text | Yes |  |  | No |  |
| start_date | text | Yes |  |  | No |  |
| end_date | text | Yes |  |  | No |  |
| org_type | text | Yes |  |  | No |  |
| marketplace | text | Yes |  |  | No |  |
| region | text | Yes |  |  | No |  |
| product_code_type | text | Yes |  |  | No |  |
| source_system_id | text | Yes |  |  | No |  |

---

## product_pricing_range_filtered

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| upc | varchar | Yes |  |  | No |  |
| url | varchar | Yes |  |  | No |  |
| month | varchar | Yes |  |  | No |  |
| a_plus | varchar | Yes |  |  | No |  |
| author | varchar | Yes |  |  | No |  |
| period | varchar | Yes |  |  | No |  |
| region | varchar | Yes |  |  | No |  |
| ISBN_10 | varchar | Yes |  |  | No |  |
| ISBN_13 | varchar | Yes |  |  | No |  |
| category | varchar | Yes |  |  | No |  |
| Publisher | varchar | Yes |  |  | No |  |
| images_url | varchar | Yes |  |  | No |  |
| list_price | numeric(38,9) | Yes |  |  | No |  |
| seller_url | varchar | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | No |  |
| offer_price | numeric(38,9) | Yes |  |  | No |  |
| parent_asin | varchar | Yes |  |  | No |  |
| scrape_date | varchar | Yes |  |  | No |  |
| time_of_day | int8(64) | Yes |  |  | No |  |
| manufacturer | varchar | Yes |  |  | No |  |
| model_number | varchar | Yes |  |  | No |  |
| photos_count | numeric(38,9) | Yes |  |  | No |  |
| product_code | varchar | Yes |  |  | No |  |
| sub_category | varchar | Yes |  |  | No |  |
| videos_count | numeric(38,9) | Yes |  |  | No |  |
| A_plus_source | varchar | Yes |  |  | No |  |
| buy_box_price | numeric(38,9) | Yes |  |  | No |  |
| html_location | varchar | Yes |  |  | No |  |
| product_title | varchar | Yes |  |  | No |  |
| total_reviews | int8(64) | Yes |  |  | No |  |
| average_rating | numeric(38,9) | Yes |  |  | No |  |
| bsr_cat_change | numeric(38,9) | Yes |  |  | No |  |
| prime_eligible | varchar | Yes |  |  | No |  |
| bsr_in_category | numeric(38,9) | Yes |  |  | No |  |
| platform_source | varchar | Yes |  |  | No |  |
| pp_bsr_category | numeric(38,9) | Yes |  |  | No |  |
| reporting_range | varchar | Yes |  |  | No |  |
| shipping_charge | varchar | Yes |  |  | No |  |
| shipping_weight | varchar | Yes |  |  | No |  |
| full_description | varchar | Yes |  |  | No |  |
| pp_buy_box_price | numeric(38,9) | Yes |  |  | No |  |
| product_category | varchar | Yes |  |  | No |  |
| scrape_timestamp | varchar | Yes |  |  | No |  |
| bullet_point_text | varchar | Yes |  |  | No |  |
| date_first_listed | varchar | Yes |  |  | No |  |
| domestic_shipping | varchar | Yes |  |  | No |  |
| item_model_number | varchar | Yes |  |  | No |  |
| product_condition | varchar | Yes |  |  | No |  |
| bsr_sub_cat_change | numeric(38,9) | Yes |  |  | No |  |
| per_change_bsr_ctg | numeric(38,9) | Yes |  |  | No |  |
| product_dimensions | varchar | Yes |  |  | No |  |
| product_variations | varchar | Yes |  |  | No |  |
| availability_status | varchar | Yes |  |  | No |  |
| bsr_in_sub_category | numeric(38,9) | Yes |  |  | No |  |
| one_star_percentage | numeric(38,9) | Yes |  |  | No |  |
| pp_bsr_sub_category | numeric(38,9) | Yes |  |  | No |  |
| two_star_percentage | numeric(38,9) | Yes |  |  | No |  |
| amazons_choice_badge | varchar | Yes |  |  | No |  |
| five_star_percentage | numeric(38,9) | Yes |  |  | No |  |
| four_star_percentage | numeric(38,9) | Yes |  |  | No |  |
| price_exception_flag | varchar | Yes |  |  | No |  |
| valid_buy_box_seller | varchar | Yes |  |  | No |  |
| availability_quantity | numeric(38,9) | Yes |  |  | No |  |
| three_star_percentage | numeric(38,9) | Yes |  |  | No |  |
| Buy_box_winning_seller | varchar | Yes |  |  | No |  |
| available_book_formats | varchar | Yes |  |  | No |  |
| international_shipping | varchar | Yes |  |  | No |  |
| per_change_bsr_sub_ctg | numeric(38,9) | Yes |  |  | No |  |
| amazon_best_seller_rank | varchar | Yes |  |  | No |  |
| answered_questions_count | numeric(38,9) | Yes |  |  | No |  |
| buybox_price_availability | varchar | Yes |  |  | No |  |
| frequently_bought_together | varchar | Yes |  |  | No |  |
| _airbyte_raw_id | varchar(36) | No |  |  | Yes |  |
| _airbyte_extracted_at | timestamptz | No |  |  | Yes |  |
| _airbyte_meta | jsonb | No |  |  | No |  |

---

## product_pricing_range_filtered_ab_soft_reset

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| upc | varchar | Yes |  |  | No |  |
| url | varchar | Yes |  |  | No |  |
| month | varchar | Yes |  |  | No |  |
| a_plus | varchar | Yes |  |  | No |  |
| author | varchar | Yes |  |  | No |  |
| period | varchar | Yes |  |  | Yes |  |
| region | varchar | Yes |  |  | Yes |  |
| ISBN_10 | varchar | Yes |  |  | No |  |
| ISBN_13 | varchar | Yes |  |  | No |  |
| category | varchar | Yes |  |  | No |  |
| Publisher | varchar | Yes |  |  | No |  |
| images_url | varchar | Yes |  |  | No |  |
| input_asin | varchar | Yes |  |  | No |  |
| list_price | numeric(38,9) | Yes |  |  | No |  |
| seller_url | varchar | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | Yes |  |
| offer_price | numeric(38,9) | Yes |  |  | No |  |
| parent_asin | varchar | Yes |  |  | No |  |
| scrape_date | varchar | Yes |  |  | No |  |
| time_of_day | int8(64) | Yes |  |  | No |  |
| manufacturer | varchar | Yes |  |  | No |  |
| model_number | varchar | Yes |  |  | No |  |
| photos_count | numeric(38,9) | Yes |  |  | No |  |
| product_code | varchar | Yes |  |  | Yes |  |
| sub_category | varchar | Yes |  |  | No |  |
| videos_count | numeric(38,9) | Yes |  |  | No |  |
| A_plus_source | varchar | Yes |  |  | No |  |
| buy_box_price | numeric(38,9) | Yes |  |  | No |  |
| html_location | varchar | Yes |  |  | No |  |
| product_title | varchar | Yes |  |  | No |  |
| total_reviews | int8(64) | Yes |  |  | No |  |
| average_rating | numeric(38,9) | Yes |  |  | No |  |
| bsr_cat_change | numeric(38,9) | Yes |  |  | No |  |
| prime_eligible | varchar | Yes |  |  | No |  |
| bsr_in_category | numeric(38,9) | Yes |  |  | No |  |
| platform_source | varchar | Yes |  |  | No |  |
| pp_bsr_category | numeric(38,9) | Yes |  |  | No |  |
| reporting_range | varchar | Yes |  |  | No |  |
| shipping_charge | varchar | Yes |  |  | No |  |
| shipping_weight | varchar | Yes |  |  | No |  |
| full_description | varchar | Yes |  |  | No |  |
| pp_buy_box_price | numeric(38,9) | Yes |  |  | No |  |
| product_category | varchar | Yes |  |  | No |  |
| scrape_timestamp | varchar | Yes |  |  | No |  |
| bullet_point_text | varchar | Yes |  |  | No |  |
| date_first_listed | varchar | Yes |  |  | No |  |
| domestic_shipping | varchar | Yes |  |  | No |  |
| item_model_number | varchar | Yes |  |  | No |  |
| product_condition | varchar | Yes |  |  | No |  |
| bsr_sub_cat_change | numeric(38,9) | Yes |  |  | No |  |
| per_change_bsr_ctg | numeric(38,9) | Yes |  |  | No |  |
| product_dimensions | varchar | Yes |  |  | No |  |
| product_variations | varchar | Yes |  |  | No |  |
| availability_status | varchar | Yes |  |  | No |  |
| bsr_in_sub_category | numeric(38,9) | Yes |  |  | No |  |
| one_star_percentage | numeric(38,9) | Yes |  |  | No |  |
| pp_bsr_sub_category | numeric(38,9) | Yes |  |  | No |  |
| two_star_percentage | numeric(38,9) | Yes |  |  | No |  |
| amazons_choice_badge | varchar | Yes |  |  | No |  |
| five_star_percentage | numeric(38,9) | Yes |  |  | No |  |
| four_star_percentage | numeric(38,9) | Yes |  |  | No |  |
| price_exception_flag | varchar | Yes |  |  | No |  |
| valid_buy_box_seller | varchar | Yes |  |  | No |  |
| availability_quantity | numeric(38,9) | Yes |  |  | No |  |
| three_star_percentage | numeric(38,9) | Yes |  |  | No |  |
| Buy_box_winning_seller | varchar | Yes |  |  | No |  |
| available_book_formats | varchar | Yes |  |  | No |  |
| international_shipping | varchar | Yes |  |  | No |  |
| per_change_bsr_sub_ctg | numeric(38,9) | Yes |  |  | No |  |
| amazon_best_seller_rank | varchar | Yes |  |  | No |  |
| answered_questions_count | numeric(38,9) | Yes |  |  | No |  |
| buybox_price_availability | varchar | Yes |  |  | No |  |
| frequently_bought_together | varchar | Yes |  |  | No |  |
| _airbyte_raw_id | varchar(36) | No |  |  | Yes |  |
| _airbyte_extracted_at | timestamptz | No |  |  | Yes |  |
| _airbyte_meta | jsonb | No |  |  | No |  |

---

## scheduler_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| marketplace_id | int4(32) | No |  |  | No |  |
| dag_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| dag_name | varchar(200) | Yes |  |  | No |  |
| dag_file | varchar(200) | Yes |  |  | No |  |
| schedule | varchar(200) | Yes |  |  | No |  |

---

## scraper_subprocess_id_mapper

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No | nextval('i2oretail_dp.scraper_subprocess_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| sub_process_id | int4(32) | No |  |  | No |  |
| scraper_type | varchar(50) | Yes |  |  | No |  |

---

## search_terms

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| Department | text | Yes |  |  | No |  |
| Search_Term | text | Yes |  |  | No |  |
| Search_Frequency_Rank | float8(53) | Yes |  |  | No |  |
| _1_Clicked_ASIN | text | Yes |  |  | No |  |
| _1_Product_Title | text | Yes |  |  | No |  |
| _1_Click_Share | float8(53) | Yes |  |  | No |  |
| _1_Conversion_Share | float8(53) | Yes |  |  | No |  |
| _2_Clicked_ASIN | text | Yes |  |  | No |  |
| _2_Product_Title | text | Yes |  |  | No |  |
| _2_Click_Share | float8(53) | Yes |  |  | No |  |
| _2_Conversion_Share | float8(53) | Yes |  |  | No |  |
| _3_Clicked_ASIN | text | Yes |  |  | No |  |
| _3_Product_Title | text | Yes |  |  | No |  |
| _3_Click_Share | float8(53) | Yes |  |  | No |  |
| _3_Conversion_Share | float8(53) | Yes |  |  | No |  |
| Enter_ASINs_or_Products | float8(53) | Yes |  |  | No |  |
| Reporting_Range | text | Yes |  |  | No |  |
| Viewing | text | Yes |  |  | No |  |
| start_date | text | Yes |  |  | No |  |
| end_date | text | Yes |  |  | No |  |
| org_type | text | Yes |  |  | No |  |
| marketplace | text | Yes |  |  | No |  |
| region | text | Yes |  |  | No |  |
| product_code_type | text | Yes |  |  | No |  |
| source_system_id | text | Yes |  |  | No |  |

---

## search_terms_copy

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | Yes |  |  | No |  |
| name | varchar(50) | Yes |  |  | No |  |
| salary | int4(32) | Yes |  |  | No |  |

---

## sh_validations

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| rule_index | varchar(5) | No |  | PRIMARY KEY | Yes |  |
| rule_name | varchar(600) | Yes |  |  | No |  |
| threshold_limit | int4(32) | No |  |  | No |  |
| is_active | bool | Yes |  |  | No |  |

---

## sp_api_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| sub_process_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| request_body | json | No |  |  | No |  |
| column_mapping | json | No |  |  | No |  |
| source_file_type | varchar(40) | No | 'json'::character varying |  | No |  |
| api_type | varchar(128) | Yes |  |  | No |  |
| data_load_check | json | Yes | '{}'::json |  | No |  |
| filters | json | Yes |  |  | No |  |

---

## sp_api_config_bck_25_04_2024

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| sub_process_id | int4(32) | Yes |  |  | No |  |
| request_body | json | Yes |  |  | No |  |
| column_mapping | json | Yes |  |  | No |  |
| source_file_type | varchar(40) | Yes |  |  | No |  |
| api_type | varchar(128) | Yes |  |  | No |  |
| data_load_check | json | Yes |  |  | No |  |
| filters | json | Yes |  |  | No |  |

---

## sp_api_config_havingdatalevel

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| sub_process_id | int4(32) | Yes |  |  | No |  |
| request_body | json | Yes |  |  | No |  |
| column_mapping | json | Yes |  |  | No |  |
| source_file_type | varchar(40) | Yes |  |  | No |  |
| api_type | varchar(128) | Yes |  |  | No |  |
| data_load_check | json | Yes |  |  | No |  |
| filters | json | Yes |  |  | No |  |

---

## sp_api_properties

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| api_type | varchar(256) | No |  |  | No |  |
| api_group | varchar(256) | No |  |  | No |  |
| process_ids | json | No | '[]'::json |  | No |  |
| sub_process_ids | json | No | '[]'::json |  | No |  |
| retry_config | json | No | '{}'::json |  | No |  |
| audit_stage | varchar(256) | Yes |  |  | No |  |
| audit_status | varchar(256) | Yes |  |  | No |  |

---

## sp_api_retry_config

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| api_type | varchar(256) | No |  | PRIMARY KEY | Yes |  |
| retry_config | json | No | '{}'::json |  | No |  |

---

## sp_api_schema_change_alerts

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| detail_id | int4(32) | No |  | FOREIGN KEY, PRIMARY KEY | Yes |  |
| unknown_columns | json | No | '[]'::json |  | No |  |
| missing_columns | json | No | '[]'::json |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| email_sent_at | timestamptz | Yes |  |  | No |  |

---

## sub_process_account_brand_type_param

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| sub_process_id | int4(32) | No |  | FOREIGN KEY | No |  |
| account_id | int4(32) | No |  | FOREIGN KEY | No |  |
| brand_id | int4(32) | No |  | FOREIGN KEY | No |  |
| is_active | bool | Yes |  |  | No |  |

---

## sub_process_account_type_param

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | int4(32) | No |  | FOREIGN KEY | No |  |
| sub_process_id | int4(32) | No |  | FOREIGN KEY | No |  |
| account_type_cd | varchar(50) | Yes |  |  | No |  |
| is_active | varchar(20) | Yes |  |  | No |  |
| po_item_lvl_chunk_size | int4(32) | Yes |  |  | No |  |
| supports_history | varchar | Yes |  |  | No |  |

---

## sub_process_audit

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| detail_id | int4(32) | No | nextval('i2oretail_dp.sub_process_audit_detail_id_seq'::regclass) | PRIMARY KEY | Yes |  |
| process_instance_id | int8(64) | No |  | FOREIGN KEY | Yes |  |
| sub_process_id | int4(32) | No |  | FOREIGN KEY | Yes |  |
| start_date | date | Yes |  |  | No |  |
| end_date | date | Yes |  |  | No |  |
| frequency | varchar(20) | Yes |  |  | No |  |
| account_name | varchar(100) | Yes |  |  | No |  |
| account_id | int4(32) | Yes |  |  | No |  |
| brand_name | varchar(50) | Yes |  |  | No |  |
| brand_id | int4(32) | Yes |  |  | No |  |
| start_datetime | timestamp | Yes |  |  | No |  |
| end_datetime | timestamp | Yes |  |  | No |  |
| stage | varchar(40) | Yes |  |  | Yes |  |
| status | varchar(40) | Yes |  |  | Yes |  |
| error_msg | text | Yes |  |  | No |  |
| retry_attempts | int4(32) | Yes |  |  | No |  |
| rows_count | int4(32) | Yes |  |  | No |  |
| run_type | varchar(40) | Yes |  |  | No |  |
| gcs_location | varchar(500) | Yes |  |  | No |  |
| created_at | timestamptz | No | now() |  | No |  |
| updated_at | timestamptz | No | now() |  | No |  |
| priority_weight | int4(32) | Yes | 0 |  | No |  |
| metadata | json | Yes |  |  | No |  |
| is_automated | bool | Yes | true |  | No |  |
| application_load | bool | Yes | true |  | No |  |
| report_timestamp | timestamp | Yes | '1900-01-01 00:00:00'::timestamp without time zone |  | No |  |

---

## sub_process_dq_query

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| id | int4(32) | No |  |  | No |  |
| sub_process_id | int4(32) | No |  |  | No |  |
| query_id | int4(32) | No |  |  | No |  |
| frequency | varchar | No |  |  | No |  |
| is_active | varchar | No |  |  | No |  |
| error_level | varchar | Yes |  |  | No |  |
| condition_checks | varchar | Yes |  |  | No |  |
| priority | varchar | Yes | 'check'::character varying |  | No |  |
| marketplace_id | _int4 | No |  |  | No |  |
| metric_type | varchar | Yes |  |  | No |  |

---

## sub_process_org_param

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No | '-1'::integer | FOREIGN KEY | Yes |  |
| sub_process_id | int4(32) | No |  | FOREIGN KEY | No |  |
| sub_process_name | varchar(300) | No |  |  | No |  |
| files_config | varchar(1000) | Yes |  |  | No |  |
| config | json | Yes |  |  | No |  |

---

## sub_process_org_type_param

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| org_id | int4(32) | No |  | FOREIGN KEY | No |  |
| sub_process_id | int4(32) | No |  | FOREIGN KEY | No |  |
| is_active | bool | Yes |  |  | No |  |
| marketplace_id | int4(32) | No |  |  | No |  |
| trigger_json | json | Yes |  |  | No |  |
| update_check | bool | Yes |  |  | No |  |
| metadata | json | Yes |  |  | No |  |
| is_automated | bool | Yes | true |  | No |  |
| application_load | bool | Yes | true |  | No |  |
| start_date | date | Yes | '1900-01-01'::date |  | No |  |
| end_date | date | Yes | '9999-12-31'::date |  | No |  |

---

## sub_process_param

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| sub_process_id | int4(32) | No |  | FOREIGN KEY | No |  |
| sub_process_name | varchar(300) | No |  |  | No |  |
| files_config | varchar(800) | Yes |  |  | No |  |
| config | json | Yes |  |  | No |  |

---

## sub_processes

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| process_id | int4(32) | No |  | FOREIGN KEY | No |  |
| sub_process_id | int4(32) | No |  | PRIMARY KEY | Yes |  |
| sub_process_name | varchar(300) | Yes |  |  | No |  |
| frequency | varchar(200) | Yes |  |  | No |  |
| expected_start_time_utc | time | Yes |  |  | No |  |
| expected_end_time_utc | time | Yes |  |  | No |  |
| required_process | varchar(50) | Yes |  |  | No |  |
| retry_config | int4(32) | Yes |  |  | No |  |
| supports_history | varchar(50) | Yes |  |  | No |  |
| report_name | varchar(300) | Yes |  |  | No |  |
| max_timeout | int4(32) | Yes |  |  | No |  |
| report_count | int4(32) | Yes |  |  | No |  |
| input_location | varchar(150) | Yes |  |  | No |  |

---

## translation_table

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| region | varchar(50) | Yes |  |  | No |  |
| key | varchar(50) | Yes |  |  | No |  |
| value | varchar(250) | Yes |  |  | No |  |

---

## vantage_record_count

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| account_id | int4(32) | No |  |  | Yes |  |
| org_id | int4(32) | No |  |  | Yes |  |
| org_name | varchar | Yes |  |  | No |  |
| account_name | varchar | Yes |  |  | No |  |
| record_count | int4(32) | Yes |  |  | No |  |
| report_name | varchar | No |  |  | Yes |  |
| period | date | Yes |  |  | No |  |

---

## viz_app_usage_metrics

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| Sessions | int8(64) | Yes |  |  | No |  |
| Agency_User | varchar | Yes |  |  | No |  |
| Customer_Org | varchar | Yes |  |  | Yes |  |
| double_field_8 | numeric(38,9) | Yes |  |  | No |  |
| Week_Start_Date | varchar | Yes |  |  | Yes |  |
| Modules_Accessed | varchar | Yes |  |  | No |  |
| Cumstomer_Mail_ID | varchar | Yes |  |  | Yes |  |
| Subscription_Type | varchar | Yes |  |  | No |  |
| Total_Time__Mins_ | numeric(38,9) | Yes |  |  | No |  |
| _airbyte_raw_id | varchar(36) | No |  |  | Yes |  |
| _airbyte_extracted_at | timestamptz | No |  |  | Yes |  |
| _airbyte_meta | jsonb | No |  |  | No |  |

---

## viz_content_change

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| rank | int8(64) | Yes |  |  | No |  |
| month | varchar | Yes |  |  | No |  |
| latest | varchar | Yes |  |  | No |  |
| period | varchar | Yes |  |  | Yes |  |
| region | varchar | Yes |  |  | Yes |  |
| top_50 | varchar | Yes |  |  | No |  |
| rank_1P | int8(64) | Yes |  |  | No |  |
| rank_3P | int8(64) | Yes |  |  | No |  |
| previous | varchar | Yes |  |  | No |  |
| watchlist | bool | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | Yes |  |
| output_asin | varchar | Yes |  |  | Yes |  |
| product_code | varchar | Yes |  |  | No |  |
| buybox_winner | varchar | Yes |  |  | No |  |
| reporting_range | varchar | Yes |  |  | No |  |
| date_first_listed | varchar | Yes |  |  | No |  |
| in_product_master | bool | Yes |  |  | No |  |
| product_code_type | varchar | Yes |  |  | No |  |
| product_image_urls | varchar | Yes |  |  | No |  |
| variation_affected | varchar | Yes |  |  | No |  |
| content_change_type | varchar | Yes |  |  | No |  |
| amazon_best_seller_rank | varchar | Yes |  |  | No |  |
| _airbyte_raw_id | varchar(36) | No |  |  | Yes |  |
| _airbyte_extracted_at | timestamptz | No |  |  | Yes |  |
| _airbyte_meta | jsonb | No |  |  | No |  |

---

## viz_latest_product_details_dump

| Column Name | Column Type | Nullable | Default Value | Constraint | Index | Column Description |
| --- | --- | --- | --- | --- | --- | --- |
| product_code | varchar | Yes |  |  | No |  |
| marketplace | varchar | Yes |  |  | No |  |
| region | varchar | Yes |  |  | No |  |
| full_description | varchar | Yes |  |  | No |  |
| product_category | varchar | Yes |  |  | No |  |
| bullet_point_text | varchar | Yes |  |  | No |  |
| images_url | varchar | Yes |  |  | No |  |
| product_dimensions | varchar | Yes |  |  | No |  |
| shipping_weight | varchar | Yes |  |  | No |  |
| legal_disclaimer | text | Yes |  |  | No |  |
| safety_information | text | Yes |  |  | No |  |
| ingredients | text | Yes |  |  | No |  |
| product_title | varchar | Yes |  |  | No |  |
| video_url | varchar | Yes |  |  | No |  |
| video_thumbnail_url | varchar | Yes |  |  | No |  |
| period | date | Yes |  |  | No |  |
| time_of_day | varchar | Yes |  |  | No |  |
| a_plus | varchar | Yes |  |  | No |  |
| sh_row | int4(32) | Yes |  |  | No |  |

---
