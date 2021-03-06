from .datatypes import DATATYPES_STRUCTS


FIELDS = {
    'ACC_1': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'ACCIDENT_DATE_TIME', None, -1),
    'ACC_2': ('leaf', None, 'ID', 'ACCIDENT_CODE', None, -1),
    'ACC_3': ('leaf', None, 'ST', 'ACCIDENT_LOCATION', None, -1),
    'ADD_1': ('leaf', None, 'ST', 'ADDENDUM_CONTINUATION_POINTER', None, -1),
    'BHS_1': ('leaf', None, 'ST', 'BATCH_FIELD_SEPARATOR', None, -1),
    'BHS_2': ('leaf', None, 'ST', 'BATCH_ENCODING_CHARACTERS', None, -1),
    'BHS_3': ('leaf', None, 'ST', 'BATCH_SENDING_APPLICATION', None, -1),
    'BHS_4': ('leaf', None, 'ST', 'BATCH_SENDING_FACILITY', None, -1),
    'BHS_5': ('leaf', None, 'ST', 'BATCH_RECEIVING_APPLICATION', None, -1),
    'BHS_6': ('leaf', None, 'ST', 'BATCH_RECEIVING_FACILITY', None, -1),
    'BHS_7': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'BATCH_CREATION_DATE_TIME', None, -1),
    'BHS_8': ('leaf', None, 'ST', 'BATCH_SECURITY', None, -1),
    'BHS_9': ('leaf', None, 'ST', 'BATCH_NAME_ID_TYPE', None, -1),
    'BHS_10': ('leaf', None, 'ST', 'BATCH_COMMENT', None, -1),
    'BHS_11': ('leaf', None, 'ST', 'BATCH_CONTROL_ID', None, -1),
    'BHS_12': ('leaf', None, 'ST', 'REFERENCE_BATCH_CONTROL_ID', None, -1),
    'BLG_1': ('leaf', None, 'CM', 'WHEN_TO_CHARGE', None, -1),
    'BLG_2': ('leaf', None, 'ID', 'CHARGE_TYPE', None, -1),
    'BLG_3': ('leaf', None, 'CM', 'ACCOUNT_ID', None, -1),
    'BTS_1': ('leaf', None, 'ST', 'BATCH_MESSAGE_COUNT', None, -1),
    'BTS_2': ('leaf', None, 'ST', 'BATCH_COMMENT', None, -1),
    'BTS_3': ('leaf', None, 'CM', 'BATCH_TOTALS', None, -1),
    'DG1_1': ('leaf', None, 'SI', 'SET_ID_DIAGNOSIS', None, -1),
    'DG1_2': ('leaf', None, 'ID', 'DIAGNOSIS_CODING_METHOD', None, -1),
    'DG1_3': ('leaf', None, 'ID', 'DIAGNOSIS_CODE', None, -1),
    'DG1_4': ('leaf', None, 'ST', 'DIAGNOSIS_DESCRIPTION', None, -1),
    'DG1_5': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'DIAGNOSIS_DATE_TIME', None, -1),
    'DG1_6': ('leaf', None, 'ID', 'DIAGNOSIS_DRG_TYPE', None, -1),
    'DG1_7': ('leaf', None, 'ST', 'MAJOR_DIAGNOSTIC_CATEGORY', None, -1),
    'DG1_8': ('leaf', None, 'ID', 'DIAGNOSTIC_RELATED_GROUP', None, -1),
    'DG1_9': ('leaf', None, 'ID', 'DRG_APPROVAL_INDICATOR', None, -1),
    'DG1_10': ('leaf', None, 'ID', 'DRG_GROUPER_REVIEW_CODE', None, -1),
    'DG1_11': ('leaf', None, 'ID', 'OUTLIER_TYPE', None, -1),
    'DG1_12': ('leaf', None, 'NM', 'OUTLIER_DAYS', None, -1),
    'DG1_13': ('leaf', None, 'NM', 'OUTLIER_COST', None, -1),
    'DG1_14': ('leaf', None, 'ST', 'GROUPER_VERSION_AND_TYPE', None, -1),
    'DSC_1': ('leaf', None, 'ST', 'CONTINUATION_POINTER', None, -1),
    'DSP_1': ('leaf', None, 'SI', 'SET_ID_DISPLAY_DATA', None, -1),
    'DSP_2': ('leaf', None, 'SI', 'DISPLAY_LEVEL', None, -1),
    'DSP_3': ('leaf', None, 'TX', 'DATA_LINE', None, -1),
    'DSP_4': ('leaf', None, 'ST', 'LOGICAL_BREAK_POINT', None, -1),
    'DSP_5': ('leaf', None, 'TX', 'RESULT_ID', None, -1),
    'ERR_1': ('leaf', None, 'ID', 'ERROR_CODE_AND_LOCATION', None, -1),
    'EVN_1': ('leaf', None, 'ID', 'EVENT_TYPE_CODE', None, -1),
    'EVN_2': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'DATE_TIME_OF_EVENT', None, -1),
    'EVN_3': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'DATE_TIME_PLANNED_EVENT', None, -1),
    'EVN_4': ('leaf', None, 'ID', 'EVENT_REASON_CODE', None, -1),
    'FHS_1': ('leaf', None, 'ST', 'FILE_FIELD_SEPARATOR', None, -1),
    'FHS_2': ('leaf', None, 'ST', 'FILE_ENCODING_CHARACTERS', None, -1),
    'FHS_3': ('leaf', None, 'ST', 'FILE_SENDING_APPLICATION', None, -1),
    'FHS_4': ('leaf', None, 'ST', 'FILE_SENDING_FACILITY', None, -1),
    'FHS_5': ('leaf', None, 'ST', 'FILE_RECEIVING_APPLICATION', None, -1),
    'FHS_6': ('leaf', None, 'ST', 'FILE_RECEIVING_FACILITY', None, -1),
    'FHS_7': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'FILE_CREATION_DATE_TIME', None, -1),
    'FHS_8': ('leaf', None, 'ST', 'FILE_SECURITY', None, -1),
    'FHS_9': ('leaf', None, 'ST', 'FILE_NAME_ID', None, -1),
    'FHS_10': ('leaf', None, 'ST', 'FILE_HEADER_COMMENT', None, -1),
    'FHS_11': ('leaf', None, 'ST', 'FILE_CONTROL_ID', None, -1),
    'FHS_12': ('leaf', None, 'ST', 'REFERENCE_FILE_CONTROL_ID', None, -1),
    'FT1_1': ('leaf', None, 'SI', 'SET_ID_FINANCIAL_TRANSACTION', None, -1),
    'FT1_2': ('leaf', None, 'ST', 'TRANSACTION_ID', None, -1),
    'FT1_3': ('leaf', None, 'ST', 'TRANSACTION_BATCH_ID', None, -1),
    'FT1_4': ('leaf', None, 'DT', 'TRANSACTION_DATE', None, -1),
    'FT1_5': ('leaf', None, 'DT', 'TRANSACTION_POSTING_DATE', None, -1),
    'FT1_6': ('leaf', None, 'ID', 'TRANSACTION_TYPE', None, -1),
    'FT1_7': ('leaf', None, 'ID', 'TRANSACTION_CODE', None, -1),
    'FT1_8': ('leaf', None, 'ST', 'TRANSACTION_DESCRIPTION', None, -1),
    'FT1_9': ('leaf', None, 'ST', 'TRANSACTION_DESCRIPTION_ALT', None, -1),
    'FT1_10': ('leaf', None, 'NM', 'TRANSACTION_AMOUNT_EXTENDED', None, -1),
    'FT1_11': ('leaf', None, 'NM', 'TRANSACTION_QUANTITY', None, -1),
    'FT1_12': ('leaf', None, 'NM', 'TRANSACTION_AMOUNT_UNIT', None, -1),
    'FT1_13': ('leaf', None, 'ST', 'DEPARTMENT_CODE', None, -1),
    'FT1_14': ('leaf', None, 'ID', 'INSURANCE_PLAN_ID', None, -1),
    'FT1_15': ('leaf', None, 'NM', 'INSURANCE_AMOUNT', None, -1),
    'FT1_16': ('leaf', None, 'ST', 'PATIENT_LOCATION', None, -1),
    'FT1_17': ('leaf', None, 'ID', 'FEE_SCHEDULE', None, -1),
    'FT1_18': ('leaf', None, 'ID', 'PATIENT_TYPE', None, -1),
    'FT1_19': ('leaf', None, 'ID', 'DIAGNOSIS_CODE', None, -1),
    'FT1_20': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'PERFORMED_BY_CODE', None, -1),
    'FT1_21': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'ORDERED_BY_CODE', None, -1),
    'FT1_22': ('leaf', None, 'NM', 'UNIT_COST', None, -1),
    'FTS_1': ('leaf', None, 'ST', 'FILE_BATCH_COUNT', None, -1),
    'FTS_2': ('leaf', None, 'ST', 'FILE_TRAILER_COMMENT', None, -1),
    'GT1_1': ('leaf', None, 'SI', 'SET_ID_GUARANTOR', None, -1),
    'GT1_2': ('leaf', None, 'ID', 'GUARANTOR_NUMBER', None, -1),
    'GT1_3': ('sequence', DATATYPES_STRUCTS['PN'], 'PN', 'GUARANTOR_NAME', None, -1),
    'GT1_4': ('sequence', DATATYPES_STRUCTS['PN'], 'PN', 'GUARANTOR_SPOUSE_NAME', None, -1),
    'GT1_5': ('sequence', DATATYPES_STRUCTS['AD'], 'AD', 'GUARANTOR_ADDRESS', None, -1),
    'GT1_6': ('leaf', None, 'TN', 'GUARANTOR_PHONE_NUMBER_HOME', None, -1),
    'GT1_7': ('leaf', None, 'TN', 'GUARANTOR_PHONE_NUMBER_BUSINESS', None, -1),
    'GT1_8': ('leaf', None, 'DT', 'GUARANTOR_DATE_OF_BIRTH', None, -1),
    'GT1_9': ('leaf', None, 'ID', 'GUARANTOR_SEX', None, -1),
    'GT1_10': ('leaf', None, 'ID', 'GUARANTOR_TYPE', None, -1),
    'GT1_11': ('leaf', None, 'ID', 'GUARANTOR_RELATIONSHIP', None, -1),
    'GT1_12': ('leaf', None, 'ST', 'GUARANTOR_SSN', None, -1),
    'GT1_13': ('leaf', None, 'DT', 'GUARANTOR_DATE_BEGIN', None, -1),
    'GT1_14': ('leaf', None, 'DT', 'GUARANTOR_DATE_END', None, -1),
    'GT1_15': ('leaf', None, 'NM', 'GUARANTOR_PRIORITY', None, -1),
    'GT1_16': ('leaf', None, 'ST', 'GUARANTOR_EMPLOYER_NAME', None, -1),
    'GT1_17': ('sequence', DATATYPES_STRUCTS['AD'], 'AD', 'GUARANTOR_EMPLOYER_ADDRESS', None, -1),
    'GT1_18': ('leaf', None, 'TN', 'GUARANTOR_EMPLOY_PHONE_NUMBER', None, -1),
    'GT1_19': ('leaf', None, 'ST', 'GUARANTOR_EMPLOYEE_ID_NUMBER', None, -1),
    'GT1_20': ('leaf', None, 'ID', 'GUARANTOR_EMPLOYMENT_STATUS', None, -1),
    'IN1_1': ('leaf', None, 'SI', 'SET_ID_INSURANCE', None, -1),
    'IN1_2': ('leaf', None, 'ID', 'INSURANCE_PLAN_ID', None, -1),
    'IN1_3': ('leaf', None, 'ST', 'INSURANCE_COMPANY_ID', None, -1),
    'IN1_4': ('leaf', None, 'ST', 'INSURANCE_COMPANY_NAME', None, -1),
    'IN1_5': ('sequence', DATATYPES_STRUCTS['AD'], 'AD', 'INSURANCE_COMPANY_ADDRESS', None, -1),
    'IN1_6': ('sequence', DATATYPES_STRUCTS['PN'], 'PN', 'INSURANCE_COMPANY_CONTACT_PERS', None, -1),
    'IN1_7': ('leaf', None, 'TN', 'INSURANCE_COMPANY_PHONE_NUMBER', None, -1),
    'IN1_8': ('leaf', None, 'ST', 'GROUP_NUMBER', None, -1),
    'IN1_9': ('leaf', None, 'ST', 'GROUP_NAME', None, -1),
    'IN1_10': ('leaf', None, 'ST', 'INSURED_S_GROUP_EMPLOYER_ID', None, -1),
    'IN1_11': ('leaf', None, 'ST', 'INSURED_S_GROUP_EMPLOYER_NAME', None, -1),
    'IN1_12': ('leaf', None, 'DT', 'PLAN_EFFECTIVE_DATE', None, -1),
    'IN1_13': ('leaf', None, 'DT', 'PLAN_EXPIRATION_DATE', None, -1),
    'IN1_14': ('leaf', None, 'ST', 'AUTHORIZATION_INFORMATION', None, -1),
    'IN1_15': ('leaf', None, 'ID', 'PLAN_TYPE', None, -1),
    'IN1_16': ('sequence', DATATYPES_STRUCTS['PN'], 'PN', 'NAME_OF_INSURED', None, -1),
    'IN1_17': ('leaf', None, 'ID', 'INSURED_S_RELATIONSHIP_TO_PATIENT', None, -1),
    'IN1_18': ('leaf', None, 'DT', 'INSURED_S_DATE_OF_BIRTH', None, -1),
    'IN1_19': ('sequence', DATATYPES_STRUCTS['AD'], 'AD', 'INSURED_S_ADDRESS', None, -1),
    'IN1_20': ('leaf', None, 'ID', 'ASSIGNMENT_OF_BENEFITS', None, -1),
    'IN1_21': ('leaf', None, 'ID', 'COORDINATION_OF_BENEFITS', None, -1),
    'IN1_22': ('leaf', None, 'ST', 'COORDINATION_OF_BENEFITS_PRIORITY', None, -1),
    'IN1_23': ('leaf', None, 'ID', 'NOTICE_OF_ADMISSION_CODE', None, -1),
    'IN1_24': ('leaf', None, 'DT', 'NOTICE_OF_ADMISSION_DATE', None, -1),
    'IN1_25': ('leaf', None, 'ID', 'REPORT_OF_ELIGIBILITY_CODE', None, -1),
    'IN1_26': ('leaf', None, 'DT', 'REPORT_OF_ELIGIBILITY_DATE', None, -1),
    'IN1_27': ('leaf', None, 'ID', 'RELEASE_INFORMATION_CODE', None, -1),
    'IN1_28': ('leaf', None, 'ST', 'PRE_ADMIT_CERTIFICATION_PAC', None, -1),
    'IN1_29': ('leaf', None, 'DT', 'VERIFICATION_DATE', None, -1),
    'IN1_30': ('leaf', None, 'CM', 'VERIFICATION_BY', None, -1),
    'IN1_31': ('leaf', None, 'ID', 'TYPE_OF_AGREEMENT_CODE', None, -1),
    'IN1_32': ('leaf', None, 'ID', 'BILLING_STATUS', None, -1),
    'IN1_33': ('leaf', None, 'NM', 'LIFETIME_RESERVE_DAYS', None, -1),
    'IN1_34': ('leaf', None, 'NM', 'DELAY_BEFORE_LIFETIME_RESERVE_DAYS', None, -1),
    'IN1_35': ('leaf', None, 'ST', 'COMPANY_PLAN_CODE', None, -1),
    'IN1_36': ('leaf', None, 'ST', 'POLICY_NUMBER', None, -1),
    'IN1_37': ('leaf', None, 'NM', 'POLICY_DEDUCTIBLE', None, -1),
    'IN1_38': ('leaf', None, 'NM', 'POLICY_LIMIT_AMOUNT', None, -1),
    'IN1_39': ('leaf', None, 'NM', 'POLICY_LIMIT_DAYS', None, -1),
    'IN1_40': ('leaf', None, 'NM', 'ROOM_RATE_SEMI_PRIVATE', None, -1),
    'IN1_41': ('leaf', None, 'NM', 'ROOM_RATE_PRIVATE', None, -1),
    'IN1_42': ('leaf', None, 'ID', 'INSURED_S_EMPLOYMENT_STATUS', None, -1),
    'IN1_43': ('leaf', None, 'ID', 'INSURED_S_SEX', None, -1),
    'IN1_44': ('sequence', DATATYPES_STRUCTS['AD'], 'AD', 'INSURED_S_EMPLOYER_ADDRESS', None, -1),
    'MRG_1': ('sequence', DATATYPES_STRUCTS['CK'], 'CK', 'PRIOR_PATIENT_ID_INTERNAL', None, -1),
    'MRG_2': ('sequence', DATATYPES_STRUCTS['CK'], 'CK', 'PRIOR_ALTERNATE_PATIENT_ID', None, -1),
    'MRG_3': ('sequence', DATATYPES_STRUCTS['CK'], 'CK', 'PRIOR_PATIENT_ACCOUNT_NUMBER', None, -1),
    'MSA_1': ('leaf', None, 'ID', 'ACKNOWLEDGEMENT_CODE', None, -1),
    'MSA_2': ('leaf', None, 'ST', 'MESSAGE_CONTROL_ID', None, -1),
    'MSA_3': ('leaf', None, 'ST', 'TEXT_MESSAGE', None, -1),
    'MSA_4': ('leaf', None, 'NM', 'EXPECTED_SEQUENCE_NUMBER', None, -1),
    'MSA_5': ('leaf', None, 'ID', 'DELAYED_ACKNOWLEDGEMENT_TYPE', None, -1),
    'MSH_1': ('leaf', None, 'ST', 'FIELD_SEPARATOR', None, -1),
    'MSH_2': ('leaf', None, 'ST', 'ENCODING_CHARACTERS', None, -1),
    'MSH_3': ('leaf', None, 'ST', 'SENDING_APPLICATION', None, -1),
    'MSH_4': ('leaf', None, 'ST', 'SENDING_FACILITY', None, -1),
    'MSH_5': ('leaf', None, 'ST', 'RECEIVING_APPLICATION', None, -1),
    'MSH_6': ('leaf', None, 'ST', 'RECEIVING_FACILITY', None, -1),
    'MSH_7': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'DATE_TIME_OF_MESSAGE', None, -1),
    'MSH_8': ('leaf', None, 'ST', 'SECURITY', None, -1),
    'MSH_9': ('sequence', DATATYPES_STRUCTS['CM_MSG'], 'CM_MSG', 'MESSAGE_TYPE', None, -1),
    'MSH_10': ('leaf', None, 'ST', 'MESSAGE_CONTROL_ID', None, -1),
    'MSH_11': ('leaf', None, 'ID', 'PROCESSING_ID', None, -1),
    'MSH_12': ('leaf', None, 'NM', 'VERSION_ID', None, -1),
    'MSH_13': ('leaf', None, 'NM', 'SEQUENCE_NUMBER', None, -1),
    'MSH_14': ('leaf', None, 'ST', 'CONTINUATION_POINTER', None, -1),
    'NCK_1': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'SYSTEM_DATE_TIME', None, -1),
    'NK1_1': ('leaf', None, 'SI', 'SET_ID_NEXT_OF_KIN', None, -1),
    'NK1_2': ('sequence', DATATYPES_STRUCTS['PN'], 'PN', 'NEXT_OF_KIN_NAME', None, -1),
    'NK1_3': ('leaf', None, 'ST', 'NEXT_OF_KIN_RELATIONSHIP', None, -1),
    'NK1_4': ('sequence', DATATYPES_STRUCTS['AD'], 'AD', 'NEXT_OF_KIN_ADDRESS', None, -1),
    'NK1_5': ('leaf', None, 'TN', 'NEXT_OF_KIN_PHONE_NUMBER', None, -1),
    'NPU_1': ('leaf', None, 'ID', 'BED_LOCATION', None, -1),
    'NPU_2': ('leaf', None, 'ID', 'BED_STATUS', None, -1),
    'NSC_1': ('leaf', None, 'ID', 'NETWORK_CHANGE_TYPE', None, -1),
    'NSC_2': ('leaf', None, 'ST', 'CURRENT_CPU', None, -1),
    'NSC_3': ('leaf', None, 'ST', 'CURRENT_FILESERVER', None, -1),
    'NSC_4': ('leaf', None, 'ST', 'CURRENT_APPLICATION', None, -1),
    'NSC_5': ('leaf', None, 'ST', 'CURRENT_FACILITY', None, -1),
    'NSC_6': ('leaf', None, 'ST', 'NEW_CPU', None, -1),
    'NSC_7': ('leaf', None, 'ST', 'NEW_FILESERVER', None, -1),
    'NSC_8': ('leaf', None, 'ST', 'NEW_APPLICATION', None, -1),
    'NSC_9': ('leaf', None, 'ST', 'NEW_FACILITY', None, -1),
    'NST_1': ('leaf', None, 'ID', 'STATISTICS_AVAILABLE', None, -1),
    'NST_2': ('leaf', None, 'ST', 'SOURCE_IDENTIFIER', None, -1),
    'NST_3': ('leaf', None, 'ID', 'SOURCE_TYPE', None, -1),
    'NST_4': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'STATISTICS_START', None, -1),
    'NST_5': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'STATISTICS_END', None, -1),
    'NST_6': ('leaf', None, 'NM', 'RECEIVE_CHARACTER_COUNT', None, -1),
    'NST_7': ('leaf', None, 'NM', 'SEND_CHARACTER_COUNT', None, -1),
    'NST_8': ('leaf', None, 'NM', 'MESSAGES_RECEIVED', None, -1),
    'NST_9': ('leaf', None, 'NM', 'MESSAGES_SENT', None, -1),
    'NST_10': ('leaf', None, 'NM', 'CHECKSUM_ERRORS_RECEIVED', None, -1),
    'NST_11': ('leaf', None, 'NM', 'LENGTH_ERRORS_RECEIVED', None, -1),
    'NST_12': ('leaf', None, 'NM', 'OTHER_ERRORS_RECEIVED', None, -1),
    'NST_13': ('leaf', None, 'NM', 'CONNECT_TIMEOUTS', None, -1),
    'NST_14': ('leaf', None, 'NM', 'RECEIVE_TIMEOUTS', None, -1),
    'NST_15': ('leaf', None, 'NM', 'NETWORK_ERRORS', None, -1),
    'NTE_1': ('leaf', None, 'SI', 'SET_ID_NOTES_AND_COMMENTS', None, -1),
    'NTE_2': ('leaf', None, 'ID', 'SOURCE_OF_COMMENT', None, -1),
    'NTE_3': ('leaf', None, 'TX', 'COMMENT', None, -1),
    'OBR_1': ('leaf', None, 'SI', 'SET_ID_OBSERVATION_REQUEST', None, -1),
    'OBR_2': ('leaf', None, 'CM', 'PLACER_ORDER_NUMBER', None, -1),
    'OBR_3': ('leaf', None, 'CM', 'FILLER_ORDER_NUMBER', None, -1),
    'OBR_4': ('sequence', DATATYPES_STRUCTS['CE'], 'CE', 'UNIVERSAL_SERVICE_ID', None, -1),
    'OBR_5': ('leaf', None, 'ST', 'PRIORITY', None, -1),
    'OBR_6': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'REQUESTED_DATE_TIME', None, -1),
    'OBR_7': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'OBSERVATION_DATE_TIME', None, -1),
    'OBR_8': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'OBSERVATION_END_DATE_TIME', None, -1),
    'OBR_9': ('sequence', DATATYPES_STRUCTS['CQ'], 'CQ', 'COLLECTION_VOLUME', None, -1),
    'OBR_10': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'COLLECTOR_IDENTIFIER', None, -1),
    'OBR_11': ('leaf', None, 'ST', 'SPECIMEN_ACTION_CODE', None, -1),
    'OBR_12': ('leaf', None, 'CM', 'DANGER_CODE', None, -1),
    'OBR_13': ('leaf', None, 'ST', 'RELEVANT_CLINICAL_INFORMATION', None, -1),
    'OBR_14': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'SPECIMEN_RECEIVED_DATE_TIME', None, -1),
    'OBR_15': ('leaf', None, 'CM', 'SPECIMEN_SOURCE', None, -1),
    'OBR_16': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'ORDERING_PROVIDER', None, -1),
    'OBR_17': ('leaf', None, 'TN', 'ORDER_CALLBACK_PHONE_NUMBER', None, -1),
    'OBR_18': ('leaf', None, 'ST', 'PLACERS_FIELD_1', None, -1),
    'OBR_19': ('leaf', None, 'ST', 'PLACERS_FIELD_2', None, -1),
    'OBR_20': ('leaf', None, 'ST', 'FILLERS_FIELD_1', None, -1),
    'OBR_21': ('leaf', None, 'ST', 'FILLERS_FIELD_2', None, -1),
    'OBR_22': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'RESULTS_REPORT_STATUS_CHANGE_DATE_TIME', None, -1),
    'OBR_23': ('leaf', None, 'CM', 'CHARGE_TO_PRACTICE', None, -1),
    'OBR_24': ('leaf', None, 'ID', 'DIAGNOSTIC_SERVICE_SECTION_ID', None, -1),
    'OBR_25': ('leaf', None, 'ID', 'RESULT_STATUS', None, -1),
    'OBR_26': ('leaf', None, 'CM', 'LINKED_RESULT', None, -1),
    'OBR_27': ('leaf', None, 'CM', 'QUANTITY_TIMING', None, -1),
    'OBR_28': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'RESULT_COPIES_TO', None, -1),
    'OBR_29': ('leaf', None, 'CM', 'PARENT_ACCESSION', None, -1),
    'OBR_30': ('leaf', None, 'ID', 'TRANSPORTATION_MODE', None, -1),
    'OBR_31': ('sequence', DATATYPES_STRUCTS['CE'], 'CE', 'REASON_FOR_STUDY', None, -1),
    'OBR_32': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'PRINCIPAL_RESULT_INTERPRETER', None, -1),
    'OBR_33': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'ASSISTANT_RESULT_INTERPRETER', None, -1),
    'OBR_34': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'TECHNICIAN', None, -1),
    'OBR_35': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'TRANSCRIPTIONIST', None, -1),
    'OBR_36': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'SCHEDULED_DATE_TIME', None, -1),
    'OBX_1': ('leaf', None, 'SI', 'SET_ID_OBSERVATIONAL_SIMPLE', None, -1),
    'OBX_2': ('leaf', None, 'ID', 'VALUE_TYPE', None, -1),
    'OBX_3': ('sequence', DATATYPES_STRUCTS['CE'], 'CE', 'OBSERVATION_IDENTIFIER', None, -1),
    'OBX_4': ('leaf', None, 'NM', 'OBSERVATION_SUB_ID', None, -1),
    'OBX_5': ('leaf', None, 'varies', 'OBSERVATION_RESULTS', None, -1),
    'OBX_6': ('leaf', None, 'ID', 'UNITS', None, -1),
    'OBX_7': ('leaf', None, 'ST', 'REFERENCES_RANGE', None, -1),
    'OBX_8': ('leaf', None, 'ST', 'ABNORMAL_FLAGS', None, -1),
    'OBX_9': ('leaf', None, 'NM', 'PROBABILITY', None, -1),
    'OBX_10': ('leaf', None, 'ID', 'NATURE_OF_ABNORMAL_TEST', None, -1),
    'OBX_11': ('leaf', None, 'ID', 'OBSERVATION_RESULT_STATUS', None, -1),
    'OBX_12': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'EFFECTIVE_DATE_LAST_OBSERVATION_NORMAL_VALUES', None, -1),
    'ORC_1': ('leaf', None, 'ST', 'ORDER_CONTROL', None, -1),
    'ORC_2': ('leaf', None, 'CM', 'PLACER_ORDER_NUMBER', None, -1),
    'ORC_3': ('leaf', None, 'CM', 'FILLER_ORDER_NUMBER', None, -1),
    'ORC_4': ('leaf', None, 'CM', 'PLACER_GROUP_NUMBER', None, -1),
    'ORC_5': ('leaf', None, 'ST', 'ORDER_STATUS', None, -1),
    'ORC_6': ('leaf', None, 'ST', 'RESPONSE_FLAG', None, -1),
    'ORC_7': ('leaf', None, 'CM', 'TIMING_QUANTITY', None, -1),
    'ORC_8': ('leaf', None, 'CM', 'PARENT', None, -1),
    'ORC_9': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'DATE_TIME_OF_TRANSACTION', None, -1),
    'ORC_10': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'ENTERED_BY', None, -1),
    'ORC_11': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'VERIFIED_BY', None, -1),
    'ORC_12': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'ORDERING_PROVIDER', None, -1),
    'ORC_13': ('leaf', None, 'CM', 'ENTERER_S_LOCATION', None, -1),
    'ORC_14': ('leaf', None, 'TN', 'CALL_BACK_PHONE_NUMBER', None, -1),
    'ORO_1': ('sequence', DATATYPES_STRUCTS['CE'], 'CE', 'ORDER_ITEM_ID', None, -1),
    'ORO_2': ('leaf', None, 'ID', 'SUBSTITUTE_ALLOWED', None, -1),
    'ORO_3': ('leaf', None, 'CN', 'RESULTS_COPIES_TO', None, -1),
    'ORO_4': ('leaf', None, 'ID', 'STOCKLOCATION', None, -1),
    'PID_1': ('leaf', None, 'SI', 'SET_ID_PATIENT_ID', None, -1),
    'PID_2': ('sequence', DATATYPES_STRUCTS['CK'], 'CK', 'PATIENT_ID_EXTERNAL_ID', None, -1),
    'PID_3': ('sequence', DATATYPES_STRUCTS['CK'], 'CK', 'PATIENT_ID_INTERNAL_ID', None, -1),
    'PID_4': ('leaf', None, 'ST', 'ALTERNATE_PATIENT_ID', None, -1),
    'PID_5': ('sequence', DATATYPES_STRUCTS['PN'], 'PN', 'PATIENT_NAME', None, -1),
    'PID_6': ('leaf', None, 'ST', 'MOTHER_S_MAIDEN_NAME', None, -1),
    'PID_7': ('leaf', None, 'DT', 'DATE_OF_BIRTH', None, -1),
    'PID_8': ('leaf', None, 'ID', 'SEX', None, -1),
    'PID_9': ('sequence', DATATYPES_STRUCTS['PN'], 'PN', 'PATIENT_ALIAS', None, -1),
    'PID_10': ('leaf', None, 'ID', 'ETHNIC_GROUP', None, -1),
    'PID_11': ('sequence', DATATYPES_STRUCTS['AD'], 'AD', 'PATIENT_ADDRESS', None, -1),
    'PID_12': ('leaf', None, 'ID', 'COUNTY_CODE', None, -1),
    'PID_13': ('leaf', None, 'TN', 'PHONE_NUMBER_HOME', None, -1),
    'PID_14': ('leaf', None, 'TN', 'PHONE_NUMBER_BUSINESS', None, -1),
    'PID_15': ('leaf', None, 'ST', 'LANGUAGE_PATIENT', None, -1),
    'PID_16': ('leaf', None, 'ID', 'MARITAL_STATUS', None, -1),
    'PID_17': ('leaf', None, 'ID', 'RELIGION', None, -1),
    'PID_18': ('sequence', DATATYPES_STRUCTS['CK'], 'CK', 'PATIENT_ACCOUNT_NUMBER', None, -1),
    'PID_19': ('leaf', None, 'ST', 'SOCIAL_SECURITY_NUMBER_PATIENT', None, -1),
    'PID_20': ('leaf', None, 'CM', 'DRIVER_S_LICENSE_NUMBER_PATIENT', None, -1),
    'PD1_1': ('leaf', None, 'ST', 'LIVING_DEPENDENCY', None, -1),
    'PR1_1': ('leaf', None, 'SI', 'SET_ID_PROCEDURE', None, -1),
    'PR1_2': ('leaf', None, 'ID', 'PROCEDURE_CODING_METHOD', None, -1),
    'PR1_3': ('leaf', None, 'ID', 'PROCEDURE_CODE', None, -1),
    'PR1_4': ('leaf', None, 'ST', 'PROCEDURE_DESCRIPTION', None, -1),
    'PR1_5': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'PROCEDURE_DATE_TIME', None, -1),
    'PR1_6': ('leaf', None, 'ID', 'PROCEDURE_TYPE', None, -1),
    'PR1_7': ('leaf', None, 'NM', 'PROCEDURE_MINUTES', None, -1),
    'PR1_8': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'ANESTHESIOLOGIST', None, -1),
    'PR1_9': ('leaf', None, 'ID', 'ANESTHESIA_CODE', None, -1),
    'PR1_10': ('leaf', None, 'NM', 'ANESTHESIA_MINUTES', None, -1),
    'PR1_11': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'SURGEON', None, -1),
    'PR1_12': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'RESIDENT_CODE', None, -1),
    'PR1_13': ('leaf', None, 'ID', 'CONSENT_CODE', None, -1),
    'PV1_1': ('leaf', None, 'SI', 'SET_ID_PATIENT_VISIT', None, -1),
    'PV1_2': ('leaf', None, 'ID', 'PATIENT_CLASS', None, -1),
    'PV1_3': ('leaf', None, 'ID', 'ASSIGNED_PATIENT_LOCATION', None, -1),
    'PV1_4': ('leaf', None, 'ID', 'ADMISSION_TYPE', None, -1),
    'PV1_5': ('leaf', None, 'ST', 'PREADMIT_NUMBER', None, -1),
    'PV1_6': ('leaf', None, 'ID', 'PRIOR_PATIENT_LOCATION', None, -1),
    'PV1_7': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'ATTENDING_DOCTOR', None, -1),
    'PV1_8': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'REFERRING_DOCTOR', None, -1),
    'PV1_9': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'CONSULTING_DOCTOR', None, -1),
    'PV1_10': ('leaf', None, 'ID', 'HOSPITAL_SERVICE', None, -1),
    'PV1_11': ('leaf', None, 'ID', 'TEMPORARY_LOCATION', None, -1),
    'PV1_12': ('leaf', None, 'ID', 'PREADMIT_TEST_INDICATOR', None, -1),
    'PV1_13': ('leaf', None, 'ID', 'READMISSION_INDICATOR', None, -1),
    'PV1_14': ('leaf', None, 'ID', 'ADMIT_SOURCE', None, -1),
    'PV1_15': ('leaf', None, 'ID', 'AMBULATORY_STATUS', None, -1),
    'PV1_16': ('leaf', None, 'ID', 'VIP_INDICATOR', None, -1),
    'PV1_17': ('sequence', DATATYPES_STRUCTS['CN'], 'CN', 'ADMITTING_DOCTOR', None, -1),
    'PV1_18': ('leaf', None, 'ID', 'PATIENT_TYPE', None, -1),
    'PV1_19': ('leaf', None, 'NM', 'VISIT_NUMBER', None, -1),
    'PV1_20': ('leaf', None, 'ID', 'FINANCIAL_CLASS', None, -1),
    'PV1_21': ('leaf', None, 'ID', 'CHARGE_PRICE_INDICATOR', None, -1),
    'PV1_22': ('leaf', None, 'ID', 'COURTESY_CODE', None, -1),
    'PV1_23': ('leaf', None, 'ID', 'CREDIT_RATING', None, -1),
    'PV1_24': ('leaf', None, 'ID', 'CONTRACT_CODE', None, -1),
    'PV1_25': ('leaf', None, 'DT', 'CONTRACT_EFFECTIVE_DATE', None, -1),
    'PV1_26': ('leaf', None, 'NM', 'CONTRACT_AMOUNT', None, -1),
    'PV1_27': ('leaf', None, 'NM', 'CONTRACT_PERIOD', None, -1),
    'PV1_28': ('leaf', None, 'ID', 'INTEREST_CODE', None, -1),
    'PV1_29': ('leaf', None, 'ID', 'TRANSFER_TO_BAD_DEBT_CODE', None, -1),
    'PV1_30': ('leaf', None, 'DT', 'TRANSFER_TO_BAD_DEBT_DATE', None, -1),
    'PV1_31': ('leaf', None, 'ID', 'BAD_DEBT_AGENCY_CODE', None, -1),
    'PV1_32': ('leaf', None, 'NM', 'BAD_DEBT_TRANSFER_AMOUNT', None, -1),
    'PV1_33': ('leaf', None, 'NM', 'BAD_DEBT_RECOVERY_AMOUNT', None, -1),
    'PV1_34': ('leaf', None, 'ID', 'DELETE_ACCOUNT_INDICATOR', None, -1),
    'PV1_35': ('leaf', None, 'DT', 'DELETE_ACCOUNT_DATE', None, -1),
    'PV1_36': ('leaf', None, 'ID', 'DISCHARGE_DISPOSITION', None, -1),
    'PV1_37': ('leaf', None, 'ID', 'DISCHARGED_TO_LOCATION', None, -1),
    'PV1_38': ('leaf', None, 'ID', 'DIET_TYPE', None, -1),
    'PV1_39': ('leaf', None, 'ID', 'SERVICING_FACILITY', None, -1),
    'PV1_40': ('leaf', None, 'ID', 'BED_STATUS', None, -1),
    'PV1_41': ('leaf', None, 'ID', 'ACCOUNT_STATUS', None, -1),
    'PV1_42': ('leaf', None, 'ID', 'PENDING_LOCATION', None, -1),
    'PV1_43': ('leaf', None, 'ID', 'PRIOR_TEMPORARY_LOCATION', None, -1),
    'PV1_44': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'ADMIT_DATE_TIME', None, -1),
    'PV1_45': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'DISCHARGE_DATE_TIME', None, -1),
    'PV1_46': ('leaf', None, 'NM', 'CURRENT_PATIENT_BALANCE', None, -1),
    'PV1_47': ('leaf', None, 'NM', 'TOTAL_CHARGES', None, -1),
    'PV1_48': ('leaf', None, 'NM', 'TOTAL_ADJUSTMENTS', None, -1),
    'PV1_49': ('leaf', None, 'NM', 'TOTAL_PAYMENTS', None, -1),
    'QRD_1': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'QUERY_DATE_TIME', None, -1),
    'QRD_2': ('leaf', None, 'ID', 'QUERY_FORMAT_CODE', None, -1),
    'QRD_3': ('leaf', None, 'ID', 'QUERY_PRIORITY', None, -1),
    'QRD_4': ('leaf', None, 'ST', 'QUERY_ID', None, -1),
    'QRD_5': ('leaf', None, 'ID', 'DEFERRED_RESPONSE_TYPE', None, -1),
    'QRD_6': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'DEFERRED_RESPONSE_DATE_TIME', None, -1),
    'QRD_7': ('sequence', DATATYPES_STRUCTS['CQ'], 'CQ', 'QUANTITY_LIMITED_REQUEST', None, -1),
    'QRD_8': ('leaf', None, 'ST', 'WHO_SUBJECT_FILTER', None, -1),
    'QRD_9': ('leaf', None, 'ID', 'WHAT_SUBJECT_FILTER', None, -1),
    'QRD_10': ('leaf', None, 'ST', 'WHAT_DEPARTMENT_DATA_CODE', None, -1),
    'QRD_11': ('leaf', None, 'ST', 'WHAT_DATA_CODE_VALUE_QUALIFIER', None, -1),
    'QRD_12': ('leaf', None, 'ID', 'QUERY_RESULTS_LEVEL', None, -1),
    'QRF_1': ('leaf', None, 'ST', 'WHERE_SUBJECT_FILTER', None, -1),
    'QRF_2': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'WHEN_DATA_START_DATE_TIME', None, -1),
    'QRF_3': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'WHEN_DATA_END_DATE_TIME', None, -1),
    'QRF_4': ('leaf', None, 'ST', 'WHAT_USER_QUALIFIER', None, -1),
    'QRF_5': ('leaf', None, 'ST', 'OTHER_QRY_SUBJECT_FILTER', None, -1),
    'RX1_1': ('leaf', None, 'ST', 'UNUSED', None, -1),
    'RX1_2': ('leaf', None, 'ST', 'UNUSED_NUMBER_2', None, -1),
    'RX1_3': ('leaf', None, 'ST', 'ROUTE', None, -1),
    'RX1_4': ('leaf', None, 'ST', 'SITE_ADMINISTERED', None, -1),
    'RX1_5': ('sequence', DATATYPES_STRUCTS['CQ'], 'CQ', 'IV_EVOLUTION_RATE', None, -1),
    'RX1_6': ('sequence', DATATYPES_STRUCTS['CQ'], 'CQ', 'DRUG_STRENGTH', None, -1),
    'RX1_7': ('leaf', None, 'NM', 'FINAL_CONCENTRATION', None, -1),
    'RX1_8': ('leaf', None, 'NM', 'FINAL_VOLUME_IN_ML', None, -1),
    'RX1_9': ('leaf', None, 'CM', 'DRUG_DOSE', None, -1),
    'RX1_10': ('leaf', None, 'ID', 'DRUG_ROLE', None, -1),
    'RX1_11': ('leaf', None, 'NM', 'PRESCRIPTION_SEQUENCE_NUMBER', None, -1),
    'RX1_12': ('sequence', DATATYPES_STRUCTS['CQ'], 'CQ', 'QUANTITY_DISPENSED', None, -1),
    'RX1_13': ('leaf', None, 'ST', 'UNUSED_NUMBER_3', None, -1),
    'RX1_14': ('sequence', DATATYPES_STRUCTS['CE'], 'CE', 'DRUG_ID', None, -1),
    'RX1_15': ('leaf', None, 'ID', 'COMPONENT_DRUG_IDS', None, -1),
    'RX1_16': ('leaf', None, 'ID', 'PRESCRIPTION_TYPE', None, -1),
    'RX1_17': ('leaf', None, 'ID', 'SUBSTITUTION_STATUS', None, -1),
    'RX1_18': ('leaf', None, 'ID', 'RX_ORDER_STATUS', None, -1),
    'RX1_19': ('leaf', None, 'NM', 'NUMBER_OF_REFILLS', None, -1),
    'RX1_20': ('leaf', None, 'ST', 'UNUSED_NUMBER_4', None, -1),
    'RX1_21': ('leaf', None, 'NM', 'REFILLS_REMAINING', None, -1),
    'RX1_22': ('leaf', None, 'ID', 'DEA_CLASS', None, -1),
    'RX1_23': ('leaf', None, 'NM', 'ORDERING_MD_S_DEA_NUMBER', None, -1),
    'RX1_24': ('leaf', None, 'ST', 'UNUSED_NUMBER_5', None, -1),
    'RX1_25': ('sequence', DATATYPES_STRUCTS['TS'], 'CE', 'LAST_REFILL_DATE_TIME', None, -1),
    'RX1_26': ('leaf', None, 'ST', 'RX_NUMBER', None, -1),
    'RX1_27': ('leaf', None, 'ID', 'PRN_STATUS', None, -1),
    'RX1_28': ('leaf', None, 'TX', 'PHARMACY_INSTRUCTIONS', None, -1),
    'RX1_29': ('leaf', None, 'TX', 'PATIENT_INSTRUCTIONS', None, -1),
    'RX1_30': ('leaf', None, 'TX', 'CE', 'INSTRUCTIONS_SIG', None, -1),
    'UB1_1': ('leaf', None, 'SI', 'SET_ID_UB82', None, -1),
    'UB1_2': ('leaf', None, 'ST', 'BLOOD_DEDUCTIBLE', None, -1),
    'UB1_3': ('leaf', None, 'ST', 'BLOOD_FURNISHED_PINTS_OF_40', None, -1),
    'UB1_4': ('leaf', None, 'ST', 'BLOOD_REPLACED_PINTS_41', None, -1),
    'UB1_5': ('leaf', None, 'ST', 'BLOOD_NOT_REPLACED_PINTS_42', None, -1),
    'UB1_6': ('leaf', None, 'ST', 'CO_INSURANCE_DAYS_25', None, -1),
    'UB1_7': ('leaf', None, 'ID', 'CONDITION_CODE', None, -1),
    'UB1_8': ('leaf', None, 'ST', 'COVERED_DAYS_23', None, -1),
    'UB1_9': ('leaf', None, 'ST', 'NON_COVERED_DAYS_24', None, -1),
    'UB1_10': ('leaf', None, 'CM', 'VALUE_AMOUNT_AND_CODE_46_49', None, -1),
    'UB1_11': ('leaf', None, 'ST', 'NUMBER_OF_GRACE_DAYS_90', None, -1),
    'UB1_12': ('leaf', None, 'ID', 'SPECIAL_PROGRAM_INDICATOR_44', None, -1),
    'UB1_13': ('leaf', None, 'ID', 'PSRO_UR_APPROVAL_INDICATOR_87', None, -1),
    'UB1_14': ('leaf', None, 'DT', 'PSRO_UR_APPROVED_STAY_FROM_88', None, -1),
    'UB1_15': ('leaf', None, 'DT', 'PSRO_UR_APPROVED_STAY_TO_89', None, -1),
    'UB1_16': ('leaf', None, 'CM', 'OCCURRENCE_28_32', None, -1),
    'UB1_17': ('leaf', None, 'ID', 'OCCURRENCE_SPAN_33', None, -1),
    'UB1_18': ('leaf', None, 'DT', 'OCCURRENCE_SPAN_START_DATE_33', None, -1),
    'UB1_19': ('leaf', None, 'DT', 'OCCURRENCE_SPAN_END_DATE_33', None, -1),
    'UB1_20': ('leaf', None, 'ST', 'UB_82_LOCATOR_2', None, -1),
    'UB1_21': ('leaf', None, 'ST', 'UB_82_LOCATOR_9', None, -1),
    'UB1_22': ('leaf', None, 'ST', 'UB_82_LOCATOR_27', None, -1),
    'UB1_23': ('leaf', None, 'ST', 'UB_82_LOCATOR_45', None, -1),
    'URD_1': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'R_U_DATE_TIME', None, -1),
    'URD_2': ('leaf', None, 'ID', 'REPORT_PRIORITY', None, -1),
    'URD_3': ('leaf', None, 'ST', 'R_U_WHO_SUBJECT_DEFINITION', None, -1),
    'URD_4': ('leaf', None, 'ID', 'R_U_WHAT_SUBJECT_DEFINITION', None, -1),
    'URD_5': ('leaf', None, 'ST', 'R_U_WHAT_DEPARTMENT_CODE', None, -1),
    'URD_6': ('leaf', None, 'ST', 'R_U_DISPLAY_PRINT_LOCATIONS', None, -1),
    'URD_7': ('leaf', None, 'ID', 'R_U_RESULTS_LEVEL', None, -1),
    'URS_1': ('leaf', None, 'ST', 'R_U_WHERE_SUBJECT_DEFINITION', None, -1),
    'URS_2': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'R_U_WHEN_DATA_START_DATE_TIME', None, -1),
    'URS_3': ('sequence', DATATYPES_STRUCTS['TS'], 'TS', 'R_U_WHEN_DATA_END_DATE_TIME', None, -1),
    'URS_4': ('leaf', None, 'ST', 'R_U_WHAT_USER_QUALIFIER', None, -1),
    'URS_5': ('leaf', None, 'ST', 'R_U_OTHER_RESULTS_SUBJECT_DEFINITION', None, -1),
}
