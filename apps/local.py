import frappe
# from intella import utils, data_utils

def create_doctype():
    # Define the Doctype with all fields
    # doctype_data = {
    #     "doctype":"DocType",
    #     "name":"EQC",  # Replace with your Doctype name
    #     "module":"Intella",  # Replace with your module name
    #     "custom": 0,
    #     "fields" : [ 
    #         {"fieldname": "section1", "fieldtype": "Section Break", "label": "Common Fields"},
    #             {"fieldname":"batch_id", "fieldtype":"Data", "label":"Batch ID"},
    #             {"fieldname":"processed_docs", "fieldtype":"Int", "label":"Processed Docs"},
    #             {"fieldname":"processed_pages", "fieldtype":"Int", "label":"Processed Pages"},
    #             {"fieldname":"total_docs", "fieldtype":"Int", "label":"Total Docs"},
    #             {"fieldname":"qc_status", "fieldtype":"Select", "label":"QC Status", "options": "Queued\nPending\nAssigned\nHold\nSubmitted\nRejected\nFailed"},
    #             {"fieldname":"process_mode", "fieldtype":"Select", "label":"Process Mode", "options": "Doceye\nManual\nDeleted"},
    #                 {"fieldname": "column_break_1", "fieldtype": "Column Break"},
    #             {"fieldname":"branch", "fieldtype":"Data", "label":"Branch"},
    #             {"fieldname":"case_category", "fieldtype":"Select", "label":"Case Category", "options": "NO_DIR\nNON_IND\nNON_WORK\nDE_FAIL\nDE_MASK\nDE_PARTIAL\nDE_PASS\nUNEXPECTED"},
    #             {"fieldname":"processing_status", "fieldtype":"Data", "label":"Processing Status"},
    #             {"fieldname":"assigned_to", "fieldtype":"Data", "label":"Assigned To"},
    #             {"fieldname":"stp_status", "fieldtype":"Data", "label":"STP Status"},

    #         {"fieldname": "section2", "fieldtype": "Section Break", "label": "Report"},
    #             {"fieldname": "ref_no", "fieldtype": "Data", "label": "Application Number", "length":12},
    #             {"fieldname": "branch_code", "fieldtype": "Data", "label": "Branch Code", "length":10},
    #             {"fieldname": "uin_no", "fieldtype": "Data", "label": "UIN Number", "length":10},
    #             {"fieldname": "life_assured_prefix", "fieldtype": "Data", "label": "Prefix", "length":4},
    #             {"fieldname": "life_assured_name", "fieldtype": "Data", "label": "Name"},
    #             {"fieldname": "life_assured_dob", "fieldtype": "Date", "label": "Date of Birth"},
    #             {"fieldname": "life_assured_gender", "fieldtype": "Select", "label": "Gender", "options": "Male\nFemale\nOther"},
    #             {"fieldname": "life_assured_address_1", "fieldtype": "Data", "label": "Address Line 1"},
    #             {"fieldname": "life_assured_address_2", "fieldtype": "Data", "label": "Address Line 2"},
    #             {"fieldname": "life_assured_address_3", "fieldtype": "Data", "label": "Address Line 3"},
    #             {"fieldname": "life_assured_post", "fieldtype": "Data", "label": "Postal Code", "length":8},
    #             {"fieldname": "life_assured_pan", "fieldtype": "Data", "label": "PAN Number", "length":10},
    #             {"fieldname": "life_assured_mobile", "fieldtype": "Data", "label": "Mobile Number", "length":12},
    #             {"fieldname": "owner_prefix", "fieldtype": "Data", "label": "Prefix", "length":4},
    #             {"fieldname": "owner_name", "fieldtype": "Data", "label": "Name"},
    #             {"fieldname": "owner_address_1", "fieldtype": "Data", "label": "Address Line 1"},
    #             {"fieldname": "owner_address_2", "fieldtype": "Data", "label": "Address Line 2"},
    #             {"fieldname": "owner_address_3", "fieldtype": "Data", "label": "Address Line 3"},
    #                 {"fieldname": "column_break_2", "fieldtype": "Column Break"},
    #             {"fieldname": "owner_dob", "fieldtype": "Date", "label": "Date of Birth"},
    #             {"fieldname": "owner_pincode", "fieldtype": "Data", "label": "Pincode", "length":8},
    #             {"fieldname": "owner_mobile", "fieldtype": "Data", "label": "Mobile Number", "length":12},
    #             {"fieldname": "owner_email", "fieldtype": "Data", "label": "Email"},
    #             {"fieldname": "owner_gender", "fieldtype": "Select", "label": "Gender", "options": "Male\nFemale\nOther"},
    #             {"fieldname": "owner_relationship_desc", "fieldtype": "Data", "label": "Relationship Description"},
    #             {"fieldname": "owner_age", "fieldtype": "Data", "label": "Age", "length":3},
    #             {"fieldname": "owner_pan", "fieldtype": "Data", "label": "PAN Number", "length":10},
    #             {"fieldname": "owner_father_name", "fieldtype": "Data", "label": "Father's Name"},
    #             {"fieldname": "nominee_prefix", "fieldtype": "Data", "label": "Prefix", "length":4},
    #             {"fieldname": "nominee_name", "fieldtype": "Data", "label": "Name"},
    #             {"fieldname": "nominee_age", "fieldtype": "Data", "label": "Age", "length":3},
    #             {"fieldname": "nominee_relationship", "fieldtype": "Data", "label": "Relationship"},
    #             {"fieldname": "nominee_dob", "fieldtype": "Date", "label": "Date of Birth"},
    #             {"fieldname": "nominee_share", "fieldtype": "Data", "label": "Share (%)"},
    #             {"fieldname": "rider_name", "fieldtype": "Data", "label": "Rider Name"},
    #             {"fieldname": "rider_risk_term", "fieldtype": "Data", "label": "Risk Term"},
    #             {"fieldname": "rider_policy_term", "fieldtype": "Data", "label": "Policy Term"},
    #             {"fieldname": "rider_premium_paying_term", "fieldtype": "Data", "label": "Premium Paying Term"},
    #                 {"fieldname": "column_break_3", "fieldtype": "Column Break"},
    #             {"fieldname": "rider_premium_amount", "fieldtype": "Data", "label": "Premium Amount"},
    #             {"fieldname": "rider_sum_assured", "fieldtype": "Data", "label": "Sum Assured"},
    #             {"fieldname": "policy_product_name", "fieldtype": "Data", "label": "Product Name"},
    #             {"fieldname": "premium_frequency", "fieldtype": "Data", "label": "Premium Frequency"},
    #             {"fieldname": "sum_assured", "fieldtype": "Data", "label": "Sum Assured"},
    #             {"fieldname": "installment_premium", "fieldtype": "Data", "label": "Installment Premium"},
    #             {"fieldname": "premium_payment_term", "fieldtype": "Data", "label": "Premium Payment Term"},
    #             {"fieldname": "policy_term", "fieldtype": "Data", "label": "Policy Term"},
    #             {"fieldname": "annual_premium", "fieldtype": "Data", "label": "Annual Premium"},
    #             {"fieldname": "cover_total_premium", "fieldtype": "Data", "label": "Total Premium"},
    #             {"fieldname": "plan_option", "fieldtype": "Data", "label": "Plan Option"},
    #             {"fieldname": "frequency_of_annuity_payout", "fieldtype": "Data", "label": "Annuity Payout Frequency"},
    #             {"fieldname": "annuity_option", "fieldtype": "Data", "label": "Annuity Option"},
    #             {"fieldname": "return_of_premium", "fieldtype": "Data", "label": "Return of Premium"},
    #             {"fieldname": "billing_frequency", "fieldtype": "Data", "label": "Billing Frequency"},
    #             {"fieldname": "fund_option", "fieldtype": "Data", "label": "Fund Option"},
    #             {"fieldname": "sum_assured_on_death", "fieldtype": "Data", "label": "Sum Assured on Death"},
    #             {"fieldname": "policy_admin_charges", "fieldtype": "Data", "label": "Policy Admin Charges"},
    #             {"fieldname": "fund_name", "fieldtype": "Data", "label": "Fund Name"},
    #             {"fieldname": "fund_allocation", "fieldtype": "Data", "label": "Fund Allocation"},
                
    #         {"fieldname": "section3","fieldtype": "Section Break","label": "DocEye"},
    #             {"fieldname": "ref_no_doceye","fieldtype": "Data","label": "Application Number DocEye"},
    #             {"fieldname": "branch_code_doceye","fieldtype": "Data","label": "Branch Code DocEye", "length":8},
    #             {"fieldname": "uin_no_doceye","fieldtype": "Data","label": "UIN Number DocEye", "length":15},
    #             {"fieldname": "life_assured_prefix_doceye","fieldtype": "Data","label": "Prefix DocEye", "length":4},
    #             {"fieldname": "life_assured_name_doceye","fieldtype": "Data","label": "Name DocEye"},
    #             {"fieldname": "life_assured_dob_doceye","fieldtype": "Date","label": "Date of Birth DocEye"},
    #             {"fieldname": "life_assured_gender_doceye","fieldtype": "Select","label": "Gender DocEye","options": "Male\nFemale\nOther"},
    #             {"fieldname": "life_assured_address_1_doceye","fieldtype": "Data","label": "Address Line 1 DocEye"},
    #             {"fieldname": "life_assured_address_2_doceye","fieldtype": "Data","label": "Address Line 2 DocEye"},
    #             {"fieldname": "life_assured_address_3_doceye","fieldtype": "Data","label": "Address Line 3 DocEye"},
    #             {"fieldname": "life_assured_post_doceye","fieldtype": "Data","label": "Postal Code DocEye", "length":8},
    #             {"fieldname": "life_assured_pan_doceye","fieldtype": "Data","label": "PAN Number DocEye", "length":10},
    #             {"fieldname": "life_assured_mobile_doceye","fieldtype": "Data","label": "Mobile Number DocEye", "length":12},
    #             {"fieldname": "owner_prefix_doceye","fieldtype": "Data","label": "Prefix DocEye", "length":4},
    #             {"fieldname": "owner_name_doceye","fieldtype": "Data","label": "Name DocEye"},
    #             {"fieldname": "owner_address_1_doceye","fieldtype": "Data","label": "Address Line 1 DocEye"},
    #             {"fieldname": "owner_address_2_doceye","fieldtype": "Data","label": "Address Line 2 DocEye"},
    #             {"fieldname": "owner_address_3_doceye","fieldtype": "Data","label": "Address Line 3 DocEye"},
    #                 {"fieldname": "column_break_4", "fieldtype": "Column Break"},

    #             {"fieldname": "owner_dob_doceye","fieldtype": "Date","label": "Date of Birth DocEye"},
    #             {"fieldname": "owner_pincode_doceye","fieldtype": "Data","label": "Pincode DocEye", "length":8},
    #             {"fieldname": "owner_mobile_doceye","fieldtype": "Data","label": "Mobile Number DocEye", "length":12},
    #             {"fieldname": "owner_email_doceye","fieldtype": "Data","label": "Email DocEye"},
    #             {"fieldname": "owner_gender_doceye","fieldtype": "Select","label": "Gender DocEye","options": "Male\nFemale\nOther"},
    #             {"fieldname": "owner_relationship_desc_doceye","fieldtype": "Data","label": "Relationship Description DocEye"},
    #             {"fieldname": "owner_age_doceye","fieldtype": "Data","label": "Age DocEye", "length":3},
    #             {"fieldname": "owner_pan_doceye","fieldtype": "Data","label": "PAN Number DocEye", "length":10},
    #             {"fieldname": "owner_father_name_doceye","fieldtype": "Data","label": "Father's Name DocEye"},
    #             {"fieldname": "nominee_prefix_doceye","fieldtype": "Data","label": "Prefix DocEye"},
    #             {"fieldname": "nominee_name_doceye","fieldtype": "Data","label": "Name DocEye"},
    #             {"fieldname": "nominee_age_doceye","fieldtype": "Data","label": "Age DocEye", "length":3},
    #             {"fieldname": "nominee_relationship_doceye","fieldtype": "Data","label": "Relationship DocEye"},
    #             {"fieldname": "nominee_dob_doceye","fieldtype": "Date","label": "Date of Birth DocEye"},
    #             {"fieldname": "nominee_share_doceye","fieldtype": "Data","label": "Share (%) DocEye"},
    #             {"fieldname": "rider_name_doceye","fieldtype": "Data","label": "Rider Name DocEye"},
    #             {"fieldname": "rider_risk_term_doceye","fieldtype": "Data","label": "Risk Term DocEye"},
    #             {"fieldname": "rider_policy_term_doceye","fieldtype": "Data","label": "Policy Term DocEye"},
    #             {"fieldname": "rider_premium_paying_term_doceye","fieldtype": "Data","label": "Premium Paying Term DocEye"},
    #                 {"fieldname": "column_break_5", "fieldtype": "Column Break"},

    #             {"fieldname": "rider_premium_amount_doceye","fieldtype": "Data","label": "Premium Amount DocEye"},
    #             {"fieldname": "rider_sum_assured_doceye","fieldtype": "Data","label": "Sum Assured DocEye"},
    #             {"fieldname": "policy_product_name_doceye","fieldtype": "Data","label": "Product Name DocEye"},
    #             {"fieldname": "premium_frequency_doceye","fieldtype": "Data","label": "Premium Frequency DocEye"},
    #             {"fieldname": "sum_assured_doceye","fieldtype": "Data","label": "Sum Assured DocEye"},
    #             {"fieldname": "installment_premium_doceye","fieldtype": "Data","label": "Installment Premium DocEye"},
    #             {"fieldname": "premium_payment_term_doceye","fieldtype": "Data","label": "Premium Payment Term DocEye"},
    #             {"fieldname": "policy_term_doceye","fieldtype": "Data","label": "Policy Term DocEye"},
    #             {"fieldname": "annual_premium_doceye","fieldtype": "Data","label": "Annual Premium DocEye"},
    #             {"fieldname": "cover_total_premium_doceye","fieldtype": "Data","label": "Total Premium DocEye"},
    #             {"fieldname": "plan_option_doceye","fieldtype": "Data","label": "Plan Option DocEye"},
    #             {"fieldname": "frequency_of_annuity_payout_doceye","fieldtype": "Data","label": "Annuity Payout Frequency DocEye"},
    #             {"fieldname": "annuity_option_doceye","fieldtype": "Data","label": "Annuity Option DocEye"},
    #             {"fieldname": "return_of_premium_doceye","fieldtype": "Data","label": "Return of Premium DocEye"},
    #             {"fieldname": "billing_frequency_doceye","fieldtype": "Data","label": "Billing Frequency DocEye"},
    #             {"fieldname": "fund_option_doceye","fieldtype": "Data","label": "Fund Option DocEye"},
    #             {"fieldname": "sum_assured_on_death_doceye","fieldtype": "Data","label": "Sum Assured on Death DocEye"},
    #             {"fieldname": "policy_admin_charges_doceye","fieldtype": "Data","label": "Policy Admin Charges DocEye"},
    #             {"fieldname": "fund_name_doceye","fieldtype": "Data","label": "Fund Name DocEye"},
    #             {"fieldname": "fund_allocation_doceye","fieldtype": "Data","label": "Fund Allocation DocEye"},

    #         {"fieldname": "section4", "fieldtype": "Section Break", "label": "Coord"},
    #             {"fieldname": "ref_no_coord", "fieldtype": "JSON", "label": "Application Number Coord"},
    #             {"fieldname": "branch_code_coord", "fieldtype": "JSON", "label": "Branch Code Coord"},
    #             {"fieldname": "uin_no_coord", "fieldtype": "JSON", "label": "UIN Number Coord"},
    #             {"fieldname": "life_assured_prefix_coord", "fieldtype": "JSON", "label": "Prefix Coord"},
    #             {"fieldname": "life_assured_name_coord", "fieldtype": "JSON", "label": "Name Coord"},
    #             {"fieldname": "life_assured_dob_coord", "fieldtype": "JSON", "label": "Date of Birth Coord"},
    #             {"fieldname": "life_assured_gender_coord", "fieldtype": "JSON", "label": "Gender Coord", "options": "Male\nFemale\nOther"},
    #             {"fieldname": "life_assured_address_1_coord", "fieldtype": "JSON", "label": "Address Line 1 Coord"},
    #             {"fieldname": "life_assured_address_2_coord", "fieldtype": "JSON", "label": "Address Line 2 Coord"},
    #             {"fieldname": "life_assured_address_3_coord", "fieldtype": "JSON", "label": "Address Line 3 Coord"},
    #             {"fieldname": "life_assured_post_coord", "fieldtype": "JSON", "label": "Postal Code Coord"},
    #             {"fieldname": "life_assured_pan_coord", "fieldtype": "JSON", "label": "PAN Number Coord"},
    #             {"fieldname": "life_assured_mobile_coord", "fieldtype": "JSON", "label": "Mobile Number Coord"},
    #             {"fieldname": "owner_prefix_coord", "fieldtype": "JSON", "label": "Prefix Coord"},
    #             {"fieldname": "owner_name_coord", "fieldtype": "JSON", "label": "Name Coord"},
    #             {"fieldname": "owner_address_1_coord", "fieldtype": "JSON", "label": "Address Line 1 Coord"},
    #             {"fieldname": "owner_address_2_coord", "fieldtype": "JSON", "label": "Address Line 2 Coord"},
    #             {"fieldname": "owner_address_3_coord", "fieldtype": "JSON", "label": "Address Line 3 Coord"},
    #                 {"fieldname": "column_break_6", "fieldtype": "Column Break"},

    #             {"fieldname": "owner_dob_coord", "fieldtype": "JSON", "label": "Date of Birth Coord"},
    #             {"fieldname": "owner_pincode_coord", "fieldtype": "JSON", "label": "Pincode Coord"},
    #             {"fieldname": "owner_mobile_coord", "fieldtype": "JSON", "label": "Mobile Number Coord"},
    #             {"fieldname": "owner_email_coord", "fieldtype": "JSON", "label": "Email Coord"},
    #             {"fieldname": "owner_gender_coord", "fieldtype": "JSON", "label": "Gender Coord", "options": "Male\nFemale\nOther"},
    #             {"fieldname": "owner_relationship_desc_coord", "fieldtype": "JSON", "label": "Relationship Description Coord"},
    #             {"fieldname": "owner_age_coord", "fieldtype": "JSON", "label": "Age Coord"},
    #             {"fieldname": "owner_pan_coord", "fieldtype": "JSON", "label": "PAN Number Coord"},
    #             {"fieldname": "owner_father_name_coord", "fieldtype": "JSON", "label": "Father's Name Coord"},
    #             {"fieldname": "nominee_prefix_coord", "fieldtype": "JSON", "label": "Prefix Coord"},
    #             {"fieldname": "nominee_name_coord", "fieldtype": "JSON", "label": "Name Coord"},
    #             {"fieldname": "nominee_age_coord", "fieldtype": "JSON", "label": "Age Coord"},
    #             {"fieldname": "nominee_relationship_coord", "fieldtype": "JSON", "label": "Relationship Coord"},
    #             {"fieldname": "nominee_dob_coord", "fieldtype": "JSON", "label": "Date of Birth Coord"},
    #             {"fieldname": "nominee_share_coord", "fieldtype": "JSON", "label": "Share (%) Coord"},
    #             {"fieldname": "rider_name_coord", "fieldtype": "JSON", "label": "Rider Name Coord"},
    #             {"fieldname": "rider_risk_term_coord", "fieldtype": "JSON", "label": "Risk Term Coord"},
    #             {"fieldname": "rider_policy_term_coord", "fieldtype": "JSON", "label": "Policy Term Coord"},
    #             {"fieldname": "rider_premium_paying_term_coord", "fieldtype": "JSON", "label": "Premium Paying Term Coord"},
    #                 {"fieldname": "column_break_76", "fieldtype": "Column Break"},

    #             {"fieldname": "rider_premium_amount_coord", "fieldtype": "JSON", "label": "Premium Amount Coord"},
    #             {"fieldname": "rider_sum_assured_coord", "fieldtype": "JSON", "label": "Sum Assured Coord"},
    #             {"fieldname": "policy_product_name_coord", "fieldtype": "JSON", "label": "Product Name Coord"},
    #             {"fieldname": "premium_frequency_coord", "fieldtype": "JSON", "label": "Premium Frequency Coord"},
    #             {"fieldname": "sum_assured_coord", "fieldtype": "JSON", "label": "Sum Assured Coord"},
    #             {"fieldname": "installment_premium_coord", "fieldtype": "JSON", "label": "Installment Premium Coord"},
    #             {"fieldname": "premium_payment_term_coord", "fieldtype": "JSON", "label": "Premium Payment Term Coord"},
    #             {"fieldname": "policy_term_coord", "fieldtype": "JSON", "label": "Policy Term Coord"},
    #             {"fieldname": "annual_premium_coord", "fieldtype": "JSON", "label": "Annual Premium Coord"},
    #             {"fieldname": "cover_total_premium_coord", "fieldtype": "JSON", "label": "Total Premium Coord"},
    #             {"fieldname": "plan_option_coord", "fieldtype": "JSON", "label": "Plan Option Coord"},
    #             {"fieldname": "frequency_of_annuity_payout_coord", "fieldtype": "JSON", "label": "Annuity Payout Frequency Coord"},
    #             {"fieldname": "annuity_option_coord", "fieldtype": "JSON", "label": "Annuity Option Coord"},
    #             {"fieldname": "return_of_premium_coord", "fieldtype": "JSON", "label": "Return of Premium Coord"},
    #             {"fieldname": "billing_frequency_coord", "fieldtype": "JSON", "label": "Billing Frequency Coord"},
    #             {"fieldname": "fund_option_coord", "fieldtype": "JSON", "label": "Fund Option Coord"},
    #             {"fieldname": "sum_assured_on_death_coord", "fieldtype": "JSON", "label": "Sum Assured on Death Coord"},
    #             {"fieldname": "policy_admin_charges_coord", "fieldtype": "JSON", "label": "Policy Admin Charges Coord"},
    #             {"fieldname": "fund_name_coord", "fieldtype": "JSON", "label": "Fund Name Coord"},
    #             {"fieldname": "fund_allocation_coord", "fieldtype": "JSON", "label": "Fund Allocation Coord"}
    #         ],
    #     "permissions": [
    #         {"role":"System Manager", "permlevel": 0, "read": 1, "write": 1, "create": 1, "delete": 1, "submit": 0, "cancel": 0, "amend": 0},
    #     ]
    # }
    
    doctype_data = {
        "doctype":"DocType",
        "name":"PMFBY CH",
        "module":"Intella",
        "custom":0,
        "fields": [
            {"fieldname": "common_fields_section", "fieldtype": "Section Break", "label": "Common Fields"},
                {"fieldname": "batch_id", "fieldtype": "Data", "label": "Batch ID", "search_index": 1},
                {"fieldname": "qc_status","fieldtype": "Select","label": "QC Status","options": "Queued\nPending\nAssigned\nHold\nSubmitted\nRejected\nFailed","search_index": 1},
                {"fieldname": "processing_status","fieldtype": "Select","label": "Processing Status","options": "Processing\nDoc Processed\nFailed\nProcessed\nHold"},
                {"fieldname": "branch","fieldtype": "Data","label": "Branch"},

            {"fieldname": "column_break_ceyf","fieldtype": "Column Break"},
                {"fieldname": "total_docs","fieldtype": "Int","label": "Total Docs","length": 5},
                {"fieldname": "assigned_to","fieldtype": "Link","label": "Assigned To","options": "Intella Users"},
                {"fieldname": "check_status","fieldtype": "Select","label": "Check Status","options": "\nQC Okay\nQC Not Okay"},
                {"fieldname": "process_mode", "fieldtype": "Select", "label": "Process Mode","options": "\nDoceye\nManual\nDeleted"},
                
            {"fieldname": "mis_data_section","fieldtype": "Section Break","label": "MIS Data"},
                {"fieldname": "ref_no","fieldtype": "Data","label": "Application ID","unique": 1},
                {"fieldname": "farmer_name","fieldtype": "Data","label": "Farmer Name"},
                {"fieldname": "farmer_nature", "fieldtype": "Select", "label": "Farmer Nature", "options": "owner\ntenant\nsharecropper"},
                {"fieldname": "state","fieldtype": "Data","label": "State"},
                {"fieldname": "season","fieldtype": "Data","label": "Season"},
                {"fieldname": "bank","fieldtype": "Data","label": "Bank"},
                {"fieldname": "account","fieldtype": "Data","label": "Account"},
                {"fieldname": "farmer_id","fieldtype": "Data","label": "Farmer_ID","options": "Owner\nTenant"},
                {"fieldname": "scheme","fieldtype": "Data","label": "Scheme"},
                {"fieldname": "year","fieldtype": "Data","label": "Year"},
                {"fieldname": "ifsc","fieldtype": "Data","label": "IFSC"},
                {"fieldname": "crop_name","fieldtype": "Data","label": "Crop Name"},
                {"fieldname": "land_survey_number","fieldtype": "Data","label": "Land Survey Number"},
                {"fieldname": "land_subdivision_number","fieldtype": "Data","label": "Land SubDivision Number"},
                {"fieldname": "area_insured","fieldtype": "Data","label": "Area Insured"},
                
            {"fieldname": "coord_data_section","fieldtype": "Section Break","label": "Coord Data"},
                {"fieldname": "farmer_nature_coord","fieldtype": "JSON","label": "Farmer Nature Coord"}
                ],
        
        "permissions": [
            {"role":"System Manager", "permlevel": 0, "read": 1, "write": 1, "create": 1, "delete": 1, "submit": 0, "cancel": 0, "amend": 0},
        ]
    }

    # Create Doctype
    doc = frappe.get_doc(doctype_data)
    doc.insert()
    frappe.db.commit()

