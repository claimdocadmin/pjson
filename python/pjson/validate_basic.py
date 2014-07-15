#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

# Written by Alan Viars
import json, sys, datetime


def validate_basic_dict(d, enumeration_type, number=None):
    """
    Input a python dict(d) object. Return a list of errors. If error list
    is empty then basic section is valid.
    """
    errors =[]
    
    
    if enumeration_type == "NPI-1":
        #Ensure required fields for NPI-1
    
        if d.get("name_prefix") not in ('Ms.', 'Mr.', 'Miss', 'Mrs.', 'Dr.', 'Prof.'):
            error = "name_prefix must be one of the following: 'Ms.', 'Mr.', 'Miss', 'Mrs.', 'Dr.', 'Prof.'"
            errors.append(error)
        
    
        if not d.get('first_name', ""):
            error = "first_name is required."
            errors.append(error)
        else:
            if len(d.get('first_name')) > 150:
                error = "first_name is longer than allowable."
                errors.append(error)
            
            
        if not d.get('last_name'):
            error = "last_name is required."
            errors.append(error)
        else:
            if len(d.get('last_name')) > 150:
                error = "last_name is longer than allowable."
                errors.append(error)
                        
        if len(d.get('middle_name')) > 150:
            
                error = "middle_name is longer than allowable."
                errors.append(error)

        if not d.get('sole_proprietor'):
            error = "sole_proprietor is required and must be in ('YES', 'NO')."
            errors.append(error)
        else:
            if d.get('sole_proprietor') not in ("YES","NO"):
                error = "sole_proprietor must be in ('YES', 'NO')."
                errors.append(error)
                
        if not d.get('gender'):
            error = "gender is required."
            errors.append(error)
        else:
            if d.get('gender') not in ("M","F", "T"):
                error = "gender must be in ('F','M', 'T')."
                errors.append(error)
        
        if not d.get('date_of_birth'):
            error = "date_of_birth is required."
            errors.append(error)
        else:
            # date supplied so let's make sure it is valid
            try:
                date = datetime.datetime.strptime(d.get('date_of_birth'), '%Y-%m-%d').date()
            except ValueError:
                error = "date_of_birth must be in YYYY-MM-DD format."
                errors.append(error)
                
        
        if not d.get('state_of_birth'):
            error = "state_of_birth is required. Use ZZ if born outside the US."
            errors.append(error)
        else:
            if d.get('state_of_birth') not in ('AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL',
                    'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
                    'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH',
                    'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI',
                    'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI',
                    'WY', 'AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW', 'VI', 'ZZ'):
                error = "state_of_birth must be 2 letter ISO code or ZZ for foreign born."    
                errors.append(error)
        
        
        if not d.get('country_of_birth'):
            error = "country_of_birth is required."
            errors.append(error)
        else:
             if d.get('country_of_birth') not in ('AF', 'AX', 'AL', 'DZ', 'AS',
                    'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT',
                    'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM',
                    'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG',
                    'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL',
                    'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI',
                    'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC',
                    'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 
                    'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI',
                    'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY',
                    'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR',
                    'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ',
                    'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS',
                    'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY',
                    'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM',
                    'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR',
                    'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP',
                    'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH',
                    'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL',
                    'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA',
                    'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO',
                    'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE',
                    'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO',
                    'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB',
                    'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF',
                    'EH', 'YE', 'ZM', 'ZW'):
                error = "country_of_birth must be 2 letter ISO code."    
                errors.append(error)
        
        
        # Validate the interdependecies
        if (d.get('country_of_birth')) != "US" and (d.get('state_of_birth') != "ZZ"):
            error = """country_of_birth and state_of_birth mismatch. A person
                      cannot be born in both a foreign contry and a US state at the same time."""    
            errors.append(error)
            
        if not d.get('ssn') and not d.get('itin'):
            error = "An NPI-1 individual provider must supppy an SSN or an EIN."    
            errors.append(error)
        
        if d.get('ssn') and len(d.get('ssn')) != 9 :
            error = "SSN must be 9 digits."    
            errors.append(error)
        
        if d.get('itin') and len(d.get('itin')) != 9 :
            error = "ITIN must be 9 digits."    
            errors.append(error)
            
        if d.get('ein') and len(d.get('ein')) != 9 :
            error = "EIN must be 9 digits."    
            errors.append(error)


        #Validate the not required items NPI-1
            #check values do not exceed max length
            
            max_values ={
                'other_first_name_1'          : 150, 
                'other_first_name_2'          : 150, 
                'other_last_name_1'           : 150, 
                'other_last_name_2'           : 150, 
                'other_middle_name_1'         : 150,  
                'other_middle_name_2'         : 150, 
                'other_name_code_1'           : 150, 
                'other_name_code_2'           : 150, 
                'other_name_credential_1'     : 150, 
                'other_name_credential_2'     : 150, 
                'other_name_prefix_1'         : 150, 
                'other_name_prefix_2'         : 150, 
                'other_name_suffix_1'         : 150, 
                'other_name_suffix_2'         : 150, 
                }
            for k in max_values.keys():
                print  max_values[k], d.get(k)
                
                if max_values[k] < len(d.get(k)):
                    error = "%s max allowable length %s." % (k, max_values[k])
                    errors.append(error)
    
    if enumeration_type == "NPI-2":
        
            #Validate the organization
            if not d.get('organization_name', ""):
                error = "organization_name is required."
                errors.append(error)
            else:
                if len(d.get('organization_name')) > 300:
                    error = "organization_name is longer than allowable."
                    errors.append(error)
            
            #"organization_name": "", 
            #"organization_other_name": "", 
            #"organization_other_name_code": "", 
            #"organizational_subpart": false, 
            #"ssn": "222222222", 
            #"ein": "", 
            #"itin": "", 
            #"gender": "M", 
            #"date_of_birth": "1970-11-01", 
            #"state_of_birth": "KY", 
            #"country_of_birth": "US", 
            #"number": "138724606", 
            #"initial_enumeration_date": "2014-07-14", 
            #"enumeration_date": "2014-07-14", 
            #"last_updated": "2014-07-15", 
            #"updated": "2014-07-15 14:39:59.079910+00:00", 
            #"date_of_death": "None", 
            #"reactivation_date": "None", 
            #"classification": "C", 
            #"mode": "W", 
            #"status": "A", 
            #"contact_method": "E", 
            #"deactivated_details": "", 
            #"deactivation_date": "None", 
            #"deactivation_reason_code": "", 
            #"decativation_note": "", 
            #"deceased_notes": "", 
            #"parent_organization": null, 
            #"parent_organization_ein": "", 
            #"parent_organization_legal_business_name": "", 
            #"recativation_note": "", 
            #"comments": "", 
            #"authorized_official_credential": "", 
            #"authorized_official_email": "", 
            #"authorized_official_first_name": "", 
            #"authorized_official_last_name": "", 
            #"authorized_official_middle_name": "", 
            #"authorized_official_prefix": "", 
            #"authorized_official_suffix": "", 
            #"authorized_official_telephone_number": "", 
            #"authorized_official_telephone_extension": "", 
            #"authorized_official_title": "", 
            #"authorized_official_title_or_position": "", 
            #"contact_person_credential": "", 
            #"contact_person_email": "", 
            #"contact_person_first_name": "", 
            #"contact_person_last_name": "", 
            #"contact_person_middle_name": "", 
            #"contact_person_prefix": "", 
            #"contact_person_suffix": "", 
            #"contact_person_telephone_extension": "", 
            #"contact_person_telephone_number": "", 
            #"contact_person_title": "", 
            #"contact_person_title_or_position": "", 
            #"website": "", 
            #"facebook_handle": "", 
            #"twitter_handle": "", 
            #"public_email": "", 
            #"gravatar_email": "", 
            #"driving_directions": "", 
            #"bio_headline": ""
            #
    return errors
