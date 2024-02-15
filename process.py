# Data decoded from: https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2022.pdf

import sqlite3

def parse_line(line):
    data = {
        'birth_year': line[8:12].strip(),
        'birth_month': line[12:14].strip(),
        'time_of_birth': line[18:22].strip(),
        'birth_day_of_week': line[22:23].strip(),
        'birth_place': line[31:32].strip(),
        'mothers_age_imputed_flag': line[72:73].strip(),
        'mothers_reported_age_used_flag': line[73:74].strip(),
        'mothers_age': line[74:76].strip(),
        'mothers_nativity': line[83:84].strip(),
        'residence_status': line[103:104].strip(),
        'mothers_race_recode_31': line[104:106].strip(),
        'mothers_hispanic_origin': line[111:112].strip(),
        'mothers_hispanic_origin_recode': line[114:115].strip(),
        'mothers_education': line[123:124].strip(),
        'marital_status': line[119:120].strip(),
        'fathers_age': line[146:148].strip(),
        'fathers_race_recode_31': line[151:153].strip(),
        'fathers_hispanic_origin': line[159:160].strip(),
        'fathers_education': line[162:163].strip(),
        'prior_births_living': line[171:173].strip(),
        'prior_births_dead': line[173:175].strip(),
        'prior_terminations': line[175:177].strip(),
        'live_birth_order': line[178:179].strip(),
        'total_birth_order': line[181:182].strip(),
        'interval_last_live_birth': line[198:200].strip(),
        'prenatal_care_month': line[224:225].strip(),
        'number_prenatal_visits': line[238:240].strip(),
        'cigarettes_before_pregnancy': line[252:254].strip(),
        'cigarettes_first_trimester': line[254:256].strip(),
        'mothers_height': line[280:281].strip(),
        'mothers_bmi': line[282:286].strip(),
        'mothers_prepregnancy_weight': line[292:294].strip(),
        'mothers_delivery_weight': line[299:301].strip(),
        'mothers_weight_gain': line[304:305].strip(),
        'diabetes_pre_pregnancy': line[312:313].strip(),
        'gestational_diabetes': line[313:314].strip(),
        'hypertension_pre_pregnancy': line[314:315].strip(),
        'gestational_hypertension': line[315:316].strip(),
        'eclampsia': line[316:317].strip(),
        'labor_induction': line[382:383].strip(),
        'augmentation_labor': line[383:384].strip(),
        'delivery_method': line[401:402].strip(),
        'maternal_transfusion': line[414:415].strip(),
        'perineal_laceration': line[415:416].strip(),
        'admission_to_icu': line[418:419].strip(),
        'birth_attendant': line[432:433].strip(),
        'payment_source': line[434:435].strip(),
        'apgar_score_5min': line[444:445].strip(),
        'infant_sex': line[474:475].strip(),
        'last_menses_month': line[477:478].strip(),
        'last_menses_year': line[478:482].strip(),
        'gestation_weeks': line[490:491].strip(),
        'birth_weight': line[504:507].strip()
    }
    return data

conn = sqlite3.connect('natality_data.db')
c = conn.cursor()

# Create table with all columns
c.execute('''CREATE TABLE IF NOT EXISTS natality_data (
                birth_year TEXT,
                birth_month TEXT,
                time_of_birth TEXT,
                birth_day_of_week TEXT,
                birth_place TEXT,
                mothers_age_imputed_flag TEXT,
                mothers_reported_age_used_flag TEXT,
                mothers_age TEXT,
                mothers_nativity TEXT,
                residence_status TEXT,
                mothers_race_recode_31 TEXT,
                mothers_hispanic_origin TEXT,
                mothers_hispanic_origin_recode TEXT,
                mothers_education TEXT,
                marital_status TEXT,
                fathers_age TEXT,
                fathers_race_recode_31 TEXT,
                fathers_hispanic_origin TEXT,
                fathers_education TEXT,
                prior_births_living TEXT,
                prior_births_dead TEXT,
                prior_terminations TEXT,
                live_birth_order TEXT,
                total_birth_order TEXT,
                interval_last_live_birth TEXT,
                prenatal_care_month TEXT,
                number_prenatal_visits TEXT,
                cigarettes_before_pregnancy TEXT,
                cigarettes_first_trimester TEXT,
                mothers_height TEXT,
                mothers_bmi TEXT,
                mothers_prepregnancy_weight TEXT,
                mothers_delivery_weight TEXT,
                mothers_weight_gain TEXT,
                diabetes_pre_pregnancy TEXT,
                gestational_diabetes TEXT,
                hypertension_pre_pregnancy TEXT,
                gestational_hypertension TEXT,
                eclampsia TEXT,
                labor_induction TEXT,
                augmentation_labor TEXT,
                delivery_method TEXT,
                maternal_transfusion TEXT,
                perineal_laceration TEXT,
                admission_to_icu TEXT,
                birth_attendant TEXT,
                payment_source TEXT,
                apgar_score_5min TEXT,
                infant_sex TEXT,
                last_menses_month TEXT,
                last_menses_year TEXT,
                gestation_weeks TEXT,
                birth_weight TEXT
            )''')

with open('natality_data.txt', 'r') as file:
    for line in file:
        data = parse_line(line)
        c.execute('''INSERT INTO natality_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  tuple(data.values()))

conn.commit()
conn.close()