# Run the function to create the Doctype
# create_doctype()

# "fields": [
#                     {"fieldname": "section1", "fieldtype": "Section Break", "label": "Plan Detail Fields"},
#                         {"fieldname": "policy_term", "fieldtype": "Data", "label": "Cover Risk Term"},
#                         {"fieldname": "premium_payment_term", "fieldtype": "Data", "label": "Cover Premium Term1"},
#                         {"fieldname": "installment_premium", "fieldtype": "Data", "label": "Installment Premium"},
#                         {"fieldname": "sum_assured", "fieldtype": "Data", "label": "Sum Assured"},
#                         {"fieldname": "rider_name", "fieldtype": "Data", "label": "Rider Name"},
#                             {"fieldname": "column_break_1", "fieldtype": "Column Break"},
#                         {"fieldname": "policy_term_doceye", "fieldtype": "Data", "label": "Cover Risk Term DocEye"},
#                         {"fieldname": "premium_payment_term_doceye", "fieldtype": "Data", "label": "Cover Premium Term1 DocEye"},
#                         {"fieldname": "installment_premium_doceye", "fieldtype": "Data", "label": "Installment Premium DocEye"},
#                         {"fieldname": "sum_assured_doceye", "fieldtype": "Data", "label": "Sum Assured DocEye"},
#                         {"fieldname": "rider_name_doceye", "fieldtype": "Data", "label": "Rider Name DocEye"},
#                             {"fieldname": "column_break_2", "fieldtype": "Column Break"},
#                         {"fieldname": "policy_term_doceye_coord", "fieldtype": "JSON", "label": "Cover Risk Term DocEye Coord"},
#                         {"fieldname": "premium_payment_term_doceye_coord", "fieldtype": "JSON", "label": "Cover Premium Term1 DocEye Coord"},
#                         {"fieldname": "installment_premium_doceye_coord", "fieldtype": "JSON", "label": "Installment Premium DocEye Coord"},
#                         {"fieldname": "sum_assured_doceye_coord", "fieldtype": "JSON", "label": "Sum Assured DocEye Coord"},
#                         {"fieldname": "rider_name_doceye_coord", "fieldtype": "JSON", "label": "Rider Name DocEye Coord"}
#             ],
        


def doc_processed_post_process_test():
    batch_id = "ECS-00016"
    case_number = frappe.get_list("ECS", {"batch_id": batch_id}, ["ref_no", "name"])
    # case_number = [{"ref_no": "3MNH904944"}]
    # print(case_number)
    batch_doctype = "ECS"
    usecase = "ECS UseCase"
    batch_rec = {'batch_id': batch_id, 'batch_doctype': "ECS", 'usecase': "ECS UseCase"}
    ucd_config = {}
    for case in case_number:
        print(f'-----------------------------------{case.get("ref_no")}----------------------------------')
        docname = case.get("name")
        original_case_number = case.get("ref_no")
        utils.doc_processed_post_process(batch_id, batch_rec, ucd_config, original_case_number, batch_doctype, docname, usecase)

from intella.ops import ecs
def ecs_generate_flat_file():
    out = ecs.generate_flat_file("ECS-00016")
    print(out)

from datetime import datetime
def test():
    string = datetime.strptime("2025-02-05 11:29:40.109", "%Y-%m-%d %H:%M:%S.%f")
    string2 = datetime.strptime("2024-12-05", "%Y-%m-%d")
    # out = data_utils.format_date((string).split(" ")[0])
    print(abs((string - string2).days))
    if string>string2:
        print("true")
    else:
        print("False")

def test1():
    a = {"a": 1, "b": 2}
    a.pop("c")

def test_date():
    validator = {
        "m_acct_num": {"match_fields": ["d_acct_num_mandate", "d_acct_num_support"], "func_type": "amount_match", "match_type": "or", "dtype": "mandate", "empty_tag": "1003", "mismatch_tag": "1002"},
        # /"m_eft_acct_num": {"match_fields": ["d_acct_num_mandate", "d_acct_num_support"], "func_type": "exact_match", "match_type": "or", "dtype": "mandate", "empty_tag": "1003", "mismatch_tag": "1002"},
        "d_start_date": {"match_fields": ["d_mandate_date"], "func_type": "date_match", "match_type": [">="], "dtype": "mandate", "empty_tag": "1066", "mismatch_tag": "1068"},
        "d_end_date": {"match_fields": ["d_start_date"], "func_type": "date_match", "match_type": [">"], "month_diff": [480], "dtype": "mandate" },
        "d_mandate_date": {"match_fields": ["creation"], "func_type": "date_match", "match_type": ["<="], "diff": [110], "dtype": "mandate", "empty_tag": "1066", "mismatch_tag": "1068"}
    }
    # print(validator)

    test_cases = [
    {"m_acct_num": "01236548", "d_acct_num_mandate": "1236548", "d_mandate_date": "05-12-2024", "d_start_date": "05-12-2024", "d_end_date": "05-12-2054", "creation": "06-01-2024"},
    # {"d_mandate_date": None, "d_start_date": "09-10-2023", "d_end_date": "12-10-2025", "creation": "06-01-2024", "Error": "Error: Start date cannot be earlier than Mandate date."},
    # {"d_mandate_date": "10-08-2023", "d_start_date": "12-08-2023", "d_end_date": "12-09-2063", "creation": "06-01-2024", "Error": "Error: User date exceeds the allowed 40-year limit from the start date."},
    # {"d_mandate_date": "01-01-2023", "d_start_date": "02-01-2023", "d_end_date": "02-01-2063", "creation": "06-01-2024", "Error": "All conditions satisfied. Form can be processed."},
    # {"d_mandate_date": "10-09-2023", "d_start_date": "12-09-2023", "d_end_date": "11-09-2063", "creation": "06-01-2024", "Error": "All conditions satisfied. Form can be processed."}
    ]
    # print(test_cases)

    for case in test_cases:
        print(case)
        for key, val in validator.items():
            kwargs = {"m_key": key, "m_conf": val, "case_dict": case}
            if key == "m_acct_num":
                out = data_utils.is_amount_matching(**kwargs)
            else:
                out = data_utils.get_date_match(**kwargs)
            print(out)
        print("---------------------------------------------------------------------------------------")

def test_format_date():
    string = "03/12/1976"
    out = data_utils.format_date(string)
    print(out)

def test_generate_report():
    ecs.generate_report("ECS-00014")

def test_ecs():
    kwargs = {'remark': '', 'd_prop_num': '2KYJ085471', 'd_ifsc_on_mandate': 'SBIN0007065', 'd_ifsc_on_support': None, 'd_acct_num_mandate': '32691254881', 'd_acct_num_support': None, 'd_start_date': '28-12-2024', 'd_end_date': '28-12-2044', 'd_mandate_date': '28-12-2024', 'd_amt_fig': '52250', 'd_amt_words': 'ten four two', 'd_amt_match_flag': 'Yes', 'd_name_sign_flag': 'Yes', 'd_hit_date': None, 'd_name_mandate': 'Rugmen .', 'policy_holder_name_match_flag': 'Yes', 'd_policyholder_name': 'Rugmen', 'd_freq': 'As and when presented', 'case_number': '2KYJ085471-00388', 'doc_name': '2KYJ085471-00388', 'batch_id': 'ECS-00029', 'batch_doctype': 'ECS', 'usecase': 'ECS UseCase', 'mandate_type': 'CMP'}
    out = ecs.populate_data(**kwargs)
    # print(out)
    kwargs.update(out)
    kwargs["process_mode_flag"] = 1
    out1 = ecs.stp_process(**kwargs)

    # print(out1)